-- USANDO AGREGAÇÕES E COLOCANDO EM GRUPO (GROUP BY REGIAO)

-- SOMA
select 
	regiao as 'Regiao',
    sum(populacao) as Total
from estados
group by regiao
order by Total desc

-- MEDIA
select 
    avg(populacao) as MediaTotal
from estados

