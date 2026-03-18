import anvil.server
import sqlite3
from anvil.files import data_files


def get_connection():
  return sqlite3.connect(data_files["Club.db"])


def get_connection_dict():
  conn = sqlite3.connect(data_files["Club.db"])
  conn.row_factory = sqlite3.Row
  return conn


@anvil.server.callable
def query_database(query: str):
  with get_connection() as conn:
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return result


@anvil.server.callable
def query_database_dict(query: str):
  with get_connection_dict() as conn:
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return [dict(row) for row in result]


@anvil.server.callable
def get_spiele_by_club(club_name):
  with get_connection_dict() as conn:
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
      ORDER BY sp.Datum
    """, (club_name,)).fetchall()

  return [dict(row) for row in result]


@anvil.server.callable
def get_spieler_by_club(club_name):
  with get_connection_dict() as conn:
    cur = conn.cursor()
    result = cur.execute("""
      SELECT 
        s.SID AS sid,
        s.Vorname AS vorname,
        s.Nachname AS nachname,
        s.Position AS position,
        s.Geburtsdatum AS geburtsdatum
      FROM Spieler s
      JOIN Fussballclub f ON s.FID = f.FID
      WHERE f.Name = ?
      ORDER BY s.Nachname
    """, (club_name,)).fetchall()

  return [dict(row) for row in result]


@anvil.server.callable
def get_vertrag_by_spieler(sid):
  with get_connection_dict() as conn:
    cur = conn.cursor()
    result = cur.execute("""
      SELECT
        VID AS vid,
        Gehalt AS gehalt,
        Vertragsbeginn AS vertragsbeginn,
        Vertragsende AS vertragsende
      FROM Vertrag
      WHERE SID = ?
    """, (sid,)).fetchone()

  return dict(result) if result else None


@anvil.server.callable
def get_stadion_by_name(stadion_name):
  with get_connection_dict() as conn:
    cur = conn.cursor()
    result = cur.execute("""
      SELECT
        Name AS name,
        Ort AS ort,
        Kapazitaet AS kapazitaet
      FROM Stadion
      WHERE Name = ?
    """, (stadion_name,)).fetchone()

  return dict(result) if result else None


@anvil.server.callable
def get_trikots_by_spieler(sid):
  with get_connection_dict() as conn:
    cur = conn.cursor()
    result = cur.execute("""
      SELECT
        TID AS tid,
        Zustand AS zustand,
        Trikotnummer AS trikotnummer,
        Saison AS saison,
        Groesse AS groesse
      FROM Trikot
      WHERE SID = ?
    """, (sid,)).fetchall()

  return [dict(row) for row in result]


@anvil.server.callable
def get_trainer_by_club(club_name):
  with get_connection_dict() as conn:
    cur = conn.cursor()
    result = cur.execute("""
      SELECT
        t.Vorname AS vorname,
        t.Nachname AS nachname,
        t.Staatsbuergerschaft AS staatsbuergerschaft,
        t.Alter_Jahre AS alter_jahre,
        t.Gehalt AS gehalt
      FROM Trainer t
      JOIN Fussballclub f ON t.FID = f.FID
      WHERE f.Name = ?
    """, (club_name,)).fetchall()

  return [dict(row) for row in result]

@anvil.server.callable
def get_spieler_alter_by_club(club_name):
  with get_connection_dict() as conn:
    cur = conn.cursor()
    result = cur.execute("""
      SELECT
        s.Vorname || ' ' || s.Nachname AS name,
        CAST((julianday('now') - julianday(s.Geburtsdatum)) / 365.25 AS INT) AS alter_jahre
      FROM Spieler s
      JOIN Fussballclub f ON s.FID = f.FID
      WHERE f.Name = ?
    """, (club_name,)).fetchall()

  return [dict(row) for row in result]


@anvil.server.callable
def get_alter_statistik_by_club(club_name):
  daten = get_spieler_alter_by_club(club_name)

  if not daten:
    return {
      "durchschnitt": 0,
      "juengster": None,
      "aeltester": None
    }

  alter_liste = [d["alter_jahre"] for d in daten]

  return {
    "durchschnitt": round(sum(alter_liste) / len(alter_liste), 1),
    "juengster": min(daten, key=lambda x: x["alter_jahre"]),
    "aeltester": max(daten, key=lambda x: x["alter_jahre"])
  }


@anvil.server.callable
def get_spiel_statistik_by_club(club_name):
  with get_connection_dict() as conn:
    cur = conn.cursor()
    result = cur.execute("""
      SELECT
        Ergebnis AS ergebnis,
        Gegner AS gegner
      FROM Spiel sp
      JOIN Fussballclub f ON sp.FID = f.FID
      WHERE f.Name = ?
    """, (club_name,)).fetchall()

  spiele = [dict(row) for row in result]

  siege = 0
  unentschieden = 0
  niederlagen = 0
  hoechster_sieg = None
  hoechste_niederlage = None

  for spiel in spiele:
    tore_eigen, tore_gegner = map(int, spiel["ergebnis"].split(":"))

    diff = tore_eigen - tore_gegner

    if diff > 0:
      siege += 1
      if not hoechster_sieg or diff > hoechster_sieg["diff"]:
        hoechster_sieg = {
          **spiel,
          "diff": diff
        }

    elif diff == 0:
      unentschieden += 1

    else:
      niederlagen += 1
      if not hoechste_niederlage or diff < hoechste_niederlage["diff"]:
        hoechste_niederlage = {
          **spiel,
          "diff": diff
        }

  gesamt = len(spiele)

  return {
    "siege": siege,
    "unentschieden": unentschieden,
    "niederlagen": niederlagen,
    "gewinnrate": round((siege / gesamt) * 100, 1) if gesamt else 0,
    "hoechster_sieg": hoechster_sieg,
    "hoechste_niederlage": hoechste_niederlage
  }