import customtkinter as ctk
from PIL import Image, ImageTk

class PlayerBar(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(padx=10, pady=10)

        # Load and resize avatar image with PIL for smooth scaling
        avatar_img = Image.open("assets/img/gwen_premium.png").resize((160, 160), Image.LANCZOS)
        self.avatar_photo = ImageTk.PhotoImage(avatar_img)
        avatar_label = ctk.CTkLabel(self, image=self.avatar_photo, text="")
        avatar_label.grid(row=0, column=0, padx=10)

        # Health bar and label
        health_label = ctk.CTkLabel(self, text="Health:")
        health_label.grid(row=0, column=1, padx=10, sticky="w")

        self.health_bar = ctk.CTkProgressBar(self, width=200)
        self.health_bar.grid(row=0, column=2, padx=10)
        self.health_bar.set(0.8)  # 80% health

        # Energy label
        energy_label = ctk.CTkLabel(self, text="Energy: 50")
        energy_label.grid(row=0, column=3, padx=10, sticky="w")

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")  # Optional: "dark" or "light"
    ctk.set_default_color_theme("dark-blue")  # Optional color theme

    root = ctk.CTk()
    root.title("VR_SURVIVORS Player Bar")
    root.geometry("500x80")

    player_bar = PlayerBar(root)

    root.mainloop()
