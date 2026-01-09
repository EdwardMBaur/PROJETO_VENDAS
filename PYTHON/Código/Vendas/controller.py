from Configs import paths
from Extract.extract import Extract
from Transform.transform import Transform
from Load.load import Load

class ImportacaoPlanilhaController:
    @staticmethod
    def run():
        dataframe = Extract.import_data(paths.file_path)
        dataframe = Transform.transform_data(dataframe)
        Load.load_data(dataframe)

if __name__ == "__main__":

    ImportacaoPlanilhaController.run()