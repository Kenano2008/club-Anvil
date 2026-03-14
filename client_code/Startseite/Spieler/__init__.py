from ._anvil_designer import SpielerTemplate
from anvil import *
import anvil.server
import plotly.graph_objects as go

class Spieler(SpielerTemplate):
  def __init__(self, club, **properties):
    self.init_components(**properties)

    self.club = club
    club_name = club["club_name"]

    spieler = anvil.server.call('get_spieler_by_club', club_name)
    self.repeating_panel_spieler.items = spieler

    daten = anvil.server.call('get_spieler_alter_by_club', club_name)

    namen = [d["name"] for d in daten]
    alter = [d["alter_jahre"] for d in daten]

    fig = go.Figure(
      data=[go.Bar(
        x=namen,
        y=alter
      )]
    )

    fig.update_layout(
      title=f"Alter der Spieler - {club_name}",
      xaxis_title="Spieler",
      yaxis_title="Alter"
    )

    self.plot_alter.figure = fig


    stats = anvil.server.call('get_alter_statistik_by_club', club_name)

    self.label_durchschnitt.text = f"Durchschnittsalter: {stats['durchschnitt']}"
    self.label_juengster.text = f"Jüngster Spieler: {stats['juengster']['name']} ({stats['juengster']['alter_jahre']} Jahre)"
    self.label_aeltester.text = f"Ältester Spieler: {stats['aeltester']['name']} ({stats['aeltester']['alter_jahre']} Jahre)"


  @handle("button_zurueck", "click")
  def button_zurueck_click(self, **event_args):
    open_form('Startseite')

  @handle("plot_alter", "click")
  def plot_alter_click(self, points, **event_args):
    """This method is called when a data point is clicked."""
    pass
    