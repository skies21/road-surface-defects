# Road Surface Defects Detection

Этот проект использует Django и предварительно обученную нейронную сеть для определения дефектов на поверхности дороги. Пользователи могут загружать изображения, которые анализируются моделью, и результаты отображаются на веб-странице.

## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/skies21/road-surface-defects.git
    cd road_surface_defects
    ```

2. Создайте и активируйте виртуальное окружение:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Windows используйте `venv\Scripts\activate`
    ```

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

4. Убедитесь, что у вас есть файл модели `ResNet152V2.h5` в директории `app`.
