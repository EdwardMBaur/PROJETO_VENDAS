import pandas as pd
import datetime as dt
import numpy as np

class Transform:
    @staticmethod
    def transform_data(dataframe: pd.DataFrame) -> pd.DataFrame:
        try:
            print('[TRANSFORM] Iniciando limpeza profunda...')

            pd.set_option('future.no_silent_downcasting', True)

            dataframe = dataframe.replace(r'^\s*$', np.nan, regex=True)
            dataframe = dataframe.dropna(axis=1, how='all')
            dataframe = dataframe.loc[:, ~dataframe.columns.str.contains('^Unnamed')]
            dataframe.columns = dataframe.columns.str.strip()

            cols_texto = dataframe.select_dtypes(include=['object']).columns
            for col in cols_texto:
                dataframe[col] = dataframe[col].astype(str).str.strip()

            dataframe = dataframe.dropna(axis=0, how='all')

            print('[TRANSFORM] Iniciando transformação de datas...')

            dataframe['Data da Venda'] = pd.to_datetime(dataframe['Data da Venda'], format='mixed', dayfirst=True, errors='coerce')

            print(f'[TRANSFORM] Removendo colunas vazias...')
            dataframe = dataframe.dropna(axis=1, how='all')

            print(f'[TRANSFORM] Renomeando as colunas...')
            rename_map = {
                "Data da Venda" : "DT_VENDA",
                "Produto":"PRODUTO",
                "Categoria":"CATEGORIA",
                "PrecoUnitario":"PRECO_UNITARIO",
                "Custo Unitário":"CUSTO_UNITARIO",
                "Marca":"MARCA",
                "Qtd. Vendida":"QTD_VENDIDA",
                "Nome Cliente":"NOME_CLIENTE",
                "Localidade":"LOCALIDADE",
            }
            dataframe.rename(columns=rename_map, inplace=True)

            print('[TRANSFORM] Sanitizando dados para SQL...')

            dataframe = dataframe.astype(object)

            dataframe = dataframe.where(pd.notnull(dataframe), None)
            
            return dataframe
            
        except Exception as e:
            print(f'[TRANSFORM] Erro na transformação: {e}')
            raise e