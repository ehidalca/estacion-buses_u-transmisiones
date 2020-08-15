import time
import json
from datetime import datetime
from Negocio.Buses import Buses
from Negocio.SondaWS import SondaWS
from Negocio.UltimasTransmisiones import UltimasTransmisiones
from Negocio.Tracktec import Tracktec
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
    print(buses)
    busesMemoria = []
    if len(buses)>0:
      for bus in buses:
        patente = bus["ppu"]
        print(patente)
        datosSonda = SondaWS().UltimaTransmisionPorBus(patente)
        if len(datosSonda) > 0:
          #print(datosSonda)
          busPatente = datosSonda[0]["patente"]
          busLatitud = datosSonda[0]["latitudgps"]
          busLongitud = datosSonda[0]["longitudgps"]
          busServicio = datosSonda[0]["servicio"]
          busSentido = datosSonda[0]["sentido"]
          busSS = str(datosSonda[0]["servicio_sentido_a_bordo_del_bus"])
          print(busServicio)
          print(busSentido)
          print(busSS)
          #buses.append(transmision)
  
          ut = UltimasTransmisiones().ConsultaPorPantente(patente)
          if len(ut)>0:  
            #pto1_latitud  = ut[0]["pto1_latitud"]
            #pto1_longitud = ut[0]["pto1_longitud"]
            pto2_latitud  = ut[0]["pto2_latitud"]
            pto2_longitud = ut[0]["pto2_longitud"] 
            pto2_fecha    = ut[0]["pto2_fecha"]   
            pto2_hora     = ut[0]["pto2_hora"]  

            fechaHora = datetime.now().replace(microsecond=0) 
            fecha = str(fechaHora.date())
            hora  = str(fechaHora.time())
            brujula = 0 
            if pto2_latitud is not None:
              brujula = self.Brujula(float(pto2_latitud),float(pto2_longitud),float(busLatitud),float(busLongitud))
              brujula = round(brujula,2)
            
            #obtengo SOC desde ultimas tranmisiones de tracktec
            SOC = 0
            SOC = Tracktec().SOC(patente)

            actualiza = UltimasTransmisiones().ActualizaPantente(patente, pto2_latitud , pto2_longitud, pto2_fecha,pto2_hora, busLatitud, busLongitud, fecha, hora, busServicio,busSentido, brujula , busSS, SOC)
                                                             
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


