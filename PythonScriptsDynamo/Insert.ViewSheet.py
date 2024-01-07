import clr

clr.AddReference('RevitAPI')
clr.AddReference("RevitServices")

from Autodesk.Revit.DB import *

from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

import math

doc = DocumentManager.Instance.CurrentDBDocument

# input a list of view
# in this sample with 4 views
views = UnwrapElement(IN[0])

# titleblock family
sheets = UnwrapElement(IN[1])

# transaction start
TransactionManager.Instance.EnsureInTransaction(doc)

#Empty list
viewPorts = []

posicoes = []

for s in sheets:
  o = s.Outline
  # net values
  xMax = o.Max.U
  xMin = o.Min.U
  yMax = o.Max.V
  yMin = o.Min.V
  dX = math.fabs(xMax - xMin)
  dY = math.fabs(yMax - yMin)
  # first role
  uv = XYZ(xMin + dX / 2, yMin + dY / 2, 0)
  posicoes.append(uv)

# create viewport for each view
for v, s, loc in zip(views, sheets, posicoes):
  Viewport.Create(doc, s.Id, v.Id, loc)
  viewPorts.append(Viewport)

# transaction close
TransactionManager.Instance.TransactionTaskDone()

# output sheet
OUT = sheets, viewPorts
