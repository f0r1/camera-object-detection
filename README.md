# Обнаружение объектов с использованием модели YOLO v2/v3
Этот репозиторий содержит код для выполнения обнаружения объектов с использованием модели YOLO (You Only Look Once) v2/v3. Для различных операций используются библиотеки OpenCV, NumPy и argparse.

## Начало работы
Для начала работы выполните следующие шаги:

1. Клонируйте репозиторий на свой компьютер.
2. Установите необходимые библиотеки, выполнив следующую команду:
## *pip install opencv-python numpy argparse*
3. [Скачайте](https://pjreddie.com/darknet/yolo/) файлы конфигурации и весов модели YOLO. Разместите их в соответствующих каталогах:
- Файл конфигурации модели (`cfg/.cfg`)
- Файл весов модели (`weights/.weights`)
4. Запустите скрипт с помощью следующей команды:
## *python object_detection.py*

## Использование

Скрипт предоставляет два метода обнаружения объектов:
1. **Метод веб-камеры**: Установите в переменную `method`  значение `0`, чтобы использовать веб-камеру в качестве источника видео.
2. **Метод камеры телефона**: Установите в переменную `method` значение `1` и укажите IP-адрес и порт камеры телефона в переменных `ip` и `port` соответственно.
Скрипт будет отображать результаты обнаружения объектов в режиме реального времени на экране. Нажмите клавишу 'q' для остановки выполнения.

## Настройка
Вы можете настроить скрипт в соответствии с вашими требованиями. Вы можете изменить порог уверенности и порог подавления немаксимальных значений, изменив переменные `confidence_threshold` и `nms_threshold` соответственно.

## Зависимости
- Python 3.x
- OpenCV
- NumPy
- argparse

## Лицензия
Этот проект лицензирован в соответствии с [MIT License](LICENSE).

## Примечание
Пожалуйста, убедитесь, что у вас есть необходимые файлы и зависимости перед запуском скрипта. Если у вас возникнут вопросы или проблемы, не стесняйтесь задавать их в разделе [Issues](https://github.com/username/repository/issues) этого репозитория.

**Примечание**: Замените `username/repository` на фактическое имя вашего репозитория в ссылке выше.

Приятного использования обнаружения объектов с помощью модели YOLO v2/v3!

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Object Detection using YOLO v2/v3
This repository contains code for performing object detection using the YOLO (You Only Look Once) v2/v3 model. It utilizes the OpenCV, NumPy, and argparse libraries for various operations.

## Getting Started
To get started, follow the steps below:

1. Clone the repository to your local machine.
2. Install the required libraries by running the following command:
## *pip install opencv-python numpy argparse*
3. [Download](https://pjreddie.com/darknet/yolo/) the YOLO model configuration and weights files. Place them in the appropriate directories:
- Model configuration file (`cfg/.cfg`)
- Model weights file (`weights/.weights`)
4. Run the script using the following command:
## *python object_detection.py*

## Usage
The script provides two methods for object detection:

1. **Webcam Method**: Set in the `method` variable to `0` to use the webcam as the video source.
2. **Phone Camera Method**: Set in the `method` variable to `1` and provide the IP address and port of the phone camera in the `ip` and `port` variables, respectively.
The script will display the real-time object detection results on the screen. Press the 'q' key to stop the execution.

## Customization
Feel free to customize the script as per your requirements. You can adjust the confidence threshold and non-maxima suppression threshold by modifying the `confidence_threshold` and `nms_threshold` variables, respectively.

## Dependencies
- Python 3.x
- OpenCV
- NumPy
- argparse

## License
This project is licensed under the [MIT License](LICENSE).

## Note
Please make sure you have the necessary files and dependencies before running the script. If you encounter any issues, feel free to raise them in the [Issues](https://github.com/username/repository/issues) section of this repository.

**Note**: Remember to replace `username/repository` with your actual repository name in the above link.

Enjoy object detection using YOLO v2/v3!



