from PIL import Image
import numpy as np


def main():
    simple_icon = "simple_icon.png"
    #carregar a imagem original salvando na variável img
    img = Image.open(simple_icon)
    img.show()

    #converter a imagem em dados binários
    img_data = np.array(img)
    binary_data = img_data.tobytes()

    #salva os arquivos binários em um arquivo
    with open ("original_img.bin", "wb") as file:
        file.write(binary_data)
    
    #copiar o arquivo binário
    with open("original_img.bin", "rb") as original_file:
        data = original_file.read()

    with open("copy_img.bin", "wb") as copy_file:
        copy_file.write(data)

    #manipular dados do arquivo binário copa
    #exemplo 1: invertendo os bytes
    with open("copy_img.bin", "rb") as file:
        data = bytearray(file.read())

    #inverte todos os bytes
    data = data[::-1]

    with open("copy_img.bin","wb") as file:
        file.write(data)
    
    #carregar e mostrar a imagem manipulada
    modified_data = np.frombuffer(data, dtype=np.uint8).reshape(img_data.shape)
    modified_img = Image.fromarray(modified_data)
    modified_img.show()
    
if __name__ == "__main__":
    main()