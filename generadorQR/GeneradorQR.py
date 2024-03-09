#   https://www.twitter.com/Leandro_Re_Av
#   instalar pip install qrcode

import qrcode

qr = qrcode.QRCode(version=1,
                   error_correction = qrcode.constants.ERROR_CORRECT_L,
                   box_size=7,
                   border=2)

qr.add_data('https://www.twitter.com/Leandro_Re_Av')
qr.make(fit =True)

img = qr.make_image(fill_color = "black", black_color ='white')
img.save('codigoQR.png')