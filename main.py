# Importación de librerías necesarias para la interfaz, procesamiento de imágenes y modelo YOLO
from tkinter import *
from PIL import Image, ImageTk
import imutils
import cv2
import numpy as np
from ultralytics import YOLO
import math


# Función para mostrar las imágenes de detección y texto informativo
def images(img, imgtxt):
    # Convertir la imagen de detección en un formato compatible con OpenCV
    img = np.array(img, dtype="uint8")
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    img = Image.fromarray(img)

    # Convertir la imagen a un formato que Tkinter pueda mostrar
    img_ = ImageTk.PhotoImage(image=img)
    lblimg.configure(image=img_)  # Mostrar la imagen en el label
    lblimg.image = img_  # Guardar referencia para evitar que el objeto sea recolectado por el GC

    # Procesar y mostrar la imagen de texto
    imgtxt = np.array(imgtxt, dtype="uint8")
    imgtxt = cv2.cvtColor(imgtxt, cv2.COLOR_BGR2RGB)
    imgtxt = Image.fromarray(imgtxt)

    # Convertir y mostrar la imagen de texto
    img_txt = ImageTk.PhotoImage(image=imgtxt)
    lblimgtxt.configure(image=img_txt)
    lblimgtxt.image = img_txt


# Función de escaneo que procesa el video y detecta objetos
def Scanning():
    global lblimg, lblimgtxt

    # Crear y posicionar labels para mostrar imágenes y texto en la ventana
    lblimg = Label(pantalla)
    lblimg.place(x=75, y=260)
    lblimgtxt = Label(pantalla)
    lblimgtxt.place(x=995, y=310)

    # Leer la captura de video si está activa
    if cap is not None:
        ret, frame = cap.read()  # Leer el cuadro actual de la cámara
        frame_show = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convertir a RGB para visualización en Tkinter

        if ret == True:  # Si la cámara funciona correctamente
            results = model(frame, stream=True, verbose=False)  # Ejecutar el modelo YOLO sobre el cuadro de video
            for res in results:
                boxes = res.boxes  # Obtener las cajas delimitadoras de los objetos detectados
                for box in boxes:
                    # Obtener las coordenadas de la caja delimitadora
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                    # Asegurar que las coordenadas no sean negativas
                    if x1 < 0: x1 = 0
                    if x2 < 0: x2 = 0
                    if y1 < 0: y1 = 0
                    if y2 < 0: y2 = 2

                    cls = int(box.cls[0])  # Obtener la clase del objeto detectado
                    conf = math.ceil(box.conf[0])  # Obtener el nivel de confianza de la detección

                    # Solo mostrar detecciones con confianza mayor a 0.5
                    if conf > 0.5:
                        # Dependiendo de la clase detectada, dibujar la caja delimitadora y mostrar información
                        if cls == 0:  # Metal
                            cv2.rectangle(frame_show, (x1, y1), (x2, y2), (255, 255, 0), 2)
                            text = f'{clsName[cls]} {int(conf) * 100}%'
                            sizetext = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
                            dim, baseLine = sizetext[0], sizetext[1]
                            cv2.rectangle(frame_show, (x1, y1 - dim[1] - baseLine), (x1 + dim[0], y1 + baseLine),
                                          (0, 0, 0), cv2.FILLED)
                            cv2.putText(frame_show, text, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
                            images(img_Metal, img_Metaltxt)

                        if cls == 1:  # Vidrio
                            cv2.rectangle(frame_show, (x1, y1), (x2, y2), (255, 255, 255), 2)
                            text = f'{clsName[cls]} {int(conf) * 100}%'
                            sizetext = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
                            dim, baseLine = sizetext[0], sizetext[1]
                            cv2.rectangle(frame_show, (x1, y1 - dim[1] - baseLine), (x1 + dim[0], y1 + baseLine),
                                          (0, 0, 0), cv2.FILLED)
                            cv2.putText(frame_show, text, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                            images(img_Glass, img_Glasstxt)

                        if cls == 2:  # Plástico
                            cv2.rectangle(frame_show, (x1, y1), (x2, y2), (255, 255, 0), 2)
                            text = f'{clsName[cls]} {int(conf) * 100}%'
                            sizetext = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
                            dim, baseLine = sizetext[0], sizetext[1]
                            cv2.rectangle(frame_show, (x1, y1 - dim[1] - baseLine), (x1 + dim[0], y1 + baseLine),
                                          (0, 0, 0), cv2.FILLED)
                            cv2.putText(frame_show, text, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
                            images(img_Plastic, img_Plastictxt)

                        if cls == 3:  # Cartón
                            cv2.rectangle(frame_show, (x1, y1), (x2, y2), (150, 150, 150), 2)
                            text = f'{clsName[cls]} {int(conf) * 100}%'
                            sizetext = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
                            dim, baseLine = sizetext[0], sizetext[1]
                            cv2.rectangle(frame_show, (x1, y1 - dim[1] - baseLine), (x1 + dim[0], y1 + baseLine),
                                          (0, 0, 0), cv2.FILLED)
                            cv2.putText(frame_show, text, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (150, 150, 150), 2)
                            images(img_Carton, img_Cartontxt)

                        if cls == 4:  # Médico
                            cv2.rectangle(frame_show, (x1, y1), (x2, y2), (255, 0, 0), 2)
                            text = f'{clsName[cls]} {int(conf) * 100}%'
                            sizetext = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
                            dim, baseLine = sizetext[0], sizetext[1]
                            cv2.rectangle(frame_show, (x1, y1 - dim[1] - baseLine), (x1 + dim[0], y1 + baseLine),
                                          (0, 0, 0), cv2.FILLED)
                            cv2.putText(frame_show, text, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                            images(img_Medico, img_Medicotxt)

            # Redimensionar el cuadro para ajustar el tamaño
            frame_show = imutils.resize(frame_show, width=640)

            # Convertir el frame para mostrarlo en la interfaz
            im = Image.fromarray(frame_show)
            img = ImageTk.PhotoImage(image=im)

            # Actualizar el video en tiempo real
            labelVideo.configure(image=img)
            labelVideo.image = img
            labelVideo.after(10, Scanning)  # Continuar escaneando con un retraso de 10ms
        else:
            print("Error: No se pudo acceder a la cámara")
            cap.release()


# Función principal de la ventana
def ventana_principal():
    global pantalla, model, clsName, img_Metal, img_Glass, img_Plastic, img_Carton, img_Medico, labelVideo
    global img_Metaltxt, img_Glasstxt, img_Plastictxt, img_Cartontxt, img_Medicotxt, cap

    # Crear la ventana principal
    pantalla = Tk()
    pantalla.title("ECO_VISHIONAI")
    pantalla.geometry("1280x720")

    # Cargar imagen de fondo
    imagenfondo = PhotoImage(file="setUp/Canva.png")
    background = Label(image=imagenfondo)
    background.place(x=0, y=0, relwidth=1, relheight=1)

    # Cargar el modelo YOLO entrenado para detección de basura
    model = YOLO("Modelos/best.pt")

    # Definir las clases que el modelo puede detectar
    clsName = ["metal", "Glass", "Plastic", "Carton", "Medico"]

    # Cargar imágenes de los contenedores de reciclaje correspondientes a cada clase
    img_Metal = cv2.imread("setUp/Metal.png")
    img_Glass = cv2.imread("setUp/vidrio.png")
    img_Plastic = cv2.imread("setUp/plastico.png")
    img_Carton = cv2.imread("setUp/carton.png")
    img_Medico = cv2.imread("setUp/medical.png")

    # Cargar imágenes de texto explicativo de cada material
    img_Metaltxt = cv2.imread("setUp/metaltxt.png")
    img_Glasstxt = cv2.imread("setUp/vidriotxt.png")
    img_Plastictxt = cv2.imread("setUp/plasticotxt.png")
    img_Cartontxt = cv2.imread("setUp/cartontxt.png")
    img_Medicotxt = cv2.imread("setUp/medicaltxt.png")

    # Crear label para mostrar el video capturado
    labelVideo = Label(pantalla)
    labelVideo.place(x=319, y=118)

    # Iniciar la captura de video desde la cámara
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)  # Ancho del video
    cap.set(4, 480)  # Alto del video

    # Iniciar el escaneo y detección
    Scanning()

    # Iniciar el loop de la interfaz
    pantalla.mainloop()


# Ejecutar la ventana principal si se llama el script
if __name__ == '__main__':
    ventana_principal()
