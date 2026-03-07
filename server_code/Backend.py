import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import anvil.server
import sqlite3


@anvil.server.callable
def query_database(query: str):
  with sqlite3.connect(data_files["Club.db"]) as conn:
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return result


@anvil.server.callable
def query_database_dict(query: str):
  with sqlite3.connect(data_files["Club.db"]) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return [dict(row) for row in result]



@anvil.server.callable
def get_spiele_by_club(club):
  with sqlite3.connect(data_files["Club.db"]) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute("""
      SELECT 
        st.Name AS stadion,
        sp.Datum AS datum,
        sp.Ergebnis AS ergebnis,
        sp.Gegner AS gegner,
        sp.Wettbewerb AS wettbewerb
      FROM Spiel sp
      JOIN Fussballclub f ON sp.FID = f.FID
      JOIN Stadion st ON sp.STID = st.STID
      WHERE f.Name = ?
    """, (club,)).fetchall()
  return [dict(row) for row in result]
