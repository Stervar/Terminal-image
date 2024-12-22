import cv2
import numpy as np
import shutil

def advanced_image_preprocessing(image_path):
    # Загрузка изображения
    image = cv2.imread(image_path)
    
    # Проверка загрузки
    if image is None:
        raise ValueError("Изображение не загружено")
    
    # Улучшенная предобработка
    
    # 1. Коррекция яркости и контраста
    alpha = 1.5  # Контраст
    beta = 20    # Яркость
    image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    
    # 2. Подавление шума
    image = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)
    
    # 3. Повышение резкости
    kernel = np.array([[-1,-1,-1], 
                       [-1, 9,-1],
                       [-1,-1,-1]])
    image = cv2.filter2D(image, -1, kernel)
    
    # 4. Эквализация гистограммы
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    equalized = cv2.equalizeHist(gray)
    
    # 5. Обнаружение краев с адаптивным порогом
    edges = cv2.Canny(equalized, 100, 200)
    
    # 6. Морфологические преобразования для улучшения краев
    kernel = np.ones((3,3), np.uint8)
    edges = cv2.dilate(edges, kernel, iterations=1)
    edges = cv2.erode(edges, kernel, iterations=1)
    
    return equalized, edges

def image_to_advanced_ascii(image_path):
    # Получаем размер терминала
    terminal_size = shutil.get_terminal_size()
    width = terminal_size.columns
    height = terminal_size.lines - 1

    # Расширенный набор символов с учетом интенсивности и краев
    detailed_chars = '@%#*+=-:. '
    edge_chars = ['/', '\\', '|', '-', '+']
    
    # Предобработка изображения
    gray_image, edge_image = advanced_image_preprocessing(image_path)
    
    # Resize с сохранением пропорций
    resized_gray = cv2.resize(gray_image, (width, height), interpolation=cv2.INTER_LANCZOS4)
    resized_edges = cv2.resize(edge_image, (width, height), interpolation=cv2.INTER_LANCZOS4)
    
    # Генерация ASCII с учетом интенсивности и краев
    ascii_image = ""
    for y in range(height):
        for x in range(width):
            pixel_intensity = resized_gray[y, x]
            is_edge = resized_edges[y, x] > 128
            
            # Выбор символа на основе интенсивности и наличия края
            if is_edge:
                char_index = int((pixel_intensity / 255) * (len(edge_chars) - 1))
                ascii_image += edge_chars[char_index]
            else:
                char_index = int((pixel_intensity / 255) * (len(detailed_chars) - 1))
                ascii_image += detailed_chars[char_index]
        
        ascii_image += "\n"
    
    return ascii_image

def center_ascii_art(ascii_art):
    terminal_size = shutil.get_terminal_size()
    width = terminal_size.columns
    height = terminal_size.lines

    # Центрирование
    lines = ascii_art.split('\n')
    centered_lines = []
    
    for line in lines:
        padding_left = (width - len(line)) // 2
        centered_line = " " * padding_left + line.ljust(width)
        centered_lines.append(centered_line)
    
    vertical_padding_top = (height - len(lines)) // 2
    vertical_padding_bottom = height - len(lines) - vertical_padding_top
    
    centered_art = (
        "\n" * vertical_padding_top + 
        "\n".join(centered_lines) + 
        "\n" * vertical_padding_bottom
    )
    
    return centered_art

# Основной блок выполнения
image_path = 'Foto.img/photo_2024-11-02_23-10-23.jpg'

try:
    # Очистка экрана
    print("\033[2J\033[H", end="")
    
    # Генерация улучшенного ASCII-арта
    ascii_art = image_to_advanced_ascii(image_path)
    
    # Центрирование и вывод
    centered_ascii_art = center_ascii_art(ascii_art)
    print(centered_ascii_art)

except Exception as e:
    print(f"Ошибка: {e}")
    
    
    
        #     Ключевые улучшения:

        # Предобработка изображения:

        # Коррекция яркости и контраста
        # Подавление шума
        # Повышение резкости
        # Эквализация гистограммы
        # Обнаружение и выделение краев
        # Генерация ASCII:

        # Динамический выбор символов
        # Учет интенсивности пикселей
        # Специальные символы для краев
        # Сохранение структуры изображения
        # Преимущества:

        # Высокая детализация
        # Выделение контуров
        # Улучшенная визуальная репрезентация
        # Технические детали:

        # Использование продвинутых алгоритмов OpenCV
        # Адаптивное масштабирование
        # Сложная обработка изображения