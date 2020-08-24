from helpers.ConexionMy import ConexionMy

class Tracktec:
    def UltimaTransmision(self,ppu):
        try:
           #print(ppu)
            parametros = (ppu)
            datos = ConexionMy().ConsultaQuery("select * from tracktec.ultimas_transmisiones where replace(patente,'-','') =%s", parametros)
            return datos
        except Exception as ex:
            print("error"  +str(ex))
    
    def TodasUltimasTransmisiones(self):
        try:
           #print(ppu)
            parametros =()
            datos = ConexionMy().ConsultaQuery("SELECT patente, carga,odometro,latitud,longitud, fecha_evento, hora_evento  FROM tracktec.ultimas_transmisiones order by patente; ", parametros)
            return datos
        except Exception as ex:
            print("error"  +str(ex))
    
    def SOC(self,ppu):
        SOC="0"
        datos = self.UltimaTransmision(ppu)
        print('prueba' +str(datos))
        if len(datos)>0:
            SOC = datos[0]["carga"]
        return SOC
        
