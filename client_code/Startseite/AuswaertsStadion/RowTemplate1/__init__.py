from ._anvil_designer import RowTemplate1Template
from anvil import *

class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    self.init_components(**properties)

    self.label_name.text = self.item["name"]
    self.label_ort.text = self.item["ort"]
    self.label_kapazitaet.text = str(self.item["kapazitaet"])
