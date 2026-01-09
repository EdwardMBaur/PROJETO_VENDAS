import pandas as pd
import os 

class Extract:
     @staticmethod
     def import_data(file_path: str) -> pd.DataFrame:
          try:
               if not file_path:
                    print('[EXTRACT] arquivo não encontrado.')
                    raise ValueError("File path cannot be empty")
               
               print(f'[EXTRACT] verificando arquivos no {file_path}')
               if not file_path.endswith((".xlsx")):
                    print('[EXTRACT] formato do arquivo não suportavel')
                    raise ValueError("Unsupported file format. Please provide an Excel file.")
               
               if not os.path.exists(file_path):
                    print('[EXTRACT] arquivo não encontrado')
                    raise FileNotFoundError(f"The file {file_path} does not exist.")
               
               #verificações se tem o arquivo necessário

               dataframe = pd.read_excel(file_path)

               if dataframe.empty:
                    print('[EXTRACT] Os dados estão vazios')
                    raise ValueError("The imported file is empty or contains no data.")
               
               print('importação feita com sucesso')

               dataframe.to_csv('extração_vendas', index=False)

               return dataframe
          
          except Exception as e:
               print(f'[EXTRACT] Exception occurred: {e}')
               raise ValueError(f"Failed to import data from {file_path}: {e}")
               

