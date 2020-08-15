from helpers.ConexionMy import ConexionMy

class Buses():
    
    def Listar(self):
        try:
            parametros = ()
            query ="SELECT * FROM buses"
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