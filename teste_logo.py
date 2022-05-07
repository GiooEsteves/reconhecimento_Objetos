import cv2

imagem = cv2.imread('teste/foo-fighters-logo-hoodie.jpg')

classificador = cv2.CascadeClassifier('cascade_logo.xml')

imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

deteccoes = classificador.detectMultiScale(imagemCinza, scaleFactor = 1.3, minNeighbors = 10, minSize = (40,40))

for(x, y, l, a) in deteccoes:
    cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 255, 0), 2)

cv2.imshow('Classificador', imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()