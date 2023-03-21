import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np

# fungsi untuk memproses citra dengan metode Transformasi Negatif
def negative_transform(img):
    negative_img = 255 - img
    return negative_img

# fungsi untuk memproses citra dengan metode Blur
def blurring(img):
    blur_img = cv2.blur(img, (15, 15))
    return blur_img

# fungsi untuk memproses citra dengan metode pertajam
def sharpening(img):
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharpened_img = cv2.filter2D(img, -1, kernel)
    return sharpened_img

# fungsi untuk menampilkan gambar dalam kotak
def show_image(img, x, y, title):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=img)
    label.image = img
    label.place(x=x, y=y)
    title_label = tk.Label(root, text=title)
    title_label.place(x=x, y=y-20)

# fungsi untuk menampilkan informasi pembuat program
def show_creator():
    creator_label = tk.Label(root, text='Nama : Afifa Wulandari   | NIM : F55121057   | Kelas : B  | ')
    creator_label.place(x=310, y=510)

# fungsi untuk membuka dan menampilkan gambar
def open_image():
    global original_img
    file_path = filedialog.askopenfilename()
    if file_path:
        original_img = cv2.imread(file_path)
        original_img = cv2.resize(original_img, (200, 300))
        show_image(original_img, 70, 118, 'Gambar Original')
        size_label.config(text='Dimensi Gambar : {} x {}'.format(original_img.shape[1], original_img.shape[0]))
        corrected_img1 = blurring(original_img)
        show_image(corrected_img1, 300, 118, 'Hasil Metode Blur')
        corrected_img2 = sharpening(original_img)
        show_image(corrected_img2, 500, 118, 'Hasil Metode Pertajam')
        corrected_img = negative_transform(original_img)
        show_image(corrected_img, 700, 118, 'Hasil Metode Negatif')


# membuat jendela utama
root = tk.Tk()
root.geometry('1000x600')
root.title('Interface Aplikasi Perbaikan Citra')

# menambahkan kotak untuk menampilkan hasil perbaikan citra
bold_font = ("Arial", 12, "bold")
result_box = tk.LabelFrame(root, text='Perbaikan Citra', padx=5, pady=5, font=bold_font)
result_box.place(x=50, y=50, width=900, height=415)

# menambahkan tombol untuk membuka gambar
open_button = tk.Button(result_box, text='Pilih Gambar Disini!', command=open_image)
open_button.place(x=10, y=348)

# menambahkan label untuk menampilkan dimensi gambar
size_label = tk.Label(result_box, text='Dimensi Gambar : -')
size_label.place(x=150, y=350)

# menambahkan kotak untuk informasi pembuat program
creator_box = tk.LabelFrame(root, text='Disusun Oleh', padx=5, pady=5, font=bold_font)
creator_box.place(x=280, y=480, width=360, height=70)

# menampilkan informasi pembuat program
show_creator()

# menjalankan aplikasi
root.mainloop()