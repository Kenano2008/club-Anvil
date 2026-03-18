from ._anvil_designer import TrainerTemplate
from anvil import *
import anvil.server

class Trainer(TrainerTemplate):
  def __init__(self, club_name, **properties):
    self.init_components(**properties)

    self.club_name = club_name

    trainer = anvil.server.call('get_trainer_by_club', club_name)
    self.repeating_panel_1.items = trainer

  @handle("button_zurueck", "click")
  def button_zurueck_click(self, **event_args):
    open_form('Startseite', selected_club=self.club_name)