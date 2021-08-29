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
    try:
      while True:  
        self.Proceso()
        time.sleep(40)
    except:
      while True:  
        self.Proceso()
        time.sleep(40)
  def Proceso(self):
    fecha = datetime.now().replace(microsecond=0)  
    print(str(fecha)) 
    buses = Buses().Listar()
    #print(buses)
    busesMemoria = []
    if len(buses)>0:
      #inicializa función de los cerdos
      geocercas = geocerca_maipu()
      # = SondaWS().DatosJefe()
      datosN = SondaWS().DatosJefe()
      datosTracktec = Tracktec().TodasUltimasTransmisiones()
      #print(datosN)
      for bus in buses:
        patente = bus["ppu"]
        enEstudio = bus["en_estudio"]
        #print(enEstudio)
        datosSonda= []
        for dato in datosN :
          if patente == dato["patente"].replace("-",""): 
            datosSonda   = dato
            busPatente    = datosSonda["patente"]
            busLatitud    = datosSonda["lat2"]
            busLongitud   = datosSonda["lon2"]
            busServicio   = datosSonda["serv"]
            busSentido    = datosSonda["sent"]
            busFecha      = datosSonda["fecha"]
            busHora       = datosSonda["hora2"]
            busSS         = str(datosSonda["consola"])
            pto2_latitud  = datosSonda["lat1"]
            pto2_longitud = datosSonda["long1"] 
            pto2_fecha    = datosSonda["fecha"]   
            pto2_hora     = datosSonda["hora1"]  

            #función brujula 
            brujula = 0 
            if pto2_latitud is not None:
               brujula = self.Brujula(float(pto2_latitud),float(pto2_longitud),float(busLatitud),float(busLongitud))
               brujula = round(brujula,2)
            
            #datos de tracktec 
            SOC= None
            tracktecLatitud = None
            tracktecLongitud = None
            tracktecFechaHora = None
            odometro = None
          
            for tracktec in datosTracktec:
              if tracktec["patente"].replace('-','')==patente:
                #print("si")
                SOC = tracktec["carga"]
                odometro = tracktec["odometro"]
                tracktecLatitud = tracktec["latitud"]
                tracktecLongitud = tracktec["longitud"]
                tracktecFechaHora = str(tracktec["fecha_evento"]) + " " + str(tracktec["hora_evento"]) 
                break
            #print(tracktecFechaHora)
            try:
               x = geocercas.cumple_geocerca_maipu(float(busLatitud),float(busLongitud))
               x2 = geocercas.cumple_geocerca_maipu(float(pto2_latitud),float(pto2_longitud))
            except:
               x= 0
               x2 = 0
            actualiza = UltimasTransmisiones().ActualizaPantente(patente, pto2_latitud , pto2_longitud, pto2_fecha,pto2_hora, busLatitud, busLongitud, busFecha, busHora, busServicio,busSentido, brujula , busSS, SOC, x,x2, tracktecLatitud, tracktecLongitud, tracktecFechaHora, odometro, enEstudio)
            break
      #Buses().InsertaBusesProximos()                                                       
      #print(busesArreglo)   
      fecha = datetime.now().replace(microsecond=0)  
      print("termino:" + str(fecha)) 

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

  
try:
  Main()
except :
    Main()
    

