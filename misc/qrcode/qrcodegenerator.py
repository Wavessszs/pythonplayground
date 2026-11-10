import qrcode

# Data to encode    
data = "iloveyouranaplsaqnalangiiyotsabaomongpink"

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # control the error correction used for the QR Code
    box_size=10,  # controls how many pixels each “box” of the QR code is
    border=4,  # controls how many boxes thick the border should be (minimum is 4)
)

# Add data to the instance
qr.add_data(data)
qr.make(fit=True)  # automatically adjust the size to fit the data

# Create an image from the QR code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("qrcode.png")
