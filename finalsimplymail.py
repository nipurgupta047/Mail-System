from os import system
import os
import smtplib
import tkinter as tk
from tkinter import *
import tkinter.font as font
from random import randint
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from twilio.rest import Client
from PIL import ImageTk
from tkinter import messagebox
import tkinter.messagebox
from captcha.image import ImageCaptcha
from captcha.audio import AudioCaptcha
from PIL import Image, ImageTk
from numpy import random
from gtts import gTTS #google text to speech
import os
from cryptography.fernet import Fernet


#--------------------------------------------MAIL PAGE------------------------------------------------------------

def mail_page():
    #clearing window
    system('cls')
    #tkinter window
    global root1
    root1=tk.Tk()
    root1.geometry("1200x700+100+50")
    root1.resizable(False,False)

    C = Canvas(root1, bg="blue", height=250, width=300)
    filename = ImageTk.PhotoImage(file = "photo.jpg")
    background_label = Label(root1, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.pack()
    #buttons
    btn1=Button(root1,command=createfilepage,text='CREATE',fg="white",bg="#4966b1",width=15,height=1,font=("Roboto Slab",12,"bold"))
    btn1.pack()
    btn2=Button(root1,command=send_mail,text='SEND MAIL',fg="white",bg="#4966b1",width=15,height=1,font=("Roboto Slab",12,"bold"))
    btn2.pack()
    btn3=Button(root1,command=root1.destroy,text='EXIT',fg="white",bg="#4966b1",width=15,height=1,font=("Roboto Slab",12,"bold"))
    btn3.pack()
    root1.mainloop()

#--------------------------------------------SENDING OTP THROUGH MAIL------------------------------------------------------------

def otp_mail(receiver_email_id,pin):
    try:
        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()
    except:
        print("no internet connection found")
        return 0
    sender_email_id=("2019kuec****@iiitkota.ac.in")
    sender_email_id_password=("******")

    # Authentication
    s.login(sender_email_id, sender_email_id_password)

    # message to be sent
    message = "Your otp is "+str(pin)
    # sending the mail
    try:
        s.sendmail(sender_email_id, receiver_email_id, message)
    except:
        print("NO such sender gmail ID exists")
        return 0
    # terminating the session
    s.quit()
    return 1

#--------------------------------------------SEND SMS------------------------------------------------------------

def sms_to_users():
    system('cls')
    try:
        sms_message=input("Enter your message :  ")
        reciever_number=input("Enter reciever's phone no. : ")
        account_sid = "*******"
        auth_token = "*******"
        client = Client(account_sid, auth_token)

        message = client.messages.create(body=sms_message,from_='+18509903488',to=reciever_number)

        print(message.sid)
        print("Message sent succesfully")
    except:
        print("Message not sent. Please check your number and internet connection")


#--------------------------------------------SEND MAIL------------------------------------------------------------

def single_mail():
    system('cls')
    # creates SMTP session
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
    except:
        print("Internet connection not found")
        return
    # start TLS for security
    s.starttls()
    sender_email_id=myusername
    sender_email_id_password=input("Enter your gmail password  ")

    try:
        # Authentication
        s.login(sender_email_id, sender_email_id_password)
    except:
        print("Incorrect password  ")
        return
    # message to be sent
    message = input("Enter your message  ")
    receiver_email_id=input("Enter receiver gmail ID  ")

    # sending the mail
    try:
        s.sendmail(sender_email_id, receiver_email_id, message)
        print("Mail sent succesfully")
    except:
        print("Couldn't send mail. Please check mail ID again and try again  ")

    # terminating the session
    s.quit()

#-----------------------------------------------------------
def mail_to_multiple_users():
    system('cls')
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        # start TLS for security
        s.starttls()
        sender_email_id=myusername
        sender_email_id_password=input("Enter your gmail password  ")
        # Authentication
        s.login(sender_email_id, sender_email_id_password)
    except:
        print("Couldn't login to your account . Please check your password and internet connection and try again ")
        return

    times='y'
    while times=='y':
        # creates SMTP session
        try:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            # start TLS for security
            s.starttls()
            sender_email_id=myusername
            # Authentication
            s.login(sender_email_id, sender_email_id_password)
            # message to be sent
            message = input("Enter your message  ")
            receiver_email_id=input("Enter receiver gmail ID  ")
            # sending the mail
            s.sendmail(sender_email_id, receiver_email_id, message)

            # terminating the session
            s.quit()
            print("Message sent sucessfully")
            tim=input("Press y to send more mail else press n  ")
            times=tim
        except:
            print("Could't send message  Please check your internet connection and email ID you entered")
            tim=input("press y to send more mail else press n  ")
            times=tim


#-----------------------------------------------------------
def mail_to_file_users():
    system('cls')


    file_name=input("Enter file name  ")
    filename=myusername+file_name+".txt"

    fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    str=""
    list=[]
    for file in fileList:
        if file['title']==filename:
            str = file.GetContentString()
            list=str.split()
            break


    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        # start TLS for security
        s.starttls()
        sender_email_id=myusername
        sender_email_id_password=input("Enter your gmail password  ")
        # Authentication
        s.login(sender_email_id, sender_email_id_password)
    except:
        print("Couldn't login to your account . Please try again  ")
        return
    message = input("Enter your message  ")

    for receiver_email_id in list:
        # creates SMTP session
        try:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            # start TLS for security
            s.starttls()
            sender_email_id=myusername
            # Authentication
            s.login(sender_email_id, sender_email_id_password)
            # message to be sent

            # sending the mail
            s.sendmail(sender_email_id, receiver_email_id, message)

            # terminating the session
            s.quit()
            print("Message sent sucessfully to "+ receiver_email_id)
        except:
            print("Could't send message to "+ receiver_email_id)



#--------------------------------------------CREATE YOUR USERNAME FILE------------------------------------------------------------
def createfilepage() :
    root1.destroy()
    #clearing window
    system('cls')
    #tkinter window
    global root3
    root3=tk.Tk()
    root3.geometry("1200x700+100+50")
    root3.resizable(False,False)

    C = Canvas(root3, bg="blue", height=250, width=300)
    filename = ImageTk.PhotoImage(file = "create.jpg")
    background_label = Label(root3, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.pack()
    #buttons
    email=tk.Label(root3,text="File Name", bg= "red")
    email.pack()
    global email1
    email1=tk.Entry(root3,width=60)
    email1.pack()
    pas=tk.Label(root3,text="List of IDs separated by space", bg= "red")
    pas.pack()
    global pas1
    pas1=tk.Entry(root3,width=60)
    pas1.pack()
    btn3=Button(root3,command=create_username_file,text='Create',fg="white",bg="#4966b1",width=15,height=1,font=("Roboto Slab",12,"bold"))
    btn3.pack()
    btn4=Button(root3,command=back_to_mail,text='BACK',fg="white",bg="#4966b1",width=15,height=1,font=("Roboto Slab",12,"bold"))
    btn4.pack()
    root3.mainloop()

def back_to_mail():
    root3.destroy()
    mail_page()

def create_username_file():

    system('cls')
    user=1

    fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    filelist=[]
    str=""
    for file in fileList:
        if file['title']==myusername+"files.txt":
            str = file.GetContentString()
            fileslist=str.split()
            break

    #checking if that file already exists
    filer1=""

    filer= email1.get()
    filer1=myusername+filer+".txt"
    str=pas1.get()
    if filer1 in fileslist:
            messagebox.showerror("Error","The file already exists! Enter different name", parent=root3)

    #adding this file name in our file names list


    #input of usernames you want to enter in it
    elif str=='' :
            messagebox.showerror("Error","Enter IDs", parent=root3)
    else :
        messagebox.showinfo("Done","File created sucessfully", parent=root3)

        file1 = drive.CreateFile({'title': filer1})
        file1.SetContentString(str)
        file1.Upload()

        fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
        for file1 in fileList:
            if file1['title']==myusername+'files.txt':
                str = file1.GetContentString()
                file1.SetContentString(str+' '+filer1)  # 'add our file name in file names list of our account'
                file1.Upload()
                break



#--------------------------------------------SEND SINGLE MAIL------------------------------------------------------------

def send_mail():
    system('cls')
    root1.destroy()

    global root2
    root2=tk.Tk()
    root2.geometry("1200x700+100+50")
    root2.resizable(False,False)

    C = Canvas(root2, bg="blue", height=250, width=300)
    filename = ImageTk.PhotoImage(file = "create.jpg")
    background_label = Label(root2, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.pack()
    btn1=Button(root2,command=single_mail,text='SINGLE MAIL',fg="white",bg="#4966b1",width=20,height=1,font=("Roboto Slab",12,"bold"))
    btn1.pack()
    btn2=Button(root2,command=mail_to_multiple_users,text='MAIL TO MULTIPLE USERS',fg="white",bg="#4966b1",width=20,height=1,font=("Roboto Slab",12,"bold"))
    btn2.pack()
    btn3=Button(root2,command=mail_to_file_users,text='MAIL TO FILE USERS',fg="white",bg="#4966b1",width=20,height=1,font=("Roboto Slab",12,"bold"))
    btn3.pack()
    btn6=Button(root2,command=sms_to_users,text='SMS TO USERS',fg="white",bg="#4966b1",width=20,height=1,font=("Roboto Slab",12,"bold"))
    btn6.pack()
    btn4=Button(root2,command=back_to_mail_page,text='BACK',fg="white",bg="#4966b1",width=20,height=1,font=("Roboto Slab",12,"bold"))
    btn4.pack()
    btn5=Button(root2,command=root2.destroy,text='EXIT',fg="white",bg="#4966b1",width=20,height=1,font=("Roboto Slab",12,"bold"))
    btn5.pack()
    root2.mainloop()

def back_to_mail_page():
    root2.destroy()
    mail_page()




#--------------------------------------------LOGIN FUNCTION------------------------------------------------------------

def login():
    system('cls')


    usernamelist=[]
    passwordlist=[]
    fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    for file in fileList:
        if file['title']=='usernamefile.txt':
            str = file.GetContentString()
            usernamelist=str.split()
            break
    fileList1 = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    for file1 in fileList1:
        if file1['title']=='passwordfile.txt':
            str1 = file1.GetContentString()
            passwordlist=str1.split()
            break
    username= d1.get()
    password=c1.get()
    #opening file having all usernames list

    #gives number of users in our list
    length=len(usernamelist)
    access=0

    #checking if that user is registered
    for i in range(length):
        if usernamelist[i]==username and passwordlist[i]==password:
            access=1
            break
    if access==1:
        global myusername
        myusername=username
        lbl_two=tk.Label(root7,text="ACCESS GRANTED", bg= "red")
        lbl_two.pack()
        #print("Access Granted")
        root7.destroy()
        mail_page()
    else:
        print("No record found !!!")


#--------------------------------------------SIGNUP FUNCTION------------------------------------------------------------

def signup():
    class Signup:
        def __init__(self,root):
            self.root=root
            self.root.title("Signup Page")
            self.root.geometry("1199x600+100+50")
            self.root.resizable(False,False)
            #----image---
            self.bg=ImageTk.PhotoImage(file="photo.jpg")
            self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
            #--signup frame----
            Frame_signup=Frame(self.root,bg="white")
            Frame_signup.place(x=150,y=40,height=520,width=500)

            title=Label(Frame_signup,text="WELCOME",font=("Ubuntu Bold",30,"bold"),bg="white").place(x=90,y=30)

            lb1_user=Label(Frame_signup,text="Enter your username",font=("Roboto Slab",15,"bold"),fg="gray",bg="white").place(x=90,y=100)
            self.text_user=Entry(Frame_signup,font=("times new roman",15),bg="lightgray")
            self.text_user.place(x=90,y=130,width=350,height=35)

            next=Button(Frame_signup,command=self.nextuser,text="Next",fg="white",bg="#4966b1",font=("Roboto Slab",12,"bold")).place(x=440,y=130)

            lb2_user=Label(Frame_signup,text="Enter OTP sent at mail",font=("Roboto Slab",15,"bold"),fg="gray",bg="white").place(x=90,y=170)
            self.text_otp=Entry(Frame_signup,font=("times new roman",15),bg="lightgray")
            self.text_otp.place(x=90,y=200,width=350,height=35)

            next=Button(Frame_signup,command=self.nextotp,text="Next",fg="white",bg="#4966b1",font=("Roboto Slab",12,"bold")).place(x=440,y=200)

            lb3_user=Label(Frame_signup,text="Enter your password",font=("Roboto Slab",15,"bold"),fg="gray",bg="white").place(x=90,y=240)
            self.text_pass=Entry(Frame_signup,font=("times new roman",15),bg="lightgray")
            self.text_pass.place(x=90,y=270,width=350,height=35)

            create=Button(Frame_signup,command=self.nextcreate,text="Create Account",fg="white",bg="#4966b1",font=("Roboto Slab",12,"bold")).place(x=90,y=320)
            back=Button(Frame_signup,command=self.goback,text="Back",fg="white",bg="#4966b1",font=("Roboto Slab",12,"bold")).place(x=90,y=360)

        def nextuser(self):
            usernamelist=[]
            fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
            global str1
            str1=""
            global file
            for file in fileList:
                if file['title']=='usernamefile.txt':
                    str1 = file.GetContentString()
                    usernamelist=str1.split()
                    break
            #user=1


            #checking if that username is already taken
            global username
            username=""

            username=self.text_user.get()
            if username in usernamelist:
                    #user=1
                messagebox.showerror("Error","Username already exists",parent=self.root)
            elif username=="":
                    #user=1
                messagebox.showerror("Error","Field required",parent=self.root)
            else:
                #generating a random 4 digit otp
                pin1=randint(1,9)
                pin2=randint(1,9)
                pin3=randint(1,9)
                pin4=randint(1,9)
                global pin
                pin=pin1*1000+pin2*100+pin3*10+pin4

                #sending otp though mail
                global net
                net=otp_mail(username,pin)

        def nextotp(self):
            #checking if internet is connected or not
            if net==1:
                otp=self.text_otp.get()
            #typecasting from string to int
                otp=int(otp)

            #if value you entered matches otp or not
                if otp!=pin :
                    messagebox.showerror("Error","Pin didn't match. Please try again",parent=self.root)
            else:
                messagebox.showerror("Error","Check your internet connection",parent=self.root)

        def nextcreate(self):
            global password
            password=self.text_pass.get()

            global myusername
            myusername=username
            fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
            for file in fileList:
                if file['title']=='usernamefile.txt':
                    str1 = file.GetContentString()
                    file.SetContentString(str1+' '+username)  # 'add our username in username list'
                    file.Upload()

            fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
            for file1 in fileList:
                if file1['title']=='passwordfile.txt':
                    str1 = file1.GetContentString()
                    file1.SetContentString(str1+' '+password)  # 'add our password in password list'
                    file1.Upload()
                    break
            #creating a file for files in our account
            title=username+"files.txt"
            file1 = drive.CreateFile({'title': title})
            file1.SetContentString(title+" ")
            file1.Upload()
            messagebox.showinfo("Congratulations!!","Your account has been created")
            root.destroy()
            mail_page()
        def goback(self):
            root.destroy()
            login_page()
    root7.destroy()
    global root
    root=Tk()
    obj=Signup(root)
    root.mainloop



#--------------------------------------------LOGIN PAGE------------------------------------------------------------

def login_page():
    global root7
    root7=tk.Tk()
    root7.geometry("1200x700+100+50")
    root7.resizable(False,False)

    C = Canvas(root7, bg="blue", height=250, width=300)
    filename = ImageTk.PhotoImage(file = "photo.jpg")
    background_label = Label(root7, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.pack()

    d=tk.Label(root7,text="email", font=("Roboto Slab",15,"bold"),fg="gray",bg="lightgray",width=15,height=2)
    d.pack()
    global d1
    d1=tk.Entry(root7,font=("times new roman",15),bg="white",width=15)
    d1.pack()
    c=tk.Label(root7,text="password",font=("Roboto Slab",15,"bold"),fg="gray",bg="lightgray",width=15,height=2)
    c.pack()
    global c1
    c1=tk.Entry(root7,font=("times new roman",15),bg="white",width=15)
    c1.pack()
    btn1=Button(root7,command=login,text='LOGIN',fg="white",bg="#4966b1",width=15,height=1,font=("Roboto Slab",12,"bold"))
    btn1.pack()
    btn2=Button(root7,command=signup,text='SIGNUP',fg="white",bg="#4966b1",width=15,height=1,font=("Roboto Slab",12,"bold"))
    btn2.pack()
    btn3=Button(root7,command=root7.destroy,text='EXIT',fg="white",bg="#4966b1",width=15,height=1,font=("Roboto Slab",12,"bold"))
    btn3.pack()
    root7.mainloop()


#--------------------------------------------Re captcha-----------------------------------------------------------

def captcha_generation():
    key = Fernet.generate_key()
    key = key.decode()                    #converting byte key to string
    i = random.randint(0,37)              #generating a random number which will help to make substring
    global captcha_text
    captcha_text = key[i:(i+5)]             #generating a 6 digit captcha text from key
    print(captcha_text)

def generate_image_captcha():
    image = ImageCaptcha()                #Creating image instance
    data = image.generate(captcha_text)
    image.write(captcha_text,"image_captcha.png")

def show_image():                         #displaying image on window
    load = Image.open("image_captcha.png")
    render = ImageTk.PhotoImage(load)
    img = Label(left_frame, image = render)
    img.image = render
    img.pack()

def new_image():
    captcha_generation()
    generate_image_captcha()
    show_image()

def check_image_captcha():
    value = ans2.get()
    if value == captcha_text:
        tkinter.messagebox.showinfo("SUCCESS!","Your Captcha Code Matched.")
        ans2.set("")
        global i
        i=i+1
    else:
        tkinter.messagebox.showinfo("WRONG! Try Again","Your Captcha Code did not match. Better luck next time :)")
        ans2.set("")

def generate_audio_captcha():
    language = 'en'
    output = gTTS(text = captcha_text.lower(), lang =language, slow = True)
    output.save("audio_captcha.mp3")


def play():
    os.system("start audio_captcha.mp3")

def new_audio():
    captcha_generation()
    generate_audio_captcha()
    play()

def check_audio_captcha():
    value = ans.get()
    if value == captcha_text.lower():
        tkinter.messagebox.showinfo("SUCCESS!","Your Captcha Code Matched.")
        ans.set("")
        global a
        a=a+1
    else:
        tkinter.messagebox.showinfo("WRONG! Try Again","Your Captcha Code did not match. Better luck next time :)")
        ans.set("")

def submit():
    if a>0 or i>0:
        tkinter.messagebox.showinfo("Please Wait!","We will be directing you to next window in just a minute .")
        root.destroy()
    else:
        tkinter.messagebox.showinfo("Woops!","Looks like you havn't completed your captcha verification .")


#--------------------------------------------main page---------------------------------------------------------------

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

captcha_generation()
print(captcha_text)
root = Tk()
root.title("GUI : CAPTCHA Generation ")
root.geometry("820x500")
root.configure(background = "#FFE4C4")

i=0
a=0
ans = StringVar()
ans2 = StringVar()
generate_image_captcha()
generate_audio_captcha()

left_frame = Frame(root,width = 400 ,height = 170, bg = '#ffffff',bd = 10)
left_frame.pack(side = 'left',fill = 'both',padx = 5, pady =5,expand = 'True')
right_frame = Frame(root,width = 400 ,height = 170, bg = '#ffffff',bd =10)
right_frame.pack(side = 'right',fill ='both',padx = 5, pady =5,expand = 'True')

Label_1 = Label(right_frame, text=" Audio Captcha ",font=('Courier New', 20,'bold'),padx=1,pady=30,bg ="#FFFFE0",fg ="black")
Label_1.pack(side = 'top',expand = 'True')

Label_2 =Label(right_frame, text= "Type all characters in lowercase",font=('arial', 9,'italic'),padx=2,pady=2, bg="#fffff0",fg = "black")
Label_2.pack(expand = 'True')

Entry_1= Entry(right_frame,bd=2,fg="grey",textvariable= ans, width=14,font=('arial',13,'bold'))
Entry_1.insert(0,"Please enter captcha here ")
Entry_1.pack(fill = 'both',padx = 5,pady =10,ipady =10,expand = 'True')

button_clear1 = Button(right_frame, font=('Arial', 10,'bold'), text="CLEAR",padx=15,pady=5, bg="white",fg = "blue",command=lambda: Entry_1.delete(0,END))
button_clear1.pack(pady = 5,expand = 'True')

button1 = Button(right_frame, font=('Arial', 10 ,'bold'), text="CHECK",padx=15,pady=5, bg="red",fg = "white",command=lambda: check_audio_captcha())
button1.pack(pady = 5,expand = 'True')

button_audio =Button(right_frame, text="Play Audio",font=('arial', 10,'bold'),padx=10,pady=5, bg="blue",fg = "white",command=lambda: play())
button_audio.pack(side ="right",pady = 5)

button_audio_new = Button(right_frame, text="New Audio",font=('arial', 10,'bold'),padx=10,pady=5, bg="blue",fg = "white",command=lambda: new_audio())
button_audio_new.pack(side ="left",pady = 5)

Label_3 = Label(left_frame, text=" Image Captcha ",font=('Courier New', 20,'bold'),padx=1,pady=30,bg ="#FFFFE0",fg ="black")
Label_3.pack(side = 'top',expand = 'True')

Label_4 = Label(left_frame, text="Click 'Check' to verify ",font=('arial', 9,'italic'),padx=2,pady=2, bg="#fffff0",fg = "black")
Label_4.pack(expand = 'True')

Entry_2 = Entry(left_frame,bd=2,fg="grey",font=('arial',13,'bold'),textvariable= ans2, width=14)
Entry_2.insert(0,"Please enter captcha here ")
Entry_2.pack(fill = 'both',padx = 5,pady =10,ipady =10,expand = 'True')

button_clear2 = Button(left_frame, font=('Arial', 10,'bold'), text="CLEAR",padx=15,pady=5, bg="white",fg = "blue",command=lambda: Entry_2.delete(0,END))
button_clear2.pack(pady = 5,expand = 'True')

button2 = Button(left_frame, font=('Arial', 10,'bold'), text="CHECK",padx=15,pady=5,  bg="red",fg = "white",command=lambda: check_image_captcha())
button2.pack(pady = 5,expand = 'True')

button_image = Button(left_frame, text="Show Image",font=('arial', 10,'bold'),padx=10,pady=5, bg="blue",fg = "white",command=lambda: show_image())
button_image.pack(side ="left",pady = 5)

button_image_new = Button(left_frame, text="New Image",font=('arial', 10,'bold'),padx=10,pady=5, bg="blue",fg = "white",command=lambda: new_image())
button_image_new.pack(side ="right",pady = 5)

button3 = Button(root,text = "Next-->",font=('Arial', 20,'bold'),command = lambda: submit())
button3.pack(side='bottom')

root.mainloop()
login_page()
