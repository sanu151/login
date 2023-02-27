from django.shortcuts import render
import mysql.connector as sql
fn=''
ln=''
s=''
em=''
pwd=''

# Create your views here.

def signupaction(request):
    global fn, ln, s, em, pwd
    if request.method=="POST":
        m = sql.connect(host='localhost', 
                    user='root',
                    password='sanu',
                    database='mydatabase')
        cursor= m.cursor()
        d=request.POST
        for key,value in d.items():
            if key == "first_name":
                fn = value
            if key == "last_name":
                ln = value
            if key == "sex":
                s = value
            if key == "email":
                em = value
            if key == "password":
                pwd = value
    
        c = "insert into user values('{}','{}','{}','{}','{}')".format(fn, ln, s, em, pwd)
        cursor.execute(c)
        m.commit()
        
    return render(request,'signup_page.html')