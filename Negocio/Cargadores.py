from helpers.ConexionMy import ConexionMy

class Cargadores:
    def Consultar(self, id):
        try:
            parametros = (id)
            marquesina = ConexionMy().ConsultaQuery("SELECT * FROM cargadores where id=%s", parametros)
            return marquesina
        except Exception as error:
            raise ValueError(str(error))
    
    def ConsultarPorMarquesinaId(self, marquesinaId):
        try:
            parametros = (marquesinaId)
            sql="SELECT * FROM stp_estacionamiento.cargadores where marquesina_id = %s"
            marquesina = ConexionMy().ConsultaQuery(sql,parametros)
            return marquesina
        except Exception as error:
            raise ValueError(str(error))
    