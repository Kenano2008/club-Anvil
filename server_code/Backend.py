import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import anvil.server
import sqlite3


# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#



def get_connection():
  db_file = anvil.files.data_files["Club.db"]
  conn = sqlite3.connect(db_file)
  conn.row_factory = sqlite3.Row
  return conn


@anvil.server.callable
def query_database(sql):
  conn = get_connection()
  cur = conn.cursor()
  cur.execute(sql)
  result = cur.fetchall()
  conn.close()
  return result


@anvil.server.callable
def query_database_dict(sql):
  conn = get_connection()
  cur = conn.cursor()
  cur.execute(sql)
  rows = cur.fetchall()
  result = [dict(row) for row in rows]
  conn.close()
  return result