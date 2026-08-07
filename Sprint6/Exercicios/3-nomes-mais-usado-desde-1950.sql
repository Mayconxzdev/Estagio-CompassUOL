WITH RankedNames AS (
  SELECT 
    nome,
    FLOOR(ano / 10) * 10 AS decada,
    COUNT(*) AS total,
    ROW_NUMBER() OVER (PARTITION BY FLOOR(ano / 10) * 10 ORDER BY COUNT(*) DESC) AS rank
  FROM meubanco.nomes_por_ano
  WHERE ano >= 1950
  GROUP BY nome, FLOOR(ano / 10) * 10
)
SELECT 
  decada,
  nome,
  total
FROM RankedNames
WHERE rank <= 3
ORDER BY decada, rank;
