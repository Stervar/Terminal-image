import cv2
import numpy as np
import shutil
import os
import sys

def debug_image_processing(image_path):
    """Расширенная функция диагностики изображения"""
    print("🔍 Диагностика изображения:")
    
    # Проверка существования файла
    if not os.path.exists(image_path):
        print(f"❌ Файл не найден: {image_path}")
        return None
    
    # Получение информации о файле
    file_stats = os.stat(image_path)
    print(f"📄 Размер файла: {file_stats.st_size} байт")
    
    # Попытка чтения изображения
    try:
        image = cv2.imread(image_path)
        
        if image is None:
            print("❌ Не удалось прочитать изображение через OpenCV")
            return None
        
        # Информация о изображении
        height, width, channels = image.shape
        print(f"🖼️ Размер изображения: {width}x{height}")
        print(f"🎨 Каналы: {channels}")
        
        return image
    
    except Exception as e:
        print(f"❌ Ошибка при чтении: {e}")
        return None

def image_to_detailed_ascii(image_path):
    """Генерация ASCII с максимальной детализацией"""
    
    # Диагностика изображения
    image = debug_image_processing(image_path)
    if image is None:
        return "Изображение не может быть обработано"
    
    # Получаем размер терминала
    try:
        terminal_size = shutil.get_terminal_size()
        width = terminal_size.columns
        height = terminal_size.lines - 2
    except Exception as e:
        print(f"❌ Ошибка определения размера терминала: {e}")
        width, height = 100, 50
    
    # Расширенный набор символов
    ascii_chars = '@%#*+=-:. '
    
    # Преобразование в оттенки серого
    try:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    except Exception as e:
        print(f"❌ Ошибка конвертации в оттенки серого: {e}")
        return "Не удалось конвертировать изображение"
    
    # Resize с сохранением пропорций
    try:
        resized_image = cv2.resize(gray_image, (width, height), 
                                   interpolation=cv2.INTER_AREA)
    except Exception as e:
        print(f"❌ Ошибка изменения размера: {e}")
        return "Не удалось изменить размер изображения"
    
    # Генерация ASCII
    ascii_image = ""
    for row in resized_image:
        ascii_row = ''.join([ascii_chars[int(pixel/25)] for pixel in row])
        ascii_image += ascii_row + "\n"
    
    return ascii_image

def main():
    # Путь к изображению
    image_path = 'Foto.img/photo_2024-11-02_23-10-23.jpg'
    
    try:
        # Очистка экрана (кроссплатформенный вариант)
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Генерация ASCII
        ascii_art = image_to_detailed_ascii(image_path)
        
        # Вывод
        print(ascii_art)
    
    except Exception as e:
        print(f"❌ Критическая ошибка: {e}")
        print(f"Трассировка: {sys.exc_info()}")

if __name__ == "__main__":
    main()