from helpers.ConexionMy import ConexionMy
from datetime import datetime

class UltimasTransmisiones():
    
    def ConsultaPorPantente(self, patente):
        try:
            parametros = (patente)
            query ="SELECT * FROM stp_estacionamiento.sonda_ultimas_transmisiones where ppu =%s"
            busDatos = ConexionMy().ConsultaQuery(query, parametros)   
            return busDatos
        except: 
            raise

    def ActualizaPantente(self, patente,pto1_latitud, pto1_longitud, pto1_fecha,pto1_hora, pto2_latitud, pto2_longitud, pto2_fecha, pto2_hora, servicio, sentido, brujula, servicioSentidoABordoDelBus, SOC):
        try:
            fechaHora = datetime.now().replace(microsecond=0) 
            #fecha = str(fechaHora.date())
            #hora  = str(fechaHora.time())
            parametros= (pto1_fecha,pto1_hora,pto1_latitud, pto1_longitud,pto2_fecha, pto2_hora,pto2_latitud, pto2_longitud,str(brujula),servicio, sentido, servicioSentidoABordoDelBus, SOC, patente)
            query ="UPDATE stp_estacionamiento.sonda_ultimas_transmisiones set pto1_fecha=%s,pto1_hora=%s, pto1_latitud=%s, pto1_longitud=%s, pto2_fecha=%s,pto2_hora=%s, pto2_latitud=%s, pto2_longitud=%s, brujula=%s, servicio=%s, sentido=%s, servicio_sentido_a_bordo_del_bus=%s, tracktec_SOC=%s  WHERE ppu =%s"
            #print(query)
            ConexionMy().EjecutaQuery(query,parametros)
        except: 
            raise

         