from ._anvil_designer import StartseiteTemplate
from anvil import *
import anvil.server

class Startseite(StartseiteTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    rows = anvil.server.call('query_database',
                             'SELECT Name FROM Fussballclub ORDER BY Name')
    club_names = [r[0] for r in rows]

    self.drop_down_clubliste.items = club_names

    if club_names:
      self.drop_down_clubliste.selected_value = club_names[0]
      self.drop_down_clubliste_change()
    else:
      self.repeating_panel_1_clubdetails.items = []


  @handle("drop_down_clubliste", "change")
  def drop_down_clubliste_change(self, **event_args):
    club_name = self.drop_down_clubliste.selected_value
    if not club_name:
      self.repeating_panel_1_clubdetails.items = []
      return

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

    data = anvil.server.call('query_database_dict', sql)
    self.repeating_panel_1_clubdetails.items = data