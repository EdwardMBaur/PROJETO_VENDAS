with base as (
    SELECT DISTINCT 
    localidade
    FROM public.STG_VENDAS
),
concatenacao as (
    SELECT DISTINCT
    localidade,
    SPLIT_PART(localidade, '-', 1) as Pais,
    SPLIT_PART(localidade, '-', 2) as Continente
    FROM BASE
)

SELECT 
    ROW_NUMBER() OVER (ORDER BY localidade) AS ID_Localidade,
    Pais,
    Continente,
    localidade
    FROM concatenacao