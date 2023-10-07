import cv2
# =====================================
print("Teste Imagem")

im01=cv2.imread("a00.png")

shape1=im01.shape
print "SHAPE: ",shape1
print "  SHAPE Tamanho: ", len(shape1)
print "    SHAPE Y  :", shape1[0]
print "    SHAPE X  :", shape1[1]
print "    SHAPE RGB:", shape1[2]
print

# -----------------------------------------------------------------------
y1=0;  x1=0;
print(  "Valor do Pixel na posicao [y,x]=[{},{}]:".format(y1,x1) )
print("  Cor PRETA:")
for bgrx in range(3):
    print( "    Para  BGR = {} eh: {} ".format(bgrx,im01[y1,x1,bgrx]) )
print

# -----------------------------------------------------------------------
y1=1;  x1=1;
print( "Valor do Pixel na posicao [y,x]=[{},{}]:".format(y1,x1) )
print("  Cor BRANCA:")
for bgrx in range(3):
    print( "    Para  BGR = {} eh: {} ".format(bgrx,im01[y1,x1,bgrx]) )
print

# -----------------------------------------------------------------------
y1=0;  x1=1;
print( "Valor do Pixel na posicao [y,x]=[{},{}]:".format(y1,x1) )
print("  Cor VERMELHA:")
for bgrx in range(3):
    print( "    Para  BGR = {} eh: {} ".format(bgrx,im01[y1,x1,bgrx]) )
print


# -----------------------------------------------------------------------
y1=0;  x1=2;
print( "Valor do Pixel na posicao [y,x]=[{},{}]:".format(y1,x1) )
print("  Cor AMARELA:")
for bgrx in range(3):
    print( "    Para  BGR = {} eh: {} ".format(bgrx,im01[y1,x1,bgrx]) )
print


# -----------------------------------------------------------------------
y1=0;  x1=3;
print( "Valor do Pixel na posicao [y,x]=[{},{}]:".format(y1,x1) )
print("  Cor VERDE")
for bgrx in range(3):
    print( "    Para  BGR = {} eh: {} ".format(bgrx,im01[y1,x1,bgrx]) )
print


# -----------------------------------------------------------------------
y1=0;  x1=4;
print( "Valor do Pixel na posicao [y,x]=[{},{}]:".format(y1,x1) )
print("  Cor Azul")
for bgrx in range(3):
    print( "    Para  BGR = {} eh: {} ".format(bgrx,im01[y1,x1,bgrx]) )
print


# -----------------------------------------------------------------------

