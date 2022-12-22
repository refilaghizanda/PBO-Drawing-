# Aplikasi Paint dengan Python

#import seluruh library yanng di butuhkan

from tkinter import *
from tkinter.ttk import Scale
from tkinter import colorchooser,filedialog,messagebox
import PIL.ImageGrab as ImageGrab


#Definisi class dan constructor program
class Draw():
    def __init__(self,root):

#Definisikan judul dan ukuran window GUI 
        self.root =root
        self.root.title("Drawing Application")
        self.root.geometry("810x530")
        self.root.configure(background="white")
        self.root.resizable(0,0)
 
#Variabel untuk cursor    
        self.pointer= "black"
        self.erase="white"

#Widgets untuk jendela tkinker
    
# Konfigurasi tata letak, ukuran font dan warna
        text=Text(root)
        text.tag_configure("tag_name", justify='center', font=('arial',25),background='#292826',foreground='orange')

# Masukan text
        text.insert("1.0", "Drawing Application in Python")

# tambahkan tag 
        text.tag_add("tag_name", "1.0", "end")
        text.pack()
        
# tentukan warna pada panel bar 
        self.pick_color = LabelFrame(self.root,text='Colors',font =('arial',15),bd=5,relief=RIDGE,bg="black")
        self.pick_color.place(x=0,y=40,width=90,height=185)

        colors = ['blue','red','green', 'orange','violet','black','yellow','purple','pink','gold','brown','indigo']
        i=j=0
        for color in colors:
            Button(self.pick_color,bg=color,bd=2,relief=RIDGE,width=3,command=lambda col=color:self.select_color(col)).grid(row=i,column=j)
            i+=1
            if i==6:
                i=0
                j=1

 # Tombol penghapus dan propertinya  
        self.eraser_btn= Button(self.root,text="Eraser",bd=4,bg='white',command=self.eraser,width=9,relief=RIDGE)
        self.eraser_btn.place(x=0,y=197)

# Tombol reset layar 
        self.clear_screen= Button(self.root,text="Clear Screen",bd=4,bg='white',command= lambda : self.background.delete('all'),width=9,relief=RIDGE)
        self.clear_screen.place(x=0,y=227)

# Tombol simpan hasil menggambar ke komputer local
        self.save_btn= Button(self.root,text="ScreenShot",bd=4,bg='white',command=self.save_drawing,width=9,relief=RIDGE)
        self.save_btn.place(x=0,y=257)

# Tombol untuk menentukan warna background 
        self.bg_btn= Button(self.root,text="Background",bd=4,bg='white',command=self.canvas_color,width=9,relief=RIDGE)
        self.bg_btn.place(x=0,y=287)


# ukuran kursor dan penghapus
        self.pointer_frame= LabelFrame(self.root,text='size',bd=5,bg='white',font=('arial',15,'bold'),relief=RIDGE)
        self.pointer_frame.place(x=0,y=320,height=200,width=70)

        self.pointer_size =Scale(self.pointer_frame,orient=VERTICAL,from_ =50 , to =0, length=170)
        self.pointer_size.set(1)
        self.pointer_size.grid(row=0,column=1,padx=15)


#Definisikan warna background pada area kerja 
        self.background = Canvas(self.root,bg='white',bd=5,relief=GROOVE,height=470,width=680)
        self.background.place(x=80,y=40)


# Bind untuk memilik warna ketika di klik
        self.background.bind("<B1-Motion>",self.paint) 



# Fungsi menggambar pada garis area kerja
    def paint(self,event):       
        x1,y1 = (event.x-2), (event.y-2)  
        x2,y2 = (event.x+2), (event.y+2)  

        self.background.create_oval(x1,y1,x2,y2,fill=self.pointer,outline=self.pointer,width=self.pointer_size.get())

# Fungsi memilih warna pada kursor  
    def select_color(self,col):
        self.pointer = col

# Fungsi memilih warna penghapus
    def eraser(self):
        self.pointer= self.erase

# Fungsi memilih warna background area kerja 
    def canvas_color(self):
        color=colorchooser.askcolor()
        self.background.configure(background=color[1])
        self.erase= color[1]

# Fungsi menyimpan gambar ke lokal komputer
    def save_drawing(self):
        try:
            # self.background update()
            file_ss =filedialog.asksaveasfilename(defaultextension='jpg')
            #print(file_ss)
            x=self.root.winfo_rootx() + self.background.winfo_x()
            #print(x, self.background.winfo_x())
            y=self.root.winfo_rooty() + self.background.winfo_y()
            #print(y)

            x1= x + self.background.winfo_width() 
            #print(x1)
            y1= y + self.background.winfo_height()
            #print(y1)
            ImageGrab.grab().crop((x , y, x1, y1)).save(file_ss)
            messagebox.showinfo('Screenshot Successfully Saved as' + str(file_ss))

        except:
            print("Error in saving the screenshot")

if __name__ =="__main__":
    root = Tk()
    p= Draw(root)
    root.mainloop()