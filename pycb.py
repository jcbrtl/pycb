#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PYCB, um Contador de 'Bactéria' em Python

    Conta colônias da bactéria Staphilococcus aureus em placas de ágar

    python pycb.py -i [arquivo_imagem]

@author: J. Cesar Bertelli <jcbrtl-@-usp-.-br>
"""

# pacotes necessários
import numpy as np
import argparse
import imutils
import cv2

#Documentação usada no trabalho, além dos links em comentários:
#https://docs.opencv.org/2.4/index.html
#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_table_of_contents_imgproc/py_table_of_contents_imgproc.html#py-table-of-content-imgproc

#Amostras das placas obtidas em:
#http://opencfu.sourceforge.net/samples.php

#Versão do OpenCV
#print("OpenCV version: {}".format(cv2.__version__))
#OpenCV version: 4.1.0

# capta a imagem de entrada
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--imagem", required=True,
    help="caminho à imagem de entrada")
args = vars(ap.parse_args())

# acumulador do número de colônias
counter = 0

# carrega a imagem de entrada
im_orig = cv2.imread(args["imagem"])
height_orig, width_orig = im_orig.shape[:2]

# copia para exibição posterior, com os futuros contornos
im_contours = im_orig.copy()

# INÍCIO DO PROCESSO
im_to_process = im_orig.copy()

# define uma faixa de cores para a máscara (vetores BGR)
# esse processo foi feito manualmente, em que se usou, no caso,
# um editor de imagem (GIMP) para a leitura do histograma de cores
lower = np.array([ 56, 129, 168])
upper = np.array([150, 216, 250])

# encontra as cores conforme os limites acima
im_mask = cv2.inRange(im_to_process, lower, upper)
# aplica a máscara
im_res = cv2.bitwise_and(im_to_process, im_to_process, mask = im_mask)

# converte o resultado para a escala de cinza
im_gray = cv2.cvtColor(im_res, cv2.COLOR_BGR2GRAY)

# desfoca o resultado para reduzir o ruído, para a detecção de
#borda (evita maus contornos)
im_gray = cv2.GaussianBlur(im_gray, (5, 5), 0)

# detecção de borda
im_edged = cv2.Canny(im_gray, 50, 100)
cv2.imwrite("4-edge.jpg",im_edged.copy())

#dilata e corroe para aproximar espaços entre objetos de borda
im_edged = cv2.dilate(im_edged, None, iterations=1)
cv2.imwrite("5-dilate.jpg",im_edged.copy())
im_edged = cv2.erode(im_edged, None, iterations=1)
cv2.imwrite("6-erode.jpg",im_edged.copy())

# encontra contornos no mapa de bordas
cnts, hiers = cv2.findContours(im_edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# a cada contorno...
for c in cnts:
    #https://en.wikipedia.org/wiki/Green%27s_theorem#Area_calculation
    #https://en.wikipedia.org/wiki/Shoelace_formula
    ca = cv2.contourArea(c)
    #ignora contornos cuja área seja muito pequena ou muito grande
    #processo manual
    if ca < 25 or ca > 2500:
        continue

    # computa o casco do contorno (Convex Hull)
    #https://www.learnopencv.com/convex-hull-using-opencv-in-python-and-c/
    hull = cv2.convexHull(c)

    # destaca em azul esse casco
    cv2.drawContours(im_contours,[hull],0,(255,0,0),2)

    counter += 1

# imprime o número de colônias encontradas na saída
print(counter)

# exibe o resultado graficamente
cv2.imshow("{} colônias encontradas".format(counter), im_contours)
cv2.waitKey()
