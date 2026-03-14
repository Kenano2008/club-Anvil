from ._anvil_designer import SpielerVertragTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class SpielerVertrag(SpielerVertragTemplate):
  def __init__(self, spieler, **properties):
    self.init_components(**properties)

    vertrag = anvil.server.call('get_vertrag_by_spieler', spieler["sid"])

    if vertrag:
      self.repeating_panel_1.items = [vertrag]
    else:
      self.repeating_panel_1.items = []
      
  @handle("button_zurueck", "click")
  def button_zurueck_click(self, **event_args):
    open_form('Startseite.Spieler', self.clu