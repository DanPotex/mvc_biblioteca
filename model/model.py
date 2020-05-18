from mysql import connector

class Model:
    """
    ********************************************
    * A data model with MySQL for a library DB *
    ********************************************
    """

    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()

    def read_config_db(self):
        d = {}
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key] = val
        return d

    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()

    def close_db(self):
        self.cnx.close()

    """
    **********************
    * Metodos de Autores *
    **********************
    """

    #Metodo para Crear Autores
    def create_autor(self, name, sname1, sname2, nacionality):
        try:
            sql = 'INSERT INTO autores (`a_fname`, `a_sname1`, `a_sname2`, `a_nacionality`) VALUES (%s, %s, %s, %s)'
            vals = (name, sname1, sname2, nacionality)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    #Metodo para Leer un Autor
    def read_a_autor(self, id_autor):
        try:
            sql = 'SELECT * FROM autores WHERE id_autor = %s'
            vals = (id_autor,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    #Metodo para Leer todos los Autores
    def read_all_autores(self): #Caution with large amount of data
        try:
            sql = 'SELECT * FROM autores'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    #Metodo para Leer a los Autores por Nacionalidad
    def read_autores_nacionality(self, nacionality):
        try:
            sql = 'SELECT * FROM autores WHERE a_nacionality = %s'
            vals = (nacionality,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    #Metodo para Actualizar un Autor
    def update_autor(self, fields, vals):
        try:
            sql = 'UPDATE autores SET '+','.join(fields)+' WHERE id_autor = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #Metodo para Borrar Autor
    def delete_autor(self, id_autor):
        try:
            sql = 'DELETE FROM autores WHERE id_autor = %s'
            vals = (id_autor,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ****************
    * Book methods *
    ****************
    """

    #Metodo para Crear un Libro
    def create_book(self, title, editorial, autor):
        try:
            sql = 'INSERT INTO book (`b_title`, `b_editorial`, `id_autor`) VALUES (%s, %s, %s)'
            vals = (title, editorial, autor)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #Metodo para Leer un Libro
    def read_a_book(self, id_book):
        try:
            sql = 'SELECT book.*,autores.a_fname,autores.a_nacionality FROM book JOIN autores ON book.id_autor = autores.fname and book.id_book = %s'
            vals = (id_book,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    #Metodo para Leer todos los Libros
    def read_all_books(self): #Caution with large amount of data
        try:
            sql = 'SELECT book.*,autores.a_fname,autores.a_nacionality FROM book JOIN autores ON book.id_autor = autores.id_autor'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    #Metodo para Actualizar un Libro
    def update_book(self, fields, vals):
        try:
            sql = 'UPDATE book SET '+','.join(fields)+' WHERE id_book = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #Metodo para Eliminar un Libro
    def delete_book(self, id_book):
        try:
            sql = 'DELETE FROM book WHERE id_book = %s'
            vals = (id_book,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    *****************
    * User methods  *
    *****************
    """

    #Metodo para Crear Usuarios
    def create_user(self, name, sname1, sname2, direction):
        try:
            sql = 'INSERT INTO users (`u_fname`, `u_sname1`, `u_sname2`, `u_direction`) VALUES (%s, %s, %s, %s)'
            vals = (name, sname1, sname2, direction)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #Metodo para Leer un Usuario
    def read_a_user(self, id_user):
        try:
            sql = 'SELECT * FROM users WHERE id_user = %s'
            vals = (id_user,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    #Metodo para Leer todos los Usuarios
    def read_all_users(self): #Caution with large amount of data
        try:
            sql = 'SELECT * FROM users'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    #Metodo para Actualizar un Usuario
    def update_user(self, fields, vals):
        try:
            sql = 'UPDATE users SET '+','.join(fields)+' WHERE id_user = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #Metodo para Borrar un Usuario
    def delete_user(self, id_user):
        try:
            sql = 'DELETE FROM user WHERE id_user = %s'
            vals = (id_user,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ****************
    * Loan methods *
    ****************
    """

    #Metodo para Crear un Prestamo
    def create_loan(self, id_user, date):
        try:
            sql = 'INSERT INTO loan (`id_user`, `l_date`) VALUES ( %s, %s)'
            vals = (id_user, date)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            id_loan = self.cursor.lastrowid
            return id_loan
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #Metodo para Leer un Prestamo
    def read_a_loan(self, id_loan):
        try:
            sql = 'SELECT loan.*, users.*, FROM loan JOIN users ON users.id_user = loan.id_user and loan.id_loan = %s'
            vals = (id_loan,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    #Metodo para Leer todos los Prestamos
    def read_all_loan(self): #Caution with large amount of data
        try:
            sql = 'SELECT loan.*, users.* FROM loan JOIN users ON users.id_user = loan.id_user'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    #Metodo para Leer todos los Prestamos de un Usuario
    def read_loan_user(self, id_user):
        try:
            sql = 'SELECT loan.*, users.* FROM loan JOIN users ON users.id_user = loan.id_users and loan.id_user = %s'
            vals = (id_user,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    #Metodo para Actualizar un Prestamo
    def update_loan(self, fields, vals):
        try:
            sql = 'UPDATE loan SET '+','.join(fields)+' WHERE id_loan = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #Metodo para Eliminar un Prestamo
    def delete_loan(self, id_loan):
        try:
            sql = 'DELETE FROM loan WHERE id_loan = %s'
            vals = (id_loan,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    *************************
    * Loan Details methods  *
    *************************
    """

    #Metodo para Crear un Detalle de Prestamo
    def create_loan_detail(self, id_loan, id_book, ld_amount):
        try:
            sql = 'INSERT INTO loan_details (`id_loan`, `id_book`, `ld_amount`) VALUES (%s, %s, %s)'
            vals = (id_loan, id_book, ld_amount)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #Metodo para Leer un Prestamo con los Detalles
    def read_a_loan_detail(self, id_loan, id_book):
        try:
            sql = 'SELECT book.id_book, book.b_title, book.b_editorial, loan_details.ld_amount FROM loan_details JOIN book ON loan_details.id_book = book.id_book and loan_details.id_loan = %s and loan_details.id_book = %s'
            vals = (id_loan, id_book)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    #Metodo para Leer todos los Detalles de un Prestamo
    def read_loan_details(self, id_order):
        try:
            sql = 'SELECT book.id_book, book.b_title, book.b_editorial, book.id_autor, loan_details.id_amount FROM loan_details JOIN book ON loan_details.id_book = book.id_book and loan_details.id_loan = %s'
            vals = (id_loan,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    #Metodo para Actualizar los Detalles de un Prestamo
    def update_loan_details(self, fields, vals):
        try:
            sql = 'UPDATE loan_details SET '+','.join(fields)+' WHERE id_loan = %s and id_book = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #Metodo para Eliminar los Detalles de un Prestamo
    def delete_loan_detail(self, id_loan, id_book):
        try:
            sql = 'DELETE FROM loan_details WHERE id_loan = %s and id_book = %s'
            vals = (id_loan, id_book)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err