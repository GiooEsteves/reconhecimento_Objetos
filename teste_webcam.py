import cv2

classificador = cv2.CascadeClassifier('cascade_caneca3.xml')
camera = cv2.VideoCapture(0)

while True:
    conectado, frame = camera.read()
    imagemCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    deteccoes = classificador.detectMultiScale(imagemCinza, scaleFactor=1.3, minNeighbors=9, minSize =(60, 60))
    
    for (x, y, l, a) in deteccoes:
        cv2.rectangle(frame, (x, y), (x + l, y + a), (0, 255, 0), 2)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()