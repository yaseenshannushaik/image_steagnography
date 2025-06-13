import sys
import numpy as np
from PIL import Image

np.set_printoptions(threshold=sys.maxsize)

# Encoding function
def Encode(src, message, dest, password):
    img = Image.open(src, 'r')
    width, height = img.size
    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4

    total_pixels = array.size // n

    message += password
    b_message = ''.join([format(ord(i), "08b") for i in message])
    req_pixels = len(b_message)

    if req_pixels > (total_pixels * 3):
        print("ERROR: Need larger file size")
        return

    index = 0
    for p in range(total_pixels):
        for q in range(0, 3):
            if index < req_pixels:
                array[p][q] = int(bin(array[p][q])[2:9] + b_message[index], 2)
                index += 1

    array = array.reshape(height, width, n)
    enc_img = Image.fromarray(array.astype('uint8'), img.mode)
    enc_img.save(dest)
    print("Image Encoded Successfully")

# Decoding function
def Decode(src, password):
    img = Image.open(src, 'r')
    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4

    total_pixels = array.size // n

    hidden_bits = ""
    for p in range(total_pixels):
        for q in range(0, 3):
            hidden_bits += bin(array[p][q])[-1]

    hidden_bits = [hidden_bits[i:i+8] for i in range(0, len(hidden_bits), 8)]

    message = ""
    hidden_message = ""
    for i in range(len(hidden_bits)):
        char = chr(int(hidden_bits[i], 2))
        message += char
        hidden_message = message
        if password in message:
            break

    # Verifying the password
    if password in message:
        print("Hidden Message:", hidden_message.split(password)[0])
    else:
        print("You entered the wrong password: Please Try Again")

# Main function
def Stego():
    while True:
        print("*--Welcome to Stego--*")
        print("1: Encode")
        print("2: Decode")
        print("3: Exit")

        func = input()

        if func == '1':
            print("Enter Source Image Path")
            src = input()
            print("Enter Message to Hide")
            message = input()
            print("Enter Destination Image Path")
            dest = input()
            print("Enter password")
            password = input()
            print("Encoding...")
            Encode(src, message, dest, password)
            

        elif func == '2':
            print("Enter Source Image Path")
            src = input()
            print("Enter Password")
            password = input()
            print("Decoding...")
            Decode(src, password)

        elif func == '3':
            print("Exiting...")
            break

        else:
            print("ERROR: Invalid option chosen")

Stego()
