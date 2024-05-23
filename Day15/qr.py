import qrcode

me = 'https://www.instagram.com/woosung.lee.7545/'
qr = qrcode.make(me)
qr.save('me.png')