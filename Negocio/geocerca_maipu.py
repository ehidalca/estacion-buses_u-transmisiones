class geocerca_maipu(object):
    # Constructor
    def __init__(self):
        # recibe dos puntos lat,lon y devuelve puntos ordenados
        # de izq,der,abajo,arriba para hacer geocercas
        def ordenar_geocerca(lat1, lon1, lat2, lon2):
            if lon1 < lon2 and lat1 < lat2:
                return lon1, lon2, lat1, lat2
            elif lon1 < lon2 and lat1 >= lat2:
                return lon1, lon2, lat2, lat1
            elif lon1 >= lon2 and lat1 < lat2:
                return lon2, lon1, lat1, lat2
            else:
                return lon2, lon1, lat2, lat1


        # devuelve pendiente entre dos puntos, a y b son tuplas x,y
        def pendiente(a, b):
            if a[0] - b[0] == 0:
                return 0
            else:
                return (a[1] - b[1]) / (a[0] - b[0])

        # devuelve el coeficiente n de ecuacion de una recta dados dos puntos,
        # p es la pendiente de la recta y g un punto de esta
        def corte(p, g):
            return g[1]-g[0]*p*1.0

        # devuelve los coeficientes m y n de la ecuacion de
        # la recta y=mx+n dados dos puntos d y e
        def coef_eq_recta(d, e):
            return [pendiente(d, e), corte(pendiente(d, e), d)]

        # devuelve coef de recta que pasa por dos tuplas latlon y
        # ademas devuelve la latitud menor y la mayor en orden m,n,latmenor,latmayor
        def eq_geocerca_Romboide(latlon1, latlon2):
            coef = coef_eq_recta((latlon1[1], latlon1[0]), (latlon2[1], latlon2[0]))
            if latlon1[0] < latlon2[0]:
                return [coef[0], coef[1], latlon1[0], latlon2[0]]
            else:
                return [coef[0], coef[1], latlon2[0], latlon1[0]]

        self.dist = 0.0001*6
        self.geocerca_it2 = ordenar_geocerca(-33.5222, -70.8009, -33.5199, -70.7974)
        self.eq_geocerca_it1_romboide = eq_geocerca_Romboide([-33.5222, -70.8009], [-33.5199, -70.8015])

    def __repr__(self):
        return str(self.dist)


    def cumple_geocerca_maipu(self, lat, lon):
        # boolean para filtrar columnas fuera del rombo descrito por funcion coordenadas_poligono_romboide
        def geocerca_romboideX(Lat, Lon, eq_rombo, Ancho_geocerca_ejeX):
            return ((Lat - eq_rombo[0]*Lon - eq_rombo[1] > 0) and
                    (Lat - eq_rombo[0]*Lon - eq_rombo[1] < -1.0*eq_rombo[0]*Ancho_geocerca_ejeX) and
                    (Lat > eq_rombo[2]) & (Lat < eq_rombo[3]))

        # boolean para filtrar columnas fuera del cuadrado
        def geocerca_rectangular(Lat, Lon, geocerca_rectangulo):
            return (((Lon >= geocerca_rectangulo[0]) and
                    (Lon <= geocerca_rectangulo[1])) and
                    ((Lat >= geocerca_rectangulo[2]) and
                     (Lat <= geocerca_rectangulo[3])))

        if (geocerca_rectangular(lat, lon, self.geocerca_it2) or
            geocerca_romboideX(lat, lon, self.eq_geocerca_it1_romboide, self.dist)):
            return 1
        else:
            return 0