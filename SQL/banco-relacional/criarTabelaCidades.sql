-- é relacao 1:n
-- criando a tabela cidades; usei if not exists para só criar se n existir a tabela no banco
CREATE TABLE IF NOT EXISTS cidades(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nome VARCHAR(250) NOT NULL,
    estado_id INT UNSIGNED NOT NULL,
    area DECIMAL (10,2),
    PRIMARY KEY (id),
    FOREIGN KEY (estado_id) REFERENCES estados(id)
);

-- CREATE TABLE IF NOT EXISTS testeDrop(
--     id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY
-- );

-- DROP TABELE IF EXISTS testeDrop;