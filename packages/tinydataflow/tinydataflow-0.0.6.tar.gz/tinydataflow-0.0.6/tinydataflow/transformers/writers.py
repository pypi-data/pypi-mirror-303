from tinydataflow.core import DataTransformer, DataTransformerException
from typing import List, Type, Union

       
class LineWriter(DataTransformer):
    '''
    The LineWriter appends a new line to the end of file provided by the user
    '''
    def __init__(self, output_file: str):
        self.__output_file = output_file
    
    @property
    def input_type(self) -> Type:        
        return str  # Espera uma linha para ser escrita no arquivo

    @property
    def output_type(self) -> Type:
        return str # retorna a linha escrita

    def setup(self, params: dict):
        """Opcionalmente, configurar o arquivo de saída (por exemplo, modo de abertura)."""
        open_mode = params.get('open_mode', 'a')  # 'a' para adicionar ou 'w' para sobrescrever
        if open_mode == 'w':
            with open(self.__output_file, open_mode) as f:
                pass  # Limpa o arquivo se estiver no modo 'w'
            
    def transform(self, input_data: str) -> str:

        try:
            with open(self.__output_file, 'a') as f:
                f.write(input_data + '\n')            
            return input_data
        except Exception as e:
            raise DataTransformerException(f"Failed to write {self.__output_file}: {str(e)}")

class FileWriter(DataTransformer):
    '''
    The FileWriter writes a list of lines to the end of a file provided by the user
    '''
    def __init__(self, output_file: str):
        self.__output_file = output_file
    
    @property
    def input_type(self) -> Type:        
        return list[str]  # Espera uma lista de strings para ser escrita no arquivo

    @property
    def output_type(self) -> Type:
        return str # retorna o nome do arquivo

    def setup(self, params: dict):
        """Opcionalmente, configurar o arquivo de saída (por exemplo, modo de abertura)."""
        open_mode = params.get('open_mode', 'a')  # 'a' para adicionar ou 'w' para sobrescrever
        if open_mode == 'w':
            with open(self.__output_file, open_mode) as f:
                pass  # Limpa o arquivo se estiver no modo 'w'
            
    def transform(self, input_data: str) -> str:
        try:
            with open(self.__output_file, 'a') as f:
                for line in input_data:
                    f.write(line + '\n')
        except Exception as e:
            raise DataTransformerException(f"Erro ao escrever no arquivo {self.__output_file}: {str(e)}")
        return self.__output_file
