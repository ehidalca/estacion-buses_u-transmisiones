
from helpers.ConexionMy import ConexionMy
from datetime import datetime

class Pistolas:
    def Consultar(self, id):
        try:
            parametros = (id)
            marquesina = ConexionMy().ConsultaQuery("SELECT * FROM pistolas where id=%s", parametros)
            return marquesina
        except Exception as error:
            raise ValueError(str(error))

    def ConsultarPorCargador(self, Cargadorid):
        try:
            parametros = (Cargadorid)
            marquesina = ConexionMy().ConsultaQuery("SELECT * FROM pistolas where cargador_id=%s", parametros)
            return marquesina
        except Exception as error:
            raise ValueError(str(error))
    
    def CambiaEstado(self, pistolaId, estado):
        try:
            fechaHora = datetime.now().replace(microsecond=0)
            parametros = (estado,str(fechaHora),pistolaId)
            query = "UPDATE pistolas SET pistola_estado=%s, pistola_estado_fecha_hora=%s WHERE id=%s"
            proceso = ConexionMy().EjecutaQuery(query, parametros)
            return proceso
        except Exception as error:
            raise ValueError(str(error))

    def AsociaReserva(self, pistolaId, reservaId):
        try:
            #fechaHora = datetime.now().replace(microsecond=0)
            parametros = (reservaId,pistolaId)
            query = "UPDATE pistolas SET reserva_id=%s  WHERE id=%s"
            proceso = ConexionMy().EjecutaQuery(query, parametros)
            return proceso
        except Exception as error:
            raise ValueError(str(error))

    #consultado estado del cargador en la ultima transmision
    def ConsultaUltimaTransmision(self, cargadorNombre, nroPistola):
        try:
            parametros = (cargadorNombre, nroPistola)
            
            query = "SELECT * FROM stp_estacionamiento.cargadores_ultimas_transmisiones where cargador_nombre=%s and pistola_nro=%s"
            
            datos = ConexionMy().ConsultaQuery(query, parametros)
            return datos 
        except Exception as error:
            raise ValueError(str(error))
    
    def ListarPistolasEnProcesoCarga(self):
        try:
            sql="SELECT p.*, c.nombre as cargadorNombre FROM stp_estacionamiento.pistolas p inner join  stp_estacionamiento.cargadores c on p.cargador_id= c.id where p.pistola_estado=3"
            datos = ConexionMy().ConsultaQuery_(sql)
            return datos 
        except Exception as error:
            raise ValueError(str(error))
    def Listar(self):
        try:
            sql = "SELECT * FROM stp_estacionamiento.pistolas"
            datos = ConexionMy().ConsultaQuery_(sql)
            return datos 
        except Exception as error:
            raise ValueError(str(error))
    
    def ActualizaConnectorStatus(self,pistolaId,estado):
        try:
            fechaHora = datetime.now().replace(microsecond=0)
            parametros = (estado, fechaHora, pistolaId)
            query = "UPDATE pistolas SET connector_status=%s , fecha_hora_connector_status=%s WHERE id=%s"
            proceso = ConexionMy().EjecutaQuery(query, parametros)
            return proceso
        except Exception as error:
            raise ValueError(str(error))