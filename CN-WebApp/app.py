from flask import Flask

# Crear una instancia de la aplicación Flask
app = Flask(_name_)

# Definir una ruta para la página de inicio
@app.route('/')
def home():
    return "¡Hola, Azure App Service! Esta es mi primera aplicación web en Python."

# Punto de entrada para ejecutar la aplicación
if _name_ == '_main_':
    # Ejecutar la aplicación en el puerto 5000
    app.run(host='0.0.0.0', port=5000)