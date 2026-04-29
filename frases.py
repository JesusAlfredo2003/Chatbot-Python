# frases.py

saludos = [
    "¡Hola! 😊",
    "¡Buenas! ¿Cómo estás?",
    "¡Hey! ¿Qué tal todo?",
    'como va todo?',
    "Que hubo!",
    "Buen dia!",
    "Como puedo ayudarte?"
]

despedidas = [
    "¡Hasta luego! 👋",
    "¡Nos vemos pronto!",
    "¡Cuídate mucho!",
    "Adios!!",
    "Hasta la proxima",
    "Me piro vampiro"
]

sin_respuesta = [
    "Okeyyy??",
    "No tengo lineas de codigo para responder",
    "Sin respuestas bro",
    "No entendi",
    "No tengo RAM para procesarlo"
]

def frase_aleatoria(lista):
    import random
    return random.choice(lista)
