# chatbot.py
import frases
import chistes
import operaciones 

print('Hola soy un Bot llamado Dovah, escribe "salir" para finalizar')
while True:
   user =  input("yo: ").lower()
   
   if user == 'salir':
      print('Nos vemos pronto')
      break
   elif user in ['hola', 'como estas', 'que hubo', 'hey que tal']:
    print("Dovah:", frases.frase_aleatoria(frases.saludos))
    
   elif user in ['adios', 'nos vemos', 'hasta pronto', 'hasta luego']:
    print("Dovah:", frases.frase_aleatoria(frases.despedidas))
    
   elif user in ['cuentame un chiste', 'dime un chiste', 'di algo gracioso', 'cuenta algo gracioso', 'di un chiste']:
      print("Dovah: ", chistes.chiste_aleatoria(chistes.chistes) )
   
   
   
   
   else:
       print("Dovah:", frases.frase_aleatoria(frases.sin_respuesta))
     

    

    
    