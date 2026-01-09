with base as (
    SELECT DISTINCT 
    produto,
    categoria,
    preco_unitario,
    custo_unitario,
    marca
    FROM public.STG_VENDAS
)
SELECT 
    ROW_NUMBER() OVER (ORDER BY produto) AS ID_Item,
    produto,
    categoria,
    marca,
    preco_unitario,
    custo_unitario,
    (preco_unitario - custo_unitario) AS LUCRO
    FROM base