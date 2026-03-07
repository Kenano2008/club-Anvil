from ._anvil_designer import StartseiteTemplate
from anvil import *
import anvil.server


class Startseite(StartseiteTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    return_value = anvil.server.call('query_database', 'SELECT Name FROM Fussballclub')
    return_value = [entry[0] for entry in return_value]

    self.drop_down_clubliste.items = return_value

    if return_value:
      self.drop_down_clubliste.selected_value = return_value[0]

    self.drop_down_clubliste_change()

  @handle("drop_down_clubliste", "change")
  def drop_down_clubliste_change(self, **event_args):
    sql_club = f"""
      SELECT 
        f.Name AS club_name,
        f.Gruendungsjahr AS gruendungsjahr,
        t.Vorname || ' ' || t.Nachname AS trainer_name
      FROM Fussballclub f
      LEFT JOIN Trainer t ON f.FID = t.FID
      WHERE f.Name = '{self.drop_down_clubliste.selected_value}'
    """

    club_info = anvil.server.call('query_database_dict', sql_club)
    self.repeating_panel_clubinfo.items = club_info