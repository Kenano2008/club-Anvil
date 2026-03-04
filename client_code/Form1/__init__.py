from ._anvil_designer import StartseiteTemplate
from anvil import *
import anvil.server

class Startseite(StartseiteTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    # Dropdown befüllen (wie bei dir: SELECT name FROM ...)
    return_value = anvil.server.call('query_database', 'SELECT Name FROM Fussballclub ORDER BY Name')
    return_value = [entry[0] for entry in return_value]

    print(return_value)
    self.drop_down_clubliste.items = return_value
    self.drop_down_clubliste_change()

  @handle("drop_down_clubliste", "change")
  def drop_down_clubliste_change(self, **event_args):
    club_name = self.drop_down_clubliste.selected_value
    if not club_name:
      self.repeating_panel_1_clubdetails.items = []
      return

    # Club-Übersicht ähnlich wie "Gebäude" Query:
    # - Spieleranzahl
    # - Anzahl Trikots
    # - Durchschnittsgehalt (Verträge)
    sql = f"""
      SELECT
        fc.Name AS club_name,
        COUNT(DISTINCT sp.SID) AS anzahl_spieler,
        COUNT(DISTINCT tr.TID) AS anzahl_trikots,
        ROUND(AVG(v.Gehalt), 2) AS avg_gehalt
      FROM Fussballclub fc
      LEFT JOIN Spieler sp ON sp.FID = fc.FID
      LEFT JOIN Trikot tr ON tr.SID = sp.SID
      LEFT JOIN Vertrag v ON v.SID = sp.SID
      WHERE fc.Name = '{club_name}'
      GROUP BY fc.Name;
    """

    return_value = anvil.server.call('query_database_dict', sql)

    # Extra Feld wie bei dir "gefaengnis_name"
    for d in return_value:
      d["selected_club"] = club_name

    print(return_value)
    self.repeating_panel_1_clubdetails.items = return_value