from ._anvil_designer import RowTemplate1Template
from anvil import *

class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    self.init_components(**properties)

    self.label_vorname.text = self.item["vorname"]
    self.label_nachname.text = self.item["nachname"]
    self.label_staatsbuergerschaft.text = self.item["staatsbuergerschaft"]
    self.label_alter.text = str(self.item["alter_jahre"])
    self.label_gehalt.text = str(self.item["gehalt"])