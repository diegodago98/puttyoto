from fileinput import close
import json
import os
from shutil import SameFileError



f = "mijson.json"
mi_diccionario= json.load(open('mijson.json'))


#opciones


while True :

    print("\n1. Mostrar los servidores")
    print("2. Agregar servidor")
    print("3. Eliminar servidor")
    print("4. Salir del programa")

    pregunta = input("\nElige una opcion:")


    #Mostrar y conectarte a servidores

    if pregunta == "1":


        print ("\n")
        for key in mi_diccionario:
            print (key)


        print("\n1. Conectar a un servidor")
        print("2. Volver al menu principal")


        opcion = input("\nQue quieres hacer?")

        #Conectar a servidor

        if opcion == "1":

            servidores = input("\nIntroduce el nombre del servidor al que quieres conectarte: ")
            usuario= mi_diccionario[servidores]['user']
            conexion= mi_diccionario[servidores]['ip']

            cmd = ' ssh ' + usuario  + "@" + conexion
            os.system(cmd)

        #Volver al menu principal

        elif opcion == "2":

                 print("\nMenu Principal\n")    

        else:

            print("Esa no es una opcion correcta")

    #Añadir nuevo servidor

    elif pregunta == "2":

        print ("\n")
        for key in mi_diccionario:
            print (key)
        print ("\n")

        print("\n1. Nuevo servidor")
        print("2. Volver al menu principal\n")

        opcion = input("Elige la opcion que necesites: ")

        #Agregar nuevo servidor

        if opcion == "1":

            usuario= input("Introduce el nuevo usuario: ")
            servidor= input("Introduce el nombre del servidor: ")
            ip= input("Introduce la ip de conexion: ")

            nuevo_servidor = {
                "user": usuario,
                "ip": ip
            }

            mi_diccionario[servidor] = nuevo_servidor

            json.dump (mi_diccionario, open('mijson.json', 'w'), indent = 4)

            print("Servidor agregado correctamente")

        #Volver al menu principal

        if opcion == "2":
            
            print("\nMenu Principal\n")     

    #Eliminar servidores

    elif pregunta == "3":

        print ("\n")
        for key in mi_diccionario:
            print (key)

        print("\n1. Borrar un servidor")
        print("2. Volver al menu principal\n")

        opcion = input("Elige la opcion que necesites: ")

        #Eliminar servidor

        if opcion == "1":


            print ("\n")
            del_servidor = input("Introduce el nombre del servidor que quieras borrar: ")
            mi_diccionario.pop(del_servidor)

            json.dump (mi_diccionario, open('mijson.json', 'w'), indent = 4)

            print("Servidor borrado correctamente")

        #Volver al maenu principal

        else:
            print("\nMenu Principal\n")         

    #Salir del programa

    elif pregunta=="4":

        print("Hasta pronto!")
        break  

    else:
        print("Esa no es una opción valida")

    







