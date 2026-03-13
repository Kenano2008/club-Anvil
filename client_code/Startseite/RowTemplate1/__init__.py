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


  @handle("button_spieler", "click")
  def button_spieler_click(self, **event_args):
    open_form('Startseite.Spieler', self.item)

  @handle("trainer_Name", "click")
  def button_trainer_click(self, **event_args):
    open_form('Startseite.Trainer', self.item)