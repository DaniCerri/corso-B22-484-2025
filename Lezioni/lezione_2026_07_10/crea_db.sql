-- crea il db gestionale per l'ecommerce
CREATE DATABASE IF NOT EXISTS gestionale2026;
-- crea lo user solo se non esiste già
CREATE USER db484user@localhost IDENTIFIED BY 'db2026!';
-- assegno i privilegi sul db gestionale per lo user
GRANT ALL ON gestionale2026.* TO db484user@localhost;