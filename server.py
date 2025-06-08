from flask import Flask

# Inicializar la aplicación Flask
app = Flask(__name__)

# Ruta principal
@app.route('/')
def home():
    return "¡Hola, Flask está en Render!"

# Verificar si el script se está ejecutando directamente
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)