from tinydataflow.core import DataConnector, DataConnectorException
from typing import List, Type
from pathlib import Path
import csv

    
class FileReader(DataConnector):
    '''
    The FileReader returns a list of lines from a given text file.
    '''
    
    def __init__(self, filename: str):
        self.filename = filename
   
    @property
    def output_type(self) -> Type:
        return list[str] # Gera uma lista de linhas de um arquivo TXT
    
    def read(self) -> list[str]:
        try:
            if self.filename is not None:
                with open(self.filename, 'r') as f:
                    return f.readlines()
            raise DataConnectorException(f'Nenhum arquivo informado no arquivo de configuração: parâmetro [{self.filename}]')
        except IOError as e:
            raise DataConnectorException(e.message)
        finally:
            self.close()


class LineReader(DataConnector):
    '''
    The LineReader reads a line from a given text file provided in the constructor.
    Each line can be readed and iterated sequentially to be transmitted to the next transformer in each iteration
    '''
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.file = None        
    
    def setup(self, params):
        """Abre o arquivo de texto no modo leitura."""
        try:
            self.file = open(self.file_path, 'r', encoding=params.get('encoding', 'utf-8'))
        except FileNotFoundError:
            raise DataConnectorException(f"Arquivo {self.file_path} não encontrado.")    
    
    @property
    def output_type(self) -> Type:
        """Retorna o tipo de saída que este conector gera (lista de strings)."""
        return str  # Uma linha de um arquivo TXT
        
    def read(self) -> str:
        """Lê uma linha do arquivo de texto."""
        if self.file is None:
            raise DataConnectorException("Arquivo não foi aberto corretamente.")
        
        line = self.file.readline()
        
        if line:
            return line.strip()  # Retorna a linha sem os espaços extras
        else:
            self.set_eof(True)  # Marca o fim do arquivo
            return None

    def close(self):
        """Fecha o arquivo."""
        if self.file:
            self.file.close()
        self.set_eof(True)


class CSVReader(DataConnector):
    '''
    The CSVReader reads a line from a given CSV file provided in the constructor.
    Each line can be readed and iterated sequentially to be transmitted to the next transformer in each iteration
    '''
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.file = None
        self.reader = None
    
    @property
    def output_type(self) -> Type:
        """Retorna o tipo de saída que este conector gera (lista de strings)."""
        return list[str]  # Cada linha lida será uma lista de strings
    
    def setup(self, params: dict):
        """Abre o arquivo CSV e inicializa o leitor CSV."""
        try:
            self.file = open(self.file_path, mode='r', newline='', encoding=params.get('encoding', 'utf-8'))
            self.reader = csv.reader(self.file, delimiter=params.get('delimiter', ';'))
        except FileNotFoundError:
            raise DataConnectorException(f"Arquivo {self.file_path} não encontrado.")
    
    def read(self) -> list[str]:
        """Lê uma linha do arquivo CSV."""
        if self.reader is None:
            raise DataConnectorException("O arquivo CSV não foi aberto corretamente.")
        
        try:
            line = next(self.reader)
            return line
        except StopIteration:
            self.set_eof(True)
            return []
    
    def close(self):
        """Fecha o arquivo CSV."""
        super().close()
        if self.file:
            self.file.close()