from tinydataflow.core import DataTransformer, DataTransformerException
from typing import List, Type, Union


class ListToDict(DataTransformer):
    '''
    The ListToDict transforms a list of strings into a dictionary with the specified keys in a order provided by the user.
    '''
    
    def __init__(self, k_names: list[str]):
        """
        Creates a ListToDictTransformer object.

        Args:
            k_names: The list of keys in the order they should be used to create the dictionary from a list of strings.
        """
        self.__k_names = k_names  
    
    @property
    def input_type(self) -> Type:
        return list[str]  # Espera uma lista de strings
    
    @property
    def output_type(self) -> Type:
        return dict[str]  # Converte em dicinário com valores em strings

    def transform(self, input_data: list[str]) -> dict[str]:
        """
        Transforms a list of strings into a dictionary with the specified keys in a order provided by the user.

        Args:
            input_data: A list of strings to be transformed into a dictionary.

        Returns:
            The dictionary with the specified keys and values from the input_data list.
        """
        return dict(zip(self.__k_names, input_data))

    def setup(self, config: dict):
        pass  # Nenhuma configuração necessária para este exemplo
