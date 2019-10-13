from tkinter import *
from tkinter import messagebox as msg
import sqlite3 as sq
from PIL import ImageTk,Image
import scrolling_area
import pyttsx3 as py
import smtplib                      #for mail
import os                           #for mail

import string              #for otp
import random              #random function for otp     
root=Tk()
root.geometry('1400x700')
root.title('welcome to bank application')

def speak(event):
      
    tts=py.init()
    # volume
    vol=tts.getProperty("volume")
    tts.setProperty("volume",vol-3)
    # rate
    r=tts.getProperty("rate")
    tts.setProperty("rate",r-70)

    tts.say("please enter the button")
    tts.runAndWait()

    
def mails(frame,p1):
    email=p1.get()
    frame.destroy()
    frame15=Frame(root,width=1400,height=700)
    frame15.pack(expand=True)
    img=ImageTk.PhotoImage(Image.open('C:\\images\\pixal.jpg'))
    lgs1=Label(frame15,image=img)
    lgs1.image=img
    lgs1.place(x=0,y=0)
    lg2=Label(frame15,text=' Changing OTP  ',bg='light gray',fg='black',font=('times',38,"bold",'underline'),width=42)
    lg2.place(x=0,y=0)

    lg3=Label(frame15,text='Email id',bg='light gray',fg='black',font=('times',18,"bold",'italic'),width=15)
    lg3.place(x=620,y=220)

    eg1=Entry(frame15,bg='white',bd=6,fg='black',font=('times',16,"bold",'italic'),width=20)
    eg1.place(x=900,y=220)

    lg4=Label(frame15,text='OTP',bg='light gray',fg='black',font=('times',18,"bold",'italic'),width=15)
    lg4.place(x=620,y=280)


    eg2=Entry(frame15,bg='white',show='*',bd=6,fg='black',font=('times',16,"bold",'italic'),width=20)
    eg2.place(x=900,y=280)
    
    password=string.digits
    otp=""
    for var in range(6):
        otp=otp+random.choice(password)
    else:
        print('otp :',otp)
        
    sender='piyushkedia002@gmail.com'
    reciver='piyushkedia002@gmail.com'
    content=otp
    mail=smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("piyushkedia002@gmail.com","kedia123")
    mail.sendmail(sender,reciver,content)
    print("Mail send sucessfully")
    mail.close()           
    bg1=Button(frame15,text='Submit',bg='dark gray',bd=9,command=lambda:pas(frame15),fg='black',font=('times',16,"bold",'italic'),width=7)
    bg1.place(x=840,y=400)

    

def pas(frame):
    frame.destroy()
    frame1=Frame(root,width=1400,height=700)
    frame1.pack(expand=True)
    img=ImageTk.PhotoImage(Image.open('C:\\images\\pixal.jpg'))
    lg1=Label(frame1,image=img)
    lg1.image=img
    lg1.place(x=0,y=0)

    lg2=Label(frame1,text='enter changing password ',bg='light gray',fg='black',font=('times',38,"bold",'underline'),width=42)
    lg2.place(x=0,y=0)

    lg3=Label(frame1,text='New password',bg='light gray',fg='black',font=('times',18,"bold",'italic'),width=15)
    lg3.place(x=620,y=220)

    eg1=Entry(frame1,bg='white',bd=6,fg='black',font=('times',16,"bold",'italic'),width=20)
    eg1.place(x=900,y=220)

    lg4=Label(frame1,text='confirm Password',bg='light gray',fg='black',font=('times',18,"bold",'italic'),width=15)
    lg4.place(x=620,y=280)


    eg2=Entry(frame1,bg='white',show='*',bd=6,fg='black',font=('times',16,"bold",'italic'),width=20)
    eg2.place(x=900,y=280)
    
    bg1=Button(frame1,text='Submit',bg='dark gray',bd=9,command=lambda:account(frame1,eg1,eg2),fg='black',font=('times',16,"bold",'italic'),width=7)
    bg1.place(x=840,y=400)

def exit(frame):
    frame.destroy()
    main(root)
    
def exit1(egs1,egs2,frame):
    show(frame,root)

def logout(frame):
    login(frame)
    
def exits(frame,root):
    frame.destroy()
    root.destroy()

def bk(frame,eg1,eg2):
    frame.destroy()
    account(frame,eg1,eg2)

def show (frame,root):
    frame.destroy()
    frame6=Frame(root,width=1400,height=700)
    frame6.pack(expand=True)
    img=ImageTk.PhotoImage(Image.open('C:\\images\\pixal.jpg'))
    lgs1=Label(frame6,image=img)
    lgs1.image=img
    lgs1.place(x=0,y=0)

    q="Welcome To Bank Detail"
    lgs2=Label(frame6,text=q.center(80),bg='light gray',fg='dark blue',font=('times',42,'bold','underline'),width=42)
    lgs2.place(x=0,y=0)

    lgs3=Label(frame6,text='Email or Phone',bg='light gray',fg='black',font=('times',20,'bold'),width=15)
    lgs3.place(x=620,y=220)

    egs1=Entry(frame6,bg='white',bd=6,fg='black',font=('times',18,'bold'),width=19)
    egs1.place(x=900,y=220)

    lgs4=Label(frame6,text='Password',bg='light gray',fg='black',font=('times',20,'bold'),width=15)
    lgs4.place(x=620,y=280)

    egs2=Entry(frame6,bg='white',bd=6,show=('*'),fg='black',font=('times',18,'bold'),width=19)
    egs2.place(x=900,y=280)
    
    bgs1=Button(frame6,text='Submit',bg='dark gray',bd=9,command=lambda:personal(egs1,egs2,frame6),fg='black',font=('times',20,'bold'),width=7)
    bgs1.place(x=840,y=400)


    bgs3=Button(frame6,text='Back',bg='dark gray',bd=9,command=lambda:exit(frame6),fg='black',font=('times',20,'bold'),width=7)
    bgs3.place(x=80,y=520)


def alldetail(frame):
    frame.destroy()
    conn=sq.connect('bank.db')
    cur=conn.execute('''select * from banking''')
    frame5=Frame(root,width=1400,height=700)
    frame5.pack(expand=True)
    img=ImageTk.PhotoImage(Image.open('C:\\images\\pixal.jpg'))
    lgs1=Label(frame5,image=img)
    lgs1.image=img
    lgs1.place(x=0,y=0)
    bgs1=Button(frame5,text='Back',bg='dark gray',bd=9,command=lambda:exit1(egs1,egs2,frame7),fg='black',font=('times',19,'bold'),width=7)
    bgs1.place(x=80,y=580)
    scl=scrolling_area.Scrolling_Area(frame5,height=700,width=1400)
    scl.place(x=10,y=10)
    table=scrolling_area.Table(scl.innerframe,['Name','fathers name','email','Mobile no','Address','Gender','Password','Confirm Password','field'],column_minwidths=[130,130,130,130,130,130,130,130,130])
    table.pack(expand=True,fill=X)
    table.on_change_data(scl.update_viewport)
    
    data=[]
    for row in cur:
        column=[]
        data.append(column)

        for r in row:
            column.append(r)
                
    table.set_data(data)
    frame5.mainloop()

def personal(egs1,egs2,frame):
    p1=egs1.get()
    p2=egs2.get()
    if(p1=='piyushkedia')and(p2=='pkedia'):
       
        frame.destroy()
        frame7=Frame(root,width=1400,height=700)
        frame7.pack(expand=True)
        img=ImageTk.PhotoImage(Image.open('C:\\images\\pixal.jpg'))
        lg1=Label(frame7,image=img)
        lg1.image=img
        lg1.place(x=0,y=0)

        
        x="Welcome To Detail Page"
        lg2=Label(frame7,text=x.center(80),bg='light gray',fg='dark blue',font=('times',38,'bold','underline'),width=42)
        lg2.place(x=0,y=0)

        lg3=Label(frame7,text='Account No.',bg='light gray',fg='black',font=('times',20,'bold'),width=15)
        lg3.place(x=620,y=180)

        eg1=Entry(frame7,bg='white',bd=6,fg='black',font=('arial',17),width=19)
        eg1.place(x=900,y=180)


        bgp1=Button(frame7,text='View All Detail',bg='dark gray',bd=9,command=lambda:alldetail(frame7),fg='black',font=('times',19,'bold'),width=12)
        bgp1.place(x=79,y=156)

        bgp1=Button(frame7,text='Detail',bg='dark gray',bd=9,command=lambda:alldetail(frame7),fg='black',font=('times',19,'bold'),width=7)
        bgp1.place(x=840,y=340)


        bgp3=Button(frame7,text='Back',bg='dark gray',bd=9,command=lambda:exit1(egs1,egs2,frame7),fg='black',font=('times',19,'bold'),width=7)
        bgp3.place(x=80,y=520)

    else:
         msg.showinfo('TITLE',"password incorrect")

def bal(frame,ldd1,eg1,eg2):
    frame.destroy()
    frame18=Frame(root,width=1400,height=700)
    frame18.pack(expand=True)
    img=ImageTk.PhotoImage(Image.open('C:\\images\\pixal.jpg'))
    lb1=Label(frame18,image=img)
    lb1.image=img
    lb1.place(x=0,y=0)
    submit1(eg1,eg2,edd1)
        
def debit(frame,eg1,eg2):
    frame.destroy()
    frame8=Frame(root,width=1400,height=700)
    frame8.pack(expand=True)
    img=ImageTk.PhotoImage(Image.open('C:\\images\\pixal.jpg'))
    ldd1=Label(frame8,image=img)
    ldd1.image=img
    ldd1.place(x=0,y=0)

    ldd2=Label(frame8,text='Enter amount ',bg='light gray',fg='black',font=('arial',20,'bold'),width=22)
    ldd2.place(x=120,y=180)
    edd1=Entry(frame8,bg='white',bd=6,fg='black',font=('arial',17),width=19)
    edd1.place(x=130,y=280)
    bdd1=Button(frame8,text='Confirm',bg='dark gray',bd=9,command=lambda: bal(frame8,edd1,eg1,eg2),fg='black',font=('arial',17,'bold'),width=7)
    bdd1.place(x=80,y=420)
    bdd2=Button(frame8,text='Back',bg='dark gray',bd=9,command=lambda:bk(frame8,eg1,eg2),fg='black',font=('arial',17,'bold'),width=7)
    bdd2.place(x=80,y=520)

def credit(frame,eg1,eg2):
    frame.destroy()
    frame9=Frame(root,width=1400,height=700)
    frame9.pack(expand=True)
    img=ImageTk.PhotoImage(Image.open('C:\\images\\pixal.jpg'))
    ldc1=Label(frame9,image=img)
    ldc1.image=img
    ldc1.place(x=0,y=0)

    ldc2=Label(frame9,text='Enter amount ',bg='light gray',fg='black',font=('arial',20,'bold'),width=22)
    ldc2.place(x=120,y=180)
    edc1=Entry(frame9,bg='white',bd=6,fg='black',font=('arial',17),width=19)
    edc1.place(x=130,y=280)
    bdc3=Button(frame9,text='Confirm',bg='dark gray',bd=9,command=lambda:exit1(frame9,edc1,eg1,eg2),fg='black',font=('arial',17,'bold'),width=7)
    bdc3.place(x=80,y=420)
    bdc1=Button(frame9,text='Back',bg='dark gray',bd=9,command=lambda:bk(frame9,eg1,eg2),fg='black',font=('arial',17,'bold'),width=7)
    bdc1.place(x=80,y=520)
    
        
def checkbal(frame,eg1,eg2):
    t1=eg1.get()
    t2=eg2.get()
    

    ldcb2=Label(frame10,text='Balance is : ',bg='light gray',fg='black',font=('arial',20,'bold'),width=22)
    ldcb2.place(x=120,y=180)
    bdcb3=Button(frame10,text='Back',bg='dark gray',bd=9,command=lambda:account(frame10,t1,t2),fg='black',font=('arial',17,'bold'),width=7)
    bdcb3.place(x=80,y=520)


def submit1(eg1,eg2,edd1):
    t1=eg1.get()
    t2=eg2.get()
    t3=eg3.get()
    conn=sq.connect('bank.db')
    #conn.execute('''create table if not exists bankdetail(Email INTVAR,Password INTVAR,Balance INTGER)''')
    #conn.execute('''insert into bankdetail values(?,?,?)''',(t1,t2,int(t3)))
    #conn.commit()
    #conn.close()    
   
    
def account(frame,eg1,eg2):
    
    email=eg1.get()
    password=eg2.get()
    conn=sq.connect('bank.db')
    cur=conn.execute('select Name,Email,Password from banking')
    f=0
    for i in cur:
        
        if(i[1]==email and i[2]==password) :
            s=i[0]
            f=1
            
            break
        
    if(f==1):
            msg.showinfo('Title','Login sucess...')
           
            frame.destroy()
            frame3=Frame(root,width=1400,height=700)
            frame3.pack(expand=True)
            img=ImageTk.PhotoImage(Image.open('C:\\images\\pixal.jpg'))
            lg1=Label(frame3,image=img)
            lg1.image=img
            lg1.place(x=0,y=0)
            
            conn=sq.connect('bank.db')
            p="Welcome to bank your account"   
            lsu2=Label(frame3,text=p.center(82),bg='light gray',fg='black',font=('times',38,"underline"))
            lsu2.place(x=0,y=2)
            lsu2=Label(frame3,text="Welcome  " +s.capitalize(),fg='red',font=('times',28,"underline",))
            lsu2.place(x=0,y=80)

               
            bsu1=Button(frame3,text='Credit',bg='dark gray',bd=11,command=lambda:credit(frame3,eg1,eg2),fg='black',font=('times',20,'bold'),width=12)
            bsu1.place(x=70,y=160)

            bsu2=Button(frame3,text='Debit',bg='dark gray',bd=11,command=lambda:debit(frame3,eg1,eg2),fg='black',font=('times',20,'bold'),width=12,height=1)
            bsu2.place(x=70,y=260)

            bsu3=Button(frame3,text='Check Balance',bg='dark gray',bd=11,command=lambda:checkbal(frame3,eg1,eg2),fg='black',font=('times',20,'bold'),width=13)
            bsu3.place(x=980,y=160)

            bsu4=Button(frame3,text='Mini Statement',bg='dark gray',bd=11,command=lambda:login(frame3,eg1,eg2),fg='black',font=('times',19,'bold'),width=13)
            bsu4.place(x=980,y=260)

            bsu5=Button(frame3,text='Logout',bg='red',bd=11,command=lambda:logout(frame3),fg='black',font=('times',20,'bold'),width=7)
            bsu5.place(x=40,y=560)
    else:
            msg.showwarning('Title','Incorrect Username or Password')
        
def success(frame):
    msg.showinfo('TITLE',"incorrect password??")
    


def submit(frame2,es1,es2,es3,es4,es5,es6,es7,es8,es9):
    t1=es1.get()
    t2=es2.get()
    t3=es3.get()
    t4=es4.get()
    t5=es5.get()
    t6=es6.get()
    t7=es7.get()
    t8=es8.get()
    t9=es9.get()
    
    if (t7!=t8):
        msg.showwarning('TITLE',"password incorrect")
    elif (len(t7)<6):
        msg.showwarning('TITLE',"password is too short")
        
    else :
        
        conn=sq.connect('bank.db')
        conn.execute('''create table if not exists banking(Name Text,Fathers name Text,Email INTVAR,Mob_no INTERGER,Address INTVAR,Gender Text,Password INTVAR,Confirm Pass INTVAR,Field TEXT)''')
        conn.execute('''insert into banking values(?,?,?,?,?,?,?,?,?)''',(t1,t2,t3,int(t4),t5,t6,t7,t8,t9))
        conn.commit()
        conn.close()    
        msg.showinfo('TITLE',"succefully updated")
        login(frame2)
        
def login(frame):
    frame.destroy()
    frame1=Frame(root,width=1400,height=700)
    frame1.pack(expand=True)
    img=ImageTk.PhotoImage(Image.open('C:\\images\\pixal.jpg'))
    lg1=Label(frame1,image=img)
    lg1.image=img
    lg1.place(x=0,y=0)

    lg2=Label(frame1,text='Welcome  To  Login  Page  ',bg='light gray',fg='black',font=('times',38,"bold",'underline'),width=42)
    lg2.place(x=0,y=0)

    lg3=Label(frame1,text='Email or Phone',bg='light gray',fg='black',font=('times',18,"bold",'italic'),width=15)
    lg3.place(x=620,y=220)

    eg1=Entry(frame1,bg='white',bd=6,fg='black',font=('times',16,"bold",'italic'),width=20)
    eg1.place(x=900,y=220)

    lg4=Label(frame1,text='Password',bg='light gray',fg='black',font=('times',18,"bold",'italic'),width=15)
    lg4.place(x=620,y=280)


    eg2=Entry(frame1,bg='white',show='*',bd=6,fg='black',font=('times',16,"bold",'italic'),width=20)
    eg2.place(x=900,y=280)
    
    bg1=Button(frame1,text='Submit',bg='dark gray',bd=9,command=lambda:account(frame1,eg1,eg2),fg='black',font=('times',16,"bold",'italic'),width=7)
    bg1.place(x=840,y=400)
    bg1.bind('<Button>',speak)


    bg2=Button(frame1,text='Forget Password???',bg='light gray',bd=4,command=lambda:mails(frame1,eg1),fg='black',font=('times',10,"bold",'italic'),width=18,height=1)
    bg2.place(x=830,y=500)

    bg3=Button(frame1,text='Back',bg='dark gray',bd=9,command=lambda:exit(frame1),fg='black',font=('times',16,"bold",'italic'),width=7)
    bg3.place(x=80,y=520)



def signup(frame):
    frame.destroy()
    frame2=Frame(root,width=1400,height=700)
    frame2.pack(expand=True)
    img=ImageTk.PhotoImage(Image.open('C:\\images\\sbicb.png'))
    ls1=Label(frame2,image=img)
    ls1.image=img
    ls1.place(x=0,y=0)
    s="Welcome To Signup Page "
    ls9=Label(frame2,text=s.center(84),bg='light gray',fg='black',font=('times',38,'bold','underline'),width=42)
    ls9.place(x=0,y=0)


    
    ls2=Label(frame2,text='Name',fg='black',bg='light gray',font=("times",18,"bold",'italic'),width=11)
    ls2.place(x=90,y=101)

    ls3=Label(frame2,text="Father's Name",fg='black',bg='light gray',font=('times',18,"bold",'italic'),width=12)
    ls3.place(x=85,y=152)

    ls4=Label(frame2,text='Email',fg='black',bg='light gray',font=('times',18,"bold",'italic'),width=11)
    ls4.place(x=90,y=202)

    ls5=Label(frame2,text='Mob_no.',fg='black',bg='light gray',font=('times',18,"bold",'italic'),width=11)
    ls5.place(x=90,y=252)

    ls6=Label(frame2,text='Address',fg='black',bg='light gray',font=('times',18,"bold",'italic'),width=11)
    ls6.place(x=90,y=302)

    ls7=Label(frame2,text='Gender',fg='black',bg='light gray',font=('times',18,"bold",'italic'),width=11)
    ls7.place(x=90,y=352)

   
    ls8=Label(frame2,text='Password',fg='black',bg='light gray',font=('times',18,"bold",'italic'),width=11)
    ls8.place(x=90,y=402)

    
    ls9=Label(frame2,text='Confirm Pass',fg='black',bg='light gray',font=('times',18,"bold",'italic'),width=11)
    ls9.place(x=90,y=452)

    ls10=Label(frame2,text='Field',fg='black',bg='light gray',font=('times',18,"bold",'italic'),width=11)
    ls10.place(x=90,y=503)
    
    es1=Entry(frame2,fg='blue',bd=6,bg='white',font=('times',16,"bold",'italic'))
    es1.place(x=280,y=100)

    es2=Entry(frame2,fg='blue',bd=6,bg='white',font=('times',16,"bold",'italic'))
    es2.place(x=280,y=150)

    es3=Entry(frame2,fg='blue',bd=6,bg='white',font=('times',16,"bold",'italic'))
    es3.place(x=280,y=200)

    es4=Entry(frame2,fg='blue',bd=6,bg='white',font=('times',16,"bold",'italic'))
    es4.place(x=280,y=250)

    es5=Entry(frame2,fg='blue',bd=6,bg='white',font=('times',16,"bold",'italic'))
    es5.place(x=280,y=300)

    es6=Entry(frame2,fg='blue',bd=6,bg='white',font=('times',16,"bold",'italic'))
    es6.place(x=280,y=350)

    es7=Entry(frame2,fg='blue',show='*',bd=6,bg='white',font=('times',16,"bold",'italic'))
    es7.place(x=280,y=400)

    es8=Entry(frame2,fg='blue',show='*',bd=6,bg='white',font=('times',16,"bold",'italic'))
    es8.place(x=280,y=450)

    var=StringVar()
    var.set('ACCOUNT TYPE')
    es9=OptionMenu(frame2,var,'   SAVING   ACCOUNT  ','  CURRENT  ACCOUNT  ',)
    es9.config(font=('times',12,"bold",'italic'),bg='light gray',bd=6,width=23)
    es9.place(x=280,y=500)

    bs1=Button(frame2,text='Submit',bg='dark gray',bd=9,command=lambda:submit(frame2,es1,es2,es3,es4,es5,es6,es7,es8,var),fg='black',font=('times',16,"bold",'italic'),width=7)
    bs1.place(x=970,y=580)

    bs2=Button(frame2,text='Back',bg='dark gray',bd=9,command=lambda:exit(frame2),fg='black',font=('times',16,"bold",'italic'),width=7)
    bs2.place(x=70,y=580)

def main(root):
    frame=Frame(root,width=1400,height=700)
    frame.pack(expand=True)
    img=ImageTk.PhotoImage(Image.open('C:\\images\\buss.jpg'))
    l1=Label(frame,image=img)
    l1.image=img
    l1.place(x=0,y=0)
    
    '''1st page'''
    n="Welcome To Bank Application"
    l2=Label(frame,text=n.center(86),bd=5,fg='black',bg='light gray',font=("times",37,'bold','underline'),width=44)
    l2.place(x=0,y=0)

    b1=Button(frame,text='Login',bg='dark gray',bd=8,command=lambda:login(frame),fg='black',font=('times',19,'bold'),width=8)
    b1.place(x=90,y=250)
    b1.bind('<Button>',speak)

    b2=Button(frame,text='Sign Up',bg='dark gray',bd=8,command=lambda:signup(frame),fg='black',font=('times',19,'bold'),width=8)
    b2.place(x=90,y=350)

    b4=Button(frame,text='Show all data',bg='dark gray',bd=8,command=lambda:show(frame,root),fg='black',font=('times',19,'bold'))
    b4.place(x=90,y=450)
    
    b3=Button(frame,text='Exit',bg='dark gray',bd=8,command=lambda:exits(frame,root),fg='black',font=('times',19,'bold'),width=8)
    b3.place(x=90,y=550)

    

main(root)
