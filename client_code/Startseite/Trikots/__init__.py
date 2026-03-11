from ._anvil_designer import TrikotsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Trikots(TrikotsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    trikots = anvil.server.call('get_trikots_by_spieler', spieler["sid"])
    self.repeating_panel_1.items = trikots

    # Any code you write here will run before the form opens.
