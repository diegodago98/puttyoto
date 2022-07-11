from fileinput import close
import json
import os



f = "mijson.json"
mi_diccionario= json.load(open('mijson.json'))


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
    usuario= mi_diccionario[servidores]['user']
    conexion= mi_diccionario[servidores]['ip']
       
    cmd = ' ssh ' + usuario  + "@" + conexion

    os.system(cmd)

elif pregunta == "2":

    print ("\n")
    for key in mi_diccionario:
        print (key)
    print ("\n")

    usuario= input("Introduce el nuevo usuario: ")
    servidor= input("Introduce el nombre del servidor: ")
    ip= input("Introduce la ip de conexion: ")

    nuevo_servidor = {
        "user": usuario,
        "ip": ip
    }

    mi_diccionario[servidor] = nuevo_servidor

    json.dump (mi_diccionario, open('mijson.json', 'w'), indent = 4)

elif pregunta == "3":

    print ("\n")
    for key in mi_diccionario:
        print (key)

    print ("\n")
    del_servidor = input("Introduce el nombre del servidor que quieras borrar: ")
    mi_diccionario.pop(del_servidor)

    json.dump (mi_diccionario, open('mijson.json', 'w'), indent = 4)

    

else:
    print("Esa no es una opción valida")







