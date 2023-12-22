
import clr

import sys
sys.path.append('C:\Program Files (x86)\IronPython 2.7\Lib')

import System
from System import *
from System.Collections.Generic import *

clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# Importar ToDSType(bool) 
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
# Importar extensão de conversão de geometria
clr.ImportExtensions(Revit.GeometryConversion)

# Importar gerenciamento de documento e de transação
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager 
from RevitServices.Transactions import TransactionManager 

# Importar API do revit
clr.AddReference("RevitAPI")
clr.AddReference("RevitAPIUI")
import Autodesk 
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *


#Insira aqui seus inputs 
walls = IN[0]
solids = IN[1]

# Insira o código abaixo desta linha
void = []

#extrai os itens das listas dos inputs
for wall, solid, in zip(walls, solids):

#Subtrai a diferenca entre os dois solidos e os coloca na lista vazia anteriormente criaca chamada "void[]"
	saida = wall.Difference(solid)
	void.append(saida)
 

# Atribua a sua saída para a variável OUT.
OUT = void