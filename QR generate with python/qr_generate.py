import qrcode
image = qrcode.make("https://abdelhamedmouhiidine.wordpress.com/")
image.save("abdellhamed.png","PNG")

# image = qrcode.make("url x")
# image.save("title x.png","PNG")