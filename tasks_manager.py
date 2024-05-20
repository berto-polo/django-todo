import modules.classes as classes
import modules.mini_db as db

#Menú principal
def main_menu(*, rerun=False):
    # Inicio del contador y límite de intentos para romper el bucle
    counter = 1
    tries = 3

    # Presentación si es la primera vez que se ejecuta
    if not rerun:
        print('¡Hola! 👋\n¿Qué te gustaría hacer hoy? 🌞\n')
    else:
        print('Estas son las opciones disponibles:\n')
    
    # Bucle que muestra las opciones disponibles
    while True:
        print('1) 📋 Crear lista\n\
            \r2) 👁️ Ver y editar listas\n\
            \r3) 🎯 Añadir tarea a una lista\n\
            \r4) 🛫 Salir\n\n\
            \rIntroduce la opción >>> ', end=''
            )
        
        # Input del usuario y manejo de errores (valor no es un número)
        selection = input()
        try:
            selection = int(selection)
        except ValueError:
            print(f'\n⚠️ {selection} no es una opción válida\n\
            \rTe quedan {tries - counter} intentos\n')
            counter += 1
        
        # Condiciones para salir del bucle
        if selection in range(1, 7):
            break
        elif counter < tries:
            print(f'\n⚠️ {selection} no es una opción válida\n\
                \rTe quedan {tries - counter} intentos\n')
            counter += 1
        else:
            print('Hasta luego!')
            return

    # Condicionales de las opciones del menú
    if selection == 1:
        return create_list()
    elif selection == 2:
        return display_lists()
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

# Creación de lista nueva
def create_list():
    counter = 1
    tries = 3

    print(
          '\nVas a crear una lista nueva:\n\
           \r¿Cómo quieres llamarla? >>> ', end=''
         )

    name = str(input())
    todo_list = classes.ToDoList(name)
    print(f'\n✅ «{name}» ha sido creada\n')

    print(f'¿Qué quieres hacer ahora?\n')
    while True:
        print(f'1) 🎯 Añadir tarea a {name}\n\
            \r2) ✍🏻 Editar lista\n\
            \r3) 🆕 Crear otra lista\n\
            \r4) 👁️ Explorar listas creadas\n\
            \r5) 🕹️ Ir al menú\n\
            \r6) ↗️ Salir\n')

        print('>>>', end=' ')
        selection = int(input())
        if selection in range(1, 5):
            break
        elif counter < tries:
            print(f'\n⚠️ {selection} no es una opción válida\n\
                \rTe quedan {tries - counter} intentos\n')
            counter += 1
        else:
            print('Hasta luego!')
            return
    
    if selection == 1:
        return add_task_to_list(todo_list)
    if selection == 2:
        return manage_list(todo_list)
    if selection == 3:
        return create_list()
    if selection == 4:
        return display_lists()
    if selection == 5:
        return main_menu(rerun=True)
    if selection == 6:
        pass

# Añadir tarea a lista existente
def add_task_to_list(todo_list: classes.ToDoList):
    counter = 1
    tries = 3

    list_name = todo_list.get_name()
    print(
         f'\n--- ✍🏻 Vas a añadir una tarea a {list_name} ---\n\
         \rIntrodúcela aquí:\n\
         \r>>>', end=' '
        )

    task_name = str(input())
    task = classes.Task(task_name)
    todo_list.add_task(task)

    print(f'\n👌🏻 ¡Perfecto!\n\
          "{task_name}" ha sido añadida a «{list_name}»\n\n\
          \r¿Qué hacemos ahora?\n')

    while True:
        print(
            f'1) ✍🏻 Añadir otra tarea a {list_name}\n\
            \r2) 👁️ Explorar la lista\n\
            \r3) 🆕 Crear otra lista\n\
            \r4) 🕹️ Ir al menú\n\
            \r5) ↗️ Salir'
            )

        print('>>>', end=' ')
        selection = input()
        try:
            selection = int(selection)
        except ValueError:
            print(f'\n⚠️ {selection} no es una opción válida\n\
            \rTe quedan {tries - counter} intentos\n')
            counter += 1

        if selection in range(1, 6):
            break
        elif counter < tries:
            print(f'\n⚠️ {selection} no es una opción válida\n\
                \rTe quedan {tries - counter} intentos\n')
            counter += 1
        else:
            print('Hasta luego!')
            return
    
    if selection == 1:
        return add_task_to_list(todo_list)
    if selection == 2:
        return manage_list(todo_list)
    if selection == 3:
        return new_list()
    if selection == 4:
        return main_menu(rerun=True)
    if selection == 5:
        print('Hasta luego!')

def display_lists():
    counter = 1
    tries = 3

    if len(db.lists_list) == 0:
        print('\n¡Vaya! Parece que de momento no hay ninguna lista 😥\n\
            \r¿Quieres añadir una nueva? (S/N)\n>>>', end=' ')
        selection = str(input()).lower().strip()

        if selection == 's':
            return create_list()
        else:
            return main_menu(rerun=True)
    
    else:
        while True: 
            print('Las listas disponibles son:')
            for i, todo_list in enumerate(db.lists_list):
                print(f'{i+1}) {todo_list.get_name()}\n\
                    \r  → {len(todo_list.get_tasks())} tareas.')
            
            print('\nIntroduce el número de la lista que quieres ver o 0 para ir al menú\n\
                \r>>>', end=' ')

            selection = input()
            try:
                selection = int(selection)
            except ValueError:
                print(f'\n⚠️ {selection} no es una opción válida\n\
                \rTe quedan {tries - counter} intentos\n')
                counter += 1
            
            # Condiciones para salir del bucle
            if selection in range(0, len(db.lists_list)):
                break
            elif counter < tries:
                print(f'\n⚠️ {selection} no es una opción válida\n\
                    \rTe quedan {tries - counter} intentos\n')
                counter += 1
            else:
                print('Hasta luego!')
                return

        if selection == 0:
            return main_menu(rerun=True)
        else:
            return manage_list(db.lists_list[selection - 1])

def manage_list(todo_list: classes.ToDoList):
    print()


if __name__ == '__main__':
    main_menu()