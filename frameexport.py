import cv2
"""
Videoları karelerine ayırmak için bu kod bloğunu kullanın

"""
vidcap = cv2.VideoCapture('chikadance.mp4') #video yolu
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frames/image/frame%d.jpg" % count, image)    
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1