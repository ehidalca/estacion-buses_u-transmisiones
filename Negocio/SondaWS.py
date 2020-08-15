from helpers.ConexionPG import ConexionPG
from datetime import datetime

class SondaWS():
    
    def UltimaTransmisionPorBus(self, patente):
        try:
            fechaHora = datetime.now().replace(microsecond=0)  
            fecha = fechaHora.date()        
            parametros = ()
            query = "SELECT * from ws_pos_dia_2019 where fecha ='"+ str(fecha) +"' AND REPLACE(patente,'-','') ='"+ patente +"'  limit 1"
            ultimaTransmision = ConexionPG().EjecutaConsulta(query)   
            return ultimaTransmision
        except: 
            raise
