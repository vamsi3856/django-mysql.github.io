from django.shortcuts import render
import mysql.connector as sql
fn=''
ln=''
s=''
em=''
pwd=''

# Create your views here.
def register(request):
    global fn,ln,s,em,pwd 
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="vamsi",database="loginsys")
        cursor=m.cursor()
        d=request.POST 
        for key,value in d.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="sex":
                s=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        c="insert into tab values('{}','{}','{}','{}','{}')".format(fn,ln,s,em,pwd)
        cursor.execute(c)
        m.commit()
                
    return render(request,"register.html")


def login(request):
    global em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="vamsi",database="loginsys")
        cursor=m.cursor()
        d=request.POST 
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        c="select * from tab where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,"error.html")
        else:
            return render(request,"index.html")
                
    return render(request,"login.html")