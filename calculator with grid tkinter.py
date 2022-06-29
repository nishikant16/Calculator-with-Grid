#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
root=Tk()
root.title('My Calculator')
root.geometry('')
data=StringVar()
val=''
def btnClick(num):
    global val
    val=val+str(num)
    data.set(val)
    
def Clear():
    global val
    val=" "
    data.set("")
    data.set(0)
    
def Equals():
    global val
    result=str(eval(val))
    data.set(result)
    
display=Entry(root,textvariable=data,bd=29,bg='sky blue',justify='right',font=("times new roman",20))
display.grid(row=0,columnspan=4)
button7=Button(root,text='7',bd=12,height=2,font=('times new roman',12,'bold'),width=6,command=lambda:btnClick(7))
button7.grid(row=1,column=0)
button8=Button(root,text='8',bd=12,height=2,font=('times new roman',12,'bold'),width=6,command=lambda:btnClick(8))
button8.grid(row=1,column=1)
button9=Button(root,text='9',bd=12,height=2,font=('times new roman',12,'bold'),width=6,command=lambda:btnClick(9))
button9.grid(row=1,column=2)
button_add=Button(root,text='+',bd=12,height=2,font=('times new roman',12,'bold'),width=6,command=lambda:btnClick('+'))
button_add.grid(row=1,column=3)
button4=Button(root,text='4',bd=12,height=2,font=('times new roman',12,'bold'),width=6,command=lambda:btnClick(4))
button4.grid(row=2,column=0)
button5=Button(root,text='5',bd=12,height=2,font=('times new roman',12,'bold'),width=6,command=lambda:btnClick(5))
button5.grid(row=2,column=1)
button6=Button(root,text='6',bd=12,height=2,font=('times new roman',12,'bold'),width=6,command=lambda:btnClick(6))
button6.grid(row=2,column=2)
button_min=Button(root,text='-',bd=12,height=2,font=('times new roman',12,'bold'),width=6,command=lambda:btnClick('-'))
button_min.grid(row=2,column=3)
button1=Button(root,text='1',bd=12,height=2,font=('times new roman',12,'bold'),width=6,command=lambda:btnClick(1))
button1.grid(row=3,column=0)
button2=Button(root,text='2',bd=12,height=2,font=('times new roman',12,'bold'),width=6,command=lambda:btnClick(2))
button2.grid(row=3,column=1)
button3=Button(root,text='3',bd=12,height=2,font=('times new roman',12,'bold'),width=6,command=lambda:btnClick(3))
button3.grid(row=3,column=2)
button_mul=Button(root,text='*',bd=12,height=2,font=('times new roman',12,'bold'),width=6,command=lambda:btnClick('*'))
button_mul.grid(row=3,column=3)

buttonC=Button(root,text='C',bd=12,height=2,font=('times new roman',12,'bold'),width=6,command=Clear)
buttonC.grid(row=4,column=0)
button0=Button(root,text='0',bd=12,height=2,font=('times new roman',12,'bold'),width=6,command=lambda:btnClick(0))
button0.grid(row=4,column=1)
buttondiv=Button(root,text='/',bd=12,height=2,font=('times new roman',12,'bold'),width=6,command=lambda:btnClick('/'))
buttondiv.grid(row=4,column=2)
button_eql=Button(root,text='=',bd=12,height=2,font=('times new roman',12,'bold'),width=6,command=Equals)
button_eql.grid(row=4,column=3)

root.mainloop()


# In[ ]:




