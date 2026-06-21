"""Tema Biru Pastel Modern untuk Sistem Absensi"""
import tkinter as tk
from tkinter import ttk

# ==========================================================
# PALET WARNA BIRU PASTEL
# ==========================================================
COLOR_BG = "#eaf4ff"
COLOR_PANEL = "#ffffff"

COLOR_ACCENT = "#7cb7e8"
COLOR_ACCENT_DARK = "#5ea6e0"

COLOR_CARD = "#ffffff"

COLOR_TEXT = "#2c3e50"
COLOR_MUTED = "#6b7a8f"

COLOR_FIELD = "#f8fbff"
COLOR_FIELD_FOCUS = "#eef7ff"

COLOR_BORDER = "#d6e8f5"

# warna tambahan
SYN_KEYWORD = "#7cb7e8"
SYN_FUNC = "#5ea6e0"
SYN_STRING = "#90caf9"
SYN_COMMENT = "#90a4ae"
SYN_NUMBER = "#42a5f5"

MONO = "Segoe UI"


# ==========================================================
# WINDOW
# ==========================================================
def center_window(window, width, height):

    window.update_idletasks()

    screen_w = window.winfo_screenwidth()
    screen_h = window.winfo_screenheight()

    x = (screen_w - width) // 2
    y = (screen_h - height) // 3

    window.geometry(f"{width}x{height}+{x}+{y}")


# ==========================================================
# TITLE BAR
# ==========================================================
def make_title_bar(parent, title):

    bar = tk.Frame(
        parent,
        bg="#dcefff",
        height=35
    )

    bar.pack(fill="x")
    bar.pack_propagate(False)

    tk.Label(
        bar,
        text="●",
        fg="#ff6b6b",
        bg="#dcefff",
        font=("Segoe UI", 11)
    ).pack(side="left", padx=(10, 0))

    tk.Label(
        bar,
        text="●",
        fg="#ffd166",
        bg="#dcefff",
        font=("Segoe UI", 11)
    ).pack(side="left")

    tk.Label(
        bar,
        text="●",
        fg="#06d6a0",
        bg="#dcefff",
        font=("Segoe UI", 11)
    ).pack(side="left")

    tk.Label(
        bar,
        text=title,
        font=("Segoe UI", 10, "bold"),
        fg=COLOR_TEXT,
        bg="#dcefff"
    ).pack(side="left", padx=10)

    return bar


# ==========================================================
# BUTTON
# ==========================================================
def make_button(parent, text, command, primary=True):

    if primary:
        fg = "white"
        bg = COLOR_ACCENT
        hover = COLOR_ACCENT_DARK
    else:
        fg = COLOR_TEXT
        bg = "#eef7ff"
        hover = "#dcefff"

    btn = tk.Button(
        parent,
        text=text,
        command=command,
        font=("Segoe UI", 10, "bold"),
        fg=fg,
        bg=bg,
        activebackground=hover,
        activeforeground=fg,
        relief="flat",
        cursor="hand2",
        bd=0,
        padx=16,
        pady=8
    )

    btn.bind(
        "<Enter>",
        lambda e: btn.config(bg=hover)
    )

    btn.bind(
        "<Leave>",
        lambda e: btn.config(bg=bg)
    )

    return btn


# ==========================================================
# TREEVIEW
# ==========================================================
def style_treeview(style_name="Pastel.Treeview"):

    style = ttk.Style()

    try:
        style.theme_use("clam")
    except:
        pass

    style.configure(
        style_name,
        background="white",
        fieldbackground="white",
        foreground=COLOR_TEXT,
        rowheight=28,
        borderwidth=0,
        font=("Segoe UI", 10)
    )

    style.map(
        style_name,
        background=[("selected", "#b9ddff")],
        foreground=[("selected", COLOR_TEXT)]
    )

    style.configure(
        style_name + ".Heading",
        background="#dcefff",
        foreground=COLOR_TEXT,
        font=("Segoe UI", 10, "bold"),
        relief="flat",
        padding=8
    )

    style.map(
        style_name + ".Heading",
        background=[("active", "#cce7ff")]
    )

    style.configure(
        "Coding.Vertical.TScrollbar",
        background="#dcefff",
        troughcolor="#eef7ff",
        bordercolor="#eef7ff",
        arrowcolor=COLOR_TEXT
    )

    return style_name