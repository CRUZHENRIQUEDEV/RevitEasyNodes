#Element.ViewDuplicate

#Duplicate, views

#DUPLICA UMA VISTA EXISTENTE E RENOMEIA de acordo com os nomes fornecidos nos inputs

#Views = IN[0]
#Names = IN[1]

#O script começa depois dos traços
#----------------------------------------------

# Importando as bibliotecas necessárias
import clr

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
import Autodesk

# Importando as bibliotecas do Dynamo
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager


# Função para duplicar uma vista com um novo nome
def DuplicateView(view, name, doc):
  try:
    # Duplica a vista com o nome especificado
    newViewId = view.Duplicate(Autodesk.Revit.DB.ViewDuplicateOption.Duplicate)
    newView = doc.GetElement(newViewId)
    try:
      newView.Name = name
    except:
      pass
    return newView
  except:
    return None


# Obter o documento atual do Dynamo
doc = DocumentManager.Instance.CurrentDBDocument

# Lista de vistas a serem duplicadas
Views = UnwrapElement(IN[0])

# Lista de nomes para as vistas duplicadas
Names = IN[1]

# Iniciar uma transação
TransactionManager.Instance.EnsureInTransaction(doc)

# Duplicar as vistas
if isinstance(Views, list):
  OUT = []  # Inicializar a lista de saída
  for view, name in zip(Views, Names):
    if isinstance(name, list):
      # Se houver uma lista de nomes, duplicar a vista para cada nome
      OUT.append([DuplicateView(view, x, doc) for x in name])
    else:
      # Se houver um único nome, duplicar a vista com esse nome
      OUT.append(DuplicateView(view, name, doc))
else:
  # Se houver uma única vista, duplicar para o nome fornecido
  if isinstance(Names, list):
    OUT = [DuplicateView(Views, x, doc) for x in Names]
  else:
    OUT = DuplicateView(Views, Names, doc)

# Finalizar a transação
TransactionManager.Instance.TransactionTaskDone()
