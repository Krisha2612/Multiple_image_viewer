import os
from tkinter import Tk, Button, Label, filedialog, PhotoImage
from PIL import Image, ImageTk

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Multiple Image Viewer")
        self.root.geometry("800x600")
        self.image_list = []
        self.current_index = 0

        self.label = Label(self.root)
        self.label.pack(pady=20)

        self.button_frame = Button(self.root, text="Select Images", command=self.load_images)
        self.button_frame.pack()

        self.prev_button = Button(self.root, text="<< Prev", command=self.show_prev)
        self.prev_button.pack(side="left", padx=20, pady=20)

        self.next_button = Button(self.root, text="Next >>", command=self.show_next)
        self.next_button.pack(side="right", padx=20, pady=20)

    def load_images(self):
        file_paths = filedialog.askopenfilenames(
            title="Select Images",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
        )
        self.image_list = [Image.open(fp) for fp in file_paths]
        self.current_index = 0
        self.show_image()

    def show_image(self):
        if not self.image_list:
            return
        img = self.image_list[self.current_index].copy()
        img.thumbnail((700, 500))
        self.tkimage = ImageTk.PhotoImage(img)
        self.label.config(image=self.tkimage)

    def show_next(self):
        if self.image_list and self.current_index < len(self.image_list) - 1:
            self.current_index += 1
            self.show_image()

    def show_prev(self):
        if self.image_list and self.current_index > 0:
            self.current_index -= 1
            self.show_image()

if __name__ == "__main__":
    root = Tk()
    viewer = ImageViewer(root)
    root.mainloop()
