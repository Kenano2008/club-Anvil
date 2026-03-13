from ._anvil_designer import TrainerTemplate
from anvil import *
import anvil.server


class Trainer(TrainerTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    trainer = anvil.server.call('get_trainer')
    self.repeating_panel_trainer.items = trainer