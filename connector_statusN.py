import time
import json
from datetime import datetime
from Negocio.Reservas import Reservas
from Negocio.Cargadores import Cargadores
from Negocio.Pistolas import  Pistolas
import requests


def EjecutaProceso():
        while True:
                CargasFinalizadasv2()
                time.sleep(10)

def CargasFinalizadasv2():
        try:
                fechaHora = datetime.now().replace(microsecond=0)
                print("inicia servicio de connector status "+ str(fechaHora))
                #reservas = Reservas().ListaActivas()
                #if len(reservas) ==0:
                    #print('No se han encontrado reservas activas') 
                #print(reservas)
                arregloPistolasCerradas = []
                try:
                    pistolas = Pistolas().Listar()
                except:
                        return 0
                for pistola in pistolas:
                        #print(pistola)
                        cargadorId = pistola["cargador_id"]
                        pistolaId = pistola["id"]
                        pistolaNro = pistola["nro_pistola"]
                        #pistolaNombre = pistola["pistola_nombre"]
                        #marquesinaId = reserva["marquesina_id"]
                        cargador = Cargadores().Consultar(cargadorId)
                        
                        cargadorNombre ="" #pistolaNombre.split("-")[0]
                        if len(cargador)>0:
                                cargadorNombre = "STP_" + cargador[0]["nombre"]
                                print(cargadorNombre)

                        #print(cargadorNombre)
                        #pistolaNro = 0 
                        #pistolaEstado = 0
                        #pistola =  Pistolas().Consultar(pistolaId)
                        #if len(pistola)>0:
                         #       pistolaNro = pistola[0]["nro_pistola"]
                        #        pistolaEstado = pistola[0]["pistola_estado"]
                        
                        estado = ""
                        estado = EstadoPistola(cargadorNombre,pistolaNro) 
                        #print(estado)
                        if estado !="":
                                try:
                                        Pistolas().ActualizaConnectorStatus(pistolaId,estado)
                                except:
                                        return 0
                     
                fecha = datetime.now().replace(microsecond=0)
                print("Finaliza Proceso" + str(fecha))
        except Exception as ex:
                print("Se ha provocado un error"+ str(ex))
        
def EstadoPistola( cargadorNombre, pistolaNro):
        try:               
                urlApiCopecComienzaCarga = "http://ocpp.dhemax.cl:3002/connectorStatus"
                #tokenApi = "eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxNCwiZXhwIjoxNjI4NTI1NDM3fQ.ieXeaV7RXVYb4F-mlYyW12IEv3FCFSRiUQq2enGEG64" 
                tokenApi ="eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxNCwiZXhwIjoyNTQ0MDM4NTQzfQ.CBm8kMhAJNf2NW0A-r5kA7qYQ-A0B6ka5at9489SFwg"

                parametros = {'equipo':cargadorNombre,'pistola': int(pistolaNro)}
                #print('parametros que envío para el estado de la pistola ' + str(parametros))
                #print(datetime.now().replace(microsecond=0))
                resp = requests.post(urlApiCopecComienzaCarga, data = json.dumps(parametros) , headers = {'Content-type': 'application/json', "Authorization": tokenApi}, timeout=3)
                #print(datetime.now().replace(microsecond=0))
                #print('codigo respuesta api estado pistola' + str(resp.status_code))
                datos = resp.json()
                #print(datos)
                estado = datos["mensaje"]
                #print(estado)
                return estado
        except Exception as ex:
                print("la Api Fallo")
                print( ex)
                
try: 
        EjecutaProceso()   
     
except:
        time.sleep(5)
        EjecutaProceso()  