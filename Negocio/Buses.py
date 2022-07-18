from helpers.ConexionMy import ConexionMy

class Buses():
    
    def Listar(self):
        try:
            parametros = ()
            query ="SELECT * FROM buses order by ppu"
            busesDatos = ConexionMy().ConsultaQuery(query, parametros)   
            return busesDatos
        except: 
            raise
    
    def ConsultaPorPantente(self, patente):
        try:
            parametros = (patente)
            query ="SELECT * FROM stp_estacionamiento.sonda_ultimas_transmisiones where ppu =%s"
            busDatos = ConexionMy().ConsultaQuery(query, parametros)   
            return busDatos
        except: 
            raise
    
    def InsertaBusesProximos(self):
        try:
            query = "INSERT INTO buses_llegando_maipu(" + \
            " ppu,  " + \
            " bus_tipo,  " + \
            " pto1_fecha,  " + \
            " pto1_hora,  " + \
            " pto1_latitud,  " + \
            " pto1_longitud, " + \
            " pto2_fecha,  " + \
            " pto2_hora,  " + \
            " pto2_latitud,  " + \
            " pto2_longitud, " + \
            " brujula, " + \
            " servicio, " + \
            " sentido, " + \
            " servicio_sentido_a_bordo_del_bus, " + \
            " tracktec_SOC, " + \
            " dentro_geo_pto1, " + \
            " dentro_geo_pto2, " + \
            " en_estudio " + \
            " )   " + \
            " (SELECT  " + \
            " ppu,  " + \
            " bus_tipo,  " + \
            " pto1_fecha,  " + \
            " pto1_hora,  " + \
            " pto1_latitud,  " + \
            " pto1_longitud, " + \
            " pto2_fecha,  " + \
            " pto2_hora,  " + \
            " pto2_latitud,  " + \
            " pto2_longitud, " + \
            " brujula, " + \
            " servicio, " + \
            " sentido, " + \
            " servicio_sentido_a_bordo_del_bus, " + \
            " tracktec_SOC, " + \
            " dentro_geo_pto1, " + \
            " dentro_geo_pto2, " + \
            " en_estudio " +\
            " FROM " + \
            " sonda_ultimas_transmisiones " + \
            " WHERE " + \
            " (brujula < - 61 OR brujula > 147)" + \
            " AND bus_tipo='e'  "+ \
            " AND (dentro_geo_pto1 = 1 OR dentro_geo_pto2 = 1)" + \
            " AND (ppu NOT IN (SELECT ppu FROM buses_llegando_maipu)))"
            #print(query)
            return ConexionMy().EjecutaQueryN(query)
        except:
            raise
   
    def EliminaRegistros(self):
         try:
            print("elimina")
            query = "DELETE FROM buses_llegando_maipu"
            return ConexionMy().EjecutaQueryN(query)
         except:
            raise
   