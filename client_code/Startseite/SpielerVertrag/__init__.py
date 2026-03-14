from ._anvil_designer import SpielerVertragTemplate
from anvil import *
import anvil.server

class SpielerVertrag(SpielerVertragTemplate):
  def __init__(self, spieler, club, **properties):
    self.init_components(**properties)

    self.club = club

    vertrag = anvil.server.call('get_vertrag_by_spieler', spieler["sid"])

    if vertrag:
      self.repeating_panel_1.items = [vertrag]
    else:
      self.repeating_panel_1.items = []

  @handle("button_zurueck", "click")
  def button_zurueck_click(self, **event_args):
    open_form('Startseite.Spieler', self.club)