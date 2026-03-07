from ._anvil_designer import ItemTemplate2Template
from anvil import *

class ItemTemplate2(ItemTemplate2Template):
  def __init__(self, **properties):
    self.init_components(**properties)

    self.label_1.text = str(self.item)