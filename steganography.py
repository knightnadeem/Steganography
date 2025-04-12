import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image, ImageTk
from stegano import lsb

class SteganographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Steganography Tool")
        self.root.geometry("800x600")
        self.root.configure(bg="#ffffff")

        # Define colors
        self.bg_color = "#ffffff"
        self.primary_color = "#2196F3"  # Blue
        self.secondary_color = "#1976D2"  # Darker blue
        self.accent_color = "#FF4081"  # Pink
        self.text_color = "#333333"
        self.font_style = ("Segoe UI", 10)
        self.title_font = ("Segoe UI", 16, "bold")

        # Main container
        self.main_container = tk.Frame(root, bg=self.bg_color)
        self.main_container.pack(expand=True, fill="both", padx=20, pady=20)

        # Title
        self.title_label = tk.Label(
            self.main_container,
            text="Steganography Tool",
            font=self.title_font,
            bg=self.bg_color,
            fg=self.primary_color
        )
        self.title_label.pack(pady=(0, 20))

        # Image Display Frame
        self.image_frame = tk.Frame(self.main_container, bg=self.bg_color)
        self.image_frame.pack(fill="x", pady=(0, 20))

        self.image_label = tk.Label(
            self.image_frame,
            bg=self.bg_color,
            text="No image selected",
            font=self.font_style
        )
        self.image_label.pack(pady=10)

        # Encode Section
        self.encode_frame = tk.LabelFrame(
            self.main_container,
            text="Encode Message",
            font=self.font_style,
            bg=self.bg_color,
            fg=self.text_color
        )
        self.encode_frame.pack(fill="x", pady=(0, 10))

        # Encode controls
        self.encode_button = tk.Button(
            self.encode_frame,
            text="Choose Image",
            command=self.load_image_for_encoding,
            bg=self.primary_color,
            fg="white",
            font=self.font_style,
            relief=tk.FLAT,
            padx=15,
            pady=8
        )
        self.encode_button.pack(side="left", padx=10, pady=10)

        self.encode_entry = tk.Entry(
            self.encode_frame,
            width=40,
            font=self.font_style,
            relief=tk.SOLID,
            bd=1
        )
        self.encode_entry.pack(side="left", padx=10, pady=10)

        self.encode_message_button = tk.Button(
            self.encode_frame,
            text="Encode Text",
            command=self.encode_message,
            bg=self.accent_color,
            fg="white",
            font=self.font_style,
            relief=tk.FLAT,
            padx=15,
            pady=8
        )
        self.encode_message_button.pack(side="right", padx=10, pady=10)

        # Decode Section
        self.decode_frame = tk.LabelFrame(
            self.main_container,
            text="Decode Message",
            font=self.font_style,
            bg=self.bg_color,
            fg=self.text_color
        )
        self.decode_frame.pack(fill="x", pady=(0, 10))

        # Decode controls
        self.decode_button = tk.Button(
            self.decode_frame,
            text="Choose Encoded Image",
            command=self.load_encoded_image,
            bg=self.primary_color,
            fg="white",
            font=self.font_style,
            relief=tk.FLAT,
            padx=15,
            pady=8
        )
        self.decode_button.pack(side="left", padx=10, pady=10)

        self.decode_message_button = tk.Button(
            self.decode_frame,
            text="Decode Text",
            command=self.decode_message,
            bg=self.accent_color,
            fg="white",
            font=self.font_style,
            relief=tk.FLAT,
            padx=15,
            pady=8
        )
        self.decode_message_button.pack(side="right", padx=10, pady=10)

        # Add button hover effects
        self.add_button_hover_effects()

    def add_button_hover_effects(self):
        # Encode buttons hover effect
        self.encode_button.bind("<Enter>", lambda event: self.on_enter_button(event, self.encode_button, self.secondary_color))
        self.encode_button.bind("<Leave>", lambda event: self.on_leave_button(event, self.encode_button, self.primary_color))
        self.encode_message_button.bind("<Enter>", lambda event: self.on_enter_button(event, self.encode_message_button, "#E91E63"))
        self.encode_message_button.bind("<Leave>", lambda event: self.on_leave_button(event, self.encode_message_button, self.accent_color))

        # Decode buttons hover effect
        self.decode_button.bind("<Enter>", lambda event: self.on_enter_button(event, self.decode_button, self.secondary_color))
        self.decode_button.bind("<Leave>", lambda event: self.on_leave_button(event, self.decode_button, self.primary_color))
        self.decode_message_button.bind("<Enter>", lambda event: self.on_enter_button(event, self.decode_message_button, "#E91E63"))
        self.decode_message_button.bind("<Leave>", lambda event: self.on_leave_button(event, self.decode_message_button, self.accent_color))

    def on_enter_button(self, event, button, color):
        button.configure(bg=color)

    def on_leave_button(self, event, button, color):
        button.configure(bg=color)

    # Load image for encoding
    def load_image_for_encoding(self):
        filename = filedialog.askopenfilename(
            title="Select Image",
            filetypes=(("Image files", ".png;.jpg;.jpeg"), ("All files", ".*"))
        )
        if filename:
            self.image = Image.open(filename)
            # Maintain aspect ratio while resizing
            aspect_ratio = self.image.width / self.image.height
            new_width = 400
            new_height = int(new_width / aspect_ratio)
            self.image = self.image.resize((new_width, new_height))
            self.photo = ImageTk.PhotoImage(self.image)
            self.image_label.config(image=self.photo)
            self.encode_entry.delete(0, tk.END)
            self.encode_entry.insert(0, filename)

    # Encode message into image
    def encode_message(self):
        image_path = self.encode_entry.get()
        if image_path:
            message = self.get_message_from_user("Enter Message", "Enter the message to encode:")
            if message:
                output_path = filedialog.asksaveasfilename(
                    defaultextension=".png",
                    filetypes=(("PNG files", ".png"), ("All files", ".*"))
                )
                if output_path:
                    encrypted_message = lsb.hide(image_path, message)
                    encrypted_message.save(output_path)
                    messagebox.showinfo("Success", "Message encoded successfully!")
        else:
            messagebox.showerror("Error", "Please select an image first.")

    # Load encoded image for decoding
    def load_encoded_image(self):
        filename = filedialog.askopenfilename(
            title="Select Encoded Image",
            filetypes=(("PNG files", ".png"), ("All files", ".*"))
        )
        if filename:
            self.encoded_image_path = filename
            messagebox.showinfo("Success", "Encoded image loaded successfully!")

    # Decode message from image
    def decode_message(self):
        if hasattr(self, 'encoded_image_path'):
            message = lsb.reveal(self.encoded_image_path)
            messagebox.showinfo("Decoded Message", message)
        else:
            messagebox.showerror("Error", "Please select an encoded image first.")

    # Get message from user using simple dialog
    def get_message_from_user(self, title, prompt):
        message = simpledialog.askstring(title, prompt)
        if message is None:
            return None
        return message

if __name__ == "__main__":
    root = tk.Tk()
    app = SteganographyApp(root)
    root.mainloop()