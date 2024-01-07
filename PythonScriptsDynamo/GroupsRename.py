# Importar as bibliotecas necessárias
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

# Importar DocumentManager
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

# Entradas
grupos = UnwrapElement(IN[0])  # Lista de grupos
novos_nomes = IN[1]            # Lista de novos nomes

# Obter o documento atual do Revit
doc = DocumentManager.Instance.CurrentDBDocument

# Iniciar uma transação no documento do Revit
TransactionManager.Instance.EnsureInTransaction(doc)

# Iterar sobre cada grupo e definir o novo nome
for grupo, novo_nome in zip(grupos, novos_nomes):
    grupo.GroupType.Name = novo_nome

# Finalizar a transação
TransactionManager.Instance.TransactionTaskDone()

# Saída
OUT = grupos
