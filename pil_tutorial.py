from PIL import Image, ImageDraw, ImageFont

i_path = 'imput.png'
o_path = 'outp.png'

im = Image.open(i_path)

print(im.format, im.size, im.mode)
# Drawインスタンス生成
draw = ImageDraw.Draw(im)
#フォントの設定(フォントファイルのパスと文字の大きさ)
font = ImageFont.truetype("C:\Windows\Fonts\meiryob.ttc", 60)

#文字を書く
royalblue = (65,105, 225)
crimson = (220, 20, 60)
draw.text((500, 500), '日本語で文字列を出力する。', fill=royalblue, font=font)
#改行できる
draw.text((500, 500), '\n改行して出力する。', fill=crimson, font=font)

# 図形を出力する
draw.ellipse((100, 100, 150, 200), fill=(255, 0, 0), outline=(0, 0, 0))
draw.rectangle((200, 100, 300, 200), fill=(0, 192, 192), outline=(255, 255, 255))
draw.line((350, 200, 450, 100), fill=(255, 255, 0), width=10)

im.save(o_path)