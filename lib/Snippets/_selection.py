# -*- coding: utf-8 -*-

# imports
from Autodesk.Revit.DB import *

uidoc = __revit__.ActiveUIDocument
doc   = __revit__.ActiveUIDocument.Document

# functions

def get_selected_elelemnts(uidoc):
    """

    :param uidoc:
    :return:
    """
    selected_elements = []

    for elem_id in uidoc.Selection.GetElementIds():
        elem = uidoc.Document.GetElement(elem_id)
        selected_elements.append(elem)

    return selected_elements