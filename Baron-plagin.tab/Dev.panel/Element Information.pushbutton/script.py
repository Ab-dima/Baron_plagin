# -*- coding: utf-8 -*-

__title__ = 'Element Information'
__doc__   = 'Показывает информацию об элементе'

import sys

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
# ===============================================
with forms.WarningBar(title='Выберите элемент:'):
    element = revit.pick_element()
element_type = type(element)

if element_type != Wall:
    print('Нужно было выбрать стену')
    sys.exit()
# Get information
# ===============================================
e_cat         = element.Category.Name
e_id          = element.Id
e_level       = doc.GetElement(element.LevelId)
e_wall_type   = element.WallType
e_width       = element.Width


#pycharm Shortcut: CTRL + B

print('Element Category : {}'.format(e_cat))
print('Element Id: {}'.format(e_id))
print('Element LevelId: {}'.format(e_level.Name))
print('Wall WallType: {}'.format(e_wall_type))
print('Wall Width: {}'.format(e_width))