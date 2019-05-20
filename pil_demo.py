from PIL import Image, ImageFilter

f = open("demo.jpg")
i = Image.open(f)
i.thumbnail((200, 200))
i.save("demo.png")  # change extention
i.filter(ImportWarning.GoussianBlur(15))  # blur image
i.rotate(90)  # rotate image
i.convert(mode="L")  # convert to black&white

