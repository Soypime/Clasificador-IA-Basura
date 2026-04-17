# ♻️ Sistema de Clasificación de Residuos con IA (YOLOv8)

![Estado del Proyecto](https://img.shields.io/badge/Estado-En%20Desarrollo-green)
![Universidad](https://img.shields.io/badge/Instituci%C3%B3n-UTL-blue)
![Especialidad](https://img.shields.io/badge/Carrera-Mecatr%C3%B3nica-orange)

Este proyecto es un sistema de clasificación automática de basura que utiliza **Visión Artificial** e **Inteligencia Artificial** para identificar residuos en tiempo real y gestionarlos a través de una interfaz web profesional.

## 🚀 Características

- **Detección con YOLOv8:** Modelo entrenado para clasificar: Vidrio, Plástico, Papel, Cartón y Basura General.
- **Interfaz Web (Flask):** Dashboard en modo oscuro con visualización en tiempo real y datos curiosos sobre reciclaje.
- **Control de Precisión:** Conteo de objetos validado con un umbral de confianza superior al 95%.
- **Estadísticas en Tiempo Real:** Seguimiento automático de la cantidad de residuos procesados.
- **Mecatrónica Aplicada:** Integración de software (Python/Flask) con hardware (ESP32/Motores).

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.11+
* **IA:** YOLOv8 (Ultralytics)
* **Web Framework:** Flask
* **Visión:** OpenCV
* **Frontend:** HTML5, CSS3 (Custom Dark Mode), JavaScript (jQuery)
* **Hardware:** ESP32, Servomotores, Driver A4988, Motor a pasos NEMA 17.

## 📂 Estructura del Proyecto

```text
BASURA PIME/
├── main.py              # Servidor Flask y lógica de detección
├── yolov8n-cls.pt       # Modelo entrenado de YOLOv8
├── static/              # Recursos visuales (Logos, imágenes del robot)
│   ├── logo_utl.png
│   ├── esperando.png
│   └── pensando.png
├── templates/           # Interfaz de usuario (HTML)
│   └── index.html
└── runs/                # Resultados del entrenamiento del modelo


📊 Funcionamiento de la IA
El sistema captura el feed de video y procesa cada frame. Solo cuando el modelo alcanza una certeza del 95%, el contador de la categoría correspondiente se incrementa y la interfaz muestra un dato interesante sobre ese material para fomentar la educación ambiental.

👨‍💻 Autor
Adolfo Meza
Estudiante de Ingeniería en Mecatrónica
Universidad Tecnológica de León (UTL)
