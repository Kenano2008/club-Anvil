from ._anvil_designer import RowTemplate1Template
from anvil import *

class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    self.init_components(**properties)

    self.label_zustand.text = self.item["zustand"]
    self.label_trikotnummer.text = str(self.item["trikotnummer"])
    self.label_Saison.text = self.item["saison"]
    self.label_groesse.text = self.item["groesse"]