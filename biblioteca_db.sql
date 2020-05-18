#Creando la Base de Datos
CREATE DATABASE IF NOT EXISTS biblioteca_db;

#Usando la Base de Datos
USE biblioteca_db;

CREATE TABLE IF NOT EXISTS autores
(
	id_autor INT NOT NULL AUTO_INCREMENT,
    a_fname VARCHAR(20) NOT NULL,
    a_sname1 VARCHAR(20) NOT NULL,
    a_sname2 VARCHAR(20),
    a_nacionality VARCHAR(30) NOT NULL,
    PRIMARY KEY(id_autor)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS book
(
	id_book INT NOT NULL AUTO_INCREMENT,
    b_title VARCHAR(45) NOT NULL,
    b_editorial VARCHAR(45) NOT NULL,
    id_autor INT,
    PRIMARY KEY(id_book),
    CONSTRAINT fk_id_autor FOREIGN KEY(id_autor)
		REFERENCES autores(id_autor)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS users
(
	id_user INT NOT NULL AUTO_INCREMENT,
    u_fname VARCHAR(20) NOT NULL,
    u_sname1 VARCHAR(20) NOT NULL,
    u_sname2 VARCHAR(20),
    u_direction VARCHAR(50) NOT NULL,
    PRIMARY KEY(id_user)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS loan
(
	id_loan INT NOT NULL AUTO_INCREMENT,
    id_user INT,
    l_date DATE NOT NULL,
    PRIMARY KEY(id_loan),
	CONSTRAINT fk_id_user FOREIGN KEY(id_user)
		REFERENCES users(id_user)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS loan_details
(
	id_loan INT NOT NULL,
    id_book INT,
    ld_amount INT NOT NULL,
    PRIMARY KEY(id_loan, id_book),
	CONSTRAINT fk_id_loan FOREIGN KEY(id_loan)
		REFERENCES loan(id_loan)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
	CONSTRAINT fk_id_book FOREIGN KEY(id_book)
		REFERENCES book(id_book)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)ENGINE = INNODB;
