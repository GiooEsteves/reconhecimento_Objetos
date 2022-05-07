from email import header
import urllib.request
from wsgiref import headers
import cv2
import numpy as np
import os

negativas_link = ''
headers = {}
headers['User-Agent'] = ""
requisicao = urllib.request.Request(negativas_link, headers= headers)
resp = urllib.request.urlopen(requisicao)

respData = resp.read().decode()
numero_atual = 1

if not os.path.exists('neg'):
    os.makedirs('neg')

for i in respData.split('\n'):
    try:
        print(i)
        urllib.request.urlretrieve(i, "neg/" + str(numero_atual) + ".jpg")
        img = cv2.imread("neg/" + str(numero_atual) + ".jpg", cv2.IMREAD_GRAYSCALE)

        img_redimensionada = cv2.resize(img, (100, 100))
        cv2.imwrite("neg/" + str(numero_atual) + ".jpg", img_redimensionada)
        numero_atual += 1

    except Exception as e:
        print(str(e))