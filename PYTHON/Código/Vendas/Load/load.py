import pandas as pd
import psycopg2 as pg
from psycopg2.extras import execute_values 
from Configs.settings import get_db_config 

class Load:
    @staticmethod
    def load_data(dataframe: pd.DataFrame):
        print("[LOAD] Conectando ao banco de dados")
        conn = None
        try:
            db_config = get_db_config()
            conn = pg.connect(**db_config)
            cursor = conn.cursor()

            df_to_load = dataframe.where(pd.notnull(dataframe), None)

            data_to_insert = [tuple(x) for x in df_to_load.to_numpy()]

            sql_insert = """
                INSERT INTO PUBLIC.STG_VENDAS (
                    DT_VENDA, PRODUTO, CATEGORIA, PRECO_UNITARIO, 
                    CUSTO_UNITARIO, MARCA, QTD_VENDIDA, NOME_CLIENTE, LOCALIDADE
                ) VALUES %s
            """

            print(f"[LOAD] Inserindo {len(data_to_insert)} linhas com execute_values...")

            execute_values(cursor, sql_insert, data_to_insert)

            conn.commit()
            print(f"[LOAD] SUCESSO! {len(data_to_insert)} linhas inseridas.")

        except Exception as e:
            if conn: conn.rollback()
            print(f"[ERROR] {e}")
            raise
        finally:
            if conn:
                cursor.close()
                conn.close()