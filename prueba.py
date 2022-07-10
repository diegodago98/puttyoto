import json
import os
from attr import set_run_validators


mi_diccionario = { 
    'monitor-intermark' :{
        'IP' : '13.73.148.187' ,
        'usuario' : 'intermark'
    },
    'edpsolar pre' :{
        'IP' : '10.240.7.5' ,
        'usuario' : 'EX117753'        
    }
    
}

#opciones

print("1. Mostrar los servidores")
print("2. Agregar servidor")
print("3. Eliminar servidor")

pregunta = input("\nElige una opcion:")


if pregunta == "1":

    print ("\n")
    for key in mi_diccionario:
        print (key)
    
    servidores = input("\nIntroduce el nombre del servidor al que quieres conectarte: ")
    usuario= mi_diccionario[servidores]['usuario']
    conexion= mi_diccionario[servidores]['IP']
       
    cmd = ' ssh ' + usuario  + "@" + conexion

    os.system(cmd)

else:
    print("Esa no es una opción valida")






