import base64

with open("im.bmp", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
    print(type(str))
    print(str)