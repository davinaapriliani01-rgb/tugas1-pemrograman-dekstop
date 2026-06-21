import os
import tkinter as tk
from tkinter import font as tkfont
from PIL import Image, ImageTk, ImageDraw

# ============================================================
# DATA BIODATA
# ============================================================
BIODATA = {
    "nama": "Davina Apriliani Putri",
    "foto": "davina.jpg",
    "status": "Mahasiswa Informatika",
    "data": [
        ("Tempat, Tgl Lahir", "Cilacap, 1 April 2005"),
        ("Jenis Kelamin", "Perempuan"),
        ("Alamat", "Majenang, Indonesia"),
        ("Email", "davinaapriliani01@gmail.com"),
        ("Telepon", "+62 856-0072-0961"),
        ("Hobi", "Memasak dan Membuat Kue"),
    ],
    "moto": "Kreativitas dalam rasa, ketulusan dalam karya."
}

# ============================================================
# WARNA
# ============================================================
BG = "#eaf4ff"
CARD = "#ffffff"
TEXT = "#1f3f72"
MUTED = "#6d8db3"
LINE = "#cfe0f5"
FLOWER = "#cfe8ff"

# ============================================================
# FOTO LINGKARAN
# ============================================================
def buat_foto_lingkaran(path, size):
    if not os.path.exists(path):
        return None

    img = Image.open(path).convert("RGB")

    w, h = img.size
    sisi = min(w, h)

    left = (w - sisi) // 2
    top = (h - sisi) // 2

    img = img.crop((left, top, left + sisi, top + sisi))
    img = img.resize((size, size), Image.LANCZOS)

    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)

    img.putalpha(mask)

    return ImageTk.PhotoImage(img)

# ============================================================
# BUNGA
# ============================================================
def gambar_bunga(canvas, x, y, ukuran=30):

    canvas.create_oval(
        x-ukuran, y-10,
        x, y+10,
        fill=FLOWER, outline=""
    )

    canvas.create_oval(
        x, y-10,
        x+ukuran, y+10,
        fill=FLOWER, outline=""
    )

    canvas.create_oval(
        x-10, y-ukuran,
        x+10, y,
        fill=FLOWER, outline=""
    )

    canvas.create_oval(
        x-10, y,
        x+10, y+ukuran,
        fill=FLOWER, outline=""
    )

    canvas.create_oval(
        x-8, y-8,
        x+8, y+8,
        fill="white",
        outline=""
    )

# ============================================================
# WINDOW
# ============================================================
root = tk.Tk()
root.title("Biodata Davina")
root.geometry("550x850")
root.configure(bg=BG)
root.resizable(False, False)

# ============================================================
# BACKGROUND
# ============================================================
canvas_bg = tk.Canvas(
    root,
    width=550,
    height=850,
    bg=BG,
    highlightthickness=0
)

canvas_bg.place(x=0, y=0)

# bunga pojok
gambar_bunga(canvas_bg, 50, 50, 35)
gambar_bunga(canvas_bg, 110, 100, 25)

gambar_bunga(canvas_bg, 500, 50, 35)
gambar_bunga(canvas_bg, 440, 100, 25)

gambar_bunga(canvas_bg, 50, 780, 35)
gambar_bunga(canvas_bg, 110, 720, 25)

gambar_bunga(canvas_bg, 500, 780, 35)
gambar_bunga(canvas_bg, 440, 720, 25)

# titik dekorasi
for x in range(50, 550, 80):
    canvas_bg.create_oval(
        x, 180,
        x+4, 184,
        fill="#bddfff",
        outline=""
    )

# ============================================================
# FONT
# ============================================================
f_nama = tkfont.Font(
    family="Segoe UI",
    size=20,
    weight="bold"
)

f_status = tkfont.Font(
    family="Segoe UI",
    size=12
)

f_data = tkfont.Font(
    family="Segoe UI",
    size=11
)

f_moto = tkfont.Font(
    family="Segoe UI",
    size=11,
    slant="italic"
)

# ============================================================
# CARD
# ============================================================
card = tk.Frame(
    root,
    bg=CARD,
    highlightbackground=LINE,
    highlightthickness=2
)

card.place(
    relx=0.5,
    rely=0.5,
    anchor="center",
    width=450,
    height=760
)

# ============================================================
# FOTO
# ============================================================
foto = buat_foto_lingkaran(
    BIODATA["foto"],
    160
)

if foto:
    lbl_foto = tk.Label(
        card,
        image=foto,
        bg=CARD
    )
    lbl_foto.image = foto
    lbl_foto.pack(pady=(25, 10))

# ============================================================
# NAMA
# ============================================================
tk.Label(
    card,
    text=BIODATA["nama"],
    bg=CARD,
    fg=TEXT,
    font=f_nama
).pack()

# ============================================================
# STATUS
# ============================================================
tk.Label(
    card,
    text=BIODATA["status"],
    bg=CARD,
    fg=MUTED,
    font=f_status
).pack(pady=(5, 15))

# ============================================================
# GARIS
# ============================================================
tk.Frame(
    card,
    bg=LINE,
    height=2
).pack(fill="x", padx=40)

# ============================================================
# DATA BIODATA
# ============================================================
info = tk.Frame(
    card,
    bg=CARD
)

info.pack(
    fill="x",
    padx=40,
    pady=20
)

for label, value in BIODATA["data"]:

    row = tk.Frame(
        info,
        bg=CARD
    )

    row.pack(
        fill="x",
        pady=8
    )

    tk.Label(
        row,
        text=label,
        width=18,
        anchor="w",
        bg=CARD,
        fg=TEXT,
        font=f_data
    ).pack(side="left")

    tk.Label(
        row,
        text=":",
        bg=CARD,
        fg=TEXT,
        font=f_data
    ).pack(side="left")

    tk.Label(
        row,
        text=value,
        bg=CARD,
        fg="#333333",
        font=f_data
    ).pack(side="left", padx=(10, 0))

# ============================================================
# GARIS BAWAH
# ============================================================
tk.Frame(
    card,
    bg=LINE,
    height=2
).pack(fill="x", padx=40, pady=(10, 15))

# ============================================================
# MOTO
# ============================================================
tk.Label(
    card,
    text=f'"{BIODATA["moto"]}"',
    bg=CARD,
    fg=MUTED,
    font=f_moto,
    wraplength=320,
    justify="center"
).pack(pady=10)

# ============================================================
# RUN
# ============================================================
root.mainloop()