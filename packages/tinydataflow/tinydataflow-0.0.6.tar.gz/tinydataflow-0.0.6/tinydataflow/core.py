from abc import ABC, abstractmethod
from typing import Union, List, Type


class DataFlowStrategy(ABC):
    
    @property
    def input_type(self) -> Type:
        return None
  
    @property
    def output_type(self) -> Type:
        return None
    
    def setup(self, params: dict):
        pass
 
        
class DataConnector(DataFlowStrategy):

    __eof = False

    @abstractmethod
    def read(self) -> any:
        """Lê a fonte de dados."""        
        pass
    
    def eof(self):
        return self.__eof
    
    def set_eof(self, eof: bool):
        self.__eof = eof

    def close(self):
        """Fecha a conexão com a fonte de dados."""
        self.set_eof(True)


class DataConnectorException(Exception):
    pass

# Definindo a interface comum para as estratégias com input/output types
class DataTransformer(DataFlowStrategy):    

    @abstractmethod
    def transform(self, input_data:  any) ->  any:
        """Transforma o input_data e retorna o resultado."""
        pass    

class DataTransformerException(Exception):
    pass


# Classe TinyFlow que utiliza um conector de dados e uma sequência de transformadores que serão executados na ordem determinada. 
class TinyDataFlow:
    
    __flow_results: list = []
    
    def __init__(self, connector: DataConnector, transformers: List[DataTransformer]):        
        self.transformers = transformers
        self.connector = connector
        self._validate_transformer_sequence()

    def _validate_transformer_sequence(self):
        
        """Verifica se a sequência de transformadores é compatível."""
        for i in range(len(self.transformers) - 1):
            current_transformer = self.transformers[i]
            
            if i == 0:
                if current_transformer.input_type != self.connector.output_type:
                    raise TypeError(f"Incompatibilidade entre conector e primeiro transformador: "
                                    f"{current_transformer.__class__.__name__} produz {current_transformer.output_type.__name__}, "
                                    f"mas {self.connector.__class__.__name__} espera {self.connector.input_type.__name__} como entrada.")
            
            next_transformer = self.transformers[i + 1]

            if current_transformer.output_type != next_transformer.input_type:
                raise TypeError(f"Incompatibilidade entre transformadores: "
                                f"{current_transformer.__class__.__name__} produz {current_transformer.output_type.__name__}, "
                                f"mas {next_transformer.__class__.__name__} espera {next_transformer.input_type.__name__} como entrada.")

    def run(self) -> None:
        """Executa o fluxo de leitura e transformação."""
        try:
            while not self.connector.eof():
                current_output = self.connector.read()
                if not current_output:
                    break
                for transformer in self.transformers:
                    current_output = transformer.transform(current_output)
                
                self.__flow_results.append(current_output)
        except DataConnectorException as e:
            raise e
        finally:
            self.connector.close()
        
    def setup(self, config: dict = {}):
        """Configura os parâmetros do conector e dos transformadores."""
        if self.connector is not None:  
            self.connector.setup(config)
            
        for transformer in self.transformers:
            transformer.setup(config)

    @property
    def outputs(self) -> any:
        """Retorna os resultados do fluxo após as transformações."""
        if len(self.__flow_results) == 0:
            return None 
        elif len(self.__flow_results) == 1:
            return self.__flow_results[0]
        else:       
            return self.__flow_results
