from ._anvil_designer import SpieleTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server

class Spiele(SpieleTemplate):
  def __init__(self, club, **properties):
    self.init_components(**properties)

    club_name = club["club_name"]

    spiele = anvil.server.call('get_spiele_by_club', club_name)

    self.repeating_panel_spiele.items = spiele


  @handle("button_zurueck", "click")
  def button_zurueck_click(self, **event_args):
    open_form('Startseite')