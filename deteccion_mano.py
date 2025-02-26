import pyfirmata2 # Librería para comunicarse con Arduino
import cv2 # Librería para capturar video desde la webcam
from cvzone.HandTrackingModule import HandDetector # Detector de manos
import numpy as np  # Operaciones matemáticas

# Configurar la conexión con Arduino en el puerto COM3
comport = 'COM4'
board = pyfirmata2.Arduino(comport)
servo = board.get_pin('d:7:s')  # Servo motor en el puerto 7

# Inicializar el detector de manos
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Capturar video desde la webcam
video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read() # Leer un frame del video
    if not ret:  # Si no se pudo leer el frame, salir del programa
        break

    frame = cv2.flip(frame, 1)  # Espejar la imagen
    hands, frame = detector.findHands(frame) # Detectar manos en el frame

    if hands: 
        hand = hands[0]
        x, y, w, h = hand['bbox']  # Obtener límites de la mano

        lmList = hand['lmList']  # Lista de puntos de la mano

        if len(lmList) != 21:  # Asegurar que la mano fue detectada correctamente
            continue

        # Verificar si el pulgar y el índice están tocándose (formando un círculo)
        distancia_ok = np.linalg.norm(np.array(lmList[4][:2]) - np.array(lmList[8][:2]))

        # Verificar si el pulgar está hacia abajo
        pulgar_abajo = lmList[4][1] > lmList[2][1]

        # Verificar si el pulgar está hacia abajo
        pulgar_arriba = lmList[2][1] > lmList[4][1]

        # anular extendido 
        anular_extendido = lmList[16][1] < lmList[14][1]

        # Verificar si los dedos medio
        dedos_doblados = [] 
        for i in [8, 12, 16, 20]:  # Índice, medio, anular, meñique
            if lmList[i][1] > lmList[i - 2][1]:  # Si la punta del dedo está más abajo que su base
                dedos_doblados.append(True)
            else:
                dedos_doblados.append(False)

        # Verificar si los otros dedos están extendidos
        dedos_extendidos = []
        for i in range(12, 21, 4):  # Recorremos los dedos medio, anular y meñique
            if lmList[i][1] < lmList[i - 2][1]:  # Si la punta del dedo está por encima de su base
                dedos_extendidos.append(True)
            else:
                dedos_extendidos.append(False)


        # Normalizar la posición x de la mano a un rango de 0 a 180 grados
        frame_width = frame.shape[1]
        angle = np.interp(x + w // 2, [0, frame_width], [0, 180])

        # Mover el servomotor
        servo.write(angle)

        # Mostrar ángulo en la pantalla
        cv2.putText(frame, f'Angle: {int(angle)}', (20, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)


        # GESTOS 
        

        # GESTO DE RE CHETO

        if distancia_ok < 30 and all(dedos_extendidos):  # Si el pulgar e índice están juntos y los demás abiertos
            print("🆗 Gesto de RE CHETO detectado!")
            cv2.putText(frame, "re cheto!", (50, 150), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # GESTO DE MAL

        gesto_mal = pulgar_abajo and all(dedos_doblados)  # Si el pulgar está abajo y los otros doblados}

        if gesto_mal:
            print("👎 Gesto de MAL detectado!")
            cv2.putText(frame, "MAL!", (50, 150), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        else:
            # Normalizar la posición x de la mano a un rango de 0 a 180 grados
            frame_width = frame.shape[1]
            angle = np.interp(x + w // 2, [0, frame_width], [0, 180])

        # GESTO DE BIEN

        gesto_bien = pulgar_arriba and all(dedos_doblados)

        if gesto_bien:
            print("👎 Gesto de BIEN detectado!")
            cv2.putText(frame, "BIEN!", (50, 150), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        else:
            # Normalizar la posición x de la mano a un rango de 0 a 180 grados
            frame_width = frame.shape[1]
            angle = np.interp(x + w // 2, [0, frame_width], [0, 180])


        # GESTO DE PAZ Y AMOR

        if dedos_doblados == [False, False, True, True] : 
            print("🕊️🕊️🕊️🕊️🕊️🕊️🕊️🕊️🕊️🕊️🕊️")
            cv2.putText(frame, "paz y amor", (50,150),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        else:
            # Normalizar la posición x de la mano a un rango de 0 a 180 grados
            frame_width = frame.shape[1]
            angle = np.interp(x + w // 2, [0, frame_width], [0, 180])
        

    # Mostrar la imagen en ventana
    cv2.imshow("frame", frame)
    
    # Salir del programa al presionar 'k'
    k = cv2.waitKey(1)
    if k == ord("k" or "K"): 
        break

# Liberar recursos
video.release()
cv2.destroyAllWindows()
