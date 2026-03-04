import anvil.server
from anvil.files import data_files
import sqlite3, tempfile

def _conn():
  f = data_files["Club.db"]
  tmp = tempfile.NamedTemporaryFile(delete=False)
  tmp.write(f.get_bytes())
  tmp.close()
  conn = sqlite3.connect(tmp.name)
  conn.row_factory = sqlite3.Row
  return conn

@anvil.server.callable
def get_clubs():
  with _conn() as conn:
    cur = conn.cursor()
    rows = cur.execute("SELECT FID, Name FROM Fussballclub ORDER BY Name").fetchall()
  return [dict(r) for r in rows]

@anvil.server.callable
def get_players_by_club(fid: int):
  with _conn() as conn:
    cur = conn.cursor()
    rows = cur.execute("""
      SELECT Vorname, Nachname, Position, Geburtsdatum
      FROM Spieler
      WHERE FID = ?
      ORDER BY Nachname, Vorname
    """, (fid,)).fetchall()
  return [dict(r) for r in rows]
