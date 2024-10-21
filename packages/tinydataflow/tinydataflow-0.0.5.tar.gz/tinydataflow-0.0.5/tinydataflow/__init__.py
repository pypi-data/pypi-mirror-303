__version__ = '0.0.5'

from tinydataflow.core import TinyDataFlow
from tinydataflow.connectors import CSVLineReader, FileReader, FileSelector
from tinydataflow.transformers import ListToDictTransformer, StrToCSVTransformer, EmailSender