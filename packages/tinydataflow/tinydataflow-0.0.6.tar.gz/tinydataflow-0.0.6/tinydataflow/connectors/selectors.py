from tinydataflow.core import DataConnector, DataConnectorException
from typing import List, Type
from pathlib import Path
import os


class FileListSelector(DataConnector):
    '''
    The FileListSelector returns a list of files in a directory from a given path and file extension to be selected.
    '''    
    def __init__(self, from_path: str, file_ext: str = '*.*'):
        self.from_path = from_path
        self.file_ext = file_ext
    
    @property
    def output_type(self) -> Type:
        return list[str] # Gera uma lista de nomes de arquivos a partir de um diretorio
        
    def read(self) -> list[str]:
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

class FileSelector(DataConnector):
    '''
    The FileSelector returns a file from a given path and file extension to be selected. 
    It can be iterated and read sequentially to be transmitted to the next transformer in each iteration
    '''
    
    def __init__(self, from_path: str, file_ext: str = '*.*'):
        self.from_path = from_path
        self.file_ext = file_ext
        self.selection = None
        self.current_index = 0
    
    @property
    def output_type(self) -> Type:
        return str # Retorna o caminho do arquivo selecionado

    def _select_files(self):
        """
        Selects all files in the given directory matching the given file extension.
        If no files are found, sets the end of file flag to True.
        """
        
        self.selection = []
        if os.path.isdir(self.from_path):                
            for file_path in Path(self.from_path).rglob(self.file_ext):
                self.selection.append(str(file_path)) # file_list.append(file_path) 
        if not self.selection:
            self.set_eof(True)
        
    def read(self) -> str:
        
        if self.selection is None:
            self._select_files()

        if self.current_index < len(self.selection):
            file_path = os.path.join(self.from_path, self.selection[self.current_index])
            self.current_index += 1
            return file_path
        else:
            self.set_eof(True)
            return None
 