from ._anvil_designer import RowTemplate1Template
from anvil import *
from ..Spiele import Spiele
from ..Spieler import Spieler
from ..Trainer import Trainer


class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    self.init_components(**properties)

    self.trainer_Name.text = self.item["trainer_name"]
    self.label_club_name.text = self.item["club_name"]
    self.label_gruendungsjahr.text = self.item["gruendungsjahr"]

  @handle("button_spiele", "click")
  def button_spiele_click(self, **event_args):
    form = get_open_form()
    club_name = form.drop_down_clubliste.selected_value

    form.content_panel.clear()
    form.content_panel.add_component(Spiele(club_name))

  @handle("button_spieler", "click")
  def button_spieler_click(self, **event_args):
    form = get_open_form()
    club_name = form.drop_down_clubliste.selected_value

    form.content_panel.clear()
    form.content_panel.add_component(Spieler(club_name))

  @handle("trainer_Name", "click")
  def button_trainer_click(self, **event_args):
    form = get_open_form()
    club_name = form.drop_down_clubliste.selected_value

    form.content_panel.clear()
    form.content_panel.add_component(Trainer(club_name))