import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                  box_size=10,border=4,)
qr.add_data("https://instagram.com/p_g_sarvaiya_official_107?igshid=NGVhN2U2NjQ0Yg==")
qr.make(fit=True)
img=qr.make_image(fill_color="white",back_color="black")
img.save("insta_p_g.png")