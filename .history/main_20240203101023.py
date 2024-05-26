import tkinter
import os
import sys
import subprocess
from tkinter import filedialog
from PIL import Image , ImageTk


def open_image():
    global img
    global img_name
    global submit

    img_name = filedialog.askopenfilename(initialdir='.' , title='Select Image' , filetypes=(('images' , "*.jpg") , ('images' , '*.bmp') , ('images' , '*.png' ) , ( 'images', '*.jpeg')) )
    print("Image path : " + img_name)
    input.insert(0,img_name)

    l1 = tkinter.Label(root , text = "Original Text")
    l1.grid(column =0 , row = 2)
    print("Image Name : " 
          +img_name)
    
    img = ImageTk.PhotoImage(file=img_name )
    # img = ImageTk.PhotoImage(Image,open(img_name).resize((250 , 250)))
    
    l2 = tkinter.Label(root , image=img)
    l2.grid(column=0 , row = 3)

    submit = tkinter.Button(root , text = "Submit"  , command = call_haze)
    submit.grid(column=0 , row=4)

def call_haze():
    global dehazard

    submit.destroy()

    subprocess.call(f"python haze_removal.py \"{img_name}\"" , shell=True)

    msg = tkinter.Label(root , text = "Dehazing complete Image stored in dehazed folder")
    msg.grid(column=0 , row=4 , columnspan=2)

    # l3 = tkinter.Label(root , text="Dehazed Image : ")
    # l3.grid(column=1 , row=2)

    # dehazed = ImageTk.PhotoImage(Image.open("img/dst.jpg" ).resize((250,250)))
    # temp = img_name.split(".")[0].split('/')[-1]
    # temp2 = img_name.split(".")[1]
    # dest = "C:/Users/TUF GAMING/Desktop/dcp algorithm/dehazed/"+temp+"_dehazed"+"."+temp2
    # dehazed = ImageTk.PhotoImage(file=dest )
    # l4 = tkinter.Label(root , image=dehazed)
    # l4.grid(column=1 , row = 3 , padx = 10)


    quit = tkinter.Button(root , text="Quit" , command = quit_program)
    quit.grid(column=1 , row = 5)


def quit_program():
    sys.exit()

root = tkinter.Tk()
root.title("Dehaze")
root.update_idletasks()

label = tkinter.Label(root , text = "Select  image",width=100)
label.grid(column=0 , row= 0)

input = tkinter.Entry(root , width=50)
input.grid(column=0 , row =1  , padx =10 , pady=10)

browse = tkinter.Button(root  , text="Browse"  , command=open_image)
browse.grid(column=0 , row=2)

root.mainloop()


