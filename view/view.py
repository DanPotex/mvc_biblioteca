class View:
    """
    *************************************
    * Vista de la BD de una Biblioteca  *
    *************************************
    """

    #Funcion de Inico
    def start(self):
        print('=================================')
        print('= ¡Bienvenido a la Biblioteca!  =')
        print('=================================')
    
    #Funcion de Fin de Programa
    def end(self):
        print('=================================')
        print('=       ¡Hasta la vista!        =')
        print('=================================')

    #Funcion del Menu
    def main_menu(self):
        print('************************')
        print('* -- Menu Principal -- *')
        print('************************')
        print('1. Usuarios')
        print('2. Autores')
        print('3. Libros')
        print('4. Prestamos')
        print('5. Salir')

    #Funcion Opcion
    def option(self, last):
        print('Selecciona una opcion (1-'+last+'): ', end = '')

    #Funcion "No Valida"
    def not_valid_option(self):
        print('¡Opcion no valida!\nIntenta de nuevo')
    
    #Funcion de Pregunta algo de Usuario
    def ask(self, output):
        print(output, end = '')
    
    #Funcion de Mensaje de Pantalla
    def msg(self, output):
        print(output)

    #Funcion de OK (si algo se hizo correcto en el programa)
    def ok(self, id, op):
        print('+'*(len(str(id))+len(op)+24))
        print('+ ¡'+str(id)+' se '+op+' correctamente! +')
        print('+'*(len(str(id))+len(op)+24))

    #Funcion de Error (si algo sale mal en alguna operacion en el programa)
    def error(self, err):
        print(' ¡ERROR! '.center(len(err)+4,'-'))
        print('- '+err+' -')
        print('-'*(len(err)+4))

    """
    *******************
    * Views for autor *
    *******************
    """

    #Funcion para el Menu de los Autores
    def autor_menu(self):
        print('*************************')
        print('* -- Submenu Autores -- *')
        print('*************************')
        print('1. Agregar Autor')
        print('2. Leer Autor')
        print('3. Leer todos los Autores')
        print('4. Leer todos los Autores por Nacionalidad')
        print('5. Actualizar Autor')
        print('6. Borrar Autor')
        print('7. Regresar')
    
    #Funcion de Mostrar Datos del Autor
    def show_a_autor(self, record):
        print('ID:', record[0])
        print('Nombre:', record[1])
        print('Apellido Paterno:', record[2])
        print('Apellido Materno:', record[3])
        print('Nacionalidad:', record[4])

    #Funcion para ver lo que hay en la cabecera de salida
    def show_autor_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    #Funcion para separar Diferentes Datos
    def show_autor_midder(self):
        print('-'*48)

    #Funcion de Terminacion de los Productos
    def show_autor_footer(self):
        print('*'*48)


    """
    *******************
    * Views for books *
    *******************
    """

    #Funcion para el Menu de los Productos
    def books_menu(self):
        print('***************************')
        print('* -- Submenu Libros -- *')
        print('***************************')
        print('1. Agregar Libro')
        print('2. Leer Libro')
        print('3. Leer todos los Libros')
        print('4. Actualizar Libro')
        print('5. Borrar Libro')
        print('6. Regresar')

    #Funcion Mostrar Libro
    def show_a_book(self, record):
        print('ID:', record[0])
        print('Titulo:', record[1])
        print('Editorial:', record[2])
        print('Autor:', record[3])

    #Funcion para ver lo que hay en la cabecera de salida
    def show_book_header(self, header):
        print(header.center(30,'*'))
        print('-'*30)

    #Funcion para separar Diferentes Datos
    def show_book_midder(self):
        print('-'*30)

    #Funcion de Terminacion de los Productos
    def show_book_footer(self):
        print('*'*30)

    """
    *******************
    * Views for Users *
    *******************
    """

    #Funcion de Menu de los Usuarios
    def users_menu(self):
        print('**************************')
        print('* -- Submenu Usuarios -- *')
        print('**************************')
        print('1. Agregar Usuario')
        print('2. Leer Usuario')
        print('3. Leer todos los Usuarios')
        print('4. Actualizar Usuario')
        print('5. Borrar Usuario')
        print('6. Regresar')

    #Funcion de Mostrar Usuario
    def show_a_user(self, record):
        print('ID:', record[0])
        print('Nombre:', record[1])
        print('Apellido Paterno:', record[2])
        print('Apellido Materno:', record[3])
        print('Direccion:', record[4])
    
    #Funcion para Compactar la Informacion de los usuarios (varios usuarios)
    def show_a_user_brief(self, record):
        print('ID:', record[0])
        print('Nombre:', record[1]+' '+record[2]+' '+record[3])
    
    #Funcion para ver lo que hay en la cabecera de salida
    def show_user_header(self, header):
        print(header.center(75,'*'))
        print('-'*75)

    #Funcion para separar Diferentes Datos
    def show_user_midder(self):
        print('-'*75)

    #Funcion de Terminacion de los Clientes
    def show_user_footer(self):
        print('*'*75)

    """
    *******************
    * Views for loan  *
    *******************
    """

    #Funcion de Menu de Prestamos
    def loan_menu(self):
        print('***************************')
        print('* -- Submenu Prestamos -- *')
        print('***************************')
        print('1. Agregar Prestamo')
        print('2. Leer Prestamo')
        print('3. Leer todos los Prestamos')
        print('4. Leer ordenes de un Usuario')####
        print('5. Actualizar datos de un Prestamo')
        print('6. Agregar Libros a un Prestamo')
        print('7. Modificar Libro de un Prestamo')
        print('8. Borrar Libros de un Prestamo')
        print('9. Borrar Prestamo')
        print('10. Regresar')

    #Funcion para Mostrar las Prestamos
    def show_loan(self, record):
        print('ID:', record[0])
        print('ID usuario:', record[1])
        print('Fecha:', record[2])
        print(' Datos del usuario '.center(81,'*'))
        self.show_a_user_brief(record[3:])
    
    #Funcion para ver lo que hay en la cabecera de salida
    def show_loan_header(self, header):
        print(header.center(81,'+'))
    
    #Funcion para separar Diferentes Datos
    def show_loan_midder(self):
        print('/'*81)

    #Funcion de Terminacion de los Prestamos
    def show_loan_footer(self):
        print('+'*81)

    """
    ****************************
    * Views for Loan Details  *
    ****************************
    """

    #Funcion para Mostrar los Detalles del Prestamo
    def show_a_loan_details(self, record):
        print(f'{record[0]:<5}|{record[1]:<20}|{record[2]:<20}|{record[3]:<11}')

    #Funcion para ver lo que hay en la cabecera de salida (de la vista de detalles del prestamo)
    def show_loan_details_header(self):
        print('-'*81)

        print('ID'.ljust(5)+'|'+'Libro'.ljust(20)+'|'+'Editorial'.ljust(20))
        print('-'*81)
    
    #Funcion de Terminacion de los Detalles del Prestamo
    def show_loan_details_footer(self):
        print('-'*81)