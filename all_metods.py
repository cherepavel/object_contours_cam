import cv2
import numpy as np
import time
timeout = 2
patch = 'static\img\\'
def sobel(cap):
    # cap = cv2.VideoCapture(0)
    # time.sleep(timeout)
    # Захватить изображение с камеры
    ret, frame = cap.read()
    # Преобразование изображения в оттенки серого
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Применение оператора обнаружения краев Собеля
    x = cv2.Sobel(gray, cv2.CV_16S, 1, 0)
    y = cv2.Sobel(gray, cv2.CV_16S, 0, 1)
    Scale_absX = cv2.convertScaleAbs(x)
    Scale_absY = cv2.convertScaleAbs(y)
    result = cv2.addWeighted(Scale_absX, 0.5, Scale_absY, 0.5, 0)
    # Сохранение результата в файл
    cv2.imwrite(f'{patch}sobel.jpg', result)
    # cap.release(cap)
    print("sobel Выполнение завершено")
def canny(cap):
    # cap = cv2.VideoCapture(0)
    # time.sleep(timeout)
    ret, img = cap.read()
    blur = cv2.GaussianBlur (img, (3, 3), 0) # Используйте гауссовскую фильтрацию для уменьшения шума в исходном изображении
    result = cv2.Canny (blur, 50, 150) # 50 - минимальный порог, 150 - максимальный порог
    cv2.imwrite(f'{patch}canny.jpg', result)
    print(f'{patch}sharra.jpg')
    # cap.release()
    print("canny Выполнение завершено")
def sharra(cap):
    # cap = cv2.VideoCapture(0)
    # time.sleep(timeout)
    ret, img = cap.read()
    x = cv2.Sobel(img, cv2.CV_16S, 1, 0)
    y = cv2.Sobel(img, cv2.CV_16S, 0, 1)
    # cv2.convertScaleAbs(src[, dst[, alpha[, beta]]])
    # Необязательный параметр alpha - это коэффициент масштабирования, а beta - значение, добавляемое к результату, а результат возвращает изображение типа uint.
    Scale_absX = cv2.convertScaleAbs (x) # преобразовать масштаб преобразования
    Scale_absY = cv2.convertScaleAbs(y)
    result = cv2.addWeighted(Scale_absX, 0.5, Scale_absY, 0.5, 0)
    cv2.imwrite(f'{patch}sharra.jpg', result)
    # cap.release()
def laplass(cap):
    # cap = cv2.VideoCapture(0)
    # time.sleep(timeout)
    ret, img = cap.read()
    laplacian = cv2.Laplacian(img, cv2.CV_16S, ksize=3)
    result = cv2.convertScaleAbs(laplacian)
    cv2.imwrite(f'{patch}laplass.jpg', result)
    # cap.release()