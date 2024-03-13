import qrcode as qr
img = qr.make("https://www.linkedin.com/in/yash-jethava-583238248")
img.save("yash_linkdin.png")