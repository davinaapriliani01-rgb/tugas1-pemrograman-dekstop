import tkinter as tk
from tkinter import messagebox
from models.model_users import User

# ==========================================================
# WARNA TEMA BIRU PASTEL
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


class LoginView:

    def __init__(self, master=None, on_login_success=None):

        self.master = master or tk.Tk()
        self.on_login_success = on_login_success

        self.master.title("Sistem Absensi Mahasiswa")
        self.master.configure(bg=COLOR_BG)
        self.master.resizable(False, False)

        self._center_window(900, 550)

        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        self._password_hidden = True

        self._build_ui()

    # ======================================================
    # CENTER WINDOW
    # ======================================================
    def _center_window(self, width, height):

        self.master.update_idletasks()

        screen_w = self.master.winfo_screenwidth()
        screen_h = self.master.winfo_screenheight()

        x = (screen_w - width) // 2
        y = (screen_h - height) // 3

        self.master.geometry(
            f"{width}x{height}+{x}+{y}"
        )

    # ======================================================
    # UI
    # ======================================================
    def _build_ui(self):

        container = tk.Frame(
            self.master,
            bg=COLOR_BG
        )

        container.pack(
            fill="both",
            expand=True
        )

        self._build_left_panel(container)
        self._build_right_panel(container)

    # ======================================================
    # PANEL KIRI
    # ======================================================
    def _build_left_panel(self, parent):

        left = tk.Frame(
            parent,
            bg=COLOR_BG,
            width=420
        )

        left.pack(
            side="left",
            fill="both"
        )

        left.pack_propagate(False)

        tk.Label(
            left,
            text="🎓",
            font=("Segoe UI Emoji", 70),
            bg=COLOR_BG
        ).pack(
            pady=(80, 15)
        )

        tk.Label(
            left,
            text="SISTEM ABSENSI",
            font=("Segoe UI", 24, "bold"),
            fg=COLOR_TEXT,
            bg=COLOR_BG,
            justify="center"
        ).pack()

        tk.Label(
            left,
            text="",
            font=("Segoe UI", 12),
            fg=COLOR_MUTED,
            bg=COLOR_BG
        ).pack(
            pady=(10, 30)
        )

        quote = """
"Disiplin adalah jembatan
antara tujuan dan pencapaian."
"""

        tk.Label(
            left,
            text=quote,
            font=("Segoe UI", 11, "italic"),
            fg=COLOR_ACCENT,
            bg=COLOR_BG,
            justify="center"
        ).pack()

    # ======================================================
    # PANEL KANAN
    # ======================================================
    def _build_right_panel(self, parent):

        right = tk.Frame(
            parent,
            bg=COLOR_CARD
        )

        right.pack(
            side="left",
            fill="both",
            expand=True
        )

        form = tk.Frame(
            right,
            bg=COLOR_CARD
        )

        form.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        tk.Label(
            form,
            text="LOGIN",
            font=("Segoe UI", 11, "bold"),
            fg=COLOR_ACCENT,
            bg=COLOR_CARD
        ).pack(anchor="w")

        tk.Label(
            form,
            text="Selamat Datang 👋",
            font=("Segoe UI", 22, "bold"),
            fg=COLOR_TEXT,
            bg=COLOR_CARD
        ).pack(
            anchor="w",
            pady=(5, 2)
        )

        tk.Label(
            form,
            text="Silakan masuk ke sistem absensi",
            font=("Segoe UI", 10),
            fg=COLOR_MUTED,
            bg=COLOR_CARD
        ).pack(
            anchor="w",
            pady=(0, 25)
        )

        self.username_entry = self._build_field(
            form,
            "Username",
            self.username_var
        )

        self.password_entry = self._build_field(
            form,
            "Password",
            self.password_var,
            show="*"
        )

        self.login_btn = tk.Button(
            form,
            text="Masuk",
            command=self.login,
            font=("Segoe UI", 12, "bold"),
            fg="white",
            bg=COLOR_ACCENT,
            activebackground=COLOR_ACCENT_DARK,
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            pady=10
        )

        self.login_btn.pack(
            fill="x",
            pady=(20, 0)
        )

        tk.Label(
            form,
            text="© Sistem Absensi",
            font=("Segoe UI", 9),
            fg=COLOR_MUTED,
            bg=COLOR_CARD
        ).pack(
            pady=(20, 0)
        )

        self.master.bind(
            "<Return>",
            lambda e: self.login()
        )

        self.username_entry.focus_set()

    # ======================================================
    # FIELD
    # ======================================================
    def _build_field(
        self,
        parent,
        label,
        variable,
        show=None
    ):

        tk.Label(
            parent,
            text=label,
            font=("Segoe UI", 10, "bold"),
            fg=COLOR_TEXT,
            bg=COLOR_CARD
        ).pack(
            anchor="w",
            pady=(0, 5)
        )

        wrapper = tk.Frame(
            parent,
            bg=COLOR_FIELD,
            highlightbackground=COLOR_BORDER,
            highlightthickness=1
        )

        wrapper.pack(
            fill="x",
            pady=(0, 15)
        )

        entry = tk.Entry(
            wrapper,
            textvariable=variable,
            font=("Segoe UI", 11),
            bg=COLOR_FIELD,
            fg=COLOR_TEXT,
            relief="flat",
            bd=0,
            width=30
        )

        if show:
            entry.config(show=show)

        entry.pack(
            padx=12,
            pady=10,
            fill="x"
        )

        return entry

    # ======================================================
    # LOGIN
    # ======================================================
    def login(self):

        username = self.username_var.get().strip()
        password = self.password_var.get().strip()

        if not username or not password:

            messagebox.showwarning(
                "Peringatan",
                "Username dan Password harus diisi!"
            )

            return

        user = User.login(
            username,
            password
        )

        if user:

            messagebox.showinfo(
                "Berhasil",
                f"Selamat datang, {user['nama']}"
            )

            self.master.unbind("<Return>")

            if self.on_login_success:
                self.on_login_success(user)

        else:

            messagebox.showerror(
                "Gagal",
                "Username atau Password salah!"
            )

    # ======================================================
    # RUN
    # ======================================================
    def run(self):
        self.master.mainloop()


if __name__ == "__main__":
    LoginView().run()