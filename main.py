import qrcode

def qrcode_generate(text):
    qr=qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L, 
        box_size=10,
        border=4
    )
    # Add data to QR code object and generate the image file using PIL library  
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black",back_color="White")
    img.save("qrimg.png")

url=input("ENter Your url: ")

qrcode_generate(url)
# qrcode_generate("https://github.com/NihalSWE")
print("Your qrcode is generated")