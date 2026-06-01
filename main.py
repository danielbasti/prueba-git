import json

try:
    with open("tareas.json", "r") as archivo:
        tareas = json.load(archivo)
except:
    tareas = []

while True:
    print("\n=== TASK MANAGE ===")
    print("1. ver tareas")
    print("2. agregar tarea")
    print("3. salir")

    opcion = input("selecciona la opcion: ")
    if opcion == "1":
        print("mostrando tareas...")
        if len(tareas) == 0:
            print("no ahi tareas")
        else:
            for i, tarea in enumerate(tareas, start=1):
                print(f"{i}. {tarea}")

    elif opcion == "2":
        tarea = input("nueva tarea: ")
        tareas.append(tarea)
        with open("tareas.json", "w") as archivo:
             json.dump(tareas, archivo)
        print("tarea agregada", tarea)
    
    elif opcion == "3":
        print("Hasta Luego!!!")
        break

    else:
        print("Opcion Invalida")