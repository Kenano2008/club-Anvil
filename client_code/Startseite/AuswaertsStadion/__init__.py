from ._anvil_designer import AuswaertsStadionTemplate
from anvil import *
import anvil.server

class AuswaertsStadion(AuswaertsStadionTemplate):
  def __init__(self, spiel, **properties):
    self.init_components(**properties)

    stadion = anvil.server.call('get_stadion_by_name', spiel["stadion"])

    if stadion:
      self.repeating_panel_1.items = [stadion]
    else:
      self.repeating_panel_1.items = []