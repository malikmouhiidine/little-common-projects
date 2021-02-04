import qrcode
link = input('Link: ')
name_file = input('Name the file: ')
image = qrcode.make(link)
image.save(name_file + '.png', "PNG")

# image = qrcode.make("url x")
# image.save("title x.png","PNG")
