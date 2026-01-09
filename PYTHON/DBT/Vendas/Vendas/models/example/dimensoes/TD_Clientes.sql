with base as (
    SELECT DISTINCT 
    NOME_CLIENTE
    FROM public.STG_VENDAS
),
concatenacao as (
    SELECT DISTINCT
    NOME_CLIENTE,
    SPLIT_PART(NOME_CLIENTE, ',', 1) as Sobrenome,
    SPLIT_PART(NOME_CLIENTE, ',', 2) as Primeiro_NM
    FROM BASE
)

SELECT 
    ROW_NUMBER() OVER (ORDER BY NOME_CLIENTE) AS ID_Cliente,
    Primeiro_NM || ' ' || Sobrenome  as NM_CLIENTE_COMPLETO,
    Primeiro_NM,
    Sobrenome,
    NOME_CLIENTE
    FROM concatenacao