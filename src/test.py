from ultralytics import YOLO
import cv2
import os

# Lista de classes do seu dataset
CLASSES = ['(A-18)', '(A-2a)', '(A-2b)', '(A-32a)', '(A-32b)', '(Del)', '(I-4)', '(MA)', '(MP-3)', 
           '(R-1)', '(R-15)', '(R-19)30', '(R-19)40', '(R-19)50', '(R-19)60', '(R-19)70', '(R-19)80', 
           '(R-19)90', '(R-2)', '(R-24a)', '(R-4a)', '(R-5a)', '(R-6a)', '(R-6c)']

def TestModel(model_path="runs/detect/train/weights/best.pt", source="test_images"):
    """
    model_path: caminho para o modelo treinado (.pt)
    source: pode ser uma pasta com imagens, um vídeo ou uma webcam (0)
    """

    # Carrega o modelo treinado
    model = YOLO(model_path)

    # Faz a inferência
    results = model.predict(
        source=source,    # imagens, pasta, vídeo ou webcam (0)
        save=True,        # salva imagens com predições em runs/detect/predict
        show=True,        # mostra as imagens com bounding boxes
        conf=0.5,        # confiança mínima
        imgsz=640,        # tamanho da imagem
        device=0          # usa GPU (coloque 'cpu' se não tiver GPU)
    )

    # Exemplo de como acessar os resultados programaticamente
    for r in results:
        im_bgr = r.plot(line_width=2, font_size=10)
        cv2.imshow("Resultado", im_bgr)
        cv2.waitKey(0)     # espera uma tecla
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # Exemplo: testar em uma pasta de imagens
    TestModel(model_path="runs/detect/train2/weights/best.pt", source="tests/lombada.jpg")
    # Para testar com webcam: TestModel(source=0)
    # Para testar com vídeo: TestModel(source="video.mp4")

    cv2.waitKey(1)
