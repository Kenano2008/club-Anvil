from ._anvil_designer import RowTemplate1Template
from anvil import *

class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    self.init_components(**properties)

    self.label_club.text = self.item["club"]
    self.label_stadion.text = self.item["stadion"]
    self.label_datum.text = self.item["datum"]
    self.label_ergebnis.text = self.item["ergebnis"]

