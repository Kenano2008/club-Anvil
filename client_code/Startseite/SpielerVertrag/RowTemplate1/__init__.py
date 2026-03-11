from ._anvil_designer import RowTemplate1Template
from anvil import *

class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    self.init_components(**properties)

    self.label_gehalt.text = str(self.item["gehalt"])
    self.label_vertragsbeginn.text = str(self.item["vertragsbeginn"])
    self.label_vertragsende.text = str(self.item["vertragsende"])