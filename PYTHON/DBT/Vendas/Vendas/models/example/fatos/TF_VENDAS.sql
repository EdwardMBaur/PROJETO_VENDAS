WITH stg AS (
    SELECT * FROM public.STG_VENDAS
),

clientes AS (
    SELECT * FROM {{ ref('TD_Clientes') }}
),

locais AS (
    SELECT * FROM {{ ref('TD_Localidade') }}
),

itens AS (
    SELECT * FROM {{ ref('TD_Item') }}
)

SELECT
    ROW_NUMBER() OVER (ORDER BY stg.DT_VENDA) AS ID_Venda,
    stg.DT_VENDA,
    itens.ID_Item,
    clientes.ID_Cliente,
    locais.ID_Localidade,
    stg.QTD_VENDIDA 
FROM stg
LEFT JOIN clientes ON stg.NOME_CLIENTE = clientes.NOME_CLIENTE
LEFT JOIN locais   ON stg.LOCALIDADE   = locais.LOCALIDADE
LEFT JOIN itens    ON stg.PRODUTO      = itens.produto 
                  AND stg.MARCA        = itens.marca
                  AND stg.PRECO_UNITARIO = itens.preco_unitario
                  AND stg.custo_unitario = itens.custo_unitario