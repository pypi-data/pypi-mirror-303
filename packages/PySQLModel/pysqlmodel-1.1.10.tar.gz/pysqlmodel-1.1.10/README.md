# PySQLModel

## 介绍

支持 MySQL、SQLite3 数据库。

方便快捷操作数据库。

## 安装

```cmd
pip install PySQLModel
```

更新

```cmd
pip install - U PySQLModel
```

示例

[example](./example)

# 使用介绍

#### 连接数据库

```python
# 导入MySQL模型
from PySQLModel import MySQL
# from PySQLModel.mysql import MySQL

# 导入数据库配置
from setting import MYSQL_DATABASES

# 数据库配置
# DATABASES = {
#     "database": "demo",
#     "user": "root",
#     "password": "123",
#     "host": "localhost",
#     "port": 3306,
#     "charset": "utf8",
# }
# mysql_obj = MySQL(name="demo",user="root",password="123",host="localhost",port=3306,charset="utf8")
# 推荐
mysql_obj = MySQL(**MYSQL_DATABASES)
```

---

#### show_table 查看所有表

```python
table_list = mysql_obj.show_table()
print(table_list)

['student_tb', 'test_data', 'test_data_copy1', 'test_data_copy2', 'test_data_copy3', 'test_data_copy4']
```

---

#### create_table 创建表

```python
# 表名
table_name = "class_tb"
# 表字段
# 原生 sql 语句
class_table_fields = {
    "id": "int NOT NULL PRIMARY KEY AUTO_INCREMENT",
    "name": "varchar(20)",  # 一个字符串为一个字段
}
mysql_obj.create_table(table_name=table_name, field_dict=class_table_fields)

# 原生创建
sql = """
CREATE TABLE `student_1_tb` (
    `id` int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` varchar(20) DEFAULT NULL COMMENT '名称',
    `age` int,
    `gender` enum('男','女'),
    `phone` varchar(11),
    `sid` int not null,
    FOREIGN KEY (sid) REFERENCES class_tb(id)
)COMMENT '学生表';
"""
mysql_obj.create_table(native_sql=sql)
```

---

#### table 指定操作表

```python
# 每次执行查询、添加、删除、修改需指定操作表
mysql_obj.table("class_tb")

# 主要用于：设置表名，获取表字段
# 同一对象只需设置一次即可
print(mysql_obj.table_name)  # 查看操作表名
print(mysql_obj.field_list)  # 查看字段列表

"""
class_tb
['id', 'name']
"""

mysql_obj.select()
print(mysql_obj.sql)  # 查看执行 sql
print(mysql_obj.args)  # 查看执行参数
"""
class_tb
[]
SELECT id, name FROM `class_tb`
[]
"""

```

---

#### create 添加数据

```python
# 添加数据
mysql_obj.table("class_tb").create(name="一班")

name = "张三"
age = "18"
gender = 1
phone = "12345678910"
sid = 1

create_id = mysql_obj.table("student_tb").create(name=name, age=age, gender=gender, phone=phone, sid=sid)
print(create_id)
"""
1
"""
# 或
temp_dict = {
    "name": "张三1",
    "age": "18",
    "gender": 1,
    "phone": "12345678910",
    "sid": 1,
}
create_id = mysql_obj.table("student_tb").create(**temp_dict)
print(create_id)
"""
1
"""
```

---

#### delete 删除数据

```python
delete_row = mysql_obj.table("student_tb").where("id=%s", 5).delete()
print(delete_row)
"""
1
"""
```

---

#### update 修改数据

```python
# update 修改结果
update_row = mysql_obj.table("student_tb").where("age=%s", 18).update(age=19)
print(update_row)
```

---

#### select 查询数据

查询所有数据

```python
# 查询所有数据
result = mysql_obj.table("student_tb").select()
print(result)
"""
[
    {'id': 1, 'name': '张三', 'age': 19, 'gender': '男', 'phone': '12345678910', 'sid': 1}, 
    {'id': 2, 'name': '李四', 'age': 18, 'gender': '女', 'phone': '12345678911', 'sid': 1}, 
    {'id': 3, 'name': '王五', 'age': 20, 'gender': '女', 'phone': '12345678912', 'sid': 2}, 
    {'id': 4, 'name': '赵六', 'age': 23, 'gender': '男', 'phone': '12345678913', 'sid': 1}
]
"""
```

指定字段

```python
result = mysql_obj.table("student_tb").fields("name", "age").select()
print(result)

"""
[
    {'name': '张三', 'age': 19}, 
    {'name': '李四', 'age': 18}, 
    {'name': '王五', 'age': 20}, 
    {'name': '赵六', 'age': 23}
]
"""
```

排序

```python
result = mysql_obj.table("student_tb").where("sid=%s", 1).order_by("-age", "id").select()
print(mysql_obj.sql)
print(result)
"""
SELECT id, name, age, gender, phone, sid FROM `student_tb` WHERE sid=%s ORDER BY `age` DESC, `id` DESC
[
    {'id': 2, 'name': '李四', 'age': 19, 'gender': '女', 'phone': '12345678911', 'sid': 1}, 
    {'id': 1, 'name': '张三', 'age': 16, 'gender': '男', 'phone': '12345678910', 'sid': 1}, 
    {'id': 3, 'name': '王五', 'age': 10, 'gender': '男', 'phone': '12345678912', 'sid': 1}
    {'id': 4, 'name': '赵六', 'age': 10, 'gender': '女', 'phone': '12345678913', 'sid': 1}, 
]
"""
```

分页

```python
page = 1
pagesize = 3
mysql_obj.table("student_tb").where("sid=%s", 1).order_by("-age", "id")
total, page_number = mysql_obj.page(page=page, pagesize=pagesize)
result = mysql_obj.select()
print(mysql_obj.sql)
print(f"总数：{total}, 页数:{page_number}")
print(result)
"""
SELECT id, name, age, gender, phone, sid FROM `student_tb` WHERE sid=%s ORDER BY `age` DESC, `id` ASC LIMIT 3 OFFSET 0
4 2
[
    {'id': 2, 'name': '李四', 'age': 19, 'gender': '女', 'phone': '12345678911', 'sid': 1}, 
    {'id': 1, 'name': '张三', 'age': 16, 'gender': '男', 'phone': '12345678910', 'sid': 1}, 
    {'id': 3, 'name': '王五', 'age': 10, 'gender': '男', 'phone': '12345678912', 'sid': 1}
]
"""
```

聚合查询 as 解析

```python
result = mysql_obj.table("student_tb").fields("gender", "avg(age) as age").where("id>0 group by gender").select()
print(result)
"""
[
    {'gender': '男', 'age': Decimal('45.0000')}, 
    {'gender': '女', 'age': Decimal('13.5000')}
]
"""
```

---

#### find 查询单条数据

```python
result = mysql_obj.table("student_tb").find()
print(result)
"""
{
    'id': 1, 
    'name': '张三', 
    'age': 18, 
    'gender': '男', 
    'phone': '12345678910', 
    'sid': 1
}
"""
```

指定字段

```python
result = mysql_obj.table("student_tb").fields("name", "phone").where("gender=%s", "女").find()
print(result)
"""
{
    'name': '李四', 
    'phone': '12345678911'
}
"""

```

---

#### 调用 pymysql 执行

```python
result_field = ["name", "age"]

mysql_obj.table("student_tb")
# sql 语句不限
sql = f"""
    select {",".join(result_field)}  from {mysql_obj.table_name} where name like '张%';
"""

# 调用实例属性 获取游标对象 执行sql语句
mysql_obj.cursor.execute(sql)
list_data = mysql_obj.cursor.fetchall()
print(list_data)
"""
(('张三', 18),)
[{'name': '张三', 'age': 18}]
"""
```

