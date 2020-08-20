import time
import json
from datetime import datetime
from Negocio.Buses import Buses

class Main:
  def __init__(self):
    
     while True:  
      self.Proceso()
      time.sleep(60)
   
  def Proceso(self):
    fecha = datetime.now().replace(microsecond=0)   
    proceso = Buses().InsertaBusesProximos()
    print(proceso)
  
Main()


