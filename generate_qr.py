import qrcode
from PIL import Image
import urllib.parse

def generate_qr_code(url):
    # Parse the URL to get a valid filename
    filename = urllib.parse.quote_plus(url)

    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to the QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image with the derived filename
    img.save(f'{filename}.png')

if __name__ == "__main__":
    # Get URL input from the user
    url = input("Enter the URL to generate QR code: ")

    # Generate QR code with a filename derived from the URL
    generate_qr_code(url)

    print("QR code generated successfully.")
