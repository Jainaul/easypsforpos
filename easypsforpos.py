from PIL import Image, ImageDraw, ImageFont
import sys,time,os

os.chdir(sys.path[0])

im = Image.open(sys.argv[1], 'r')
rgb_im = im.convert('RGB')
rgb_im.save('tem.jpg')

am = (os.path.split(sys.argv[1]))
ame =(os.path.splitext(am[1]))
name = ame[0],time.strftime('%Y-%m-%d',time.localtime(time.time()))
pin = '\n'.join(name)

def add_word(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('./font.ttf', size=90)
    fillcolor = "#ff0000"
    width, height = img.size
    draw.text((width-550, height-800),pin, font=myfont, fill=fillcolor)
    img.save('result.jpg','jpeg')

    return 0
if __name__ == '__main__':
    image = Image.open('tem.jpg')
    add_word(image)
    
os.remove('./tem.jpg')