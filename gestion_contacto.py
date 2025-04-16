from contacto import Contacto
import os.path

class GestionContactos:
        
        nombre_archivo = "lista_contactos.txt"
        
        def __init__(self):
            self.contactos = []
            if os.path.isfile(self.nombre_archivo):
                self.contactos = self.obtener_contactos_archivo()
            else: 
                self.agregar_ejemplos()         
            
        def agregar_ejemplos(self):
            ejemplos = [
                Contacto("Alcides", "675304234","alcidescon@gmailcom" ),
                Contacto("Roberto", "722181442","roberxiri@gmail.com" ),
                Contacto("Facundo", "692916064","facuscrollinic@gmail.com")
            ]
            
            with open(self.nombre_archivo, 'a') as archivo:
                for ejemplo in ejemplos:
                    archivo.write(f'{ejemplo.id},{ejemplo.nombre},{ejemplo.telefono},{ejemplo.telefono}\n')
                
        def obtener_contactos_archivo(self):
            contactos_archivo = []
            try:
                with open(self.nombre_archivo, 'r') as archivo:
                    for line in archivo:
                        id, nombre, telefono, email = line.strip().split(',')
                        contacto = Contacto(nombre, telefono, email)
                        contactos_archivo.append(contacto)
                        
            except Exception as e:
                print(f'Ha ocurrido un error: {e}')
            return contactos_archivo
                
            
        def agregar_contacto(self):
            try:
                nombre = input('Nombre de contacto a agregar: ')
                telefono = input('Telefono de contacto a agregar: ')
                email = input('Email de contacto a agregar: ')
                nuevo_contacto = Contacto(nombre, telefono, email)
                with open(self.nombre_archivo, 'a') as archivo:
                    archivo.write(f'{nuevo_contacto}\n')
                print(f'Nuevo contacto agregado: {nuevo_contacto}')
            
            except Exception as e:
                print(f'Ha ocurrido un error: {e}')
                
        def listar_contactos(self):
            try:
                with open(self.nombre_archivo, 'r') as archivo:
                    print(archivo.read())
                    
            except Exception as e:
                print(f'Ha ocurrido un error: {e}')
                
        def buscar_contactos(self):
            try:
                nombre_usuario = input('Introduce el nombre que quieres buscar: ').lower()
                contacto_encontrado = False
            
                for contacto in self.contactos:
                    if nombre_usuario in contacto.nombre.lower():
                        print(f'Id: {contacto.id},Nombre: {contacto.nombre},Telefono: {contacto.telefono},Email: {contacto.email}')
                        contacto_encontrado = True
                    
                if not contacto_encontrado:
                    print('Contacto no Encontrado')  
                    print(contacto_encontrado)
                    
            except Exception as e:
                print(f'Ha ocurrido un error: {e}')
            
        def eliminar_contacto(self):
            try:
                eliminar_contacto = input('Introduce el nombre del contacto que quieres eliminar: ')
                nuevos_contactos = []
                eliminado = False
                
                for contacto in self.contactos:
                    if eliminar_contacto not in contacto.nombre.lower():
                        nuevos_contactos.append(contacto)
                    else:
                        eliminado = True
                        
                if eliminado:
                    with open(self.nombre_archivo, 'w') as archivo:
                        for contacto in nuevos_contactos:
                            archivo.write(f'{contacto.id},{contacto.nombre},{contacto.telefono},{contacto.email}\n')
                            
                    self.contactos = nuevos_contactos
                    print(f'Contacto Eliminado')
                else:
                    print('No se encontro el contacto')
                        
            except Exception as e:
                print(f'Error al eliminar contacto: {e}')
                                  
            
if __name__ == '__main__':
    gestion_contacto = GestionContactos()
    # gestion_contacto.agregar_contacto()
    # gestion_contacto.buscar_contactos()
    gestion_contacto.eliminar_contacto()