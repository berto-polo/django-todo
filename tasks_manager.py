import modules.classes as classes
import modules.mini_db as db

def run():
    counter = 1
    tries = 3
    print('¡Hola! 👋\n¿Qué te gustaría hacer hoy? 🌞\n')
    
    while True:
        print('Tienes estas opciones:\n\
            \r1) 📋 Crear lista\n\
            \r2) 👁️  Ver listas\n\
            \r3) 🖋️  Modificar lista\n\
            \r4) ❇️  Añadir tarea a lista existente\n\
            \r5) 🆕 Añadir tarea a lista nueva.\n\
            \r6) 🛫 Salir\n\n\
            \rIntroduce la opción >>> ', end=''
            )
        selection = int(input())
        if selection in range(1, 7):
            break
        elif counter < tries:
            print(f'\n⚠️ {selection} no es una opción válida\n\
                \rTe quedan {tries - counter} intentos\n')
            counter += 1
        else:
            print('Hasta luego!')
            return

    if selection == 1:
        return new_list()
    elif selection == 2:
        # Ver lista
        pass
    elif selection == 3:
        # Modificar lista
        pass
    elif selection == 4:
        # Añadir a existente
        pass
    elif selection == 5:
        # Añadir a nueva
        pass
    else:
        # bai
        pass

def new_list():
    print('¿Cómo se va a llamar la lista?\n>>> ', end='')
    name = str(input())
    new = classes.ToDoList(name)
    print(f'{name} ha sido creada')
    print(f'¿Qué quieres hacer ahora?')

    while True:
        print(f'1) ❇️ Añadir tarea a {name}\n\
            \r2) 🌡️ Asignar prioridad a la lista\n\
            \r3) 🆕 Crear lista nueva\n\
            \r4) ↗️ Salir')
        selection = int(input())
        if selection in range(1, 4):
            break
        elif counter < tries:
            print(f'\n⚠️ {selection} no es una opción válida\n\
                \rTe quedan {tries - counter} intentos\n')
            counter += 1
        else:
            print('Hasta luego!')
            return


if __name__ == '__main__':
    run()