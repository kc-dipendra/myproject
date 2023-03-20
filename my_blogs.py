# %% Interactive Python Program with Postgres SQL Database
import psycopg2
import sys
import os

con = psycopg2.connect("dbname=my_blog user=postgres host=localhost port=5433")
cur = con.cursor()

def selection():
    con = psycopg2.connect("dbname=my_blog user=postgres host=localhost port=5433")
    cur = con.cursor()
    print('------------------------------------\nWELCOME TO SCHOOL MANAGEMENT SYSTEM\n------------------------------------')
    print("1. Student Page")
    print("2. Teacher Page")
    print("3. Course Page")
    print("4. Admin Page")
    print("5. Exit")

def show1():
    try:
        con = psycopg2.connect("dbname=my_blog user=postgres host=localhost port=5433")
        cur = con.cursor()
        sql = "SELECT * FROM student"
        cur.execute(sql)
        results = cur.fetchall()
        print("Student Informations")
        print("-------------------------------")
        for c in results:
            student_id = c[0]
            student_name= c[1]
            student_c_no=c[2]
            student_fee_details=c[3]
            print (student_id,student_name,student_c_no,student_fee_details)
    except:
        print ("Error: unable to fetch data")
        con.close()

def insert1():
    student_id=input("Enter Student ID : ")
    student_name=input("Enter Student Name: ")
    student_c_no=input("Enter Student Contact Number: ")
    student_fee_details = input("Enter Student Fee: ")
    con = psycopg2.connect("dbname=my_blog user=postgres host=localhost port=5433")
    cur = con.cursor()
    sql="INSERT INTO student(student_id,student_name,student_c_no,student_fee_details) VALUES ( '%s' ,'%s','%s','%s')"%(student_id,student_name,student_c_no,student_fee_details)
    try:
        cur.execute(sql)
        con.commit()
    except:
        con.rollback()
        con.close()

def delete1():
    try:
        con = psycopg2.connect("dbname=my_blog user=postgres host=localhost port=5433")
        cur = con.cursor()
        sql = "SELECT * FROM student"
        cur.execute(sql)
        results = cur.fetchall()
        for c in results:
            student_id = c[0]
            student_name= c[1]
            student_c_no=c[2]
            student_fee_details=c[3]

        temp=input("\nEnter student id to be deleted : ")

        try:
            sql = "delete from student where student_id=%s" % (temp)
            ans=input("Are you sure you want to delete the record(y/n) : ")
            if ans=='y' or ans=='Y':
                cur.execute(sql)
                con.commit()
        except Exception as e:
            print (e)

    except:
        print ("Error: unable to fetch data")
        con.close()

def show2():
    try:
        con = psycopg2.connect("dbname=my_blog user=postgres host=localhost port=5433")
        cur = con.cursor()
        sql = "SELECT * FROM teacher"
        cur.execute(sql)
        results = cur.fetchall()
        print("Teacher Informations")
        print("-------------------------------")
        for c in results:
            teacher_id = c[0]
            teacher_name= c[1]
            teacher_education=c[2]
            teacher_course=c[3]
            print (teacher_id,teacher_name,teacher_education,teacher_course)
    except:
        print ("Error: unable to fetch data")
        con.close()

def insert2():
    teacher_id=input("Enter Teacher ID : ")
    teacher_name=input("Enter Teacher Name: ")
    teacher_education=input("Enter Teacher Education: ")
    teacher_course = input("Enter Teacher Course: ")
    con = psycopg2.connect("dbname=my_blog user=postgres host=localhost port=5433")
    cur = con.cursor()
    sql="INSERT INTO teacher(teacher_id,teacher_name,teacher_education,teacher_course) VALUES ( '%s' ,'%s','%s','%s')"%(teacher_id,teacher_name,teacher_education,teacher_course)
    try:
        cur.execute(sql)
        con.commit()
    except:
        con.rollback()
        con.close()

def delete2():
    try:
        con = psycopg2.connect("dbname=my_blog user=postgres host=localhost port=5433")
        cur = con.cursor()
        sql = "SELECT * FROM teacher"
        cur.execute(sql)
        results = cur.fetchall()
        for c in results:
            teacher_id = c[0]
            teacher_name= c[1]
            teacher_education=c[2]
            teacher_course=c[3]

        temp=input("\nEnter teacher id to be deleted : ")

        try:
            sql = "delete from teacher where teacher_id=%s" % (temp)
            ans=input("Are you sure you want to delete the record(y/n) : ")
            if ans=='y' or ans=='Y':
                cur.execute(sql)
                con.commit()
        except Exception as e:
            print (e)

    except:
        print ("Error: unable to fetch data")
        con.close()

def show3():
    try:
        con = psycopg2.connect("dbname=my_blog user=postgres host=localhost port=5433")
        cur = con.cursor()
        sql = "SELECT * FROM course"
        cur.execute(sql)
        results = cur.fetchall()
        print("Course Informations")
        print("-------------------------------")
        for c in results:
            course_id = c[0]
            course_name= c[1]
            course_fees=c[2]
            course_duration=c[3]
            print (course_id,course_name,course_fees,course_duration)
    except:
        print ("Error: unable to fetch data")
        con.close()

def insert3():
    course_id=input("Enter Course ID : ")
    course_name=input("Enter Course Name: ")
    course_fees=input("Enter Course Fees: ")
    course_duration = input("Enter Course Duration: ")
    con = psycopg2.connect("dbname=my_blog user=postgres host=localhost port=5433")
    cur = con.cursor()
    sql="INSERT INTO course(course_id,course_name,course_fees,course_duration) VALUES ( '%s' ,'%s','%s','%s')"%(course_id,course_name,course_fees,course_duration)
    try:
        cur.execute(sql)
        con.commit()
    except:
        con.rollback()
        con.close()

def delete3():
    try:
        con = psycopg2.connect("dbname=my_blog user=postgres host=localhost port=5433")
        cur = con.cursor()
        sql = "SELECT * FROM course"
        cur.execute(sql)
        results = cur.fetchall()
        for c in results:
            course_id = c[0]
            course_name= c[1]
            course_fees=c[2]
            course_duration=c[3]

        temp=input("\nEnter course id to be deleted : ")

        try:
            sql = "delete from course where course_id=%s" % (temp)
            ans=input("Are you sure you want to delete the record(y/n) : ")
            if ans=='y' or ans=='Y':
                cur.execute(sql)
                con.commit()
        except Exception as e:
            print (e)

    except:
        print ("Error: unable to fetch data")
        con.close()

def show4():
    try:
        con = psycopg2.connect("dbname=my_blog user=postgres host=localhost port=5433")
        cur = con.cursor()
        sql = "SELECT * FROM admin"
        cur.execute(sql)
        results = cur.fetchall()
        print("Admin Informations")
        print("-------------------------------")
        for c in results:
            login_id = c[0]
            login_name= c[1]
            login_password=c[2]
            print (login_id,login_name,login_password)
    except:
        print ("Error: unable to fetch data")
        con.close()

def insert4():
    login_id=input("Enter Loin ID : ")
    login_name=input("Enter Login Name: ")
    login_password=input("Enter Login Password: ")
    con = psycopg2.connect("dbname=my_blog user=postgres host=localhost port=5433")
    cur = con.cursor()
    sql="INSERT INTO admin(login_id,login_name,login_password) VALUES ( '%s' ,'%s','%s')"%(login_id,login_name,login_password)
    try:
        cur.execute(sql)
        con.commit()
    except:
        con.rollback()
        con.close()

def delete4():
    try:
        con = psycopg2.connect("dbname=my_blog user=postgres host=localhost port=5433")
        cur = con.cursor()
        sql = "SELECT * FROM admin"
        cur.execute(sql)
        results = cur.fetchall()
        for c in results:
            login_id = c[0]
            login_name= c[1]
            login_password=c[2]
 
        temp=input("\nEnter login id to be deleted : ")

        try:
            sql = "delete from admin where login_id=%s" % (temp)
            ans=input("Are you sure you want to delete the record(y/n) : ")
            if ans=='y' or ans=='Y':
                cur.execute(sql)
                con.commit()
        except Exception as e:
            print (e)

    except:
        print ("Error: unable to fetch data")
        con.close()

selection()

while True:
    try:        
        ch=int(input("\nPlease enter your choice (1-5) : "))
        if ch not in [1, 2, 3, 4, 5]:
            raise ValueError("Invalid choice entered!")
    except ValueError as e:
        print(e)

    if ch==1:
            print('a. View Student List')
            print('b. Insert A New Student')
            print('c. Delete A Student')

            try:
                c=input("Enter your choice (a-c) : ")
                if c not in ['a', 'b', 'c']:
                    raise ValueError("Invalid choice entered!")
            except ValueError as e:
                print(e)

            if c=='a':
                show1()
            elif c=='b':
                insert1()
                print('\nModified details are..\n')
                show1()
            elif c=='c':
                delete1()
                print('\nModified details are..\n')
                show1()
            else:
                print('Enter correct choice...!!')
    elif ch==2:
            print('a. View Teacher List')
            print('b. Insert A New Teacher')
            print('c. Delete A Teacher')

            try:
                c=input("Enter your choice (a-c) : ")
                if c not in ['a', 'b', 'c']:
                    raise ValueError("Invalid choice entered!")
            except ValueError as e:
                print(e)

            if c=='a':
                show2()
            elif c=='b':
                insert2()
                print('\nModified details are..\n')
                show2()
            elif c=='c':
                delete2()
                print('\nModified details are..\n')
                show2()
            else:
                print('Enter correct choice...!!')
    elif ch==3:
            print('a. View Course List')
            print('b. Insert A New Course')
            print('c. Delete A Course')

            try:
                c=input("Enter your choice (a-c) : ")
                if c not in ['a', 'b', 'c']:
                    raise ValueError("Invalid choice entered!")
            except ValueError as e:
                print(e)

            if c=='a':
                show3()
            elif c=='b':
                insert3()
                print('\nModified details are..\n')
                show3()
            elif c=='c':
                delete3()
                print('\nModified details are..\n')
                show3()
            else:
                print('Enter correct choice...!!')

    elif ch==4:
            print('a. View Admin List')
            print('b. Insert A New Admin')
            print('c. Delete A Admin')

            try:
                c=input("Enter your choice (a-c) : ")
                if c not in ['a', 'b', 'c']:
                    raise ValueError("Invalid choice entered!")
            except ValueError as e:
                print(e)

            if c=='a':
                show4()
            elif c=='b':
                insert4()
                print('\nModified details are..\n')
                show4()
            elif c=='c':
                delete4()
                print('\nModified details are..\n')
                show4()
            else:
                print('Enter correct choice...!!')

    elif ch==5:
        sys.exit()

    else:
        print('Enter correct choice..!!')

# close the cursor and connection
cur.close()
con.close()

