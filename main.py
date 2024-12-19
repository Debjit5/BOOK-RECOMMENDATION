from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import requests
from io import  BytesIO
import urllib.parse




class Request:
    def __init__(self,method,args):
        self.args=args
        self.method=method
inc=0
def fetch_information(title,poster,date,rating):
    global inc
    inc=inc+1

    text[f'a{inc}'].config(text=title)

    if check_var.get():
        text2[f'a{inc}{inc}'].config(text=date)
    else:
        text2[f'a{inc}{inc}'].config(text="")

    if check_var2.get():
        text3[f'a{inc}{inc}{inc}'].config(text=rating)
    else:
        text3[f'a{inc}{inc}{inc}'].config(text="")

    
    response=requests.get(poster)
    img_data=response.content
    img=(Image.open(BytesIO(img_data)))
    resized_image=img.resize((140,200))
    photo2=ImageTk.PhotoImage(resized_image)
    image[f'b{inc}'].config(image=photo2)
    image[f'b{inc}'].image=photo2


def search():
    global inc
    inc=0
    request=Request('GET',{'search':search_var.get()})

    if request.method == 'GET':
        search=urllib.parse.quote(request.args.get('search',''))
        url=f"https://www.googleapis.com/books/v1/volumes?q={search}&maxResults=5"
        response=requests.get(url)
        #print(response.json())

        if response.status_code==200:
            data=response.json()
            for item in data.get('items',[]):
                volumn_info=item.get('volumeInfo',{})
                title=volumn_info.get('title','N/A')
                publisher=volumn_info.get('publisher','N/A')
                published_date=volumn_info.get('publishedDate','N/A')
                author=volumn_info.get('authors',['N/A'])
                rating=volumn_info.get('averageRating',['N/A'])
                image_links=volumn_info.get('imageLinks',{})
                image=image_links.get('thumbnail') if 'thumbnail' in image_links else 'N/A'

                print(title)
                print(publisher)
                print(published_date)
                print(author)
                print(rating)
                print(image)

                fetch_information(title,image,published_date,rating)

                if check_var.get() or check_var2.get():
                    Frame11.place(x=160,y=520)
                    Frame22.place(x=360,y=520)
                    Frame33.place(x=560,y=520)
                    Frame44.place(x=760,y=520)
                    Frame55.place(x=960,y=520)
                else:
                    Frame11.place_forget()
                    Frame22.place_forget()
                    Frame33.place_forget()
                    Frame44.place_forget()
                    Frame55.place_forget()

        else:
            print("Failed to fetch Data from Google Books API")
            messagebox.showinfo("info","Failed To Fetch Data")

def show_menu(event):
    menu.post(event.x_root,event.y_root)

root=Tk()
root.title("Book Recommendation System")
root.geometry("1250x700+120+30")
root.config(bg="#111119")
root.resizable(False,False)


###################################################################

#icon

icon_image=PhotoImage(file="Images/icon.png")
root.iconphoto(False,icon_image)

#Background Image

heading_image=PhotoImage(file="Images/background.png")
Label(root,image=heading_image,bg="#111119").place(x=-2,y=-2)

#logo

logo_image=PhotoImage(file="Images/logo.png")
Label(root,image=logo_image,bg="#0099ff").place(x=300,y=80)

#Heading

heading=Label(root,text="BOOK RECOMENDATION",font=("Lato",30,"bold"),fg="white",bg="#0099ff")
heading.place(x=410,y=90)

#Searchbox Image

search_box=PhotoImage(file="Images/Rectangle 2.png")
Label(root,image=search_box,bg="#0099ff").place(x=300,y=155)

#entry box

search_var=StringVar()
search_entry=Entry(root,textvariable=search_var,font=("Lato",25),bd=0,width=21,bg="white",fg='black')
search_entry.place(x=415,y=172)


#Search Button
recommend_btn_img=PhotoImage(file="Images/Search.png")
recommend_btn=Button(root,image=recommend_btn_img,bg="#0099ff",bd=0,activebackground="#252532",cursor="hand2",command=search)
recommend_btn.place(x=860,y=169)

#Setting Button
setting_img=PhotoImage(file="Images/setting.png")
setting_btn=Button(root,image=setting_img,bd=0,cursor="hand2",bg="#0099ff",activebackground="#0099ff")
setting_btn.place(x=1050,y=175)
setting_btn.bind('<Button-1>',show_menu)

menu=Menu(root,tearoff=0) #Menu For Search Button

check_var=BooleanVar()
menu.add_checkbutton(label="Publish Date",variable=check_var,command=lambda:print(f"check Option is {'checked' if check_var.get() else 'unchecked'}"))

check_var2=BooleanVar()
menu.add_checkbutton(label="Rating",variable=check_var2,command=lambda:print(f"rating check Option is {'checked' if check_var2.get() else 'unchecked'}"))



#logout Button
logout_image=PhotoImage(file="Images/logout.png")
Button(root,image=logout_image,bg="#0099ff",cursor='hand1',command=lambda:root.destroy()).place(x=1150,y=20)

#####################################################################

#First Frame
Frame1=Frame(root,width=150,height=240,bg="white")
Frame2=Frame(root,width=150,height=240,bg="white")
Frame3=Frame(root,width=150,height=240,bg="white")
Frame4=Frame(root,width=150,height=240,bg="white")
Frame5=Frame(root,width=150,height=240,bg="white")

Frame1.place(x=160,y=270)
Frame2.place(x=360,y=270)
Frame3.place(x=560,y=270)
Frame4.place(x=760,y=270)
Frame5.place(x=960,y=270)

#Book Title
text={'a1':Label(Frame1,text="Book Title",font=("arial",10),fg='green'),'a2':Label(Frame2,text="Book Title",font=("arial",10),fg='green'),'a3':Label(Frame3,text="Book Title",font=("arial",10),fg='green'),'a4':Label(Frame4,text="Book Title",font=("arial",10),fg='green'),'a5':Label(Frame5,text="Book Title",font=("arial",10),fg='green')}
text["a1"].place(x=10,y=4)
text["a2"].place(x=10,y=4)
text["a3"].place(x=10,y=4)
text["a4"].place(x=10,y=4)
text["a5"].place(x=10,y=4)

#Image of Book
image={'b1':Label(Frame1),'b2':Label(Frame2),'b3':Label(Frame3),'b4':Label(Frame4),'b5':Label(Frame5)}
image["b1"].place(x=3,y=30)
image["b2"].place(x=3,y=30)
image["b3"].place(x=3,y=30)
image["b4"].place(x=3,y=30)
image["b5"].place(x=3,y=30) 

#####################################################################

#Second Frame
Frame11=Frame(root,width=150,height=50,bg="#e6e6e6")
Frame22=Frame(root,width=150,height=50,bg="#e6e6e6")
Frame33=Frame(root,width=150,height=50,bg="#e6e6e6")
Frame44=Frame(root,width=150,height=50,bg="#e6e6e6")
Frame55=Frame(root,width=150,height=50,bg="#e6e6e6")



#Published Date
text2={'a11':Label(Frame11,text='date',font=('arial',10),bg='#e6e6e6',fg='red'),'a22':Label(Frame22,text='date',font=('arial',10),bg='#e6e6e6',fg='red'),'a33':Label(Frame33,text='date',font=('arial',10),bg='#e6e6e6',fg='red'),'a44':Label(Frame44,text='date',font=('arial',10),bg='#e6e6e6',fg='red'),'a55':Label(Frame55,text='date',font=('arial',10),bg='#e6e6e6',fg='red')}
text2["a11"].place(x=10,y=4)
text2["a22"].place(x=10,y=4)
text2["a33"].place(x=10,y=4)
text2["a44"].place(x=10,y=4)
text2["a55"].place(x=10,y=4)


#Rating
text3={'a111':Label(Frame11,text='rating',font=('arial',10),bg='#e6e6e6'),'a222':Label(Frame22,text='rating',font=('arial',10),bg='#e6e6e6'),'a333':Label(Frame33,text='rating',font=('arial',10),bg='#e6e6e6'),'a444':Label(Frame44,text='rating',font=('arial',10),bg='#e6e6e6'),'a555':Label(Frame55,text='rating',font=('arial',10),bg='#e6e6e6')}
text3["a111"].place(x=20,y=30)
text3["a222"].place(x=20,y=30)
text3["a333"].place(x=20,y=30)
text3["a444"].place(x=20,y=30)
text3["a555"].place(x=20,y=30)


####################################################################

root.mainloop()