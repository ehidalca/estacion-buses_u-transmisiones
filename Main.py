import time
import json
from datetime import datetime
from Negocio.Buses import Buses
from Negocio.SondaWS import SondaWS
from Negocio.UltimasTransmisiones import UltimasTransmisiones
from Negocio.Tracktec import Tracktec
from Negocio.geocerca_maipu import geocerca_maipu
import numpy
from numpy import arctan2,random,sin,cos,degrees,deg2rad, rad2deg
import ast


class Main:
  def __init__(self):
    
     while True:  
      self.Proceso()
      time.sleep(60)
   
  def Proceso(self):
    fecha = datetime.now().replace(microsecond=0)   
    buses = Buses().Listar()
    #print(buses)
    busesMemoria = []
    if len(buses)>0:
      #inicializa función de los cerdos
      geocercas = geocerca_maipu()
      for bus in buses:
        patente = bus["ppu"]
        #print(patente)
        datosSonda = SondaWS().UltimaTransmisionPorBus(patente)
        if len(datosSonda) > 0:
          #print(datosSonda)
          busPatente = datosSonda[0]["patente"]
          busLatitud = datosSonda[0]["latitudgps"]
          busLongitud = datosSonda[0]["longitudgps"]
          busServicio = datosSonda[0]["servicio"]
          busSentido = datosSonda[0]["sentido"]
          busFecha = datosSonda[0]["fecha"]
          busHora = datosSonda[0]["hora"]
          busSS = str(datosSonda[0]["servicio_sentido_a_bordo_del_bus"])
          
          #buses.append(transmision)
          #datos de sonda
          #ut = UltimasTransmisiones().ConsultaPorPantente(patente)
          #if len(ut)>0:  
            #pto1_latitud  = ut[0]["pto1_latitud"]
            #pto1_longitud = ut[0]["pto1_longitud"]
          pto2_latitud  = datosSonda[1]["latitudgps"]
          pto2_longitud = datosSonda[1]["longitudgps"] 
          pto2_fecha    = datosSonda[1]["fecha"]   
          pto2_hora     = datosSonda[1]["hora"]  

          fechaHora = datetime.now().replace(microsecond=0) 
          fecha = str(fechaHora.date())
          hora  = str(fechaHora.time())

          brujula = 0 
          if pto2_latitud is not None:
              brujula = self.Brujula(float(pto2_latitud),float(pto2_longitud),float(busLatitud),float(busLongitud))
              brujula = round(brujula,2)
            
          #datos de tracktec 
          SOC= None
          tracktecLatitud = None
          tracktecLongitud = None
          tracktecFechaHora = None
          datosTracktec = Tracktec().UltimaTransmision(patente)
          
          if len(datosTracktec) > 0:
            SOC = datosTracktec[0]["carga"]
            tracktecLatitud = datosTracktec[0]["latitud"]
            tracktecLongitud = datosTracktec[0]["longitud"]
            tracktecFechaHora = str(datosTracktec[0]["fecha_evento"]) + " " + str(datosTracktec[0]["hora_evento"]) 
            #print(tracktecFechaHora)
          
          try:
              x = geocercas.cumple_geocerca_maipu(float(busLatitud),float(busLongitud))
              x2 = geocercas.cumple_geocerca_maipu(float(pto2_latitud),float(pto2_longitud))
          except:
              x=0
              x2 =0
          actualiza = UltimasTransmisiones().ActualizaPantente(patente, pto2_latitud , pto2_longitud, pto2_fecha,pto2_hora, busLatitud, busLongitud, busFecha, busHora, busServicio,busSentido, brujula , busSS, SOC, x,x2, tracktecLatitud, tracktecLongitud, tracktecFechaHora)
      #Buses().InsertaBusesProximos()                                                       
      #print(busesArreglo)   

  def Brujula(self, lt1, lg1, lt2, lg2):
    try:
      lat1 = deg2rad(lt1)
      long1 = deg2rad(lg1)
      lat2 = deg2rad(lt2)
      long2 = deg2rad(lg2)
      deltaLong = (long2 - long1)
      X = sin(deltaLong) * cos(lat2)
      Y = cos(lat1) * sin(lat2) - sin(lat1) * cos(lat2) * cos(deltaLong)
      angle_dir = rad2deg(arctan2(X, Y))
      return angle_dir
    except error:
      print(error)    

  


Main()


