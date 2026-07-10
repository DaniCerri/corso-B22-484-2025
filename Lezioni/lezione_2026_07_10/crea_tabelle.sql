-- Clienti, Ordini, Articoli, Impiegati, Uffici, Categorie, Ordini_dettaglio
CREATE TABLE clienti(
	id INT AUTO_INCREMENT PRIMARY KEY,
    cognome VARCHAR(50) NOT NULL,
    nome VARCHAR(40),
    telefono VARCHAR(15),
    email VARCHAR(100) NOT NULL UNIQUE,
    indirizzo VARCHAR(100) NOT NULL,
    citta VARCHAR(50) NOT NULL,
    provincia CHAR(2) NOT NULL,
    regione VARCHAR(30) NOT NULL,
    credito SMALLINT DEFAULT 0
);

CREATE TABLE uffici(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(30) NOT NULL,
    telefono VARCHAR(30),
    citta VARCHAR(50),
    regione VARCHAR(30)
);

CREATE TABLE impiegati(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    cognome VARCHAR(50) NOT NULL,
    ruolo VARCHAR(50) NOT NULL,
    responsabile_id INT,
    stipendio DECIMAL(6,2), -- 9999,99
    ufficio_id INT,
    FOREIGN KEY(ufficio_id) REFERENCES uffici(id)
    ON UPDATE CASCADE ON DELETE SET NULL
);

CREATE TABLE ordini(
	id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT NOT NULL,
    impiegato_id INT,
    data_ordine DATETIME,
    indirizzo_spedizione VARCHAR(255),
    stato_consegna ENUM('da spedire','spedito','consegnato') DEFAULT 'da spedire',
    FOREIGN KEY(cliente_id) REFERENCES clienti(id),
    FOREIGN KEY(impiegato_id) REFERENCES impiegati(id) ON UPDATE CASCADE ON DELETE SET NULL
);

CREATE TABLE categorie(
	id INT AUTO_INCREMENT PRIMARY KEY,
    categoria VARCHAR(50),
    descrizione VARCHAR(255)
);

CREATE TABLE articoli(
	id INT AUTO_INCREMENT PRIMARY KEY,
    prezzo DECIMAL(6,2) NOT NULL,
    rimanenza TINYINT UNSIGNED,
    categoria_id INT,
    FOREIGN KEY(categoria_id) REFERENCES categorie(id)ON UPDATE CASCADE ON DELETE SET NULL
);

CREATE TABLE ordini_dettaglio(
	ordine_id INT NOT NULL,
    articolo_id INT NOT NULL,
    quantita TINYINT UNSIGNED NOT NULL,
    prezzo DECIMAL(6,2) NOT NULL,
	FOREIGN KEY(ordine_id) REFERENCES ordini(id)ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY(articolo_id) REFERENCES articoli(id),
    PRIMARY KEY(ordine_id, articolo_id)
);