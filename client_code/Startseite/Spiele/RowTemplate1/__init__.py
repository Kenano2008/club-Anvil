from ._anvil_designer import RowTemplate1Template
from anvil import *

class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.button_stadion.text = self.item["stadion"]
    self.label_datum.text = self.item["datum"]
    self.label_ergebnis.text = self.item["ergebnis"]
    self.label_gegner.text = self.item["gegner"]
    self.label_wettbewerb.text = self.item["wettbewerb"]

  @handle("button_stadion", "click")
  def button_stadion_click(self, **event_args):
    open_form('Startseite.AuswaertsStadion', self.item, self.item["club"])