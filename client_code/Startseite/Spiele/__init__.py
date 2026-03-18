from ._anvil_designer import SpieleTemplate
from anvil import *
import anvil.server
import plotly.graph_objects as go

class Spiele(SpieleTemplate):
  def __init__(self, club_name, **properties):
    self.init_components(**properties)

    self.club_name = club_name

    spiele = anvil.server.call('get_spiele_by_club', club_name)

    for spiel in spiele:
      spiel["club_name"] = club_name

    self.repeating_panel_spiele.items = spiele

    stats = anvil.server.call('get_spiel_statistik_by_club', club_name)

    if stats["hoechster_sieg"]:
      self.label_hoechster_sieg.text = (
        f"Höchster Sieg: {stats['hoechster_sieg']['ergebnis']} gegen {stats['hoechster_sieg']['gegner']}"
      )
    else:
      self.label_hoechster_sieg.text = "Höchster Sieg: -"

    if stats["hoechste_niederlage"]:
      self.label_hoechste_niederlage.text = (
        f"Höchste Niederlage: {stats['hoechste_niederlage']['ergebnis']} gegen {stats['hoechste_niederlage']['gegner']}"
      )
    else:
      self.label_hoechste_niederlage.text = "Höchste Niederlage: -"

    self.label_gewinnrate.text = f"Gewinnrate: {stats['gewinnrate']} %"

    fig = go.Figure(
      data=[go.Bar(
        x=["Siege", "Unentschieden", "Niederlagen"],
        y=[stats["siege"], stats["unentschieden"], stats["niederlagen"]]
      )]
    )

    fig.update_layout(
      title=f"Spielstatistik - {club_name}",
      xaxis_title="Ergebnisart",
      yaxis_title="Anzahl"
    )

    self.plot_spiele.figure = fig

  @handle("button_zurueck", "click")
  def button_zurueck_click(self, **event_args):
    open_form('Startseite', selected_club=self.club_name)