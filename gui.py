import tkinter as tk
from tkinter import StringVar, ttk
from typing_extensions import IntVar
from PIL import ImageTk
from PIL import Image,ImageTk
from tkinter import *

window = tk.Tk()
window.title("RSA Encryption & Decryption")
window.geometry("600x800")
window.resizable(False,False)

###########################################################
x = StringVar(window, value='53')
v = StringVar(window, value='59')

#######################################################
def gcd(x,y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
#########################################################

def displayKeys():
    public_key_box.delete(1.0,END)
    private_key_box.delete(1.0,END)

    n,e,d = keyGeneration()
     #Showing key to output 
    public_key_box.insert(1.0,str(e))
    private_key_box.insert(1.0,str(d))


def keyGeneration():
    
    # print("p=",x.get())
    # print("q=",v.get())
    p=int(v.get())
    q=int(x.get())
     #Public key 
    n= p*q
    phi = (p-1)*(q-1)
    e = 2
    while(e<phi):

        if(gcd(e,phi)==1):
            break
        
        e = e+1
    # print("PHI = ",phi)
    # print("n = ",n)
    # print("E = ",e)
    #Private Key 
    # d = (1%phi)/e #Formula one
    k = 1
    d = int((1 + (k*phi))/e)
    # d = 1/e % (p-1)*(q-1)
    

   

    return n,e,d


    ######################### Convert Text into Number ########################
def TextNumber(input):
    message =""
    
    input = input.lower()
    output = []
    for character in input:
        number = ord(character)-96
        output.append(number)
    # print("Output = ",output)
    for item in output:
        if item > 0:
            print(item)
            message= message + str(item) 
    return message



def NumberText(result):
    g =""
    for i in range(len(result)):
        if int(result[i])<97:
            formula = (int(result[i])-1) + 97
            g = g + str(chr(formula))
    return g

          

def encryptText():
    #Empty result string
    result = ""
    Encryption_output.delete(1.0,END)
    
    #For values of N,E
    n,e,d=keyGeneration()
    input = Encryption_box.get(1.0,END)
    clean_input = input.strip()
    # print("Type = ",type(input))
    # print("Encryption input = ",input)
    if clean_input.isnumeric() == True :
         c = str((int(input)**e)%n)
         Encryption_output.insert(1.0,c)
         print("Encrypted C = ",c)
    else:
        message = TextNumber(input) 
        print("Value of E inside encryption = ",e)
        print("Value of N inside encryption = ",n)  
        print("Final Message = ",message)
        # Encryption c = (msg ^ e) % n
        c = str((int(message)**e)%n)
        print("Encrypted C = ",c)
        result = NumberText(c)
        Encryption_output.insert(1.0,result)

def decryptText():
    result = ""
    Decryption_output.delete(1.0,END)
    n,e,d=keyGeneration()
    input_text = Decryption.get(1.0,END)
    clean_input = input_text.strip()
   
    if clean_input.isnumeric() == True:
        m = str((int(input_text)**d)%n)
        Decryption_output.insert(1.0,m)
        print("Decrypted M= ",m)
    else:
        ciptext = TextNumber(input_text) 
        #For values of N,E,D
       
        #Decryption m = (c ^ d) % n
        print("CyperText =",ciptext)
        m = str((int(ciptext)**d)%n)
        print("Decrypted M= ",m)
        result = NumberText(m)
            # str(chr(formula))
            # print(chr(formula))


        Decryption_output.insert(1.0,result)
        print(result)




#logo

# logo = Image.open("./tb.png")
logo = ImageTk.PhotoImage(file="./tb.png")
logo_label = tk.Label(image=logo)
logo_label.image = logo 
logo_label.pack()

#Entry Box for p & q


p_label = tk.Label(window,text="First Prime Number",font=("Arial",8))
p_label.place(x=40,y=180)
ttk.Style().configure('pad.TEntry', padding='2 3 2 3')
p = ttk.Entry(window,textvariable=v,width=10,style='pad.TEntry',justify='center')
p.place(x=140,y=178)
q_label = tk.Label(window,text="Second Prime Number",font=("Arial",8))
q_label.place(x=311,y=180)
ttk.Style().configure('pad.TEntry', padding='2 3 2 3')
q = ttk.Entry(window,textvariable=x,width=10,style='pad.TEntry',justify='center')
q.place(x=430,y=178)

#Display box for Public/Private Key
public_key_label = tk.Label(window,text="Public Key",font=("Arial",8,"bold"))
public_key_label.place(x=40,y=220)

public_key_box = Text(window,height=4,width=26,padx=10,pady=10)
public_key_box.place(x=40,y=240)

private_key_label = tk.Label(window,text="Private Key",font=("Arial",8,"bold"))
private_key_label.place(x=310,y=220)

private_key_box = Text(window,height=4,width=26,padx=10,pady=10)
private_key_box.place(x=310,y=240)

#Generate Key button
button = tk.Button(window,text="Generate Key",command= displayKeys,pady=5,padx=10,background="#7069ff",foreground="#fff",font=("Arial",11,"bold"))
button.place(x=225,y=340)

#Encryption Box 
Encryption_label = tk.Label(window,text="Enter Plain Text to Encrypt",font=("Arial",8,"bold"))
Encryption_label.place(x=40,y=390)

Encryption_box = tk.Text(window,height=4,width=26,padx=10,pady=10)
Encryption_box.place(x=40,y=410)

Decryption_label = tk.Label(window,text="Enter Encrypted Text to Decrypt",font=("Arial",8,"bold"))
Decryption_label.place(x=310,y=390)

Decryption = tk.Text(window,height=4,width=26,padx=10,pady=10)
Decryption.place(x=310,y=410)

#Button
button = tk.Button(window,text="Encrypt",command=encryptText,pady=5,padx=10,background="#0373fc",foreground="#fff",font=("Arial",11,"bold"))
button.place(x=40,y=520)

button = tk.Button(window,text="Decrypt",command=decryptText,pady=5,padx=10,background="#0373fc",foreground="#fff",font=("Arial",11,"bold"))
button.place(x=310,y=520)

#output

Encryption_output_label = tk.Label(window,text="Encrypted Output",font=("Arial",8,"bold"))
Encryption_output_label.place(x=40,y=580)

Encryption_output = tk.Text(window,height=4,width=26,padx=10,pady=10)
Encryption_output.place(x=40,y=600)

Decryption_output_label = tk.Label(window,text="Decrypted Output",font=("Arial",8,"bold"))
Decryption_output_label.place(x=310,y=580)

Decryption_output = tk.Text(window,height=4,width=26,padx=10,pady=10)
Decryption_output.place(x=310,y=600)




window.mainloop()