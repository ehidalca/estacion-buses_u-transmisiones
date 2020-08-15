import Bd
class Comercios:

    def Registrar(self, nombre, tipo_comercio, pais_id):
        try:
            conexion = Bd.Bd()
            resultado = conexion.ConsultaQueryId("INSERT INTO base_comercios(nombre, pais_id, tipo_comercio_id) VALUES('"+ nombre +"',"+str(pais_id)+",'"+ tipo_comercio+"')")
            return resultado
        except Exception as inst:
            raise ValueError(str(inst))
   
 