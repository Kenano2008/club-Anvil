from ._anvil_designer import RowTemplate1Template
from anvil import *

class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.trainer_Name.text = self.item["trainer_name"]
    self.label_club_name.text = self.item["club_name"]
    self.label_gruendungsjahr.text = self.item["gruendungsjahr"]
    

  @handle("button_spiele", "click")
  def Auswahl_click(self, **event_args):
    """This method is called when the button is clicked"""
    print(self.item)
    open_form('Startseite.Spiele',self.item)