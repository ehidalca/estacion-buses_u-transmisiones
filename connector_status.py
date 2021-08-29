import time
import json
from datetime import datetime
from Negocio.Reservas import Reservas
from Negocio.Cargadores import Cargadores
from Negocio.Pistolas import  Pistolas
import requests

class Main:
    def __init__(self):
        try:
                while True:  
                        self.CargasFinalizadas()
                        time.sleep(25)
        except:
                while True:  
                        self.CargasFinalizadas()
                        time.sleep(25)



    def CargasFinalizadas(self):
        try:
                print(datetime.now().replace(microsecond=0))
                print("inicia servicio de cargas finalizadas")
                reservas = Reservas().ListaActivas()
                if len(reservas) ==0:
                    print('No se han encontrado reservas activas') 
                #print(reservas)
                arregloPistolasCerradas = []
                for reserva in reservas:
                        cargadorId = reserva["cargador_id"]
                        pistolaId = reserva["pistola_id"]
                        marquesinaId = reserva["marquesina_id"]
                        cargador = Cargadores().Consultar(cargadorId)
                        cargadorNombre =""
                        if len(cargador)>0:
                                cargadorNombre = "STP_" + cargador[0]["nombre"]
                        pistolaNro = 0 
                        pistolaEstado = 0
                        pistola =  Pistolas().Consultar(pistolaId)
                        if len(pistola)>0:
                                pistolaNro = pistola[0]["nro_pistola"]
                                pistolaEstado = pistola[0]["pistola_estado"]
                        #Valores ultimas transmisiones pistola
                        #UT = Pistolas().ConsultaUltimaTransmision(cargadorNombre,pistolaNro)
                        #if len(UT)>0:
                                #SOC = UT[0]["soc"]
                        estado=""
                        estado = self.EstadoPistola(cargadorNombre,pistolaNro) 
                        
                        if estado !="":
                                Pistolas().ActualizaConnectorStatus(pistolaId,estado)
                        #estado="disponible"

                        #if pistolaEstado == 3 and  SOC >=99 and (estado =="disponible" or estado=="terminando"):
                        #        usuarioId = 6
                        #        amperes = 0
                        #        proceso = Carga().Detiene(marquesinaId,cargadorId,pistolaId,amperes,SOC, usuarioId)
                        #        pistolaCambiaEstado = Pistolas().CambiaEstado(pistolaId,4)
                                #fechaHora = datetime.now().replace(microsecond=0)
                        #        arregloPistolasCerradas.append({'cargador': cargadorNombre ,'pistolaNro': pistolaNro })
                fecha = datetime.now().replace(microsecond=0)
                print("Finaliza Proceso" + str(fecha ))
        except Exception as ex:
                print("Se ha provocado un error"+ str(ex))
        

    def CargasFinalizadasv2(self):
        try:
                fechaHora = datetime.now().replace(microsecond=0)
                print("inicia servicio de connector status"+ str(fechaHora))
                #reservas = Reservas().ListaActivas()
                #if len(reservas) ==0:
                    #print('No se han encontrado reservas activas') 
                #print(reservas)
                arregloPistolasCerradas = []
                pistolas = Pistolas().Listar()
                for reserva in pistolas:
                        cargadorId = reserva["cargador_id"]
                        pistolaId = reserva["pistola_id"]
                        #marquesinaId = reserva["marquesina_id"]
                        cargador = Cargadores().Consultar(cargadorId)
                        print(cargador)
                        cargadorNombre =""
                        if len(cargador)>0:
                                cargadorNombre = "STP_" + cargador[0]["nombre"]
                        pistolaNro = 0 
                        pistolaEstado = 0
                        pistola =  Pistolas().Consultar(pistolaId)
                        if len(pistola)>0:
                                pistolaNro = pistola[0]["nro_pistola"]
                                pistolaEstado = pistola[0]["pistola_estado"]
                        
                        estado=""
                        estado = self.EstadoPistola(cargadorNombre,pistolaNro) 
                        
                        if estado !="":
                                #Pistolas().ActualizaConnectorStatus(pistolaId,estado)
                     
                fecha = datetime.now().replace(microsecond=0)
                print("Finaliza Proceso" + str(fecha ))
        except Exception as ex:
                print("Se ha provocado un error"+ str(ex))
        
    def EstadoPistola(self, cargadorNombre, pistolaNro):
        try:               
                urlApiCopecComienzaCarga = "http://ocpp.dhemax.cl:3002/connectorStatus"
                tokenApi = "eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxNCwiZXhwIjoxNjI4NTI1NDM3fQ.ieXeaV7RXVYb4F-mlYyW12IEv3FCFSRiUQq2enGEG64"  
                parametros = {'equipo':cargadorNombre,'pistola': int(pistolaNro)}
                #print('parametros que envío para el estado de la pistola ' + str(parametros))
                #print(datetime.now().replace(microsecond=0))
                resp = requests.post(urlApiCopecComienzaCarga, data = json.dumps(parametros) , headers = {'Content-type': 'application/json', "Authorization": tokenApi}, timeout=30)
                #print(datetime.now().replace(microsecond=0))
                #print('codigo respuesta api estado pistola' + str(resp.status_code))
                datos = resp.json()
                #print(datos)
                estado = datos["mensaje"]
                #print(estado)
                return estado
        except Exception as ex:
                return 
                
try:
        Main()
except:
        Main()