import os
from encode import encode_manual
from decode import decode_manual
from tkinter import filedialog, Tk


def main():
    while True:
        print("=== STEGANOGRAPHY TOOL ===")
        print("1. Encode")
        print("2. Decode")
        print("3. Exit")

        choice = input("\nSelect: ")

        if choice == '1':
           print()
           secure_msg = input("Enter your secure message: ")
           img_path = filedialog.askopenfilename(
                title="Select Secret Image",
                filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
            )
           
           if img_path:
                save_path = filedialog.asksaveasfilename(
                   title="Where do you want to save the secure image?",
                   defaultextension="png",
                   filetypes=[("PNG files", "*.png")]
               )


           encode_manual(img_path, secure_msg, save_path)
           input("\nDONE!\npress Enter...")

        if choice == '2':
            print()
            img_path = filedialog.askopenfilename(
            title="Select Secret Image",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
            )

            founded_msg = decode_manual(img_path)
            print(founded_msg)
            input("\nDONE!\npress Enter...")

        if choice == '3':
            break
            


if __name__ == "__main__":
    main()