from model.model import Model
from view.view import View
from datetime import date

#Clase Controller
class Controller:
    """
    *********************************************
    * Controladore para la BD de la Biblioteca  *
    *********************************************
    """

    #Constructor de la Clase
    def __init__(self):
        self.model = Model()
        self.view = View()

    #Metodo para Inicializar todo el Proceso (Sistema)
    def start(self):
        self.view.start()
        self.main_menu()

    """
    ***********************
    * General controllers *
    ***********************
    """

    #Funcion del Menu
    def main_menu(self):
        o = '0'
        while o != '5':
            self.view.main_menu()
            self.view.option('5')
            o = input()
            if o == '1':
                self.users_of_menu()
            elif o == '2':
                self.autores_menu()
            elif o == '3':
                self.books_menu()
            elif o == '4':
                self.loan_menu()
            elif o == '5':
                self.view.end()
            else:
                self.view.not_valid_option()
        return

    #Medoto para Generar unas Listas para Cuando Necesitemos Llamar los Metodos de Actualizacion
    def update_lists(self, fs, vs):
        fields = []
        vals = []
        for f,v in zip(fs, vs):
            if v != '':
                fields.append(f+' = %s')
                vals.append(v)
        return fields,vals

    """
    ***************************
    * Controllers for Autores *
    ***************************
    """

    #Funcion del Menu de Autores
    def autores_menu(self):
        o = '0'
        while o != '8':
            self.view.autor_menu()
            self.view.option('8')
            o = input()
            if o == '1':
                self.create_autor()
            elif o == '2':
                self.read_a_autor()
            elif o == '3':
                self.read_all_autores()
            elif o == '4':
                self.read_autores_for_nacionality()
            elif o == '5':
                self.update_autor()
            elif o == '6':
                self.delete_autor()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return

    #Metodo Auxiliar para la Creacion de Autores
    #Esto le pide al Usuario Ingresar los Datos Requeridos para un Autor
    def ask_autor(self):
        self.view.ask('Nombre: ')
        name = input()
        self.view.ask('Apellido Paterno: ')
        sname1 = input()
        self.view.ask('Apellido Materno: ')
        sname2 = input()
        self.view.ask('Nacionalidad: ')
        nacionality = input()
        return [name,sname1,sname2,nacionality]
    
    #Metodo para Crear un Autor
    def create_autor(self):
        name, sname1, sname2, nacionality = self.ask_autor()
        out = self.model.create_autor(name,sname1,sname2,nacionality)
        if out == True:
            self.view.ok(name+' '+sname1, 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR EL AUTOR. REVISA.')
        return

    #Metodo para Leer un Autor
    def read_a_autor(self):
        self.view.ask('ID autor: ')
        id_autor = input()
        autor = self.model.read_a_autor(id_autor)
        if type(autor) == tuple:
            self.view.show_autor_header(' Datos del autor '+id_autor+' ')
            self.view.show_a_autor(autor)
            self.view.show_autor_midder()
            self.view.show_autor_footer()
        else:
            if autor == None:
                self.view.error('EL AUTOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL AUTOR. REVISA.')
        return

    #Metodo para la Lectura de todos los Autores
    def read_all_autores(self):
        autores = self.model.read_all_autores()
        if type(autores) == list:
            self.view.show_autor_header(' Todos los autores ')
            for autor in autores:
                self.view.show_a_autor(autor)
                self.view.show_autor_midder()
            self.view.show_autor_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS AUTORES. REVISA.')
        return

    #Metodo para Leer los Autores por Nacionalidad
    def read_autores_for_nacionality(self):
        self.view.ask('Nacionalidad: ')
        nacionality = input()
        autores = self.model.read_autores_nacionality(nacionality)
        if type(autores) == list:
            self.view.show_autor_header(' Autores con la nacionalidad '+nacionality+' ')
            for autor in autores:
                self.view.show_a_autor(autor)
                self.view.show_autor_midder()
            self.view.show_autor_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS AUTORES. REVISA.')
        return

    #Metodo para Actualizar los Autores
    def update_autor(self):
        self.view.ask('ID del autor a modificar: ')
        id_autor = input()
        autor = self.model.read_a_autor(id_autor)
        if type(autor) == tuple:
            self.view.show_autor_header(' Datos del autor '+id_autor+' ')
            self.view.show_a_autor(autor)
            self.view.show_autor_midder()
            self.view.show_autor_footer()
        else:
            if autor == None:
                self.view.error('EL AUTOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER AL AUTOR. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_autor()
        fields, vals = self.update_lists(['a_fname','a_sname1','a_sname2','a_nacionality'], whole_vals)
        vals.append(id_autor)
        vals = tuple(vals)
        out = self.model.update_autor(fields, vals)
        if out == True:
            self.view.ok(id_autor, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR AL AUTOR. REVISA.')
        return

    #Metodo para Borrar el Autor
    def delete_autor(self):
        self.view.ask('ID del autor a borrar: ')
        id_autor = input()
        count = self.model.delete_autor(id_autor)
        if count != 0:
            self.view.ok(id_autor, 'borro')
        else:
            if count == 0:
                self.view.error('EL AUTOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL AUTOR. REVISA.')
        return

    """
    *****************************
    * Controllers for the Users *
    *****************************
    """

    #Funcion del Menu de Usuarios
    def users_of_menu(self):
        o = '0'
        while o != '8':
            self.view.users_menu()
            self.view.option('8')
            o = input()
            if o == '1':
                self.create_user()
            elif o == '2':
                self.read_a_user()
            elif o == '3':
                self.read_all_users()
            elif o == '4':
                self.update_user()
            elif o == '5':
                self.delete_user()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return

    #Metodo Auxiliar para la Creacion de Usuarios
    #Esto le pide al Usuario Ingresar los Datos Requeridos para un Usuario
    def ask_user(self):
        self.view.ask('Nombre: ')
        name = input()
        self.view.ask('Apellido paterno: ')
        sname1 = input()
        self.view.ask('Apellido Materno: ')
        sname2 = input()
        self.view.ask('Direccion: ')
        direction = input()
        return [name,sname1,sname2,direction]

    #Metodo para Crear un Usuario
    def create_user(self):
        name, sname1, sname2, direction = self.ask_user()
        out = self.model.create_user(name,sname1,sname2,direction)
        if out == True:
            self.view.ok(name+' '+sname1, 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR EL USUARIO. REVISA.')
        return

    #Metodo para Leer un Usuario
    def read_a_user(self):
        self.view.ask('ID usuario: ')
        id_user = input()
        user = self.model.read_a_user(id_user)
        if type(user) == tuple:
            self.view.show_user_header(' Datos del usuario '+id_user+' ')
            self.view.show_a_user(user)
            self.view.show_user_midder()
            self.view.show_user_footer()
        else:
            if user == None:
                self.view.error('EL USUARIO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL USUARIO. REVISA.')
        return

    #Metodo para la Lectura de todos los Usuarios
    def read_all_users(self):
        users = self.model.read_all_users()
        if type(users) == list:
            self.view.show_user_header(' Todos los users ')
            for user in users:
                self.view.show_a_user(user)
                self.view.show_user_midder()
            self.view.show_user_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS USUARIOS. REVISA.')
        return

    #Metodo para Actualizar los Usuarios
    def update_user(self):
        self.view.ask('ID de usuario a modificar: ')
        id_user = input()
        user = self.model.read_a_user(id_user)
        if type(user) == tuple:
            self.view.show_user_header(' Datos del usuario '+id_user+' ')
            self.view.show_a_user(user)
            self.view.show_user_midder()
            self.view.show_user_footer()
        else:
            if user == None:
                self.view.error('EL USUARIO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL USUARIO. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_user()
        fields, vals = self.update_lists(['u_fname','u_sname1','u_sname2','u_direction'], whole_vals)
        vals.append(id_user)
        vals = tuple(vals)
        out = self.model.update_user(fields, vals)
        if out == True:
            self.view.ok(id_user, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL USUARIO. REVISA.')
        return

    #Metodo para Borrar el Usuario
    def delete_user(self):
        self.view.ask('ID del usuario a borrar: ')
        id_user = input()
        count = self.model.delete_user(id_user)
        if count != 0:
            self.view.ok(id_user, 'borro')
        else:
            if count == 0:
                self.view.error('EL USUARIO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL USUARIO. REVISA.')
        return

    """
    *************************
    * Controllers for Books *
    *************************
    """

    #Funcion del Menu para los Libros
    def books_menu(self):
        o = '0'
        while o != '7':
            self.view.books_menu()
            self.view.option('7')
            o = input()
            if o =='1':
                self.create_book()
            elif o == '2':
                self.read_a_book()
            elif o == '3':
                self.read_all_book()
            elif o == '4':
                self.update_book()
            elif o == '5':
                self.delete_book()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return

    #Metodo Auxiliar para la Creacion de Libros
    #Esto le pide al Usuario Ingresar los Datos Requeridos para un Libro
    def ask_book(self):
        self.view.ask('Titulo del libro: ')
        title = input()
        self.view.ask('Editorial: ')
        editorial = input()
        self.view.ask('Autor (Solo ID): ')
        autor = input()
        return [title,editorial,autor]
    
    #Metodo para Crear un Libro
    def create_book(self):
        title, editorial, autor = self.ask_book()
        out = self.model.create_book(title, editorial, autor)
        if out == True:
            self.view.ok(title+' '+editorial, 'agrego')#POSIBLE FALLO
        else:
            self.view.error('NO SE PUDO AGREGAR EL LIBRO. REVISA.')
        return

    #Metodo para Leer un Libro
    def read_a_book(self):
        self.view.ask('ID libro: ')
        id_book = input()
        book = self.model.read_a_book(id_book)
        if type(book) == tuple:
            self.view.show_book_header(' Datos del libro '+id_book+' ')
            self.view.show_a_book(book)
            self.view.show_book_midder()
            self.view.show_book_footer()
        else:
            if book == None:
                self.view.error('EL LIBRO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL LIBRO. REVISA.')
        return

    #Metodo para Leer todos los Libros
    def read_all_book(self):
        books = self.model.read_all_books()
        if type(books) == list:
            self.view.show_book_header(' Todos los libros ')
            for book in books:
                self.view.show_a_book(book)
                self.view.show_book_midder()
            self.view.show_book_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS LIBROS. REVISA.')
        return

    #Metodo para Actualizar un Libro
    def update_book(self):
        self.view.ask('ID del libro a modificar: ')
        id_book = input()
        book = self.model.read_a_book(id_book)
        if type(book) == tuple:
            self.view.show_book_header(' Datos del book '+id_book+' ')
            self.view.show_a_book(book)
            self.view.show_book_midder()
            self.view.show_book_footer()
        else:
            if book == None:
                self.view.error('EL LIBRO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL LIBRO. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_book()
        fields, vals = self.update_lists(['b_title','b_editorial','id_autor'], whole_vals)
        vals.append(id_book)
        vals = tuple(vals)
        out = self.model.update_book(fields, vals)
        if out == True:
            self.view.ok(id_book, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL LIBRO. REVISA.')
        return

    #Metodo para Borrar un Libro
    def delete_book(self):
        self.view.ask('ID del libro a borrar:')
        id_book = input()
        count = self.model.delete_book(id_book)
        if count != 0:
            self.view.ok(id_book, 'borro')
        else:
            if count == 0:
                self.view.error('EL LIBRO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL LIBRO. REVISA.')
        return

    """
    ************************
    * Controllers for loan *
    ************************
    """

    #Funcion de Menu para las Ordenes
    def loan_menu(self):
        o = '0'
        while o != '11':
            self.view.loan_menu()
            self.view.option('11')
            o = input()
            if o == '1':
                self.create_loan()
            elif o == '2':
                self.read_a_loan()
            elif o == '3':
                self.read_all_loan()
            elif o == '4':
                self.read_loan_user()
            elif o == '5':
                self.update_loan()
            elif o == '6':
                self.add_loan_details()
            elif o == '7':
                self.update_loan_details()
            elif o == '8':
                self.delete_loan_details()
            elif o == '9':
                self.delete_loan()
            elif o == '10':
                return
            else:
                self.view.not_valid_option()
        return

    #Metodo para Crear Prestamos
    def create_loan(self):
        self.view.ask('ID usuario: ')
        id_user = input()
        today = date.today()
        l_date = today.strftime('%y-%m-%d')
        id_loan = self.model.create_loan(id_user, l_date)
        if type(id_loan) == int:
            id_book = ' '
            while id_book != '':
                self.view.msg('---- Agrega libros al prestamo (deja vacio el id del libro para salir) ----')
                id_book = self.create_loan_details(id_book) #POSIBLE FALLO
            #self.model.update_loan(('id_loan = %s',),(id_loan))
            self.model.update_loan(('id_loan = %s',),(id_book, id_loan))
        else:
            self.view.error('NO SE PUDO CREAR EL PRESTAMO. REVISA.')
        return

    #Metodo para Leer un Prestamo
    def read_a_loan(self):
        self.view.ask('ID loan: ')
        id_loan = input()
        loan = self.model.read_a_loan(id_loan)
        if type(loan) == tuple:
            loan_details = self.model.read_loan_details(id_loan)
            if type(loan_details) != list and loan_details != None:
                self.view.error('PROBLEMA AL LEER EL PRESTAMO. REVISA.')
            else:
                self.view.show_loan_header(' Datos del prestamo '+id_loan+' ')
                self.view.show_loan(loan)
                self.view.show_loan_details_header()
                for loan_detail in loan_details:
                    self.view.show_a_loan_details(loan_detail)
                self.view.show_loan_details_footer()
                self.view.show_loan_footer()
                return loan
        else:
            if loan == None:
                self.view.error('EL PRESTAMO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL PRESTAMO. REVISA.')
        return

    #Metodo para Leer todos los Prestamos
    def read_all_loan(self):
        loans = self.model.read_all_loan()
        if type(loans) == list:
            self.view.show_loan_header(' Todos los prestamos ')
            for loan in loans:
                id_loan = loan[0]
                loan_details = self.model.read_loan_details(id_loan)
                if type(loan_details) != list and loan_details != None:
                    self.view.error('PROBLEMA AL LEER EL PRESTAMO '+id_loan+'. REVISA.')
                else:
                    self.view.show_loan(loan)
                    self.view.show_loan_details_header()
                    for loan_detail in loan_details:
                        self.view.show_a_loan_details(loan_detail)
                    self.view.show_loan_details_footer()
                    self.view.show_loan_total(loan)
                    self.view.show_loan_midder()
            self.view.show_loan_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS PRESTAMOS. REVISA.')
        return

    #Metodo para Leer los Prestamos de un Usuario
    def read_loan_user(self):
        self.view.ask('ID usuario: ')
        id_user = input()
        loans = self.model.read_loan_user(id_user)
        if type(loans) == list:
            self.view.show_loan_header(' Prestamos para el cliente '+id_user+' ')
            for loan in loans:
                id_loan = loan[0]
                loan_details = self.model.read_loan_details(id_loan)
                if type(loan_details) != list and loan_details != None:
                    self.view.error('PROBLEMA AL LEER EL PRESTAMO '+id_loan+'. REVISA.')
                else:
                    self.view.show_loan(loan)
                    self.view.show_details_header()#POSIBLE FALLO
                    for loan_detail in loan_details:
                        self.view.show_a_loan_details(loan_detail)
                    self.view.show_loan_details_footer()
                    self.view.show_loan_total(loan)
                    self.view.show_loan_midder()
            self.view.show_loan_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS PRESTAMOS. REVISA.')
        return

    #Metodo para Actualizar un Prestamo
    def update_loan(self):
        self.view.ask('ID del prestamo a modificar: ')
        id_loan = input()
        loan = self.model.read_a_loan(id_loan)
        if type(loan) == tuple:
            self.view.show_loan_header(' Datos del prestamo '+id_loan+' ')
            self.view.show_loan(loan)
            self.view.show_loan_footer()
        else:
            if loan == None:
                self.view.error('EL PRESTAMO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL PRESTAMO. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        self.view.ask('ID usuario: ')
        id_user = input()
        self.view.ask('Fecha (yyyy/mm/dd): ')
        l_date = input()
        whole_vals = [id_user, l_date]
        fields, vals = self.update_lists(['id_user','l_date'], whole_vals)
        vals.append(id_loan)
        vals = tuple(vals)
        out = self.model.update_loan(fields, vals)
        if out == True:
            self.view.ok(id_loan, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL PRESTAMO. REVISA.')
        return

    #Metodo para Borrar un Prestamo
    def delete_loan(self):
        self.view.ask('ID del prestamo a borrar: ')
        id_loan = input()
        count = self.model.delete_loan(id_loan)
        if count != 0:
            self.view.ok(id_loan, 'borro')
        else:
            if count == 0:
                self.view.error('EL PRESTAMO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL PRESTAMO. REVISA.')
        return

    """
    *********************************
    * Controllers for loan details *
    *********************************
    """

    #Metodo para Crear Prestamos con Detalles
    def create_loan_details(self, id_loan):
        self.view.ask('ID libros: ')
        id_book = input()
        if id_book != '':
            book = self.model.read_a_book(id_book)
            if type(book) == tuple:
                self.view.show_book_header(' Datos del libro '+id_book+' ')
                self.view.show_a_book(book)
                self.view.show_book_footer()
                self.view.ask('Cantidad: ')
                ld_amount = int(input())
                #od_total = ld_amount * book[4]
                out = self.model.create_loan_detail(id_loan, id_book, ld_amount)
                if out == True:
                    self.view.ok(book[1]+' '+book[2], 'agrego al prestamo')
                else:
                    if out.errno == 1062:
                        self.view.error('EL PRODUCTO YA ESTA EN EL PRESTAMO')
                    else:
                        self.view.error('NO SE PUDO AGREGAR EL LIBRO. REVISA.')
                    #od_total = 0.0
            else:
                if book == None:
                    self.view.error('EL LIBRO NO EXISTE')
                else:
                    self.view.error('PROBLEMA AL LEER EL LIBRO. REVISA.')
        return id_book
        #, od_total

    #Metodo Agregar detalles de Prestamo (Ya existente)
    def add_loan_details(self):
        loan = self.read_a_loan()
        if type(loan) == tuple:
            id_loan = loan[0]
            #l_total = loan[4]
            id_book = ' '
            while id_book != '':
                self.view.msg('---- Agrega libros a la orden (deja vacio el id del libro para salir) ----')
                id_loan, od_total = self.create_loan_details(id_loan)
                #o_total += od_total
            #self.model.update_order(('o_total = %s',),(o_total, id_loan))
        return

    #Metodo para Actualizar un Detalle de Prestamo
    def update_loan_details(self):
        loan = self.read_a_loan()
        if type(loan) == tuple:
            id_loan = loan[0]
            #o_total = loan[4]
            id_book = ' '
            while id_loan != '':
                self.view.msg('---- Modifica libros de la orden (deja vacio el id del libro para salir) ----')
                self.view.ask('ID libro: ')
                id_book = input()
                if id_book != '':
                    loan_detail = self.model.read_a_loan_detail(id_loan, id_book)
                    if type(loan_detail) == tuple:
                        #od_total_old = loan_detail[5]
                        #o_total -= od_total_old
                        book = self.model.read_a_book(id_book)
                        self.view.ask('Cantidad: ')
                        ld_amount = int(input())
                        #od_total = 1 * od_amount###
                        #o_total += od_total
                        #fields, whole_vals = self.update_lists(['od_amount','od_total'],[od_amount, od_total])
                        whole_vals.append(id_loan)
                        whole_vals.append(id_book)
                        self.model.update_loan_details(fields, whole_vals)
                        self.view.ok(id_book, 'actualizo en el prestamo')
                    else:
                        if loan_detail == None:
                            self.view.error('EL LIBRO NO EXISTE EN EL PRESTAMO')
                        else:
                            self.view.error('PROBLEMA AL ACTUALIZAR EL PRESTAMO. REVISA.')
            self.model.update_loan(('o_total = %s',),(o_total, id_loan))
        return

    #Metodo para Eliminar un detalle del Prestamo
    def delete_loan_details(self):
        loan = self.read_a_loan()
        if type(loan) == tuple:
            id_loan = loan[0]
            #o_total = loan[4]
            id_book = ' '
            while id_book != '':
                self.view.msg('---- Borra libros del prestamo (deja vacio el id del libro para salir) ----')
                self.view.ask('ID libro: ')
                id_book = input()
                if id_book != '':
                    loan_detail = self.model.read_a_loan_detail(id_loan, id_book)
                    count = self.model.delete_loan_detail(id_loan, id_book)
                    if type(loan_detail) == tuple and count != 0:
                        #od_total = loan_detail[5]
                        #o_total -= od_total
                        self.view.ok(id_book, 'borro del prestamo ')
                    else:
                        if loan_detail == None:
                            self.view.error('EL LIBRO NO EXISTE EN EL PRESTAMO')
                        else:
                            self.view.error('PROBLEMA AL BORRAR EL PRESTAMO. REVISA.')
            #self.model.update_loan(('o_total = %s',),(o_total, id_loan))
        return