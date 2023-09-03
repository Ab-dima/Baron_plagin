# -*- coding: utf-8 -*-

__title__ = 'Выбранные элементы'
__doc__ = 'Покажет выбранные элементы'

# variables
uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

# Custom imports
from Snippets._selection import get_selected_elements

if __name__ == '__main__':
    print(get_selected_elements(uidoc))
