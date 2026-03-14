from ._anvil_designer import TrikotsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Trikots(TrikotsTemplate):
  def __init__(self, spieler, **properties):
    self.init_components(**properties)

    trikots = anvil.server.call('get_trikots_by_spieler', spieler["sid"])
    self.repeating_panel_1.items = trikots

  @handle("button_zurueck", "click")
  def button_zurueck_click(self, **event_args):
    open_form('Startseite.Spieler', self.club)