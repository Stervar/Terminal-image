import cv2
import numpy as np
import shutil

def image_to_ascii(image_path):
    # Получаем размер терминала
    terminal_size = shutil.get_terminal_size()
    width = terminal_size.columns
    height = terminal_size.lines

    # Символы ASCII от темных к светлым
    ascii_chars = '@%#*+=-:. '
    
    # Чтение изображения
    image = cv2.imread(image_path)
    
    if image is None:
        raise ValueError(f"Не удалось прочитать изображение по пути: {image_path}")
    
    # Преобразование в оттенки серого
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Изменение размера изображения под размер терминала
    aspect_ratio = gray_image.shape[1] / gray_image.shape[0]
    new_height = height
    new_width = int(new_height * aspect_ratio)
    
    # Если ширина больше ширины терминала, корректируем
    if new_width > width:
        new_width = width
        new_height = int(new_width / aspect_ratio)
    
    resized_image = cv2.resize(gray_image, (new_width, new_height))
    
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

try:
    # Очистка экрана (работает в большинстве терминалов)
    print("\033[2J\033[H", end="")
    
    # Генерация и вывод ASCII-арта
    ascii_art = image_to_ascii(image_path)
    print(ascii_art)

except Exception as e:
    print(f"Ошибка: {e}")