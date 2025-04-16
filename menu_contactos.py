from gestion_contacto import GestionContactos

class MenuContactos:
    def __init__(self):
        self.gestion_contacto = GestionContactos()
    
    def menu_contactos(self):
        salir = False
        print('***Menu Contactos***')
        while not salir:
            try:
                opcion = self.mostrar_menu()
                salir = self.ejecutar_opcion(opcion)
            except Exception as e:
                print(f'Ha ocurrido un error: {e}')
    
    def mostrar_menu(self):
        print(f'''Menu:
              1. Agregar Contacto
              2. Mostrar Contactos
              3. Buscar Contacto
              4. Eliminar Contacto
              5. Salir''')
        return int(input('Elige una opción: '))
    
    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            self.gestion_contacto.agregar_contacto()
        elif opcion == 2:
            self.gestion_contacto.mostrar_contactos()
        elif opcion == 3:
            self.gestion_contacto.buscar_contactos()
        elif opcion == 4:
            self.gestion_contacto.eliminar_contacto()
        elif opcion == 5:
            print('Has salido del menu de contactos')
            return True
        else:
            print(f'Opcion invalida: {opcion}')
        return False
    
    
if __name__ == '__main__':
    menu_contactos = MenuContactos()
    menu_contactos.menu_contactos()
        