import cv2
import os
from datetime import datetime

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Não foi possível acessar a câmera")
    exit()

# Cria uma pasta para salvar as fotos (se não existir)
pasta_fotos = "fotos"
os.makedirs(pasta_fotos, exist_ok=True)

print("Pressione 'T' para tirar uma foto")
print("Pressione 'Q' para sair")

while True:
    ret, frame = camera.read()
    if not ret:
        print("Falha ao capturar imagem")
        break

    cv2.imshow("Camera", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('t'):
        # Gera um nome de arquivo único com data e hora
        nome_arquivo = datetime.now().strftime("foto_%Y%m%d_%H%M%S.png")
        caminho_completo = os.path.join(pasta_fotos, nome_arquivo)

        # Salva a foto
        cv2.imwrite(caminho_completo, frame)
        print(f"Foto salva em: {caminho_completo}")

        # Mostra a foto tirada em uma janela separada
        cv2.imshow("Foto Tirada", frame)

    elif key == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()