Proyecto: Control de Servomotor con Gestos de Mano

📜 Integrantes
Agustina Fénnema: agusfennema@gmail.com
Nicolas Gomez: anelecarg@gmail.com

🎯 Objetivo del Proyecto
Este proyecto consiste en un sistema interactivo que permite controlar un servomotor mediante los gestos de la mano, detectados a través de una cámara web. El servomotor se mueve hacia la izquierda o derecha según el movimiento de la mano, y la pantalla muestra el gesto realizado (como un saludo).

🛠️ Hardware Necesario
Arduino Uno: El cerebro del sistema, controla el servomotor.
Servomotor (SG90): Actuador que simula el movimiento de la mano.
Escarbadiente y mano de papel: Un toque creativo para visualizar el movimiento del servomotor.
Cámara Web: Se encarga de detectar y rastrear los gestos de la mano en tiempo real.
💻 Software y Bibliotecas
Bibliotecas necesarias:
OpenCV (cv2): Para el procesamiento de las imágenes de la cámara.
pyFirmata2: Facilita la comunicación entre Python y el Arduino a través del puerto serial.
mediapipe / HandTrackingModule: Para detectar los gestos de la mano y rastrear la posición de los dedos.
Numpy: Utilizado para realizar cálculos y manipulaciones de matrices derivadas de la detección de la mano.

⚙️ Funcionamiento del Proyecto
1. Captura y Procesamiento de Imagen
La cámara web captura imágenes en tiempo real y las convierte a un formato compatible con la biblioteca mediapipe, que detecta la posición de la mano y los dedos (especialmente el dedo índice).

2. Control del Servomotor
Dependiendo de la posición del dedo índice, el servomotor se moverá a:

Izquierda (0 grados)
Derecha (180 grados)
Centro (90 grados)
3. Visualización
En la pantalla, se mostrará la dirección en la que gira el servomotor (Izquierda/Derecha) y el gesto reconocido (por ejemplo, un saludo).

🔮 Funcionalidades Futuras
Juego de Preguntas y Respuestas: Implementar un juego interactivo donde los jugadores respondan preguntas usando únicamente gestos (levantar la mano para "sí", agitarla para "no", etc.).
Reconocimiento de Más Gestos: Añadir el reconocimiento de gestos adicionales, como el pulgar arriba, el saludo, entre otros.

🔄 Flujo del Proyecto
Captura de Video: Inicia la captura de imágenes desde la cámara web.
Detección y Seguimiento de Gestos: La imagen es procesada en tiempo real para detectar la posición de la mano y los gestos.
Envío de Señales al Arduino: Según el movimiento de la mano, Python envía señales a Arduino para mover el servomotor.
Visualización: La pantalla muestra la dirección del movimiento (Izquierda/Derecha) y el gesto detectado.

🤖 Interacción del Sistema
Usuario: Mueve la mano hacia la izquierda o derecha.
Cámara Web: Detecta el gesto realizado.
Python: Procesa la imagen y decide el movimiento del servomotor.
Arduino: Mueve el servomotor según la señal recibida.
Pantalla: Muestra la dirección del movimiento y el gesto realizado.
