INSERT INTO cidades(nome, area, estado_id)
VALUES(	
		'Carinhanha',
        920.9,
        (select id from estados where sigla = 'BA')
);

INSERT INTO cidades(nome, area, estado_id)
VALUES (
		'Cidade do Alagoas 1',
        780.9,
        (select id from estados where sigla = 'AL')
),
(
		'Cidade do Alagoas 2',
        780.9,
        (select id from estados where sigla = 'AL')
);
        
		
select * from cidades