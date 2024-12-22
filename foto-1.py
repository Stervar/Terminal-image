import cv2
import numpy as np

def image_to_ascii(image_path, width=100):
    # Расширенный набор символов ASCII для более точного представления
    ascii_chars = '@%#*+=-:. '
    
    # Чтение изображения
    image = cv2.imread(image_path)
    
    if image is None:
        raise ValueError(f"Не удалось прочитать изображение по пути: {image_path}")
    
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
            # Нормализация значения пикселя и маппинг на символы ASCII
            index = int((pixel / 255) * (len(ascii_chars) - 1))
            ascii_image += ascii_chars[index]
        ascii_image += "\n"
    
    return ascii_image

# Путь к изображению
image_path = 'Foto.img/photo_2024-11-02_23-10-23.jpg'
ascii_art = image_to_ascii(image_path, width=100)
print(ascii_art)