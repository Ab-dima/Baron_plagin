# -*- coding: utf-8 -*-

__title__ = 'Element Information'
__doc__   = 'Показывает информацию об элементе'

# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗
# ║║║║╠═╝║ ║╠╦╝ ║
# ╩╩ ╩╩  ╚═╝╩╚═ ╩
# =============================================
#Regular + Autodesk
from Autodesk.Revit.DB import *


# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝
# =============================================
doc   = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
app   = __revit__.Aplication


# ╔╦╗╔═╗ ╦ ╔╗╔
# ║║║╠═╣ ║ ║║║
# ╩ ╩╩ ╩ ╩ ╝╚╝
# =============================================
print('Hello World!')