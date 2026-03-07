from ._anvil_designer import StartseiteTemplate
from anvil import *
import anvil.server


class Startseite(StartseiteTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    return_value = anvil.server.call('query_database', 'SELECT Name FROM Fussballclub')

    return_value = [entry[0] for entry in return_value]
    print(return_value)

    self.drop_down_clubliste.items = return_value
    self.drop_down_clubliste_change()

  @handle("drop_down_clubliste", "change")
  def drop_down_clubliste_change(self, **event_args):
    sql_club = f"""
      SELECT 
        f.Name AS club_name,
        f.Gruendungsjahr AS gruendungsjahr,
        t.Vorname || ' ' || t.Nachname AS trainer_name,
        s.Land AS land,
        s.Stadt AS stadt
      FROM Fussballclub f
      LEFT JOIN Trainer t ON f.FID = t.FID
      LEFT JOIN Standort s ON f.FID = s.FID
      WHERE f.Name = '{self.drop_down_clubliste.selected_value}'
    """

    club_info = anvil.server.call('query_database_dict', sql_club)
    self.repeating_panel_clubinfo.items = club_info

    sql_spieler = f"""
      SELECT 
        sp.Vorname AS vorname,
        sp.Nachname AS nachname,
        sp.Position AS position,
        sp.Geburtsdatum AS geburtsdatum
      FROM Spieler sp
      JOIN Fussballclub f ON sp.FID = f.FID
      WHERE f.Name = '{self.drop_down_clubliste.selected_value}'
      ORDER BY sp.Nachname
    """

    spieler = anvil.server.call('query_database_dict', sql_spieler)
    self.repeating_panel_spieler.items = spieler