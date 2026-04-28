from PIL import Image
from tkinter import filedialog, Tk

def encode_manual(img_path, secret_msg, output_path):
    try:

        img = Image.open(img_path).convert('RGBA')
        pixels = img.load()
        

        secret_msg += "@@@"


        bin_msg = ''.join(format(ord(i), '08b') for i in secret_msg)
        msg_index = 0
        msg_len = len(bin_msg)

        width, height = img.size


        for y in range(height):
            for x in range(width):
                if msg_index < msg_len:
                    r, g, b, a = pixels[x, y]


                    new_r = (r & ~1) | int(bin_msg[msg_index])
                    pixels[x, y] = (new_r, g, b, a)

                    msg_index += 1
                else:
                    break
            if msg_index >= msg_len:
                break
        

        if not output_path.lower().endswith('.png'):
            output_path += ".png"
            
        img.save(output_path)
        print(f"\n[+] Successful! Message hidden in: {output_path}")

    except Exception as e:
        print(f"[-] An error occurred: {e}")




root = Tk()
root.withdraw()


secure_message = input("Enter your secret message: ")


image_path = filedialog.askopenfilename(
    title="Select your image", 
    filetypes=[("Image files", "*.png *.jpg *.jpeg")]
)


if image_path:
    save_name = input("Enter the name for the new secure image (e.g., secret_pic): ")
    encode_manual(image_path, secure_message, save_name)
else:
    print("No image selected. Operation cancelled.")