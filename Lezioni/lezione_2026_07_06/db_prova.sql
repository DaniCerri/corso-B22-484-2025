-- ==========================================
-- 1. CREAZIONE DELLE TABELLE (DDL)
-- ==========================================

-- Tabella Studenti
CREATE TABLE studenti (
    id_studente INT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    cognome VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    data_registrazione DATE NOT NULL
);

-- Tabella Corsi
CREATE TABLE corsi (
    id_corso INT PRIMARY KEY,
    titolo VARCHAR(100) NOT NULL,
    livello VARCHAR(20) CHECK (livello IN ('Base', 'Intermedio', 'Avanzato')),
    prezzo DECIMAL(6, 2) NOT NULL,
    durata_ore INT NOT NULL
);

-- Tabella Moduli (Relazione 1:N con Corsi)
CREATE TABLE moduli (
    id_modulo INT PRIMARY KEY,
    corso_id INT NOT NULL,
    titolo_modulo VARCHAR(100) NOT NULL,
    numero_ordine INT NOT NULL,
    FOREIGN KEY (corso_id) REFERENCES corsi(id_corso) ON DELETE CASCADE
);

-- Tabella Iscrizioni (Relazione N:M tra Studenti e Corsi)
CREATE TABLE iscrizioni (
    id_iscrizione INT PRIMARY KEY,
    studente_id INT NOT NULL,
    corso_id INT NOT NULL,
    data_iscrizione DATE NOT NULL,
    completato BOOLEAN DEFAULT FALSE,
    voto_finale INT CHECK (voto_finale BETWEEN 18 AND 30),
    FOREIGN KEY (studente_id) REFERENCES studenti(id_studente) ON DELETE CASCADE,
    FOREIGN KEY (corso_id) REFERENCES corsi(id_corso) ON DELETE CASCADE,
    UNIQUE(studente_id, corso_id) -- Evita che uno studente si iscriva due volte allo stesso corso
);

-- ==========================================
-- 2. POPOLAMENTO DELLE TABELLE (DML)
-- ==========================================

-- Inserimento Studenti
INSERT INTO studenti (id_studente, nome, cognome, email, data_registrazione) VALUES
(1, 'Marco', 'Rossi', 'marco.rossi@email.it', '2025-09-10'),
(2, 'Laura', 'Bianchi', 'laura.bianchi@email.it', '2025-10-01'),
(3, 'Alessandro', 'Verdi', 'ale.verdi@email.it', '2025-11-15'),
(4, 'Giulia', 'Neri', 'giulia.neri@email.it', '2026-01-20');

-- Inserimento Corsi
INSERT INTO corsi (id_corso, titolo, livello, prezzo, durata_ore) VALUES
(101, 'Python per il Back-End e API', 'Intermedio', '149.90', 40),
(102, 'Sviluppo Web con React', 'Base', '129.90', 35),
(103, 'Architettura dei Database e SQL', 'Avanzato', '189.50', 50);

-- Inserimento Moduli dei Corsi
INSERT INTO moduli (id_modulo, corso_id, titolo_modulo, numero_ordine) VALUES
(1, 101, 'Introduzione a FastAPI e Routing', 1),
(2, 101, 'Integrazione con SQLAlchemy e ORM', 2),
(3, 101, 'Autenticazione JWT e Sicurezza', 3),
(4, 102, 'Componenti, Props e State', 1),
(5, 102, 'Gestione degli Hooks e API Fetching', 2),
(6, 103, 'Progettazione Concettuale ed E-R', 1),
(7, 103, 'Query Complesse, JOIN e Indici', 2);

-- Inserimento Iscrizioni (Studenti ai Corsi)
INSERT INTO iscrizioni (id_iscrizione, studente_id, corso_id, data_iscrizione, completato, voto_finale) VALUES
(1, 1, 101, '2025-09-12', TRUE, 28),
(2, 1, 103, '2025-11-01', FALSE, NULL),
(3, 2, 102, '2025-10-05', TRUE, 30),
(4, 3, 101, '2025-11-20', TRUE, 25),
(5, 3, 102, '2026-01-10', FALSE, NULL),
(6, 4, 103, '2026-02-01', FALSE, NULL);