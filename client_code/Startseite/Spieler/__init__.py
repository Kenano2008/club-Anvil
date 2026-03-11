from ._anvil_designer import SpielerTemplate
from anvil import *
import anvil.server

class Spieler(SpielerTemplate):
  def __init__(self, club, **properties):
    self.init_components(**properties)

    club_name = club["club_name"]

    spieler = anvil.server.call('get_spieler_by_club', club_name)

    self.repeating_panel_spieler.items = spieler


  @handle("button_zueruck", "click")
  def button_zurueck_click(self, **event_args):
    open_form('Startseite')


    