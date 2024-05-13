import cv2
import numpy as np
import matplotlib.pyplot as plt

ima= cv2.imread('Imagen.jpg')
ima=cv2.cvtColor(ima, cv2.COLOR_BGR2RGB)
imgB=ima[:,:,2]

Umb,img=cv2.threshold(imgB ,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
R=cv2.medianBlur(img, 5)

kernel= np.ones((15,15),np.uint8)
imaOp=cv2.morphologyEx(R, cv2.MORPH_CLOSE, kernel, iterations = 1)

elem,mask=cv2.connectedComponents(imaOp)
print(f'El número de células que se encuentran en la imagen es de:{elem-1}')
#Al elem se le debe restar 1 ya que me cuenta tambien el fondo 

plt.imshow(mask)
plt.show()