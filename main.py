import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class VirtualPetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Pet")

        # Initialize pet state
        self.hunger = 50
        self.happiness = 50

        # Load and resize pet images
        self.pet_images = {
            "happy": self.load_and_resize_image("happy_pet.jpeg"),
            "hungry": self.load_and_resize_image("hungry_pet.jpg"),
            "neutral": self.load_and_resize_image("neutral_pet.jpg")
        }

        # Create UI components
        self.create_widgets()
        self.update_pet_status()

        # Start the timer
        self.update_timer()

    def load_and_resize_image(self, path, size=(200, 200)):
        image = Image.open(path)
        image = image.resize(size, Image.Resampling.LANCZOS)  # Use LANCZOS for high-quality resizing
        return ImageTk.PhotoImage(image)

    def create_widgets(self):
        self.pet_label = tk.Label(self.root)
        self.pet_label.pack(pady=20)

        self.hunger_label = tk.Label(self.root, text="Hunger: ")
        self.hunger_label.pack()

        self.happiness_label = tk.Label(self.root, text="Happiness: ")
        self.happiness_label.pack()

        self.feed_button = tk.Button(self.root, text="Feed", command=self.feed_pet)
        self.feed_button.pack(pady=10)

        self.play_button = tk.Button(self.root, text="Play", command=self.play_with_pet)
        self.play_button.pack(pady=10)

    def feed_pet(self):
        self.hunger += 10
        self.happiness -= 5
        self.update_pet_status()

    def play_with_pet(self):
        self.happiness += 10
        self.hunger -= 5
        self.update_pet_status()

    def update_pet_status(self):
        self.hunger = max(0, min(100, self.hunger))
        self.happiness = max(0, min(100, self.happiness))

        if self.hunger <= 80:
            self.pet_label.config(image=self.pet_images["hungry"])
        elif self.happiness >= 80:
            self.pet_label.config(image=self.pet_images["happy"])
        else:
            self.pet_label.config(image=self.pet_images["neutral"])

        self.hunger_label.config(text=f"Hunger: {self.hunger}")
        self.happiness_label.config(text=f"Happiness: {self.happiness}")

        if self.hunger >= 90 and self.happiness == 100:
            self.game_over_good()
        elif self.hunger <=0 or self.happiness <=0:
            self.game_over_bad()

    def update_timer(self):
        self.hunger += 1
        self.happiness -= 1
        self.update_pet_status()
        self.root.after(5000, self.update_timer)  # Update every 5 seconds

    def game_over_bad(self):
        messagebox.showinfo("Game Over", "Your pet has died!")
        self.root.quit()
    
    def game_over_good(self):
        messagebox.showinfo("Game over!", "Your pet has lived a long and happy life!")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = VirtualPetApp(root)
    root.mainloop()