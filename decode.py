from PIL import Image
from tkinter import filedialog, Tk

def decode_manual(img_path):
    try:

        img = Image.open(img_path).convert('RGBA')
        pixels = img.load()

        bin_data = ""
        width, height = img.size


        for y in range(height):
            for x in range(width):
                r, g, b, a = pixels[x, y]

                bin_data += str(r & 1)


        decode_msg = ""
        for i in range(0, len(bin_data), 8):
            byte = bin_data[i:i+8]
            

            character = chr(int(byte, 2))
            decode_msg += character


            if decode_msg.endswith("@@@"):
                return decode_msg[:-3]
        
        return "No secret message found with the expected format."

    except Exception as e:
        return f"An error occurred during decoding: {e}"