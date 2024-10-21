import unittest
import os
import sys

# Necessário para que o arquivo de testes encontre
test_root = os.path.dirname(os.path.abspath(__file__))
os.chdir(test_root)
sys.path.insert(0, os.path.dirname(test_root))
sys.path.insert(0, test_root)

from tinydataflow import TinyDataFlow
from tinydataflow.transformers.writers import FileWriter
from tinydataflow.connectors.selectors import FileListSelector

class FileSelTest(unittest.TestCase):

    def test_file_selector(self):
        
        file_selector = FileListSelector('.', '*.txt')
        writer = FileWriter('file_selector_output.txt')
        # Escreve o resultado dos arquivos selecionados no arquivo CSV
        try:
            app = TinyDataFlow(file_selector, [writer])
            app.setup({'open_mode': 'w'})
            app.run()    
            print(f"Resultados: {app.outputs}")
            
            self.assertEqual(app.outputs, 'file_selector_output.txt')
        except TypeError as e:
            print(f"Erro de compatibilidade: {e}")
               
if __name__ == '__main__':
    unittest.main()