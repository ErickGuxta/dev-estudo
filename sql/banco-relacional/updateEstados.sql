-- atualizar
UPDATE estados SET nome = 'Nome Bahia ATUALIZADO' WHERE sigla = 'BA'
UPDATE estados SET regiao = 'Norte' WHERE sigla = 'AM'

-- selecionando
SELECT nome FROM estados WHERE sigla = 'BA'

-- COMO SETAR APELIDOS
SELECT est.nome FROM estados est WHERE sigla = 'AL'

