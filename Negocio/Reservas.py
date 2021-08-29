from helpers.ConexionMy import ConexionMy
from datetime import datetime
class Reservas:

    def Reserva(self,marquesinaId,cargadorId,pistolaId, patente, usuarioId):
        try:
            fecha_hora = str(datetime.now().replace(microsecond=0))
            estado = 1
            parametros = (fecha_hora,estado , marquesinaId, cargadorId,pistolaId , patente, usuarioId)
            proceso = ConexionMy().EjecutaQueryId("INSERT INTO reservas (fecha_hora_reserva, estado, marquesina_id, cargador_id, pistola_id, patente, usuario_Id) VALUES(%s,%s,%s,%s,%s,%s,%s)", parametros)
            return proceso
        except Exception as error:
            raise ValueError(str(error))
      
    def TraeActivo(self,marquesinaId,cargadorId,pistolaId,estado):
        try:
            fecha_hora = (datetime.now().replace(microsecond=0))
            fecha = str(fecha_hora.date())
            parametros = (fecha, marquesinaId, cargadorId, pistolaId, estado)
            sql = "SELECT * FROM reservas WHERE date(fecha_hora_reserva)=%s and marquesina_id=%s and cargador_id=%s and pistola_id=%s and estado = %s"
            resultado = ConexionMy().ConsultaQuery(sql,parametros)
            return resultado
        except Exception as error:
            raise ValueError(str(error))
    
    def Verifica(self,marquesinaId,cargadorId,pistolaId,estado):
        try:
            consulta = self.TraeActivo(marquesinaId,cargadorId,pistolaId,estado)
            if len(consulta)>0:
                return True
            return False
            
        except Exception as error:
            raise ValueError(str(error))

    def Consulta(self,reservaId):
        parametros = (reservaId)
        sql = "SELECT * FROM reservas WHERE id = %s"
        resultado = ConexionMy().ConsultaQuery(sql,parametros)
        return resultado
    
    def CambiaEstado(self,reservaId, estado):
        try:
            #fecha_hora = str(datetime.now().replace(microsecond=0))
            
            parametros = (estado, reservaId)
            proceso = ConexionMy().EjecutaQuery("UPDATE reservas SET estado=%s where id =%s", parametros)
            return proceso
        except Exception as error:
            raise ValueError(str(error))
    
    #lista reservas activas
    def ListaActivas(self):
        try:
            parametros = (1)
            fecha_hora = (datetime.now().replace(microsecond=0))
            fecha = str(fecha_hora.date())
         
            reservas = ConexionMy().ConsultaQuery("Select * from reservas  where date(fecha_hora_reserva) ='"+ fecha +"' and estado =%s", parametros)
            return reservas
        except Exception as error:
            raise ValueError(str(error))
    
    def ListaPorEstado(self, estado):
        try:
            parametros = (estado)
            reservas = ConexionMy().ConsultaQuery("Select * from reservas where estado =%s", parametros)
            return reservas
        except Exception as error:
            raise ValueError(str(error))
        