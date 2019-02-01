import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def showit(img):
    
    # Para imagens preto e branco
    if(len(img.shape) < 3):
        plt.gray()
    
    plt.imshow(img)
    plt.show()

imgCol = cv.imread("coins/moedas.jpg")

# Converter para tons de cinza
imgGray = cv.cvtColor(imgCol, cv.COLOR_BGR2GRAY)

# Encontrar a região de interesse (mascara da região da moeda)
limiar, imgGrayOTSU = cv.threshold(imgGray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU) # limiar de otsu inclui as sombras
ret,imgGray = cv.threshold(imgGray,(limiar-limiar/6) ,255,cv.THRESH_BINARY_INV) # 83% do limiar de otsu

# showit(imgGray)

# Fechar buracos na estrutura encontrada
stt = cv.getStructuringElement(cv.MORPH_ELLIPSE, (31,31) )
imgBin = cv.morphologyEx(imgGray, cv.MORPH_CLOSE, stt)

# Erosão para remover pequenas falhas e separar moedas coladas
stt = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3,3) )
imgBin = cv.erode(imgBin, stt, iterations=1)

showit(imgBin)

# Convertendo imgGray para BGR para poder realizar o bitwise
imgGray = cv.cvtColor(imgBin, cv.COLOR_GRAY2BGR)

# Selecionando região de interesse na imagem colorida com a máscara encontrada
imgCol = cv.bitwise_and(imgCol, imgGray)

# Detecção de bordas
sobelVert = cv.Sobel(imgCol, cv.CV_8U, 1, 0, ksize=3)
sobelHori = cv.Sobel(imgCol, cv.CV_8U, 0, 1, ksize=3)
imgColSobel = cv.add(sobelHori, sobelVert)

# Realçando as bordas encontradas na imagem colorida
stt = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3,3))
imgColSobel = cv.morphologyEx(imgColSobel, cv.MORPH_CLOSE, stt)

# Adicionar as bordas encontradas na imagem colorida
imgCol = cv.add(imgCol, imgColSobel)

# Achar Contornos das moedas
contorno, hierarquia = cv.findContours(imgBin, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

print(len(contorno), "moedas")

# Para cada moeda encontrada
for objeto in contorno:
    
    # Encontre o menor retângulo envolvente
    x, y, w, h = cv.boundingRect(objeto)
    
    # Desenhar o retângulo
    # cv.rectangle(imgCol, (x,y), (x+w, y+h), (0,255,0), 15)
    
    # Mostre a moeda encontrada
    plt.imshow(imgCol[y:y+h, x:x+w, ::-1])
    plt.show()