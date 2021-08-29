import time
import json
from datetime import datetime
from Negocio.Buses import Buses

class Main:
  def __init__(self):
    while True:
       self.ProcesoDelete()
       time.sleep(300)

  
  def ProcesoDelete(self):
    x=0
    proceso = Buses().EliminaRegistros()
  

try:
  Main()
except:
  time.sleep(5)
  Main()
