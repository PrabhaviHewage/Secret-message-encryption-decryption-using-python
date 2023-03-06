from tinker import *
from tinker import messagebox
import base64
import os


def decrypt():
    password=code.get()

    if password=="1234":
        screen2=Toplevel(screen)
        screen2.title("encryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message=text1.get(1.0, END)
        decode_message=message.encode("ascii")
        base64_bytes=base64.b64decode(decode_message)
        decrypt=base64_bytes.decode("ascii")

        Label(screen2,text="DECYRYPT", font="arial",fg="white",bg="#00bd56").place(x=10,y=0)
        text2=Text(screen2,font="Rpbote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)

        text2.insert(END.encrypt)

    elif password=="":
        messagebox.showerror("encryption","Input Password")

    elif password !="1234":
        messagebox.showerror("encryption","Invalid Password")





def main_screen():

        screen=Tk()
        screen.geometry("375x398")

        #icon
        image_icon-PhotoImage(file="keys.png")
        screen.iconphoto(False, image_icon)
        screen.title("PctApp")

        Label(text="Enter text for encryption and decryption", fg="black", font=("calbri", 13)).place(x=10,y=10)
        text1=Text(font="Robote 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text1.place(x=10, y=50, width=355, height=100)

        Label(text="Enter secret key for encryption and decryption", fg="black", font=("calibri", 133)).place(x=10,y=170)

        code=StringVar()
        Entry(textVariable=code, width19, bd=0, font=("ariel", 25),show="*").place(x=10,y=200)

        Button(text="ENCRYPT", height="2", width=23,bg="#ed3833",fg="white",bd=0).place(x=10,y=250)
        Button(text="DECRYPT", height="2", width=23,bg="#00bd56",fg="white",bd=0).place(x=10,y=250)
        Button(text="RESET", height="2", width=50,bg="#1089ff", fg="white",bd=0, command=reset).place(x=10,y=300)



        screen.mainloop()

main_screen()
