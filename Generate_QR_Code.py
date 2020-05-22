# Import qrcode module #
import qrcode

# Now set a object called data to be hidden in QR Code #
#data = "https://bytescare.com/"
data = input("Please enter the Security Code")
# Set output file name #
filename = "site.png"

# Generate qr code  and Build an Image type object #
img = qrcode.make(data)

# save image to a file in the same directory #
img.save(filename)
