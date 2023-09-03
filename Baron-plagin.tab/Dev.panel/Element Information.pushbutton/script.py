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
from pyrevit import revit,forms


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
# selected_views = forms.select_views()
# if selected_views:
#     print(selected_views)

# Выбрать элемент
with forms.WarningBar(title='Выберите элемент:'):
    element = revit.pick_element()
    
element_type = type(element)

print(element)
print(element_type)
# Get information




#pycharm Shortcut: CTRL + B