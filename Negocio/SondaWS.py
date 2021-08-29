from helpers.ConexionPG import ConexionPG
from datetime import datetime,timedelta


class SondaWS():
    
    def UltimaTransmisionPorBus(self, patente):
        try:
            fechaHora = datetime.now().replace(microsecond=0)  
            fecha = fechaHora.date()        
            parametros = ()
            query = "SELECT * from ws_pos_dia_2019 where fecha ='"+ str(fecha) +"' AND REPLACE(patente,'-','') ='"+ patente +"'  limit 2"
            #print(query)3
            ultimaTransmision = ConexionPG().EjecutaConsulta(query)   
            return ultimaTransmision
        except: 
            raise

    def Datos30Seg(self):
        try:
            fechaHora = datetime.now().replace(microsecond=0)  
            fechaHora = fechaHora + timedelta(seconds = -40)
            print(fechaHora)
            fecha = fechaHora.date()  
            hora = fechaHora.time()      
            parametros = ()
            query = "SELECT * from ws_pos_dia_temp where fecha ='"+ str(fecha) +"' and hora >='"+ str(hora) +"'"  
            print(query)
            #print(query)
            ultimaTransmision = ConexionPG().EjecutaConsulta(query)   
            return ultimaTransmision
        except: 
            raise
    
    def DatosJefe(self):
        try:
                fechaHora = datetime.now().replace(microsecond=0)  
                fecha = str(fechaHora.date()) 
                query = "SELECT DISTINCT(N.patente),N.fecha, T.hora AS Hora1, T.latitudgps AS Lat1, T.longitudgps AS Long1, L.hora AS Hora2, L.latitudgps AS Lat2, L.longitudgps AS Lon2, L.servicio As Serv, L.sentido AS Sent, L.servicio_sentido_a_bordo_del_bus AS Consola" + \
                        " FROM ws_pos_dia_2019 T " + \
                        " RIGHT JOIN (SELECT t.patente,t.fecha,MAX(t.id) AS I " + \
                        " FROM ws_pos_dia_2019 t " + \
                        " WHERE t.fecha = '"+ fecha +"' AND t.patente LIKE 'P%' AND t.patente NOT LIKE 'PW%' AND t.id NOT IN (SELECT B.IX " + \
                        " FROM (SELECT r.patente,r.fecha,MAX(r.id) AS IX FROM ws_pos_dia_2019 r WHERE r.fecha = '"+fecha+"' AND r.patente LIKE 'P%' AND r.patente NOT LIKE 'PW%' "+\
                        " GROUP BY r.patente,r.fecha) B)" +\
                        " GROUP BY t.patente,t.fecha) AS N " +\
                        " ON T.id = N.I AND T.fecha = N.fecha AND T.patente = N.patente" + \
                        " RIGHT JOIN(SELECT DISTINCT(V.patente) as ppu,V.fecha, D.hora, D.latitudgps,D.longitudgps, D.servicio, D.sentido, D.servicio_sentido_a_bordo_del_bus" +\
                        " FROM ws_pos_dia_2019 D " + \
                        " RIGHT JOIN (SELECT patente,fecha,MAX(id) as  I" + \
                        " FROM ws_pos_dia_2019 " + \
                        " WHERE fecha = '"+ fecha +"' AND patente LIKE 'P%' AND patente NOT LIKE 'PW%'" + \
                        " GROUP BY patente,fecha) AS V " + \
                        " ON D.id = V.I AND D.fecha = V.fecha AND D.patente = V.patente " + \
                        " WHERE D.fecha = '"+ fecha +"' AND D.patente LIKE 'P%' AND D.patente NOT LIKE 'PW%'" + \
                        " ORDER BY V.patente) AS L " +\
                        " ON T.patente = L.ppu" + \
                        " WHERE T.fecha = '"+fecha +"' AND T.patente LIKE 'P%' AND T.patente NOT LIKE 'PW%'" + \
                        " ORDER BY N.patente" 
                datos  = ConexionPG().EjecutaConsulta(query)   
                return datos       
        except: 
            raise