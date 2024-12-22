import cv2
import numpy as np
import shutil

def image_to_ascii(image_path):
    # Получаем размер терминала
    terminal_size = shutil.get_terminal_size()
    width = terminal_size.columns
    height = terminal_size.lines - 1  # Небольшой запас для совместимости

    # Расширенный набор символов ASCII
    ascii_chars = '@%#*+=-:. '
    
    # Чтение изображения
    image = cv2.imread(image_path)
    
    if image is None:
        raise ValueError(f"Не удалось прочитать изображение по пути: {image_path}")
    
    # Преобразование в оттенки серого
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Расчет пропорционального масштабирования
    aspect_ratio = gray_image.shape[1] / gray_image.shape[0]
    
    # Максимальное растягивание с сохранением пропорций
    new_width = width
    new_height = height
    
    # Resize с высококачественной интерполяцией
    resized_image = cv2.resize(gray_image, (new_width, new_height), 
                                interpolation=cv2.INTER_LANCZOS4)
    
    # Преобразование пикселей в символы ASCII
    ascii_image = ""
    for row in resized_image:
        for pixel in row:
            # Нормализация значения пикселя и маппинг на символы ASCII
            index = int((pixel / 255) * (len(ascii_chars) - 1))
            ascii_image += ascii_chars[index]
        ascii_image += "\n"
    
    return ascii_image

# Центрирование ASCII-арта
def center_ascii_art(ascii_art):
    terminal_size = shutil.get_terminal_size()
    width = terminal_size.columns
    height = terminal_size.lines

    # Разбиваем ASCII-арт на строки
    lines = ascii_art.split('\n')
    
    # Центрирование по горизонтали
    centered_lines = []
    for line in lines:
        padding_left = (width - len(line)) // 2
        centered_line = " " * padding_left + line.ljust(width)
        centered_lines.append(centered_line)
    
    # Центрирование по вертикали
    vertical_padding_top = (height - len(lines)) // 2
    vertical_padding_bottom = height - len(lines) - vertical_padding_top
    
    centered_art = (
        "\n" * vertical_padding_top + 
        "\n".join(centered_lines) + 
        "\n" * vertical_padding_bottom
    )
    
    return centered_art

# Путь к изображению
image_path = 'Foto.img/photo_2024-11-02_23-10-23.jpg'

try:
    # Очистка экрана
    print("\033[2J\033[H", end="")
    
    # Генерация ASCII-арта
    ascii_art = image_to_ascii(image_path)
    
    # Центрирование и вывод
    centered_ascii_art = center_ascii_art(ascii_art)
    print(centered_ascii_art)

except Exception as e:
    print(f"Ошибка: {e}")