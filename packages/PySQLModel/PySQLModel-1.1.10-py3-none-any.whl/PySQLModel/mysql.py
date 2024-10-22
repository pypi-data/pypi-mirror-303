"""
@Project:PySqlModel
@File:mysql.py
@Author:函封封
"""
import math
from typing import Tuple, Union, List


# mysql操作
class MySQL():
    # 系统数据库
    __SYSTEM_DATABASES = ["information_schema", "mysql", "performance_schema", "sys"]

    def __init__(self, connect=None, **kwargs):
        """
        DATABASES = {
            "database": "demo",
            "user": "root",
            "password": "123",
            "host": "localhost",
            "port": 3306,
            "charset": "utf8",
        }
        """
        if connect is not None and hasattr(connect, "cursor"):
            self.connect = connect
        else:
            import pymysql
            self.connect = pymysql.connect(**kwargs)
        self.cursor = self.connect.cursor()  # 创建游标对象
        self.table_name = None  # 表名
        self.field_list = []  # 表字段
        self.where_sql = []  # 条件语句
        self.limit_sql = ""  # 分页
        self.order_sql = ""  # 排序
        self.sql = ""  # 执行 sql
        self.args = []  # 条件参数

    def show_table(self) -> List[str]:
        """
        查询当前数据库中所有表
        :return: 返回一个列表
        """
        self.sql = "show tables;"
        self.cursor.execute(self.sql)
        rows = self.cursor.fetchall()
        table_list = [row[0] for row in rows]
        return table_list  # 返回当前数据库内所有的表

    def create_table(self, table_name: str = None, field_dict: dict = None, native_sql: str = None) -> bool:
        """
        创建表，已存在直接返回，不存在则创建
        :param table_name: 表名
        :param field_dict: dict 表字段
        :param native_sql: 原生sql语句
        :return True
        """
        if native_sql is not None:
            self.sql = native_sql
        else:
            self.table_name = table_name.strip(" `'\"")  # 将表名赋值给实例属性

            self.field_list = field_dict.keys()  # 获取该表的所有的字段名

            table_list = self.show_table()  # 获取数据库里所有的表
            if self.table_name in table_list:  # 判断该表是否已存在
                return True  # 该表已存在！直接返回

            field_list = ["`{key}` {value}".format(key=key.strip(" `'\""), value=value) for key, value in field_dict.items()]
            create_field = ",".join(field_list)  # 将所有的字段与字段类型以 “ , ” 拼接
            self.sql = f"""CREATE TABLE `{self.table_name}`(
  {create_field}
);"""
        try:
            self.cursor.execute(self.sql)
            self.connect.commit()
            return True
        except Exception as err:
            self.connect.rollback()
            raise err

    def table(self, table_name: str):
        """
        设置操作表
        :param table_name: 表名
        :return: self
        """
        self.table_name = table_name.strip(" `'\"")  # 表名
        return self

    def create(self, **kwargs) -> int:
        """
        添加一条数据
        :param kwargs: 字段 = 值
        :return 添加成功：返回创建 id
        """
        try:
            field_sql = "`,`".join([field.strip(" `'\"") for field in kwargs.keys()])
            create_sql = ",".join(["%s"] * len(kwargs))

            # id 字段为null ，默认自增
            self.sql = f"INSERT INTO `{self.table_name}`  (`{field_sql}`) VALUES ({create_sql});"
            args = list(kwargs.values())
            self.cursor.execute(self.sql, args)
            self.connect.commit()
            return self.cursor.lastrowid
        except Exception as err:
            self.connect.rollback()
            raise err

    def fields(self, *fields):
        """
        查询字段
        :param fields: 字段
        :return: self
        """
        self.field_list = fields
        return self

    def where(self, sql: str, *args):
        """
        条件函数
        :param sql: sql 条件语句
        :param args: 值
        :return: self
        """
        self.where_sql.append(sql)
        self.args.extend(args)
        return self

    def order_by(self, *orders):
        order_fields = []
        for order in orders:
            order = str(order).strip(" `'\"")
            if not order:
                continue

            if order[0] == "-":
                order_sql = order[1:]
                sequence = "DESC"
            else:
                order_sql = order
                sequence = "ASC"
            order_fields.append(f"`{order_sql}` {sequence}")
        if len(order_fields) > 0:
            self.order_sql = f" ORDER BY {', '.join(order_fields)}"
        else:
            self.order_sql = ""
        return self

    # 设置分页数据，返回总数据量，总页数
    def page(self, page: int, pagesize: int) -> Tuple[int, int]:
        if not isinstance(page, int):
            page = int(page)
        if not isinstance(pagesize, int):
            pagesize = int(pagesize)
        self.limit_sql = " LIMIT {size} OFFSET {offset}".format(
            size=pagesize,
            offset=(page - 1) * pagesize,
        )
        total = self.count()
        return total, math.ceil(total / pagesize)

    def select(self) -> List[dict]:
        """
        查询数据库，返回全部数据
        :return list[dict] 返回查询到的所有行
        """
        try:
            if len(self.field_list) == 0:
                self.field_list = self.__get_fields()

            fields_str = ", ".join(self.field_list)
            self.sql = f"SELECT {fields_str} FROM `{self.table_name}`"
            if len(self.where_sql) > 0:
                self.sql += f" WHERE {' AND '.join(self.where_sql)}"
            if self.order_sql:
                self.sql += self.order_sql
            if self.limit_sql:
                self.sql += self.limit_sql

            self.cursor.execute(self.sql, self.args)
            rows = self.cursor.fetchall()
            result_field = self.__extract_field_list()
            return [dict(zip(result_field, row)) for row in rows]
        except Exception as err:
            raise err
        finally:
            self.where_sql = []
            self.limit_sql = ""
            self.order_sql = ""
            self.args = []

    def find(self) -> Union[dict, None]:
        """
        查询数据库，返回第一条数据
        :return dict
        """
        try:
            if len(self.field_list) == 0:
                self.field_list = self.__get_fields()

            fields_str = ", ".join(self.field_list)
            self.sql = f"SELECT {fields_str} FROM `{self.table_name}`"
            if len(self.where_sql) > 0:
                self.sql += f" WHERE {' AND '.join(self.where_sql)}"
            if self.order_sql:
                self.sql += self.order_sql

            self.sql += " LIMIT 1"
            self.cursor.execute(self.sql, self.args)
            row = self.cursor.fetchone()
            if row:
                result_field = self.__extract_field_list()
                kwargs = dict(zip(result_field, row))
                return kwargs
            return None
        except Exception as err:
            raise err
        finally:
            self.where_sql = []
            self.order_sql = ""
            self.args = []

    def count(self) -> int:
        """
        查询条数
        :return 返回查询条数
        """
        try:
            self.sql = f"SELECT COUNT(*) FROM `{self.table_name}`"
            if len(self.where_sql) > 0:
                self.sql += f" WHERE {' AND '.join(self.where_sql)}"
            self.cursor.execute(self.sql, self.args)
            row = self.cursor.fetchone()
            if row:
                return row[0]
        except Exception as err:
            print(err)
        return 0

    def update(self, **kwargs) -> int:
        """
        修改数据
        :param kwargs: key = value/字段 = 值 条件
        :return 返回受影响的行
        """
        try:
            if not kwargs: raise ValueError(f"**kwargs")

            update_sql = ", ".join([f"`{field}`=%s" for field in kwargs.keys()])
            self.sql = f"UPDATE `{self.table_name}` SET {update_sql}"
            if len(self.where_sql) > 0:
                self.sql += f" WHERE {' AND '.join(self.where_sql)}"

            args = list(kwargs.values())
            args.extend(self.args)
            rowcount = self.cursor.execute(self.sql, args)
            self.connect.commit()
            return rowcount
        except Exception as err:
            self.connect.rollback()
            raise err
        finally:
            self.where_sql = []
            self.args = []

    def delete(self) -> int:
        """
        删除满足条件的数据
        :return 返回受影响的行
        """
        try:
            self.sql = f"DELETE FROM `{self.table_name}`"
            if len(self.where_sql) > 0:
                self.sql += f" WHERE {' AND '.join(self.where_sql)}"
            rowcount = self.cursor.execute(self.sql, self.args)
            self.connect.commit()
            return rowcount
        except Exception as err:
            self.connect.rollback()
            raise err
        finally:
            self.where_sql = []
            self.args = []

    def __get_fields(self) -> list:
        if self.table_name is None:
            return []

        self.sql = f"SHOW COLUMNS FROM `{self.table_name}`;"
        self.cursor.execute(self.sql)
        field_list = [field[0] for field in self.cursor.fetchall()]
        return field_list

    def __extract_field_list(self) -> list:
        """
        解析字段列表，获取字段名称
        :param field_list: list 接受字段列表
        :return list 返回字段列表
        """
        result_field = []
        for field in self.field_list:
            if field == "*":
                result_field.extend(self.__get_fields())
            elif str(field).lower().find(" as ") != -1:
                field = field.split(" as ")[-1]

            field = field.strip(" `'\"")
            if not field:
                continue
            result_field.append(field)
        return result_field

    def close(self):
        self.cursor.close()
        self.connect.close()

    def __del__(self):
        self.close()