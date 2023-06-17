import cv2
import numpy as np 
import argparse

# Переменные для подключения к камере телефона через приложение droidcam (iOS,Android)
ip = "" # Введите ip камеры
port =  # Введите порт камеры
video_url = f'http://{ip}:{port}/video'

# Загрузка cfg файла и весов модели YOLO v2 или v3 
modelConfiguration = 'cfg/.cfg'
modelWeights = 'weights/.weights'
net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)

# Загрузка списка классов
classes = []
with open('data/coco.names', 'r') as f:
    classes = [line.strip() for line in f.readlines()]

# Задание пороговых значений для фильтрации слабых обнаружений (Оптимальные значения)
confidence_threshold = 0.4
nms_threshold = 0.4

# Метод и загрузка видеопотока
while True:
     try:
        method = int(input("Введите число метода: 0.Веб-камера / 1.Камера телефона "))
        if method == 0:
            cap = cv2.VideoCapture(0)
            print("Веб-камера")
        elif method == 1:
            cap = cv2.VideoCapture(video_url)
            print("Камера телефона")
        else:
            print("Ошибка: неверный выбор метода")
            continue
        break
     except ValueError:
         print("Ошибка: неверный формат числа")
         continue
         

while True:
    # Чтение кадра из видеопотока
    ret, frame = cap.read()

    if not ret:
        break

    # Получение ширины и высоты кадра
    (H, W) = frame.shape[:2]

    # Создание блоба из кадра и выполнение прямого прохода модели
    blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    layerOutputs = net.forward(net.getUnconnectedOutLayersNames())

    # Инициализация списков для обнаруженных ограничивающих прямоугольников, уверенностей и идентификаторов классов
    boxes = []
    confidences = []
    classIDs = []

    # Проход по каждому выходному слою
    for output in layerOutputs:
        # Проход по каждому обнаружению
        for detection in output:
            # Извлечение идентификатора класса и уверенности (вероятности) обнаружения
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]

            # Фильтрация слабых обнаружений с учетом порога уверенности
            if confidence > confidence_threshold:
                # Масштабирование координат ограничивающего прямоугольника относительно размеров изображения
                box = detection[0:4] * np.array([W, H, W, H])
                (centerX, centerY, width, height) = box.astype("int")

                # Вычисление координат верхнего левого угла ограничивающего прямоугольника
                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))

                # Обновление списков ограничивающих прямоугольников, уверенностей и идентификаторов классов
                boxes.append([x, y, int(width), int(height)])
                confidences.append(float(confidence))
                classIDs.append(classID)

    # Применение алгоритма non-maxima suppression для подавления перекрывающихся ограничивающих прямоугольников
    indices = cv2.dnn.NMSBoxes(boxes, confidences, confidence_threshold, nms_threshold)
    colors = np.random.uniform(0, 255, size=(len(classes), 3))

    # Проверка наличия обнаруженных объектов
    if len(indices) > 0:
        for i in indices.flatten():
            # Извлечение координат ограничивающего прямоугольника и уверенности
            (x, y, w, h) = boxes[i]
            confidence = confidences[i]

            # Отрисовка ограничивающего прямоугольника и текста с классом и уверенностью
            color = [0,255,200]  # Параметры цвета рамки в RGB
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            text = f"{classes[classIDs[i]]}: {confidence:.2f}"
            cv2.putText(frame, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Отображение кадра
    cv2.imshow("Web Detection", frame)

    # Прекращение работы при нажатии клавиши 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождение ресурсов
cap.release()
cv2.destroyAllWindows()
