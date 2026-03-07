from ._anvil_designer import SpieleTemplate
from anvil import *
import anvil.server

class Spiele(SpieleTemplate):
  def __init__(self, club, **properties):
    self.init_components(**properties)

    club_name = club["club_name"]

    spiele = anvil.server.call('get_spiele_by_club', club_name)

    self.repeating_panel_spiele.items = spiele

