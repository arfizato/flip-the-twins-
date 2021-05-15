import tkinter as tk
import random as rand
from tkinter.constants import DISABLED
from PIL import Image, ImageTk
from tkinter import Button, messagebox
import tkinter.font as font   



def buttonClick( l,c,x,button):
    button.grid_forget()
    global firstOrSecond, firstImage, firstL, firstC, firstButton, livesLeft,keepPlaying, picsFlipped, lifeImage,livesList
    if firstOrSecond==1 :
        firstImage= mat[l-1][c-1]
        firstL=l
        firstC=c
        firstButton= button
    else:
        if mat[l-1][c-1]!= firstImage : 
            livesLeft -= 1     

            lifeImage=livesList[livesLeft]    
            root.lifeImage= ImageTk.PhotoImage(Image.open(lifeImage))
            livesButton.configure(image=root.lifeImage)

            firstButton.grid(row=firstL,column=firstC,pady=2)
            button.grid(row=l,column=c,pady=2)
            if livesLeft==0:
                box= messagebox.askquestion("Game Over!","You Have No Lives Yet\nWould you like to play again?",icon="question")
                if box!="yes":
                    keepPlaying=False
                root.destroy()
        else:
            picsFlipped+=1
            if picsFlipped==4:
                box= messagebox.askquestion("You Won!","You have Flipped all the images\nWould you like to play again?",icon="question")
                if box!="yes":
                    keepPlaying=False
                root.destroy()        

    if firstOrSecond ==1:
        firstOrSecond=2
    else:
        firstOrSecond=1

def coverButtons():

    button1 = tk.Button(root,text='',width=100,height=80,bg='#353535',bd=0,image=root.image00, command= lambda: buttonClick(1,1,1,button1))
    button1.grid(row=1,column=1,padx=2,pady=2)

    button2 = tk.Button(root,text='',width=100,height=80,bg='#353535',bd=0,image=root.image00, command= lambda: buttonClick(1,2,2,button2))
    button2.grid(row=1,column=2,padx=2,pady=2)

    button3 = tk.Button(root,text='',width=100,height=80,bg='#353535',bd=0,image=root.image00, command= lambda: buttonClick(1,3,3,button3))
    button3.grid(row=1,column=3,padx=2,pady=2)

    button4 = tk.Button(root,text='',width=100,height=80,bg='#353535',bd=0,image=root.image00, command= lambda: buttonClick(1,4,4,button4))
    button4.grid(row=1,column=4,padx=2,pady=2)

    button5 = tk.Button(root,text='',width=100,height=80,bg='#353535',bd=0,image=root.image00, command= lambda: buttonClick(2,1,5,button5))
    button5.grid(row=2,column=1,padx=2,pady=2)

    button6 = tk.Button(root,text='',width=100,height=80,bg='#353535',bd=0,image=root.image00, command= lambda: buttonClick(2,2,6,button6))
    button6.grid(row=2,column=2,padx=2,pady=2)

    button7 = tk.Button(root,text='',width=100,height=80,bg='#353535',bd=0,image=root.image00, command= lambda: buttonClick(2,3,7,button7))
    button7.grid(row=2,column=3,padx=2,pady=2)

    button8 = tk.Button(root,text='',width=100,height=80,bg='#353535',bd=0,image=root.image00, command= lambda: buttonClick(2,4,8,button8))
    button8.grid(row=2,column=4,padx=2,pady=2)

def changeLayout():
    global t1
    try: 
        welcomeMessage.destroy()
    except:
        pass

    

    #image11= tk.PhotoImage(file=imageList[1]).subsample(8,8)
    button11 = tk.Button(root,text='',width=100,height=80,bg='#353535',bd=0,image= root.image11,state= DISABLED,)# command= lambda: buttonClick(root.image11,1,1))
    button11.grid(row=1,column=1,padx=2,pady=2)

    #image12= tk.PhotoImage(file=imageList[2]).subsample(8,8)
    button12 = tk.Button(root,text='',width=100,height=80,bg='#353535',bd=0,image= root.image12,state= DISABLED,)#  command= lambda: buttonClick(root.image12,1,2))
    button12.grid(row=1,column=2,padx=2,pady=2)

    #image13= tk.PhotoImage(file=imageList[3]).subsample(8,8)
    button13 = tk.Button(root,text='',width=100,height=80,bg='#353535',bd=0,image= root.image13,state= DISABLED,)# command= lambda: buttonClick(root.image13,1,3))
    button13.grid(row=1,column=3,padx=2,pady=2)

    #image14= tk.PhotoImage(file=imageList[4]).subsample(8,8)
    button14 = tk.Button(root,text='',width=100,height=80,bg='#353535',bd=0,image= root.image14,state= DISABLED,)# command= lambda: buttonClick(root.image14,1,4))
    button14.grid(row=1,column=4,padx=2,pady=2)

    #image21= tk.PhotoImage(file=imageList[1]).subsample(8,8)
    button21 = tk.Button(root,text='',width=100,height=80,bg='#353535',bd=0,image= root.image21,state= DISABLED,)# command= lambda: buttonClick(root.image21,2,1))
    button21.grid(row=2,column=1,padx=2,pady=2)

    #image22= tk.PhotoImage(file=imageList[2]).subsample(8,8)
    button22 = tk.Button(root,text='',width=100,height=80,bg='#353535',bd=0,image= root.image22,state= DISABLED,)# command= lambda: buttonClick(root.image22,2,2))
    button22.grid(row=2,column=2,padx=2,pady=2)

    #image23= tk.PhotoImage(file=imageList[3]).subsample(8,8)
    button23 = tk.Button(root,text='',width=100,height=80,bg='#353535',bd=0,image= root.image23,state= DISABLED,)# command= lambda: buttonClick(root.image23,2,3))
    button23.grid(row=2,column=3,padx=2,pady=2)

    #image24= tk.PhotoImage(file=imageList[4]).subsample(8,8)
    button24 = tk.Button(root,text='',width=100,height=80,bg='#353535',bd=0,image= root.image24,state= DISABLED,)# command= lambda: buttonClick(root.image24,2,4))
    button24.grid(row=2,column=4,padx=2,pady=2)   

    livesButton.grid(row=0,column=1,pady=2, columnspan=4)
    
    root.after(2000, coverButtons)

def OnClose():
    global keepPlaying
    keepPlaying=False
    root.destroy()

    """
    ███    ███  █████  ██ ███    ██     ███████ ██    ██ ███    ██  ██████ ████████ ██  ██████  ███    ██ 
    ████  ████ ██   ██ ██ ████   ██     ██      ██    ██ ████   ██ ██         ██    ██ ██    ██ ████   ██ 
    ██ ████ ██ ███████ ██ ██ ██  ██     █████   ██    ██ ██ ██  ██ ██         ██    ██ ██    ██ ██ ██  ██ 
    ██  ██  ██ ██   ██ ██ ██  ██ ██     ██      ██    ██ ██  ██ ██ ██         ██    ██ ██    ██ ██  ██ ██ 
    ██      ██ ██   ██ ██ ██   ████     ██       ██████  ██   ████  ██████    ██    ██  ██████  ██   ████                                                                                                       

    """   
keepPlaying=True ;playedOnce=0
while keepPlaying==True:   
    firstImage="" ; firstL=0 ; firstC=0 ; livesLeft=3; picsFlipped=0; firstOrSecond=1
    imageList=["images/empty.png","images/axe.png","images/flower.png","images/pistol.png","images/shovel.png"]
    livesList=["images/0lives.png","images/1lives.png","images/2lives.png","images/3lives.png"]
    mat=[[""]*4,[""]*4]
    for a in range(0,4):
        while True :
            l=rand.randint(0,1)
            c=rand.randint(0,3)
            if mat[l][c]=="":
                break
        mat[l][c]=imageList[a+1]
        
        while True :
            l=rand.randint(0,1)
            c=rand.randint(0,3)
            if mat[l][c]=="":
                break
        mat[l][c]=imageList[a+1]

        

    root= tk.Tk()
    root.title("Twin Cards")
    root.iconbitmap("images/poker.ico")
    root.configure(bg="#272727")
    root.geometry("+500+300")
    root.protocol('WM_DELETE_WINDOW', OnClose)
    

    image00=imageList[0]
    root.image00= ImageTk.PhotoImage(Image.open(image00))
    firstButton = tk.Button(root,text='',width=100,height=80,bg='#353535',bd=0,image=root.image00, command= lambda: buttonClick(1,1,1,firstButton))


    lifeImage=livesList[3]
    root.lifeImage= ImageTk.PhotoImage(Image.open(lifeImage))
    
    image11=mat[0][0]
    root.image11= ImageTk.PhotoImage(Image.open(image11))

    image12=mat[0][1]
    root.image12= ImageTk.PhotoImage(Image.open(image12))

    image13=mat[0][2]
    root.image13= ImageTk.PhotoImage(Image.open(image13))

    image14=mat[0][3]
    root.image14= ImageTk.PhotoImage(Image.open(image14))

    image21=mat[1][0]
    root.image21= ImageTk.PhotoImage(Image.open(image21))

    image22=mat[1][1]
    root.image22= ImageTk.PhotoImage(Image.open(image22))

    image23=mat[1][2]
    root.image23= ImageTk.PhotoImage(Image.open(image23))

    image24=mat[1][3]
    root.image24= ImageTk.PhotoImage(Image.open(image24))     

    livesFont= font.Font(family="source sans pro", size=11, slant="italic")
    livesButton = tk.Button(root,compound="right", text="\t\t\t\t\t    Lives Left:", width=420,height=20,bg="#353535", bd=0, image=root.lifeImage, state=DISABLED,  )#"\t\t\t\t\t\t\t     "
    livesButton["font"]=livesFont


    firstFont = font.Font(family="source sans pro",size=15, )# Reem kufi, Modern M, Raleway MS, Gothic, Microsoft uighur,
    if playedOnce==0:
        welcomeMessage= tk.Button(root,text="ONCE YOU CLICK ME YOU WILL HAVE\n5 SECONDS TO REMEMBER THE POSITIONS\nOF EACH PAIR OF PHOTOS",width=45,height=5,bg="#353535",bd=0,fg="#BAF9FF",command=lambda: changeLayout())#Once you click me you'll have\n5 seconds to remember the positions\n of each pair of photos
        #welcomeMessage= tk.Button(root,text="Once you click me you'll have\n5 seconds to remember the positions\n of each pair of photos",padx=120,pady=30,bg="#353535",bd=0,fg="#fff",command=lambda: changeLayout())
        welcomeMessage.grid(columnspan= 4,row= 0, column=1, pady=2)  
        welcomeMessage["font"]=firstFont
        playedOnce=1 
    else:
        changeLayout()

    root.mainloop() 
"""Coded By 
                 █████╗ ██████╗ ███████╗██╗███████╗ █████╗ ████████╗ ██████╗ 
                ██╔══██╗██╔══██╗██╔════╝██║╚══███╔╝██╔══██╗╚══██╔══╝██╔═══██╗
                ███████║██████╔╝█████╗  ██║  ███╔╝ ███████║   ██║   ██║   ██║
                ██╔══██║██╔══██╗██╔══╝  ██║ ███╔╝  ██╔══██║   ██║   ██║   ██║
                ██║  ██║██║  ██║██║     ██║███████╗██║  ██║   ██║   ╚██████╔╝
                ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ 
"""
"""
    print("\n\n\n\n\n")
    x=0
    for a in range(1,3):
        for b in range(1,5):
            x+=1
            #print("root.image"+str(a)+str(b)+".subsample(8,8)")
            #print("image"+str(a)+str(b)+"=mat["+str(a-1)+"]["+str(b-1)+"]")
            #print("root.image"+str(a)+str(b)+"= ImageTk.PhotoImage(Image.open(image"+str(a)+str(b)+") ).subsample(8,8)")
            #print("button"+str(x)+" = tk.Button(root,text='',width=100,height=80,bg='#353535',bd=0,image=root.image00, command= lambda: buttonClick("+str(a)+","+str(b)+","+str(x)+",button"+str(x)+"))")
            #print("button"+str(x)+".grid(row="+str(a)+",column="+str(b)+",padx=2,pady=2)\n")
"""