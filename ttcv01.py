import cv2
# -----------------------------------
# Ler imagem RGB
im01=cv2.imread('image01_rgb.png')
print( 'Dimensao da matriz "im01" (RGB): {}'.format(im01.shape) )

# Converte para escala de cinza (GRAY)
im02=cv2.cvtColor(im01,cv2.COLOR_BGR2GRAY)
print  'Dimensao da matriz "im02" (Gray): {}'.format(im02.shape)

# Cria uma imagem "BRANCA" da mesma dimensao da CINZA
im03=im02.copy()
for i in range(im03.shape[0]):
    for j in range(im03.shape[1]):
        # 255 = cor branca
        im03[i,j]=255

# Ler imagem do ELEMENTO ESTRUTURANTE, convertendo para GRAY
imEE01=cv2.cvtColor( cv2.imread('ee01_mask.png') ,cv2.COLOR_BGR2GRAY)
print  'Dimensao da matriz "imEE01" (Elemento Estruturante): {}'.format(imEE01.shape)

# Ler imagem PADRAO, convertendo para GRAY
imPD01=cv2.cvtColor( cv2.imread('ee02_padrao1.png') ,cv2.COLOR_BGR2GRAY)
print  'Dimensao da matriz "imPD01" (Padrao): {}'.format(imPD01.shape)
print

# Mostra imagens
st1="01-RGB";       cv2.imshow(st1,im01);   print st1,'Imagem Lida'
st1="02-Gray";      cv2.imshow(st1,im02);   print st1,'Imagem em Cinza'
st1="03-Copia";     cv2.imshow(st1,im03);   print st1,'Imagem em Branco'
st1="04-Mask";      cv2.imshow(st1,imEE01); print st1,'EE mask'
st1="05-Padrao";    cv2.imshow(st1,imPD01); print st1,'EE Padrao'


cv2.waitKey(0)
cv2.destroyAllWindows()

# -----------------------------------


