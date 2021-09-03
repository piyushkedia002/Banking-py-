from tkinter import *
import socket
from tkinter import messagebox as msg
import sqlite3 as sq
from PIL import ImageTk,Image
import scrolling_area
import time
from datetime import datetime

import smtplib                      #for mail
import os                           #for mail

import string              #for otp
import random              #random function for otp     
root=Tk()

root.title('welcome to bank application')          

##OTP page    
def mails(frame,p1):
    email=p1.get()
    if (email==''):
         msg.showwarning('Title','Enter Email ...')
    else:
        try:
            socket.create_connection(('Google.com',80))
            frame.destroy()
            frame15=Frame(root,width=1400,height=700)
            frame15.pack(expand=True)
            img=ImageTk.PhotoImage(Image.open('pixal.jpg'))
            le1=Label(frame15,image=img)
            le1.image=img
            le1.place(x=0,y=0)

            password=string.digits
            otp=""
            for var in range(6):
                otp=otp+random.choice(password)

            
            
           
            sender='piyushkedia002@gmail.com'
            reciver=email
            content=otp
            SUBJECT='OTP'
            message='Subject: {}\n\n{}'.format(SUBJECT,content)
            
            mail=smtplib.SMTP("smtp.gmail.com",587)
            mail.ehlo()
            mail.starttls()
            mail.login("piyushkedia002@gmail.com","kedia123")
            mail.sendmail(sender,reciver,message)
            mail.close()
            le2=Label(frame15,text=' Changing OTP  ',bg='light gray',fg='black',font=('times',38,"bold",'underline'),width=42)
            le2.place(x=0,y=0)

           

            le4=Label(frame15,text='Enter OTP ',bg='light gray',fg='black',font=('times',18,"bold",'italic'),width=15)
            le4.place(x=420,y=180)


            ee2=Entry(frame15,bg='white',show='*',bd=6,fg='black',font=('times',16,"bold",'italic'),width=20)
            ee2.place(x=710,y=180)

           

            
            be1=Button(frame15,text='Submit',bg='dark gray',bd=9,command=lambda:passs(frame15,ee2,otp,email),fg='black',font=('times',16,"bold",'italic'),width=7)
            be1.place(x=710,y=300)

            be2=Button(frame15,text='Back',bg='dark gray',fg='red',bd=9,command=lambda:login(frame15),font=('times',16,"bold",'italic'),width=7)
            be2.place(x=60,y=550)

        except OSError:
            time.sleep(1)
            msg.showwarning('Title','Server Problem')



##check OTP and writting password and confirm password
            
def passs(frame,ee2,otp,email):
    sp=ee2.get()
    if(otp==sp):
            msg.showinfo('Title','you entered correctly')
            frame.destroy()
            frame1=Frame(root,width=1400,height=700)
            frame1.pack(expand=True)
            img=ImageTk.PhotoImage(Image.open('pixal.jpg'))
            lg1=Label(frame1,image=img)
            lg1.image=img
            lg1.place(x=0,y=0)

            lg2=Label(frame1,text='enter changing password ',bg='light gray',fg='black',font=('times',38,"bold",'underline'),width=42)
            lg2.place(x=0,y=0)

            ls1=Label(frame1,text='New password',bg='light gray',fg='black',font=('times',18,"bold",'italic'),width=15)
            ls1.place(x=620,y=220)

            p1=Entry(frame1,bg='white',show='*',bd=6,fg='black',font=('times',16,"bold",'italic'),width=20)
            p1.place(x=900,y=220)
            
            ls2=Label(frame1,text='confirm Password',bg='light gray',fg='black',font=('times',18,"bold",'italic'),width=15)
            ls2.place(x=620,y=280)


            p2=Entry(frame1,bg='white',show='*',bd=6,fg='black',font=('times',16,"bold",'italic'),width=20)
            p2.place(x=900,y=280)
                
            bg1=Button(frame1,text='Submit',bg='dark gray',bd=9,command=lambda:pas(frame1,p1,p2,email),fg='black',font=('times',16,"bold",'italic'),width=7)
            bg1.place(x=840,y=400)
    else:
        msg.showwarning('Title','enter correct otp')
        

##update password in database
def pas(frame1,p1,p2,email):
    pk=p1.get()
    sp=p2.get()
    frame1.destroy()
    
    frame1=Frame(root,width=1400,height=700)
    frame1.pack(expand=True)
    img=ImageTk.PhotoImage(Image.open('pixal.jpg'))
    lg1=Label(frame1,image=img)
    lg1.image=img
    lg1.place(x=0,y=0)
    if(sp==pk):
        conn=sq.connect('bank.db')
        
        cursor=conn.execute("UPDATE banking SET Password='"+pk+"' WHERE Email='"+email+"'")
        print(cursor.fetchall())
        conn.commit()
        conn.close()
        login(frame1)
    else:
         msg.showinfo('Title','not correct')
        
        
            
def exit(frame):
    frame.destroy()
    main(root)
    
def lout(frame):
    x=msg.askquestion('Confirm','Are you sure?')
    if (x=='yes'):
 
        show (frame)
    

def logout(frame):
    x=msg.askquestion('Confirm','Are you sure?')
    if (x=='yes'):
        time.sleep(1)
        login(frame)
    
def exits(frame,root):
    x=msg.askquestion('Confirm','Are you sure?')
    if (x=='yes'):
        frame.destroy()
        
        root.destroy()
    

def bk(frame,eg1,eg2):
    frame.destroy()
    account(frame,eg1,eg2)

##writting email password of manager
def show (frame):
    frame.destroy()
    frame6=Frame(root,width=1400,height=700)
    frame6.pack(expand=True)
    img=ImageTk.PhotoImage(Image.open('pixal.jpg'))
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


##check detail of one person by acc no.
def fulldetail(eg1,frame):
    acc1=eg1.get()
    if (acc==""):
        msg.showwarning('Title','Enter Acc._no')
    else:
            
       
        conn=sq.connect('bank.db')
        cur=conn.execute("select * from banking WHERE Acc_no='"+acc1+"'")
        f=0
        for i in cur:
            
            
            Acc_no =i[0]
            Name =i[1]
            Fathers_name =i[2]
            email =i[3]
            Mobile_no =i[4]
            Address =i[5]
            Gender =i[6]
            field =i[8]
            Balance =i[9]
            f=1

        if (f==1):
            frame.destroy()
            frame=Frame(root,bg='gray',width=1400,height=700)
            frame.place(x=0,y=0)
            
            lg2=Label(frame,text="Personal  Details ",fg='black',bg='gray',font=('times',32,'bold'))
            lg2.place(x=460,y=2)

            lg2=Label(frame,text="Account no : "+str(Acc_no),bg='gray',fg='black',font=('times',21,'bold'))
            lg2.place(x=60,y=140)
            lg3=Label(frame,text="Name : "+str(Name.capitalize()),bg='gray',fg='black',font=('times',20,'bold'))
            lg3.place(x=60,y=180)
            lg4=Label(frame,text='Fathers_name : '+str(Fathers_name.capitalize()),bg='gray',fg='black',font=('times',20,'bold'))
            lg4.place(x=60,y=220)
            lg5=Label(frame,text="Email : "+str(email),bg='gray',fg='black',font=('times',20,'bold'))
            lg5.place(x=60,y=260)
            lg6=Label(frame,text="Moblie_no : "+str(Mobile_no),bg='gray',fg='black',font=('times',20,'bold'))
            lg6.place(x=60,y=300)
            lg7=Label(frame,text="Address : "+str(Address),bg='gray',fg='black',font=('times',20,'bold'))
            lg7.place(x=60,y=340)
            lg8=Label(frame,text="Gender : "+str(Gender),bg='gray',fg='black',font=('times',20,'bold'))
            lg8.place(x=60,y=380)
            lg9=Label(frame,text='Field : '+str(field.capitalize()),bg='gray',fg='black',font=('times',20,'bold'))
            lg9.place(x=60,y=420)
            lg10=Label(frame,text="Balance : "+str(Balance),bg='gray',fg='black',font=('times',20,'bold'))
            lg10.place(x=60,y=460)
            bgs1=Button(frame,text='Back',bg='dark gray',bd=9,command=lambda:acc(frame),fg='black',font=('times',19,'bold'),width=7)
            bgs1.place(x=80,y=580)

            
            var1=StringVar()
            var1.set('SEARCH   BY')
            e2=OptionMenu(frame,var1,'Name','Fathers_name','Email','Mob_no','Address','Gender','Field',)
            e2.config(font=('times',13,"bold",'italic'),bg='light gray',bd=4,width=18)
            e2.place(x=860,y=150)

            e1=Entry(frame,fg='blue',bd=5,bg='white',font=('times',14,"bold",'italic'),width=19)
            e1.place(x=860,y=207)
            bs4=Button(frame,text='Update',bg='dark gray',bd=4,command=lambda:update(frame,var1,e1,acc1),fg='black',font=('times',15,"bold",'italic'),width=7)
            bs4.place(x=1100,y=185)
        else:
            msg.showwarning('Title','Acc._no Not Found')

def update(frame,var1,e1,acc1):
    t1=var1.get()
    t2=e1.get()
    if(t1=='SEARCH   BY'):
        msg.showwarning('TITLE',"Select atleast one..")
    else: 
        conn=sq.connect('bank.db')
        conn.execute("UPDATE banking SET '"+str(t1)+"'='"+str(t2)+"' WHERE Acc_no='"+str(acc1)+"'")
        conn.commit()
        conn.close()
        msg.showinfo('TITLE',"succefully updated")
        acc(frame)


## main database
            
def alldetail(frame):
    frame.destroy()
    

    conn=sq.connect('bank.db')
    cur=conn.execute('''select * from banking''')
    frame5=Frame(root,width=1400,height=700)
    frame5.pack(expand=True)
    img=ImageTk.PhotoImage(Image.open('pixal.jpg'))
    lgs1=Label(frame5,image=img)
    lgs1.image=img
    lgs1.place(x=0,y=0)
    bgs1=Button(frame5,text='Back',bg='dark gray',bd=9,command=lambda:acc(frame5),fg='black',font=('times',19,'bold'),width=7)
    bgs1.place(x=80,y=580)
    scl=scrolling_area.Scrolling_Area(frame5,height=700,width=1400)
    scl.place(x=10,y=10)
    table=scrolling_area.Table(scl.innerframe,['Acc_no','Name','Fathers_name','Email','Mobile no','Address','Gender','Password','field','Balance'],column_minwidths=[100,120,130,130,130,130,110,130,120,120])
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

## ministatement Database
    
def ministatement(frame):
    frame.destroy()

    conn=sq.connect('mini.db')
    cur=conn.execute('''select * from statement''')
    frame5=Frame(root,width=1400,height=700)
    frame5.pack(expand=True)
    img=ImageTk.PhotoImage(Image.open('pixal.jpg'))
    lgs1=Label(frame5,image=img)
    lgs1.image=img
    lgs1.place(x=0,y=0)
    bgs1=Button(frame5,text='Back',bg='dark gray',bd=9,command=lambda:acc(frame5),fg='black',font=('times',19,'bold'),width=7)
    bgs1.place(x=80,y=580)
    scl=scrolling_area.Scrolling_Area(frame5,height=700,width=1400)
    scl.place(x=10,y=10)
    table=scrolling_area.Table(scl.innerframe,['Acc_no','Name','Tranction_1 ','Tranction_2','Tranction_3 ','Email'],column_minwidths=[100,180,200,200,200,20])
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

def pin(frame):
    frame.destroy()

    conn=sq.connect('pass.db')
    cur=conn.execute('''select * from pingen''')
    frame5=Frame(root,width=1400,height=700)
    frame5.pack(expand=True)
    img=ImageTk.PhotoImage(Image.open('pixal.jpg'))
    lgs1=Label(frame5,image=img)
    lgs1.image=img
    lgs1.place(x=0,y=0)
    bgs1=Button(frame5,text='Back',bg='dark gray',bd=9,command=lambda:acc(frame5),fg='black',font=('times',19,'bold'),width=7)
    bgs1.place(x=80,y=580)
    scl=scrolling_area.Scrolling_Area(frame5,height=700,width=1400)
    scl.place(x=10,y=10)
    table=scrolling_area.Table(scl.innerframe,['Acc_no','Name','Pin'],column_minwidths=[350,400,250])
    table.pack(expand=True,fill=X)
    table.on_change_data(scl.update_viewport)
    
    data=[]
    for row in cur:
        column=[]
        data.append(column)

        for r in row:
            column.append(r)
    
    table.set_data(data)
    conn.commit()
    conn.close
    frame5.mainloop()

    
##check condition for manager page
    
def personal(egs1,egs2,frame):

    p1=egs1.get()
    
    p2=egs2.get()
    if(p1=='')or(p2==''):
        msg.showwarning('TITLE'," Enter  Details ")
        
    else:
        
        if(p1=='piyushkedia')and(p2=='pkedia'):
            acc(frame)

        else:
             msg.showinfo('TITLE',"Email or Password incorrect")

##Manager page
             
def acc(frame):
    
    frame.destroy()
    frame7=Frame(root,width=1400,height=700)
    frame7.pack(expand=True)
    img=ImageTk.PhotoImage(Image.open('pixal.jpg'))
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

    bgp1=Button(frame7,text='ministatement',bg='dark gray',bd=9,command=lambda:ministatement(frame7),fg='black',font=('times',19,'bold'),width=12)
    bgp1.place(x=79,y=246)
    
    bgp1=Button(frame7,text=' Pin ',bg='dark gray',bd=9,command=lambda:pin(frame7),fg='black',font=('times',19,'bold'),width=7)
    bgp1.place(x=80,y=336)

        
    bgp1=Button(frame7,text='Submit',bg='dark gray',bd=9,command=lambda:fulldetail(eg1,frame7),fg='black',font=('times',19,'bold'),width=7)
    bgp1.place(x=900,y=300)


    bgp3=Button(frame7,text='Back',bg='dark gray',bd=9,command=lambda:lout(frame7),fg='black',font=('times',19,'bold'),width=7)
    bgp3.place(x=80,y=520)


##Mini Statement Page
def lasttransaction(frame,a,n):
    frame.destroy()
    frame8=Frame(root,width=1400,height=700)
    frame8.pack(expand=True)
    img=ImageTk.PhotoImage(Image.open('pixal.jpg'))
    lb1=Label(frame8,image=img)
    lb1.image=img
    lb1.place(x=0,y=0)
    

    conn=sq.connect('mini.db')
    data=conn.execute(" select Tranction_1,Tranction_2,Tranction_3  from statement Where Acc_no='"+str(a)+"'")
    for i in data:
        T1=i[0]
        T2=i[1]
        T3=i[2]
    conn.commit()
    conn.close

    
    lg2=Label(frame8,text='MINI STATEMENT ',bg='light gray',fg='black',font=('times',38,"bold",'underline'),width=42)
    lg2.place(x=0,y=0)

    l2=Label(frame8,text=T1,bg='light gray',fg='black',font=('arial',19,'bold'))
    l2.place(x=120,y=120)
    
    l3=Label(frame8,text=T2,bg='light gray',fg='black',font=('arial',19,'bold'))
    l3.place(x=120,y=200)

    l4=Label(frame8,text=T3,bg='light gray',fg='black',font=('arial',19,'bold'))
    l4.place(x=120,y=280)

    b1=Button(frame8,text='Back',bg='dark gray',bd=9,command=lambda:owner(frame8,a,n),fg='black',font=('arial',17,'bold'),width=7)
    b1.place(x=80,y=520)

        
##debit page        
def debit(frame,a,n):
    frame.destroy()
    frame9=Frame(root,width=1400,height=700)
    frame9.pack(expand=True)
    img=ImageTk.PhotoImage(Image.open('pixal.jpg'))
    l1=Label(frame9,image=img)
    l1.image=img
    l1.place(x=0,y=0)

    x="Welcome To Transaction Page"
    lg2=Label(frame9,text=x.center(80),bg='light gray',fg='dark blue',font=('times',38,'bold','underline'),width=42)
    lg2.place(x=0,y=0)
    l2=Label(frame9,text='Enter withdrawal amount ',bg='light gray',fg='black',font=('arial',20,'bold'),)
    l2.place(x=100,y=180)
    e1=Entry(frame9,bg='white',bd=6,fg='black',font=('arial',17),width=19)
    e1.place(x=450,y=180)
    l3=Label(frame9,text='Enter Pin',bg='light gray',fg='black',font=('arial',20,'bold'))
    l3.place(x=110,y=250)
    e2=Entry(frame9,show="*",bg='white',bd=6,fg='black',font=('arial',17),width=19)
    e2.place(x=450,y=250)
    b3=Button(frame9,text='Confirm',bg='dark gray',bd=9,command=lambda:pincheckdebit(frame9,a,e1,e2,n),fg='black',font=('arial',17,'bold'),width=7)
    b3.place(x=80,y=420)
    b1=Button(frame9,text='Back',bg='dark gray',bd=9,command=lambda:owner(frame9,a,n),fg='black',font=('arial',17,'bold'),width=7)
    b1.place(x=80,y=520)

## check pin on debit side
def pincheckdebit(frame9,a1,rs,e2,n):
    pin=int(e2.get())
    if (rs.get()):
    
        conn=sq.connect('pass.db')
        cur1=conn.execute("select Pin from pingen  WHERE Acc_no='"+str(a1)+"'")
        for i in cur1:
            p1=i[0]
        
        p1=int(p1)
        conn.commit()
        conn.close()
            
        if(pin==p1):
            debitback(frame9,a1,rs,n)
        else:
            msg.showwarning('Title','incorrect pin')
            
    else:
        msg.showwarning('Title','Enter amount')


##Debit back coding update in bank
def debitback(frame,a1,rs,n):
    if rs.get():
        try:
            socket.create_connection(('Google.com',80))
        
            rs=int(rs.get())
            
            conn=sq.connect('bank.db')
            cur1=conn.execute("select Balance,Email from banking WHERE Acc_no='"+str(a1)+"'") 
            for i in cur1:
                b1=i[0]
                email=i[1]
            
            z1=b1-rs
            if (z1<0):
                 msg.showwarning('TITLE',"Unsufficent Balance")
                 debitback(frame,a1,rs,n)

            else:
                s1=b1-rs
                
                cur4=conn.execute("UPDATE banking SET Balance='"+str(s1)+"' WHERE Acc_no='"+str(a1)+"'")
                conn.commit()
                conn.close()


            conn=sq.connect('mini.db')
            data=conn.execute(" select * from statement Where Acc_no='"+str(a1)+"'")

            now=datetime.now()
            x=now.strftime("%d-%m-%Y")
            y=now.strftime("%H:%M:%S")
            
            for i in data:
                T1=i[2]
                T2=i[3]
                T3=i[4]
            
            if (T1==None):
                conn.execute("update  statement set Tranction_1= 'Dear A/c Holder,ur A/c-"+str(a1)+"\ndebited by Rs"+str(rs)+" on "+str(x)+"' where Acc_no='"+str(a1)+"'")
                conn.commit()
                conn.close

            elif (T2==None) :
                
                conn.execute("update  statement set Tranction_2= 'Dear A/c Holder,ur A/c-"+str(a1)+"\ndebited by Rs"+str(rs)+" on "+str(x)+"' where Acc_no='"+str(a1)+"'")
                conn.commit()
                conn.close

            elif  (T3==None):
                conn.execute("update  statement set Tranction_3= 'Dear A/c Holder,ur A/c-"+str(a1)+"\ndebited by Rs"+str(rs)+" on "+str(x)+"' where Acc_no='"+str(a1)+"'")
                conn.commit()
                conn.close

                
            else:
                conn.execute("update  statement set Tranction_1= '"+str(T2)+"' where Acc_no='"+str(a1)+"'")
                conn.execute("update  statement set Tranction_2= '"+str(T3)+"' where Acc_no='"+str(a1)+"'")
                conn.execute("update  statement set Tranction_3= 'Dear A/c Holder,ur A/c-"+str(a1)+"\ndebited by Rs"+str(rs)+" on "+str(x)+"' where Acc_no='"+str(a1)+"'")
                conn.commit()
                conn.close

       
            sender='piyushkedia002@gmail.com'
            reciver=email
            SUBJECT="Balance Debited "
            content="Dear A/c Holder,ur A/c-"+str(a1)+"\ndebited by Rs"+str(rs)+"\n on"+str(x)
            message='Subject: {}\n\n{}'.format(SUBJECT,content)
            mail=smtplib.SMTP("smtp.gmail.com",587)
            mail.ehlo()
            mail.starttls()
            mail.login("piyushkedia002@gmail.com","kedia123")
            mail.sendmail(sender,reciver,message)
            mail.close()
            msg.showinfo('Title','Balance Withdraw successfully')
            
            owner(frame,a1,n)

        except OSError:
            time.sleep(1)
            msg.showwarning('Title','Server Problem')

    else:
        msg.showwarning('Title','Enter amount')
        
##credit page
def credit(frame,a,n):
    frame.destroy()
    frame9=Frame(root,width=1400,height=700)
    frame9.pack(expand=True)
    img=ImageTk.PhotoImage(Image.open('pixal.jpg'))
    l1=Label(frame9,image=img)
    l1.image=img
    l1.place(x=0,y=0)

    x="Welcome To Transaction Page"
    lg2=Label(frame9,text=x.center(80),bg='light gray',fg='dark blue',font=('times',38,'bold','underline'),width=42)
    lg2.place(x=0,y=0)
    l2=Label(frame9,text='Enter Deposit Amount',bg='light gray',fg='black',font=('arial',20,'bold'))
    l2.place(x=120,y=180)
    e1=Entry(frame9,bg='white',bd=6,fg='black',font=('arial',17),width=19)
    e1.place(x=430,y=180)

    l3=Label(frame9,text='Enter Pin',bg='light gray',fg='black',font=('arial',20,'bold'))
    l3.place(x=120,y=250)
    e2=Entry(frame9,show="*",bg='white',bd=6,fg='black',font=('arial',17),width=19)
    e2.place(x=430,y=250)
    b3=Button(frame9,text='Confirm',bg='dark gray',bd=9,command=lambda: pincheckcredit(frame9,a,e1,e2,n),fg='black',font=('arial',17,'bold'),width=7)
    b3.place(x=80,y=420)
    b1=Button(frame9,text='Back',bg='dark gray',bd=9,command=lambda:owner(frame9,a,n),fg='black',font=('arial',17,'bold'),width=7)
    b1.place(x=80,y=520)


## check pin of credit side
def pincheckcredit(frame9,a1,rs,e2,n):
    pin=int(e2.get())
    if (rs.get()):
    
        conn=sq.connect('pass.db')
        cur1=conn.execute("select Pin from pingen  WHERE Acc_no='"+str(a1)+"'")
        for i in cur1:
            p1=i[0]
        
        p1=int(p1)
        conn.commit()
        conn.close()
            
        if(pin==p1):
            creditback(frame9,a1,rs,pin,n)
        else:
            msg.showwarning('Title','incorrect pin')
            
    else:
        msg.showwarning('Title','Enter amount')


###credit update in bank
        
def creditback(frame,a1,rs,pin,n):
    
    
        try:
            socket.create_connection(('Google.com',80))
        
            rs=int(rs.get())
            conn=sq.connect('bank.db')
            cur1=conn.execute("select Balance,Email from banking WHERE Acc_no='"+str(a1)+"'") 
            for i in cur1:
                b1=i[0]
                email=i[1]

            s1=b1+rs
            cur4=conn.execute("UPDATE banking SET Balance='"+str(s1)+"' WHERE Acc_no='"+str(a1)+"'")
            conn.commit()
            conn.close()

            conn=sq.connect('mini.db')
            data=conn.execute(" select * from statement Where Acc_no='"+str(a1)+"'")

            now=datetime.now()
            x=now.strftime("%d-%m-%Y")
            y=now.strftime("%H:%M:%S")

            conn=sq.connect('mini.db')
            data=conn.execute(" select * from statement Where Acc_no='"+str(a1)+"'")
            for i in data:
                T1=i[2]
                T2=i[3]
                T3=i[4]
                
            if(T1==None):
                conn.execute("update  statement set Tranction_1= 'Dear A/c Holder,ur A/c-"+str(a1)+"\ncredited by Rs"+str(rs)+" on "+str(x)+"' where Acc_no='"+str(a1)+"'")
                conn.commit()
                conn.close()

            elif (T2==None) :
                
                conn.execute("update  statement set Tranction_2= 'Dear A/c Holder,ur A/c-"+str(a1)+"\ncredited by Rs"+str(rs)+" on "+str(x)+"' where Acc_no='"+str(a1)+"'")
                conn.commit()
                
                conn.close()

            elif  (T3==None):
                conn.execute("update  statement set Tranction_3= 'Dear A/c Holder,ur A/c-"+str(a1)+"\ncredited by Rs"+str(rs)+" on "+str(x)+"' where Acc_no='"+str(a1)+"'")
                conn.commit()
                conn.close()

            else:
                conn.execute("update  statement set Tranction_1= '"+str(T2)+"' where Acc_no='"+str(a1)+"'")
                conn.execute("update  statement set Tranction_2= '"+str(T3)+"' where Acc_no='"+str(a1)+"'")
                conn.execute("update  statement set Tranction_3= 'Dear A/c Holder,ur A/c-"+str(a1)+"\ncredited by Rs"+str(rs)+" on "+str(x)+"' where Acc_no='"+str(a1)+"'")
                conn.commit()
                conn.close()


       
            sender='piyushkedia002@gmail.com'
            reciver=email
            SUBJECT="Balance Credited "
            content="Dear A/c Holder,ur A/c-"+str(a1)+"\ndebited by Rs"+str(rs)+"\n on"+str(x)
            message='Subject: {}\n\n{}'.format(SUBJECT,content)
            mail=smtplib.SMTP("smtp.gmail.com",587)
            mail.ehlo()
            mail.starttls()
            mail.login("piyushkedia002@gmail.com","kedia123")
            mail.sendmail(sender,reciver,message)
            mail.close()

            msg.showinfo('Title','Balance Credit successfully')
            owner(frame,a1,n)

        except OSError:
            time.sleep(1)
            msg.showwarning('Title','Server Problem')




def checkbal(frame,a,n):

    frame1=Frame(frame,width=350,height=400,bg="dark gray")
    frame1.pack(expand=True)
    frame1.place(x=600,y=150)

    p="Check Balance"
    l2=Label(frame1,text=p.center(38),bd=5,fg='black',bg='dark gray',font=("times",20,'bold','underline'))
    l2.place(x=0,y=0)


    lg4=Label(frame1,text='Pin',bg='dark gray',fg='black',font=('times',18,"bold",'italic'))
    lg4.place(x=15,y=115)


    eg2=Entry(frame1,bg='white',show='*',bd=3,fg='black',font=('times',18,"bold",'italic'),width=20)
    eg2.place(x=15,y=160)
    
    bg1=Button(frame1,text='Submit',bg='blue',bd=3,command=lambda:balance(frame,frame1,a,n,eg2),fg='white',font=('times',12,"bold",'italic'),width=20)
    bg1.place(x=15,y=270)
    
    b1=Button(frame1,text='X',bg='red',bd=2,command=lambda:frame1.destroy(),fg='white',font=("times",10,'bold'))
    b1.place(x=330,y=1)
 

## Balance check
def balance(frame,frame1,a,n,pin):
    
    pin=int(pin.get())
    conn=sq.connect('pass.db')
    cur1=conn.execute("select Pin from pingen  WHERE Acc_no='"+str(a)+"'")
    for i in cur1:
        p1=i[0]
        
    p1=int(p1)
    conn.commit()
    conn.close()
            
    if(pin==p1):
        

        try:
            socket.create_connection(('Google.com',80))
            frame1.destroy()
            frame9=Frame(frame,width=350,height=400,bg="dark gray")
            frame9.pack(expand=True)
            frame9.place(x=600,y=150)
            a=str(a)
            socket.create_connection(('Google.com',80))    
            p="Account Balance"
            lg2=Label(frame9,text=p,bg='dark gray',fg='dark blue',font=('times',32,'bold','underline'))
            lg2.place(x=0,y=0)
            ldcb2=Label(frame9,text='Account No. : '+a,bg='dark gray',fg='black',font=('arial',18,'bold'),width=21)
            ldcb2.place(x=4,y=110)
            
            conn=sq.connect('bank.db')
            cur=conn.execute("select Balance,Email from banking WHERE Acc_no='"+a+"'")
            for i in cur:
                s=i[0]
                email=i[1]
            ldcb2=Label(frame9,text='Balance is : '+str(s),bg='dark gray',fg='black',font=('arial',18,'bold'),width=21)
            ldcb2.place(x=4,y=200)
            b1=Button(frame9,text='X',bg='red',bd=2,command=lambda:frame9.destroy(),fg='white',font=("times",10,'bold'))
            b1.place(x=330,y=1)

        
            sender='piyushkedia002@gmail.com'
            reciver=email
            SUBJECT="Account balance  "
            content="Your Balance is "+str(s)
            message='Subject: {}\n\n{}'.format(SUBJECT,content)
            mail=smtplib.SMTP("smtp.gmail.com",587)
            mail.ehlo()
            mail.starttls()
            mail.login("piyushkedia002@gmail.com","kedia123")
            mail.sendmail(sender,reciver,message)
            mail.close()
            
        except OSError:
            
            time.sleep(1)
            msg.showwarning('Title','Server Problem')
            frame1.destroy()
    else:
        msg.showwarning('Title','incorrect pin')
            



## Fund transfered update in bank    
def funding(a1,a2,amnt,n,frame):
        

        try:
            socket.create_connection(('Google.com',80))
            ##for Acc owner
            amnt=int(amnt)
            conn=sq.connect('bank.db')
            cur1=conn.execute("select Balance,Email from banking WHERE Acc_no='"+str(a1)+"'") 
            for i in cur1:
                b1=i[0]
                e1=i[1]

            b=b1-amnt
            if (b<0):
                
                msg.showwarning('TITLE',"Unsufficent Balance")
                funding(a1,a2,amnt,frame)

            else:
                s1=b1-amnt       
                conn=sq.connect('bank.db')        
                cur3=conn.execute("UPDATE banking SET Balance='"+str(s1)+"' WHERE Acc_no='"+str(a1)+"'")
                conn.commit()
                conn.close()

                conn=sq.connect('mini.db')
                data=conn.execute(" select * from statement Where Acc_no='"+str(a1)+"'")

                now=datetime.now()
                x=now.strftime("%d-%m-%Y")
                y=now.strftime("%H:%M:%S")
                
                for i in data:
                    T1=i[2]
                    T2=i[3]
                    T3=i[4]
                
                if (T1==None):
                    conn.execute("update  statement set Tranction_1= 'Dear A/c Holder,ur A/c-"+str(a1)+"\ndebited by Rs"+str(amnt)+" on "+str(x)+"' where Acc_no='"+str(a1)+"'")
                    conn.commit()
                    conn.close

                elif (T2==None) :
                    
                    conn.execute("update  statement set Tranction_2= 'Dear A/c Holder,ur A/c-"+str(a1)+"\ndebited by Rs"+str(amnt)+" on "+str(x)+"' where Acc_no='"+str(a1)+"'")
                    conn.commit()
                    conn.close

                elif  (T3==None):
                    conn.execute("update  statement set Tranction_3= 'Dear A/c Holder,ur A/c-"+str(a1)+"\ndebited by Rs"+str(amnt)+" on "+str(x)+"' where Acc_no='"+str(a1)+"'")
                    conn.commit()
                    conn.close

                    
                else:
                    conn.execute("update  statement set Tranction_1= '"+str(T2)+"' where Acc_no='"+str(a1)+"'")
                    conn.execute("update  statement set Tranction_2= '"+str(T3)+"' where Acc_no='"+str(a1)+"'")
                    conn.execute("update  statement set Tranction_3= 'Dear A/c Holder,ur A/c-"+str(a1)+"\ndebited by Rs"+str(amnt)+" on "+str(x)+"' where Acc_no='"+str(a1)+"'")
                    conn.commit()
                    conn.close

                        

            ## for other Acc
            conn=sq.connect('bank.db')
            cur2=conn.execute("select Balance,Email from banking WHERE Acc_no='"+str(a2)+"'")
            for j in cur2:
                b2=j[0]
                e2=j[1]

            s2=b2+amnt
            cur4=conn.execute("UPDATE banking SET Balance='"+str(s2)+"' WHERE Acc_no='"+str(a2)+"'")
            conn.commit()
            conn.close()

            conn=sq.connect('mini.db')
            dta=conn.execute(" select * from statement Where Acc_no='"+str(a2)+"'")

            now=datetime.now()
            x=now.strftime("%d-%m-%Y")
            y=now.strftime("%H:%M:%S")
                
            for i in dta:
                T1=i[2]
                T2=i[3]
                T3=i[4]
                
            if (T1==None):
                conn.execute("update  statement set Tranction_1= 'Dear A/c Holder,ur A/c-"+str(a2)+"\ncredited by Rs"+str(amnt)+" on "+str(x)+"' where Acc_no='"+str(a2)+"'")
                conn.commit()
                conn.close

            elif (T2==None) :
                    
                conn.execute("update  statement set Tranction_2= 'Dear A/c Holder,ur A/c-"+str(a2)+"\ncredited by Rs"+str(amnt)+" on "+str(x)+"' where Acc_no='"+str(a2)+"'")
                conn.commit()
                conn.close

            elif  (T3==None):
                conn.execute("update  statement set Tranction_3= 'Dear A/c Holder,ur A/c-"+str(a2)+"\ncredited by Rs"+str(amnt)+" on "+str(x)+"' where Acc_no='"+str(a2)+"'")
                conn.commit()
                conn.close

                    
            else:
                conn.execute("update  statement set Tranction_1= '"+str(T2)+"' where Acc_no='"+str(a2)+"'")
                conn.execute("update  statement set Tranction_2= '"+str(T3)+"' where Acc_no='"+str(a2)+"'")
                conn.execute("update  statement set Tranction_3= 'Dear A/c Holder,ur A/c-"+str(a2)+"\ncredited by Rs"+str(amnt)+" on "+str(x)+"' where Acc_no='"+str(a2)+"'")
                conn.commit()
                conn.close
          


            sender='piyushkedia002@gmail.com'
            reciver1=e1
            reciver2=e2
            SUBJECT1="Balance Debited "
            SUBJECT2="Balance Credited "
            content1="Dear A/c Holder,ur A/c-"+str(a1)+"\ndebited by Rs"+str(amnt)+"\n on"+str(x)
            content2="Dear A/c Holder,ur A/c-"+str(a2)+"\ncredited by Rs"+str(amnt)+"\n on"+str(x)
            
            message1='Subject: {}\n\n{}'.format(SUBJECT1,content1)
            message2='Subject: {}\n\n{}'.format(SUBJECT2,content2)
            mail=smtplib.SMTP("smtp.gmail.com",587)
            mail.ehlo()
            mail.starttls()
            mail.login("piyushkedia002@gmail.com","kedia123")
            mail.sendmail(sender,reciver1,message1)
            mail.sendmail(sender,reciver2,message2)
            mail.close()

            msg.showinfo('Title','Balance transfer successfully')
            owner(frame,a1,n)

        except OSError:
            
            time.sleep(1)
            msg.showwarning('Title','Server Problem')
            frame.destroy()


def pincheckfundtransfer(frame,a,a2,amnt,pin,n):
    a2=int(a2.get())
    amnt=amnt.get()

    if (a2==""):
         msg.showwarning('TITLE'," Enter Acc. no ...")

    elif (amnt==""):
         msg.showwarning('TITLE'," Enter Amount ...")

    elif (amnt==""):
         msg.showwarning('TITLE'," Enter pin ...")
    else:
        pin=int(pin.get())
      
        conn=sq.connect('pass.db')
        cur1=conn.execute("select Pin from pingen  WHERE Acc_no='"+str(a)+"'")
        for i in cur1:
                p1=i[0]
                

        conn.commit()
        conn.close()
                    
        if(pin==p1):
            
            conn=sq.connect('bank.db')
            cur1=conn.execute("select Acc_no from banking")
            flag=0
            for i in cur1:

                if(i[0]==a2):
                        flag=1
                        
            conn.commit()
            conn.close()           
            if(flag==0):
                msg.showwarning('Title','incorrect acc_no...')
            else:
                funding(a,a2,amnt,n,frame)
                
                        
            
            
                
            
        else:
             msg.showwarning('Title','incorrect pin')
      
        

##Amount transfer from 1 bank to another Fund transfer
        
def fund(frame,a,n):
    frame.destroy()
    frame3=Frame(root,width=1400,height=700)
    frame3.pack(expand=True)
    img=ImageTk.PhotoImage(Image.open('pixal.jpg'))
    lg1=Label(frame3,image=img)
    lg1.image=img
    lg1.place(x=0,y=0)

    z="Fund transer"
    l2=Label(frame3,text=z.center(86),bd=5,fg='black',bg='light gray',font=("times",37,'bold','underline'),width=44)
    l2.place(x=0,y=0)

    lg1=Label(frame3,text='Account No.',bg='light gray',fg='black',font=('times',20,'bold'),width=15)
    lg1.place(x=120,y=140)

    lg2=Label(frame3,text='Amount of transfer',bg='light gray',fg='black',font=('times',20,'bold'),width=15)
    lg2.place(x=120,y=220)

    e1=Entry(frame3,bg='white',bd=6,fg='black',font=('arial',17),width=19)
    e1.place(x=450,y=140)

    e2=Entry(frame3,bg='white',bd=6,fg='black',font=('arial',17),width=19)
    e2.place(x=450,y=220)

    lg3=Label(frame3,text='pin',bg='light gray',fg='black',font=('times',20,'bold'),width=15)
    lg3.place(x=120,y=300)
    
    e3=Entry(frame3,bg='white',show='*',bd=6,fg='black',font=('arial',20,'bold'),width=19)
    e3.place(x=450,y=300)

    bsu1=Button(frame3,text='Proceed',bg='blue',bd=10,command=lambda:pincheckfundtransfer(frame3,a,e1,e2,e3,n),fg='black',font=('times',18,'bold'),width=8)
    bsu1.place(x=870,y=560)

    bsu2=Button(frame3,text='Back',bg='red',bd=10,command=lambda:owner(frame3,a,n),fg='black',font=('times',18,'bold'),width=8)
    bsu2.place(x=70,y=560)


def pinchange(frame,a,n):
    conn=sq.connect('bank.db')
    cur1=conn.execute("select Email from banking WHERE Acc_no='"+str(a)+"'") 
    for i in cur1:
        email=i[0]

    conn.commit()
    conn.close
    password=string.digits
    otp=""
    for var in range(6):
        otp=otp+random.choice(password)

    try:
        socket.create_connection(('Google.com',80))
        sender='piyushkedia002@gmail.com'
        reciver=email
        content=otp
        SUBJECT='OTP'
        message='Subject: {}\n\n{}'.format(SUBJECT,content)
                
        mail=smtplib.SMTP("smtp.gmail.com",587)
        mail.ehlo()
        mail.starttls()
        mail.login("piyushkedia002@gmail.com","kedia123")
        mail.sendmail(sender,reciver,message)
        mail.close()

        msg.showinfo('Title','otp sent successfully')
        
        frame1=Frame(frame,width=350,height=400,bg="dark gray")
        frame1.pack(expand=True)
        frame1.place(x=550,y=150)

        b1=Button(frame1,text='X',bg='red',bd=2,command=lambda:frame1.destroy(),fg='white',font=("times",10,'bold'))
        b1.place(x=330,y=1)
        le2=Label(frame1,text='Changing OTP  ',bg='dark gray',fg='black',font=('times',23,"bold",'underline'))
        le2.place(x=20,y=0)      

        le4=Label(frame1,text='Enter OTP ',bg='dark gray',fg='black',font=('times',18,"bold",'italic'),width=15)
        le4.place(x=20,y=100)

        ee2=Entry(frame1,bg='white',show='*',bd=6,fg='black',font=('times',16,"bold",'italic'),width=20)
        ee2.place(x=20,y=155)
      
        be1=Button(frame1,text='Submit',bg='dark gray',bd=9,command=lambda:checkpinotp(frame,frame1,ee2,otp,email,a),fg='black',font=('times',16,"bold",'italic'),width=7)
        be1.place(x=50,y=280)

    except OSError:
            time.sleep(1)
            msg.showwarning('Title','Server Problem')
   

def checkpinotp(frame,frame1,ee2,otp,email,a):
    sp=ee2.get()
    if(otp==sp):
            frame1.destroy()
            frame1=Frame(frame,width=350,height=400,bg="dark gray")
            frame1.pack(expand=True)
            frame1.place(x=550,y=150)
   
            b1=Button(frame1,text='X',bg='red',bd=2,command=lambda:frame1.destroy(),fg='white',font=("times",10,'bold'))
            b1.place(x=330,y=1)
            lg2=Label(frame1,text='Pin Change',bg='dark gray',fg='black',font=('times',23,"bold",'underline'))
            lg2.place(x=0,y=0)

            ls1=Label(frame1,text='New Pin',bg='dark gray',fg='black',font=('times',18,"bold",'italic'),width=15)
            ls1.place(x=20,y=80)

            p1=Entry(frame1,bg='white',show='*',bd=6,fg='black',font=('times',16,"bold",'italic'),width=20)
            p1.place(x=20,y=120)
            
            ls2=Label(frame1,text='Confirm Pin',bg='dark gray',fg='black',font=('times',18,"bold",'italic'),width=15)
            ls2.place(x=20,y=170)

            p2=Entry(frame1,bg='white',show='*',bd=6,fg='black',font=('times',16,"bold",'italic'),width=20)
            p2.place(x=20,y=210)
                
            bg1=Button(frame1,text='Submit',bg='dark gray',bd=9,command=lambda:pinupdate(frame1,p1,p2,email,a),fg='black',font=('times',16,"bold",'italic'),width=7)
            bg1.place(x=40,y=290)
    else:
        msg.showwarning('Title','enter correct otp')
        

def pinupdate(frame1,p1,p2,email,a):
    a=str(a)
    pk=p1.get()
    sp=p2.get()
    frame1.destroy()
    
    if(sp==pk):
        conn=sq.connect('pass.db')
        
        cursor=conn.execute("UPDATE pingen SET Pin='"+pk+"' WHERE Acc_no='"+a+"'")
        print(cursor.fetchall())
        conn.commit()
        conn.close()
        
    else:
         msg.showinfo('Title','not correct')    


##check the login condition       
def account(frame,eg1,eg2):
    email=eg1.get()
    password=eg2.get()
    if (email=="")or(password==""):
        msg.showwarning('Title',' Enter  Details ...')
    else:  
        time.sleep(1)
        conn=sq.connect('bank.db')
        cur=conn.execute('select Acc_no,Name,Email,Password from banking')
        f=0
        for i in cur:
            
            if(i[2]==email and i[3]==password) :
                n=i[1]
                a=i[0]
                f=1
                
                break
            
        if(f==1):
            
                owner(frame,a,n)
                
        else:
                msg.showwarning('Title','Incorrect Username or Password')


## After login of any owner
def owner(frame,a,n):
    frame.destroy()
    frame3=Frame(root,width=1400,height=700)
    frame3.pack(expand=True)
    img=ImageTk.PhotoImage(Image.open('buss.jpg'))
    lg1=Label(frame3,image=img)
    lg1.image=img
    lg1.place(x=0,y=0)
            
    conn=sq.connect('bank.db')
    p="Welcome to bank your account"   
    lsu2=Label(frame3,text=p.center(82),bg='light gray',fg='black',font=('times',38,"underline"))
    lsu2.place(x=0,y=2)
    lsu2=Label(frame3,text="Welcome  " +n.capitalize(),fg='red',font=('times',28))
    lsu2.place(x=0,y=80)

               
    bsu1=Button(frame3,text='Credit',bg='dark gray',bd=11,command=lambda:credit(frame3,a,n),fg='black',font=('times',20,'bold'),width=12)
    bsu1.place(x=70,y=160)

    bsu2=Button(frame3,text='Debit',bg='dark gray',bd=11,command=lambda:debit(frame3,a,n),fg='black',font=('times',20,'bold'),width=12,height=1)
    bsu2.place(x=70,y=260)

    bsu3=Button(frame3,text='Check Balance',bg='dark gray',bd=11,command=lambda:checkbal(frame3,a,n),fg='black',font=('times',20,'bold'),width=13)
    bsu3.place(x=980,y=160)

    bsu4=Button(frame3,text='Mini Statement',bg='dark gray',bd=11,command=lambda:lasttransaction(frame3,a,n),fg='black',font=('times',19,'bold'),width=13)
    bsu4.place(x=980,y=260)

    bsu6=Button(frame3,text='Fund transfer',bg='dark gray',bd=11,command=lambda:fund(frame3,a,n),fg='black',font=('times',19,'bold'),width=13)
    bsu6.place(x=70,y=360)

    
    bsu6=Button(frame3,text='Pin change',bg='dark gray',bd=11,command=lambda:pinchange(frame3,a,n),fg='black',font=('times',19,'bold'),width=13)
    bsu6.place(x=980,y=360)

    bsu5=Button(frame3,text='Logout',bg='red',bd=11,command=lambda:logout(frame3),fg='black',font=('times',20,'bold'),width=7)
    bsu5.place(x=40,y=560)



            


##sign up submit and database created
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
        t10=500
        

        password=string.digits
        pin=""
        for var in range(4):
            pin=pin+random.choice(password)
        
        if (t1==""):
             msg.showwarning('TITLE',"Enter Name..")

        elif (t2==""):
             msg.showwarning('TITLE',"Enter Fathers Name..")

        
        elif (t3==""):
             msg.showwarning('TITLE',"Enter Email..")

        
        elif (t4==""):
             msg.showwarning('TITLE',"Enter Mob_no...")
            
        
        elif (t5==""):
            msg.showwarning('TITLE',"Enter Address..")

        elif (t6==""):
             msg.showwarning('TITLE',"Enter Gender...")

        elif (t7==""):
             msg.showwarning('TITLE',"Enter Password")

        elif (t9=='ACCOUNT TYPE'):
             msg.showwarning('TITLE',"Enter Password")

        else:
            
            if (t7!=t8):
                msg.showwarning('TITLE',"password incorrect")
            elif (len(t7)<6):
                msg.showwarning('TITLE',"password is too short")
                
            else :
                    
                try:
                    socket.create_connection(('Google.com',80))
                
                    conn=sq.connect('bank.db')
                    conn.execute('''create table if not exists banking(Acc_no INTEGER PRIMARY KEY AUTOINCREMENT ,Name Text,Fathers_name Text,Email INTVAR,Mob_no INTEGER,Address INTVAR,Gender Text,Password INTVAR,Field TEXT,Balance INTEGER)''')
                    conn.execute('''insert into banking(Name,Fathers_name,Email,Mob_no,Address,Gender,Password,Field,Balance) values(?,?,?,?,?,?,?,?,?)''',(t1,t2,t3,int(t4),t5,t6,t7,t9,t10))
                    conn.commit()
                    conn.close()    
                    


                    conn=sq.connect('mini.db')
                    conn.execute('''create table if not exists statement(Acc_no INTEGER PRIMARY KEY AUTOINCREMENT,Name Text,Tranction_1 INTVAR,Tranction_2 INTVAR,Tranction_3 INTVAR,Email INTVAR)''') 
                    conn.execute('''insert into statement(Name,Email) values(?,?)''',(t1,t3))
                    conn.commit()
                    conn.close()

                    
                    conn=sq.connect('pass.db')
                    conn.execute('''create table if not exists pingen(Acc_no INTEGER PRIMARY KEY AUTOINCREMENT,Name Text,pin INTEGER)''') 
                    conn.execute('''insert into pingen(Name,Pin) values(?,?)''',(t1,pin))
                    conn.commit()
                    conn.close()

                    pinsend(frame2,t3,pin,t1)
                    msg.showinfo('TITLE',"succefully updated")

                except OSError:
                    
                    time.sleep(1)
                    msg.showwarning('Title','Server Problem')


def pinsend(frame,email,pin,t1):
    
    try:
        socket.create_connection(('Google.com',80))

        sender='piyushkedia002@gmail.com'
        reciver=email
        content="Hello"+str(t1)+"\n your PIN is "+str(pin)
        SUBJECT=' PIN '
        message='Subject: {}\n\n{}'.format(SUBJECT,content)
        
        mail=smtplib.SMTP("smtp.gmail.com",587)
        mail.ehlo()
        mail.starttls()
        mail.login("piyushkedia002@gmail.com","kedia123")
        mail.sendmail(sender,reciver,message)
        mail.close()
        login(frame)

    except OSError:
            time.sleep(1)
            msg.showwarning('Title','Server Problem')
                    
            
def login(frame):
    frame.destroy()
    frame1=Frame(root,width=1400,height=700)
    frame1.pack(expand=True)
    img=ImageTk.PhotoImage(Image.open('pixal.jpg'))
    lg1=Label(frame1,image=img)
    lg1.image=img
    lg1.place(x=0,y=0)

    lg2=Label(frame1,text='Welcome  To  Login  Page  ',bg='light gray',fg='black',font=('times',38,"bold",'underline'),width=42)
    lg2.place(x=0,y=0)

    lg3=Label(frame1,text='Email or Phone',bg='light gray',fg='black',font=('times',18,"bold",'italic'),width=15)
    lg3.place(x=620,y=220)

    eg1=Entry(frame1,textvariable ='email',bg='white',bd=6,fg='black',font=('times',16,"bold",'italic'),width=20)
    eg1.place(x=900,y=220)

    lg4=Label(frame1,text='Password',bg='light gray',fg='black',font=('times',18,"bold",'italic'),width=15)
    lg4.place(x=620,y=280)


    eg2=Entry(frame1,bg='white',show='*',bd=6,fg='black',font=('times',16,"bold",'italic'),width=20)
    eg2.place(x=900,y=280)
    
    bg1=Button(frame1,text='Submit',bg='dark gray',bd=9,command=lambda:account(frame1,eg1,eg2),fg='black',font=('times',16,"bold",'italic'),width=7)
    bg1.place(x=840,y=400)

    bg2=Button(frame1,text='Forget Password???',bg='light gray',bd=4,command=lambda:mails(frame1,eg1),fg='black',font=('times',10,"bold",'italic'),width=18,height=1)
    bg2.place(x=830,y=500)

    bg3=Button(frame1,text='Back',bg='dark gray',bd=9,command=lambda:exit(frame1),fg='black',font=('times',16,"bold",'italic'),width=7)
    bg3.place(x=80,y=520)


def signup(frame):
    
    frame2=Frame(root,width=1400,height=700)
    frame2.pack(expand=True)
    img=ImageTk.PhotoImage(Image.open('pixal.jpg'))
    ls1=Label(frame2,image=img)
    ls1.image=img
    ls1.place(x=0,y=0)
    frame.destroy()
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


    e6=StringVar()
    e6.set('Gender')
    es6=OptionMenu(frame2,e6,'  Male  ','  Female  ','  Others  ',)
    es6.config(font=('times',12,"bold",'italic'),bg='light gray',bd=6,width=23)
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

    bs1=Button(frame2,text='Submit',bg='dark gray',bd=9,command=lambda:submit(frame2,es1,es2,es3,es4,es5,e6,es7,es8,var),fg='black',font=('times',16,"bold",'italic'),width=7)
    bs1.place(x=970,y=580)

    bs2=Button(frame2,text='Back',bg='dark gray',bd=9,command=lambda:exit(frame2),fg='black',font=('times',16,"bold",'italic'),width=7)
    bs2.place(x=70,y=580)

def main(root):
    frame=Frame(root,width=1400,height=700)
    frame.pack(expand=True)
    img=ImageTk.PhotoImage(Image.open('buss.jpg'))
    lg1=Label(frame,image=img)
    lg1.image=img
    lg1.place(x=0,y=0)



    
    '''1st page'''
    n="Welcome To Bank Application"
    l2=Label(frame,text=n.center(86),bd=5,fg='black',bg='light gray',font=("times",37,'bold','underline'),width=44)
    l2.place(x=0,y=0)

    b1=Button(frame,text='Login',bg='dark gray',bd=8,command=lambda:login(frame),fg='black',font=('times',19,'bold'),width=8)
    b1.place(x=90,y=250)

    b2=Button(frame,text='Sign Up',bg='dark gray',bd=8,command=lambda:signup(frame),fg='black',font=('times',19,'bold'),width=8)
    b2.place(x=90,y=350)

    b4=Button(frame,text='Show all data',bg='dark gray',bd=8,command=lambda:show(frame),fg='black',font=('times',19,'bold'))
    b4.place(x=90,y=450)
    
    b3=Button(frame,text='Exit',bg='dark gray',bd=8,command=lambda:exits(frame,root),fg='black',font=('times',19,'bold'),width=8)
    b3.place(x=90,y=550)

main(root)
root.mainloop()
