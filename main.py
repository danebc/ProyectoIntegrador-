def Laberinto(name:str): 
    return name
 
print ("Hola, bienvenido al Laberinto, por favor ingresa tu nombre") 
if Laberinto: 
        name = Laberinto (name=input())
        texto = "Hola," 
        print (texto,Laberinto(name))
        
import keyboard

print("Presiona la tecla '1' para detener el bucle.")

while True:
    event = keyboard.read_event()
    if event.name == '1' and event.event_type == keyboard.KEY_UP:
        print("Tecla '1' detectada. Saliendo del bucle.")
        break
    else:
        print("Tecla detectada:",event.name) 
        
        