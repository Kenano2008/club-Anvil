from ._anvil_designer import RowTemplate1Template
from anvil import *

class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.label_vorname.text = self.item["vorname"]
    self.label_nachname.text = self.item["nachname"]
    self.label_position.text = self.item["position"]
    self.label_geburtsdatum.text = self.item["geburtsdatum"]

  @handle("button_vertrag", "click")
  def button_vertrag_click(self, **event_args):
    open_form('Startseite.SpielerVertrag', self.item, self.item["club_name"])

  @handle("button_trikot", "click")
  def button_trikot_click(self, **event_args):
    open_form('Startseite.Trikots', self.item, self.item["club_name"])