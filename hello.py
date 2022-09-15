from flask import Flask

app = Flask(__name__) #para llamar a la clase Flask y ejecute

@app.route("/hola") #decorador se le indica la ruta donde está
def primera_entrada():
    return "Hola,Mundo"

@app.route("/adios")
def salida():
    return "Hasta la vista, Baby!!!!"

@app.route("/doble/<int:numero>")
def doble(numero):
    return str(numero * 2)


