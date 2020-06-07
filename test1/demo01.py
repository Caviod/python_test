#将excel中的数据导入数据库
import MySQLdb
import xlrd

file = xlrd.open_workbook(r"C:\Users\A\Desktop\2019-2020毕业设计学生-教师-选题对应表.xlsx")
sheet_1 = file.sheet_by_index(0)
row_number = sheet_1.nrows
col_number = sheet_1.ncols

conn = MySQLdb.connect(
    host = '127.0.0.1',
    user = 'root',
    db = 'testdb',
    charset = 'utf8'
)

c = conn.cursor() #创建游标对象
for i in range(row_number - 1):
    row_content = sheet_1.row_values(i + 1)
    c.execute(f"insert into t_graduate(id,name,classnum,class,teacher,title,type,title_type) values ('{row_content[0]}','{row_content[1]}','{row_content[2]}','{row_content[3]}','{row_content[4]}','{row_content[5]}','{row_content[6]}','{row_content[7]}')") #写sql语句
    conn.commit()

conn.close()
