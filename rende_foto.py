import PIL
from PIL import Image
import glob, os

extension = raw_input("Digite o formato das imagens:\n")
size = input("Digite o tamanho da imagem:\n")

bool = False
if os.path.isdir('rotated'):
        print "\nImages will be saved in 'rotated' directory.\n"
else:
    os.makedirs('rotated')
for file in glob.glob('*' + extension):
    filename, extension = os.path.splitext(file)
    print('cropping ' + filename + 'into 4 sub-images')
    bool = True
    im = Image.open(file)
    (width, height) = im.size
    left = (width - size[0])/2
    top = (height - size[1])/2
    right = (width + size[0])/2
    down = (height + size[1])/2
    im1 = im.crop((left, top, right, down))
    im = im.rotate(45)
    im2 = im.crop((left, top, right, down))
    im = im.rotate(45)
    im3 = im.crop((left, top, right, down))
    im = im.rotate(45)
    im4 = im.crop((left, top, right, down))
    im = im.rotate(45)
    im5 = im.crop((left, top, right, down))
    im = im.rotate(45)
    im6 = im.crop((left, top, right, down))
    im = im.rotate(45)
    im7 = im.crop((left, top, right, down))
    im = im.rotate(45)
    im8 = im.crop((left, top, right, down))

    im1.save('rotated/rotated1_' + filename + extension)
    im2.save('rotated/rotated2_' + filename + extension)
    im3.save('rotated/rotated3_' + filename + extension)
    im4.save('rotated/rotated4_' + filename + extension)
    im5.save('rotated/rotated5_' + filename + extension)
    im6.save('rotated/rotated6_' + filename + extension)
    im7.save('rotated/rotated7_' + filename + extension)
    im8.save('rotated/rotated8_' + filename + extension)

if bool == False:
    print ("\n\nNenhuma foto encontrada!\n\n")
