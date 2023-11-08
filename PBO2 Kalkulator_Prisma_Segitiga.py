import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END,W

def hitung_luas():
    s1 = float(txtsisi1.get())
    s2 = float(txtsisi2.get())
    s3 = float(txtsisi3.get())
    T = float(txtTinggi_prisma.get())
    at = float(txtluas_segitiga.get())

    L = round(s1 + s2 + s3 * T * at, 1)

    txtLuas.delete(0,END)
    txtLuas.insert(END,L)

def hitung_volume():
    a = float(txtalas.get())
    t = float(txttinggi.get())
    T = float(txttinggi.get())

    V = round(1/2 * a * t * T)
    txtVolume.delete(0,END)
    txtVolume.insert(END,V)

def hitung():
    hitung_luas()
    hitung_volume()


app = tk.Tk()

app.title("Aplikasi penghitung luas dan keliling Prisma Segi tiga")

app.geometry("450x450")

frame = Frame(app)
frame.pack(padx=20, pady=20)

sisi1 = Label(frame, text="sisi1:")
sisi1.grid(row=0, column=0, sticky=W, padx=5, pady=5)

txtsisi1 = Entry(frame)
txtsisi1.grid(row=0, column=1)

s2 = Label(frame, text="sisi2:")
s2.grid(row=1, column=0, sticky=W, padx=5, pady=5)

txtsisi2 = Entry(frame)
txtsisi2.grid(row=1, column=1)

sisi3 = Label(frame, text="sisi3:")
sisi3.grid(row=2, column=0, sticky=W, padx=5, pady=5)

txtsisi3 = Entry(frame)
txtsisi3.grid(row=2, column=1)

Tinggi_prisma = Label(frame, text="Tinggi_prisma:")
Tinggi_prisma.grid(row=3, column=0, sticky=W, padx=5, pady=5)

txtTinggi_prisma = Entry(frame)
txtTinggi_prisma.grid(row=3, column=1)

luas_segitiga = Label(frame, text="luas_segitiga:")
luas_segitiga.grid(row=4, column=0, sticky=W, padx=5, pady=5)

txtluas_segitiga = Entry(frame)
txtluas_segitiga.grid(row=4, column=1)

alas = Label(frame, text="alas:")
alas.grid(row=5, column=0, sticky=W, padx=5, pady=5)

txtalas = Entry(frame)
txtalas.grid(row=5, column=1)

tinggi = Label(frame, text="tinggi_segitiga:")
tinggi.grid(row=7, column=0, sticky=W, padx=5, pady=5)

txttinggi = Entry(frame)
txttinggi.grid(row=7, column=1)

hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=9, column=1, sticky=W, padx=5, pady=5)

luas = Label(frame, text="Luas: ")
luas.grid(row=10, column=0, sticky=W, padx=5, pady=5)

volume = Label(frame, text="Volume: ")
volume.grid(row=11, column=0, sticky=W, padx=5, pady=5)

txtLuas = Entry(frame)
txtLuas.grid(row=10, column=1, sticky=W, padx=5, pady=5)

txtVolume = Entry(frame)
txtVolume.grid(row=11, column=1, sticky=W, padx=5, pady=5)

app.mainloop()

