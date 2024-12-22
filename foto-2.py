import cv2
import numpy as np
import shutil
import os

def image_to_ascii(image_path):
    # Получаем размер терминала
    terminal_size = shutil.get_terminal_size()
    width = terminal_size.columns
    height = terminal_size.lines

    # Символы ASCII от темных к светлым (расширенный набор)
    ascii_chars = '@%#*+=-:. '
    
    # Чтение изображения
    image = cv2.imread(image_path)
    
    if image is None:
        raise ValueError(f"Не удалось прочитать изображение по пути: {image_path}")
    
    # Преобразование в оттенки серого
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Максимальное расширение с сохранением пропорций
    aspect_ratio = gray_image.shape[1] / gray_image.shape[0]
    new_width = width - 2  # Небольшой отступ по краям
    new_height = int(new_width / aspect_ratio)
    
    # Если высота превышает высоту терминала, корректируем
    if new_height > height:
        new_height = height - 2
        new_width = int(new_height * aspect_ratio)
    
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

def center_ascii_art(ascii_art):
    # Получаем размер терминала
    terminal_size = shutil.get_terminal_size()
    width = terminal_size.columns
    height = terminal_size.lines
    
    # Разбиваем ASCII-арт на строки
    lines = ascii_art.split('\n')
    
    # Центрирование по горизонтали и вертикали
    centered_art = ""
    max_line_length = max(len(line) for line in lines)
    
    # Добавляем вертикальные отступы
    vertical_padding = (height - len(lines)) // 2
    
    for _ in range(vertical_padding):
        centered_art += " " * width + "\n"
    
    for line in lines:
        # Центрирование строки
        padding_left = (width - len(line)) // 2
        centered_line = " " * padding_left + line + " " * (width - padding_left - len(line))
        centered_art += centered_line + "\n"
    
    return centered_art

# Путь к изображению
image_path = 'Foto.img/photo_2024-11-02_23-10-23.jpg'

try:
    # Очистка экрана (работает в большинстве терминалов)
    print("\033[2J\033[H", end="")
    
    # Генерация ASCII-арта
    ascii_art = image_to_ascii(image_path)
    
    # Центрирование ASCII-арта
    centered_ascii_art = center_ascii_art(ascii_art)
    
    # Вывод
    print(centered_ascii_art)

except Exception as e:
    print(f"Ошибка: {e}")