import sys, random, argparse
import numpy as np
import math
import time
from PIL import Image
import os


gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
gscale2 = '@%#*+=-:. '

def getAverageL(image):
	im = np.array(image)
	w,h = im.shape
	return np.average(im.reshape(w*h))

def covertImageToAscii(fileName, cols, scale, moreLevels):
	"""
	"""
	# declare globals
	global gscale1, gscale2

	image = Image.open(fileName).convert('L')

	# store dimensions
	W, H = image.size[0], image.size[1]
	print("input image dims: %d x %d" % (W, H))

	w = W/cols

	h = w/scale

	rows = int(H/h)
	
	print("cols: %d, rows: %d" % (cols, rows))
	print("tile dims: %d x %d" % (w, h))

	if cols > W or rows > H:
		print("Resim küçük!-")
		exit(0)
	aimg = []
	for j in range(rows):
		y1 = int(j*h)
		y2 = int((j+1)*h)
		if j == rows-1:
			y2 = H
		aimg.append("")
		for i in range(cols):
			x1 = int(i*w)
			x2 = int((i+1)*w)
			if i == cols-1:
				x2 = W
			img = image.crop((x1, y1, x2, y2))
			avg = int(getAverageL(img))
			if moreLevels:
				gsval = gscale1[int((avg*69)/255)]
			else:
				gsval = gscale2[int((avg*9)/255)]
			aimg[j] += gsval
	return aimg

def main():
    j=0
    while j < 448: ############ burası önemli videoyu resimlerine ayırdığınızda ortaya çıkan kare sayısını girin
        imgFile = 'frames/image/frame'+str(j)+'.jpg'
        outFile = 'frames/ascii/frame'+str(j)+'.txt'
        scale = 0.43
        cols = 80
        print('generating ASCII art...')
        aimg = covertImageToAscii(imgFile, cols, scale, "store_true")
        f = open(outFile, 'w')
        for row in aimg:
            f.write(row + '\n')
        f.close()
        j+=1
        print("  %s" % outFile)

def frameOynat():
    j = 0 
    while j < 448: ###### buraya da aynı kare sayısı gelecek
        with open('frames/ascii/frame'+str(j)+'.txt') as f:
            contents = f.read()
            print(contents, end= '\x1b[2K')
        time.sleep(.033) ### saniyede 30 kare için .033 saniye bekletmeniz ideal
        j+=1
        """-
        www.youtube.com/c/MemedAnime
        """
#main()  resimleri yazı formatına getirmek için main fonksiyonunu kullanın
frameOynat() # yazı formatındaki resimleri konsolda göstermek için bu fonksiyon çalışacak