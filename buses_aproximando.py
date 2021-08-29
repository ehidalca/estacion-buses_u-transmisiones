import time
import json
from datetime import datetime
from Negocio.Buses import Buses

class Main:
  def __init__(self):
    
     while True:  
      self.Proceso()
      time.sleep(30)

     while True:
       self.ProcesoDelete()
       time.sleep(300)
   
  def Proceso(self):
    try:
      fecha = datetime.now().replace(microsecond=0)   
      proceso = Buses().InsertaBusesProximos()
      print(proceso)
    except:
      return   
  def ProcesoDelete(self):
    try:
      x=0
      proceso = buses().EliminaRegistros()
    except:
      return 

try:
  Main()
except:
  time.sleep(15)
  Main()

