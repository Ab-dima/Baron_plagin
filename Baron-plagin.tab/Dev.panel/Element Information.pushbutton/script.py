# -*- coding: utf-8 -*-

__title__ = 'Element Information'
__doc__   = 'Показывает информацию об элементе'

# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗
# ║║║║╠═╝║ ║╠╦╝ ║
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ IMPORT
# =============================================
#Regular + Autodesk
import clr
from Autodesk.Revit.DB import *
from pyrevit import *

# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
# =============================================
doc   = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
app   = __revit__.Application


# ╔╦╗╔═╗ ╦ ╔╗╔
# ║║║╠═╣ ║ ║║║
# ╩ ╩╩ ╩ ╩ ╝╚╝ MAIN
# =============================================

#Bonus: PyRevit Input
selected_views = forms.select_views()
if selected_views:
    print(selected_views)

# Выбрать элемент
# Get information