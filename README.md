# 🕵️‍♂️ Image Steganography in Python

This project implements a simple and secure **Image Steganography tool** using Python. The tool allows you to **hide secret messages** inside image files and retrieve them later using a password. It supports both encoding (hiding text) and decoding (extracting hidden text).

---

## 📂 Project Files

| File Name              | Description                                             |
|------------------------|---------------------------------------------------------|
| `imagesteganography.py`| Python script to encode and decode hidden messages inside images using LSB (Least Significant Bit) technique. |

---

## 🎯 Features

- Encode secret messages into `.png` or `.jpg` images.
- Secure message retrieval using a **password-based unlock**.
- Works with RGB and RGBA image modes.
- Error handling for file size limitations.
- Console-based user interface.

---

## 🔐 How It Works

This project uses the **Least Significant Bit (LSB)** steganography method:
- Converts each character of the message into an 8-bit binary string.
- Hides each bit in the **least significant bit** of each RGB channel.
- Appends the password to the message to verify authenticity on decoding.

---

## 🛠️ Requirements

Install the required dependencies using:

```bash
pip install pillow numpy
````

---

## ▶️ How to Use

### Run the script:

```bash
python imagesteganography.py
```

You will see a menu:

```
*--Welcome to Stego--*
1: Encode
2: Decode
3: Exit
```

---

### 📝 Encode a Message

Steps:

1. Choose option `1`
2. Enter the **path to the source image**
3. Type the **message** you want to hide
4. Provide the **output image path** (e.g., `output.png`)
5. Enter a **password**

The script will generate a new image with the hidden message securely encoded.

---

### 🔓 Decode a Message

Steps:

1. Choose option `2`
2. Enter the **path to the image with hidden message**
3. Provide the **password** used during encoding

If the password matches, the hidden message will be revealed.

---

## 📌 Example

**Encode:**

```
Enter Source Image Path
sample.png
Enter Message to Hide
The secret code is 1234.
Enter Destination Image Path
output.png
Enter password
mypassword
```

**Decode:**

```
Enter Source Image Path
output.png
Enter Password
mypassword
Hidden Message: The secret code is 1234.
```

---

## ⚠️ Limitations

* The source image must be large enough to hide the message + password.
* Encoding will fail if the message is too long for the image capacity.
* The tool currently supports **text-based messages only**.

---

## 👨‍💻 Author

**Shaik Yaseen Shannu**
BTech in Big Data and Analytics
