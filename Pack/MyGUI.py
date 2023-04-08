from tkinter import Tk,Toplevel,PhotoImage,Label,Entry,Button,GROOVE,messagebox
from MyException import DataException
from model import File



class MyGUI:
    def __SetFormSize(self,form,wi=int,hi=int) -> None:
        w=wi
        h=hi
        root=Tk()
        if isinstance(form,Tk) or isinstance(form,Toplevel):
            ws=root.winfo_screenwidth()
            hs=root.winfo_screenheight()
            x=(ws/2)-(w/2)
            y=(hs/2)-(h/2)
            form.geometry("%dx%d+%d+%d"%(w,h,x,y))
            form.resizable(width=0,height=0)
            form.iconbitmap("icon.ico")

        root.destroy()

    def __init__(self) -> None:
        self.root=Tk()
        self.root.config(bg='red')
        self.root.title('Download YouTube')

        im=PhotoImage(file='img.png')
        self.__SetFormSize(self.root,300,400)

        self.lm=Label(master=self.root,bg="red",image=im,width='110',height='100')
        self.lm. grid(row=0,column=0,padx=15,pady=13,columnspan=2)

        self.l1=Label(master=self.root,fg="#000",bg="red",text='URL: ',font=('Agency FB',15),anchor='w')
        self.l1. grid(row=1,column=0,padx=1,pady=13)
        self.e1=Entry(master=self.root,text='URL',width='30')
        self.e1.grid(row=1,column=1)

        self.l2=Label(master=self.root,fg="#000",bg="red",text='Address: ',font=('Agency FB',15),anchor='w')
        self.l2. grid(row=2,column=0,padx=1,pady=13)
        self.e2=Entry(master=self.root,text='Address',width='30')
        self.e2.grid(row=2,column=1)

        self.b1=Button(master=self.root,text='Download',bg="#FFFFFF",fg='black',relief=GROOVE,height='1',width='38',font=('Agency FB',15))
        self.b1. grid(row=5,column=0,padx=13,pady=13,columnspan=2) 
        self.b1.bind('<Enter>',lambda i: self.b1.config(bg='black',fg='#FFFFFF')) 
        self.b1.bind('<Leave>',lambda i: self.b1.config(bg='#FFFFFF',fg='black'))
        self.b1.bind('<Button>',lambda i: self.__Download(i))

        self.b2=Button(master=self.root,text='Empty',bg="#FFFFFF",fg='black',relief=GROOVE,height='1',width='38',font=('Agency FB',15))
        self.b2. grid(row=6,column=0,padx=13,pady=13,columnspan=2) 
        self.b2.bind('<Enter>',lambda i: self.b2.config(bg='black',fg='#FFFFFF')) 
        self.b2.bind('<Leave>',lambda i: self.b2.config(bg='#FFFFFF',fg='black'))
        self.b2.bind('<Button>',lambda i: self.__Empty(i))

        self.root.mainloop()

    def __Download(self,i):
        try:
            f=File(self.e1.get(),self.e2.get())
            f.Chek(self.e1.get(),self.e2.get())
        except DataException as e:
            messagebox.showerror('Error',e)
        else:
            messagebox.showinfo('Info','Downloading...')
            f.DownloadVideo()
            messagebox.showinfo('Info','Check out the Download.')
            self.e1.delete(0,"end")

    def __Empty(self,i):
        self.e1.delete(0,"end")
        self.e2.delete(0,"end")