import clr

# Importar referências necessárias do Revit
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

# Importar referências do Dynamo para manipulação do documento
clr.AddReference("RevitServices")
from RevitServices.Persistence import DocumentManager

# Obter o documento atual do Revit
doc = DocumentManager.Instance.CurrentDBDocument

# Entrada: Grupos de modelo do Revit
grupos_modelo = UnwrapElement(IN[0])

# Função para obter os elementos de um grupo de modelo
def obter_elementos_do_grupo(grupo):
    # Verificar se o elemento de entrada é um grupo de modelo
    if not isinstance(grupo, Group):
        return None

    # Obter IDs dos membros do grupo
    member_ids = grupo.GetMemberIds()

    # Obter elementos correspondentes às IDs dos membros
    members = [doc.GetElement(member_id) for member_id in member_ids]

    return members

# Aplicar a função a cada grupo de modelo na lista de entrada
elementos_por_grupo = [obter_elementos_do_grupo(grupo) for grupo in grupos_modelo]

# Saída: Listas com elementos contidos nos grupos de modelo
OUT = elementos_por_grupo
