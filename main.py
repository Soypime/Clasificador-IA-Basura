from flask import Flask, render_template, Response, jsonify
import cv2
from ultralytics import YOLO

app = Flask(__name__)

# 1. Carga de tu modelo entrenado
model = YOLO(r"runs/classify/train4/weights/best.pt") 

# 2. Configuración de cámara optimizada (Sin DSHOW para evitar rayas)
cap = cv2.VideoCapture(1) 
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 3. Variables de control
conteo = {"glass": 0, "plastic": 0, "paper": 0, "cardboard": 0, "trash": 0}
ultima_clase_detectada = "waiting"

# 4. Datos Curiosos para la UTL
datos_curiosos = {
    "waiting": "¡Hola! Pon algo frente a la cámara para empezar a clasificar. ♻️",
    "glass": "El vidrio tarda 4,000 años en degradarse, pero ¡es 100% reciclable!",
    "plastic": "Una botella de plástico tarda hasta 500 años en descomponerse.",
    "paper": "Reciclar 1 tonelada de papel salva 17 árboles** adultos. 🌳",
    "cardboard": "El cartón se puede reciclar hasta 7 veces. ¡Aprovéchalo!",
    "trash": "Esta basura no se puede reciclar. Intentemos generar menos."
}

def gen_frames():
    global ultima_clase_detectada
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            # Inferencia YOLO
            results = model(frame, stream=True)
            for r in results:
                if r.probs is not None:
                    id_clase = r.probs.top1
                    clase = r.names[id_clase]
                    conf = r.probs.top1conf.item() * 100
                    
                    # Dibujar en pantalla (Verde si es > 95%)
                    color = (0, 255, 0) if conf >= 95 else (0, 0, 255)
                    cv2.putText(frame, f"{clase.upper()} {conf:.1f}%", (30, 60), 
                                cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)
                    
                    # Lógica de Conteo y Estado al 95%
                    if conf >= 95:
                        if clase != ultima_clase_detectada:
                            if clase in conteo:
                                conteo[clase] += 1
                            ultima_clase_detectada = clase
                    elif conf < 40:
                        ultima_clase_detectada = "waiting"

            ret, buffer = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

# --- RUTAS WEB ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/get_status')
def get_status():
    # Esta función envía todo a la vez: Conteos, Clase actual y el Dato Curioso
    return jsonify({
        "counts": conteo,
        "current_class": ultima_clase_detectada,
        "fact": datos_curiosos.get(ultima_clase_detectada, datos_curiosos["waiting"])
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)