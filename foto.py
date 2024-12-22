import cv2
import numpy as np

def image_to_ascii(image_path, width=100):
    # Символы ASCII, используемые для отображения яркости
    ascii_chars = "@%#*+=-:. "
    
    # Чтение изображения
    image = cv2.imread(image_path)
    
    # Преобразование в оттенки серого
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Изменение размера изображения
    aspect_ratio = gray_image.shape[1] / gray_image.shape[0]
    new_height = int(width / aspect_ratio)
    resized_image = cv2.resize(gray_image, (width, new_height))
    
    # Преобразование пикселей в символы ASCII
    ascii_image = ""
    for row in resized_image:
        for pixel in row:
            ascii_image += ascii_chars[pixel // 25]  # 255/10 = 25
        ascii_image += "\n"
    
    return ascii_image

# Путь к изображению
image_path = 'path/to/your/image.jpg'  # Замените на путь к вашему изображению
ascii_art = image_to_ascii(image_path, width=100)
print(ascii_art)