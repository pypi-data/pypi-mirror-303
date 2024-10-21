from tinydataflow.core import DataConnector, DataConnectorException
from typing import List, Type
from pathlib import Path
import os
import csv


class FileSelector(DataConnector):
    
    def __init__(self, from_path: str, file_ext: str = '*.*'):
        self.from_path = from_path
        self.file_ext = file_ext
    
    @property
    def output_type(self) -> Type:
        return list # Gera uma lista de nomes de arquivos a partir de um diretorio
        
    def read(self) -> list:
        try:
            file_list = []

            if os.path.isdir(self.from_path):                
                for file_path in Path(self.from_path).rglob(self.file_ext):
                    file_list.append(str(file_path)) # file_list.append(file_path) 
            return file_list
        except IOError as e:
            raise DataConnectorException(e.message)
        finally:
            self.close()
        
class FileReader(DataConnector):
    
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


class CSVLineReader(DataConnector):
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