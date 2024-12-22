import cv2
import numpy as np
import shutil
import os
import sys

def ultra_advanced_edge_detection(image):
    """Сверхпродвинутое обнаружение краев"""
    # Преобразование в оттенки серого
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Многоуровневое обнаружение краев
    edges_sobel = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    edges_canny = cv2.Canny(gray, 50, 150)
    
    # Лапласиан для выделения мельчайших деталей
    edges_laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    
    # Комбинированное обнаружение краев
    combined_edges = cv2.addWeighted(
        cv2.convertScaleAbs(edges_sobel), 0.5,
        cv2.convertScaleAbs(edges_laplacian), 0.5, 0
    )
    combined_edges = cv2.bitwise_or(combined_edges, edges_canny)
    
    # Морфологические преобразования для усиления краев
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
    edges_enhanced = cv2.morphologyEx(combined_edges, cv2.MORPH_CLOSE, kernel)
    
    return edges_enhanced, gray

def generate_ultimate_ascii_charset():
    """Генерация максимально детализированного набора символов"""
    # Unicode символы с максимальной плотностью и вариативностью
    unicode_sets = [
        # Блочные элементы и геометрические фигуры
        '▀▄█▌▐░▒▓■□▪▫◘◙◚◛◜◝◞◟◠◡◢◣◤◥◦◧◨◩◪◫◬◭◮',
        # Математические символы и операторы
        '±×÷∀∁∂∃∄∅∆∇∈∉∊∋∌∍∎∏∐∑−∓∔∕∖∗∘∙√∛∜∝∞',
        # Технические символы
        '⌀⌁⌂⌃⌄⌅⌆⌇⌈⌉⌊⌋⌌⌍⌎⌏⌐⌑⌒⌓⌔⌕⌖⌗⌘⌙⌜⌝⌞⌟',
        # Символы для заполнения
        '░▒▓▔▕▖▗▘▙▚▛▜▝▞▟'
    ]
    
    # Добавляем стандартные ASCII символы
    standard_chars = '@%#*+=-:. '
    
    # Объединяем все наборы
    ultimate_charset = standard_chars + ''.join(unicode_sets)
    
    return ultimate_charset

def image_to_phenomenal_ascii(image_path):
    """Генерация феноменального ASCII-арта"""
    # Загрузка изображения с максимальным качеством
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    
    # Расширенная предобработка
    # Коррекция цветового баланса
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    
    # Адаптивное выравнивание яркости
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    l_enhanced = clahe.apply(l)
    
    # Реконструкция изображения
    lab_enhanced = cv2.merge((l_enhanced, a, b))
    image_enhanced = cv2.cvtColor(lab_enhanced, cv2.COLOR_LAB2BGR)
    
    # Обнаружение краев и получение интенсивности
    edges, gray = ultra_advanced_edge_detection(image_enhanced)
    
    # Получаем размер терминала
    terminal_size = shutil.get_terminal_size()
    width = terminal_size.columns
    height = terminal_size.lines - 2
    
    # Resize изображений
    resized_gray = cv2.resize(gray, (width, height), interpolation=cv2.INTER_LANCZOS4)
    resized_edges = cv2.resize(edges, (width, height), interpolation=cv2.INTER_LANCZOS4)
    
    # Генерация максимально детализированного набора символов
    ultimate_charset = generate_ultimate_ascii_charset()
    
    # Генерация ASCII с феноменальной детализацией
    ascii_art = ""
    for y in range(height):
        for x in range(width):
            pixel_intensity = resized_gray[y, x]
            edge_intensity = resized_edges[y, x]
            
            # Продвинутый выбор символа
            if edge_intensity > 200:  # Сильные края
                char_index = int((edge_intensity / 255) * (len(ultimate_charset) - 1))
                ascii_art += ultimate_charset[char_index]
            else:
                # Дифференцированный выбор символа по интенсивности
                char_index = int((pixel_intensity / 255) * (len(ultimate_charset) - 1))
                ascii_art += ultimate_charset[char_index]
        
        ascii_art += "\n"
    
    return ascii_art

def main():
    image_path = 'Foto.img/photo_2024-11-02_23-10-23.jpg'
    
    try:
        # Очистка экрана
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Генерация феноменального ASCII-арта
        ascii_art = image_to_phenomenal_ascii(image_path)
        
        # Вывод
        print(ascii_art)
    
    except Exception as e:
        print(f"Критическая ошибка: {e}")
        print(f"Трассировка: {sys.exc_info()}")

if __name__ == "__main__":
    main()