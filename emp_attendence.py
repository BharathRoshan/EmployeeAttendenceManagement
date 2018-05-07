import pymysql
def menu():
    print("Employee Attendence Management")
    print("------------------------------")
    print("1.Admin")
    print("2.Employee")
    print("3.Exit")
    return(int(input("Enter your choice")))

   
        
    
def insert_emp():
    conn = pymysql.connect('localhost','root','mysql123','employee_attend')
    cursor = conn.cursor()
    Emp_name = input("Enter Employee Name :")
    Desg = input("Enter Employee Designation :")  
    E_mail = input("Enter Employee E-mail : ")
    D_o_J = input("Enter the date of joining:")
    w_d = int(input("Enter the total number of working days : "))
    emp_wd = int(input("Enter the working days of the employee : "))
    attend = int((emp_wd / w_d) * 100)
    wd_left = int(w_d - emp_wd)
    args = [Emp_name,Desg,E_mail,D_o_J,attend,wd_left]
    sql = """insert into employee(Employee_Name,Designation,E_mail,Date_of_joining,Attendence,No_of_leaves_left)values(%s,%s,%s,%s,%s,%s)"""
    cursor.execute(sql,args)
    pp = """select * from employee"""
    cursor.execute(pp)
    print("Data Entered Successfully")
    conn.commit()
    conn.close()
    return menuAdmin()
        

        

def sea_id():
    conn = pymysql.connect('localhost','root','mysql123','employee_attend')
    cur = conn.cursor()
    eid =input("Enter the Employee id you want to search for")
    sea = """select * from employee where Employee_Id = %s"""
    data = (eid)
    cur.execute(sea,data)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    conn.commit()
    conn.close()
    return menuAdmin()

def sea_name():
    conn = pymysql.connect('localhost','root','mysql123','employee_attend')
    cur = conn.cursor()
    ename =input("Enter the Employee Name you want to search for")
    sea = """select * from employee where Employee_Name = %s"""
    data = (ename)
    cur.execute(sea,data)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    conn.commit()
    conn.close()
    return menuAdmin()

def view():
    conn = pymysql.connect('localhost','root','mysql123','employee_attend')
    cursor = conn.cursor()
    viw = """select * from employee"""
    cursor.execute(viw)
    for Employee_id,Employee_Name,Designation,E_mail,Date_of_joining,Attendence,No_of_leaves_left in cursor.fetchall():
        print('-'*50)
        print(Employee_id)
        print(Employee_Name)
        print(Designation)
        print(E_mail)
        print(Date_of_joining)
        print(Attendence)
        print(No_of_leaves_left)
        print('-'*50)
    conn.commit()                                                                                                          
    conn.close()
    return menuAdmin()

def viewemp():
    conn = pymysql.connect('localhost','root','mysql123','employee_attend')
    cursor = conn.cursor()
    viw = """select * from employee"""
    cursor.execute(viw)
    for Employee_id,Employee_Name,Designation,E_mail,Date_of_joining,Attendence,No_of_leaves_left in cursor.fetchall():
        print('-'*50)
        print(Employee_id)
        print(Employee_Name)
        print(Designation)
        print(E_mail)
        print(Date_of_joining)
        print(Attendence)
        print(No_of_leaves_left)
        print('-'*50)
    conn.commit()                                                                                                          
    conn.close()
    exit(0)

def up_name():
    conn = pymysql.connect('localhost','root','mysql123','employee_attend')
    cursor = conn.cursor()
    eid = input("Enter the Employee Id")
    enam = input("Enter the name of the employee you want to update:")
    sid = """select * from employee where Employee_Id={}""".format(eid)
    up = """update employee SET Employee_name = %s WHERE Employee_id = %s"""
    data = (enam,eid)
    cursor.execute(up,data)
    print("Update Successful")
    conn.commit()
    conn.close()
    return menuAdmin()


def up_desg():
    conn = pymysql.connect('localhost','root','mysql123','employee_attend')
    cursor = conn.cursor()
    eid = input("Enter the Employee Id")
    edesg = input("Enter the designation of the employee you want to update:")
    sid = """select * from employee where Employee_Id={}""".format(eid)
    up = """update employee SET Designation = %s WHERE Employee_id = %s"""
    data = (edesg,eid)
    cursor.execute(up,data)
    print("Update Successful")
    conn.commit()
    conn.close()
    return menuAdmin()

def up_mail():
    conn = pymysql.connect('localhost','root','mysql123','employee_attend')
    cursor = conn.cursor()
    eid = input("Enter the Employee Id")
    emai = input("Enter the mail id of the employee you want to update:")
    sid = """select * from employee where Employee_Id={}""".format(eid)
    up = """update employee SET E_mail = %s WHERE Employee_id = %s"""
    data = (emai,eid)
    cursor.execute(up,data)
    print("Update Successful")
    conn.commit()
    conn.close()

def up_mailemp():
    conn = pymysql.connect('localhost','root','mysql123','employee_attend')
    cursor = conn.cursor()
    eid = input("Enter the Employee Id")
    emai = input("Enter the mail id of the employee you want to update:")
    sid = """select * from employee where Employee_Id={}""".format(eid)
    up = """update employee SET E_mail = %s WHERE Employee_id = %s"""
    data = (emai,eid)
    cursor.execute(up,data)
    print("Update Successful")
    conn.commit()
    conn.close()
    exit(0)
        

def menuAdmin():
    print("ADMIN")
    print("-----")
    print("1.Insert a new employee")
    print("2.Select employee by ID")
    print("3.Select employee by Name")
    print("4.View employee")
    print("5.Update Name")
    print("6.Update Designation")
    print("7.Update Mail Id")
    print("8.Exit")
    choice = (int(input("Enter your choice")))

    while 1:
        if choice == 1: insert_emp()
        elif choice == 2: sea_id()
        elif choice == 3: sea_name()
        elif choice == 4: view()
        elif choice == 5: up_name()
        elif choice == 6: up_desg()
        elif choice == 6: up_mail()
        elif choice == 8: exit(0)
        else: print("Invalid Choice")


    
        

while 1:
    choice = menu()
    if choice == 1: menuAdmin()
    elif choice == 2:
        print("Employee")
        print("--------")
        print("1.View your details")
        print("2.Update Mail Id")
        print("3.Exit")
        ch = int(input("Enter your choice"))
        if ch == 1:
            sea_id()
        elif ch == 2:
            up_mailemp()
        elif ch == 3:
            exit(0)
    elif choice == 3: exit(0)
    else : print("Invalid Choice")

