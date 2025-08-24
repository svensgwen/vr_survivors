import os
import customtkinter as ctk
from PIL import Image, ImageTk

class PlayerBar(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.configure(height=80, fg_color="#222")
        self.pack(side="bottom", fill="x", padx=10, pady=5)

        # Load and resize avatar image with smooth scaling
        avatar_img = Image.open("assets/img/gwen_premium.png").resize((160, 160), Image.LANCZOS)
        self.avatar_photo = ImageTk.PhotoImage(avatar_img)
        avatar_label = ctk.CTkLabel(self, image=self.avatar_photo, fg_color="#222", text="")
        avatar_label.grid(row=0, column=0, padx=10, pady=10)

        # Vertical layout frame for bars
        bars_frame = ctk.CTkFrame(self, fg_color="#222")
        bars_frame.grid(row=0, column=1, rowspan=2, pady=10)

        # Health
        health_label = ctk.CTkLabel(bars_frame, text="Health:")
        health_label.pack(anchor="w")
        self.health_bar = ctk.CTkProgressBar(bars_frame, width=200)
        self.health_bar.pack(pady=(0, 10))
        self.health_bar.set(0.8)  # 80% health example

        # Energy
        energy_label = ctk.CTkLabel(bars_frame, text="Energy:")
        energy_label.pack(anchor="w")
        self.energy_bar = ctk.CTkProgressBar(bars_frame, width=200)
        self.energy_bar.pack()
        self.energy_bar.set(0.5)  # 50% energy example

        self.grid_columnconfigure(2, weight=1)

class GameWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("VR_SURVIVORS")
        self.geometry("1600x900")

        # Main content frame with horizontal layout
        main_frame = ctk.CTkFrame(self)
        main_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Left: Frame with grid of square buttons
        actions_frame = ctk.CTkFrame(main_frame)
        actions_frame.pack(side="left", fill="both", expand=True)

        # Folder where images are stored
        self.image_folder = "assets/img/actions"
        # Define your actions and corresponding image filenames
        self.actions = ["Attack", "Map", "Inventory", "Market", "Gather", "Fixit", "Save"]
        self.image_files = ["attack.png", "map.png", "inventory.png", "market.png", "gather.png", "fixit.png", "save.png"]

        def load_actions_images(image_folder, image_names, size=(90, 90)):
            images = []
            for name in image_names:
                filepath = os.path.join(image_folder, name)
                if os.path.exists(filepath):
                    img = Image.open(filepath).resize(size, Image.LANCZOS)
                    photo = ImageTk.PhotoImage(img)
                else:
                    photo = None  # fallback
                images.append(photo)
            return images

        # Load images from folder
        self.button_images = load_actions_images(self.image_folder, self.image_files, size=(50, 50))

        # Create grid of square buttons (e.g., 6x6)
        num_rows, num_cols = 6, 6
        button_size = 90  # Size of each button

        for i, action in enumerate(self.actions):
            photo = self.button_images[i] if i < len(self.button_images) else None
            btn = ctk.CTkButton(actions_frame, text=action, width=button_size, height=button_size,
                                image=photo, compound="top")
            r = i // num_cols
            c = i % num_cols
            btn.grid(row=r, column=c, padx=5, pady=5)



        # Right: Text box like command prompt
        command_frame = ctk.CTkFrame(main_frame)
        command_frame.pack(side="right", fill="both", expand=True, padx=(10, 0))

        # Command prompt label
        cmd_label = ctk.CTkLabel(command_frame, text="Command Prompt", font=ctk.CTkFont(size=16, weight="bold"))
        cmd_label.pack(anchor="w", padx=5, pady=3)

        # Text box
        self.command_textbox = ctk.CTkTextbox(command_frame, width=300, height=400)
        self.command_textbox.pack(expand=True, fill="both", padx=5, pady=5)

        # Player bar at bottom (assuming previously defined)
        self.player_bar = PlayerBar(self)
        self.player_bar.pack(side="bottom", fill="x", padx=10, pady=5)

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")  # "dark" or "light"
    ctk.set_default_color_theme("dark-blue")  # Optional

    app = GameWindow()
    app.mainloop()
