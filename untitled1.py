import tkinter as Tk
from tkinter import *
from textblob import TextBlob




root = Tk()
root.geometry("1000x500")
root.title("Sentiment Analysis")
root.configure(bg='white')



#add label
label1 = Label(text="Test  with your own text" ,font=("italic", 20) ,bg='white')
label1.place(x=37, y=65)

#add textBox
text_box=Text(root, height=17 ,width=55)
text_box.place(x=37, y=125)

#act btn
def Classify():
    
    inputText = text_box.get("1.0",'end-1c')

    
    sent=TextBlob(inputText)
    x =sent.sentiment.polarity



    if x<0:
        text1.insert(0,"negative")
    elif x==0:
        text1.insert(0,"neutral")
    elif x>0 and x<=1:
        text1.insert(0,"positive")
        
        
  #btn      
button =Button(
text="Classify Text" ,
fg="white" , bg="#1a73e8",
width=18,relief="flat",
font=('italic', 12 ),
command=Classify
)
button.place(x=37, y=420)



#textbox2
text1 = Entry(root,width=55 ,text="") 
text1.place(x=520, y=125)


#affichage
root.mainloop()
