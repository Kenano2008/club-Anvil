from ._anvil_designer import TrainerTemplate
from anvil import *
import anvil.server

class Trainer(TrainerTemplate):
  def __init__(self, club, **properties):
    self.init_components(**properties)

    trainer = anvil.server.call('get_trainer_by_club', club["club_name"])
    self.repeating_panel_1.items = trainer