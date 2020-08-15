import psycopg2

class ConexionPG:
  def __init__(self):
      servidor = "192.168.11.199"
      puerto = "5432"
      usuario = "webservice"
      password = "Sasser.a36*"
      basedatos = "webservice"
      timeout = "100"
      self.cadenaConexion = "dbname='"+basedatos+"' user='"+usuario +"' host='"+ servidor +"' password='"+ password +"'"
  
  def EjecutaConsulta(self,query):
    results = []
    conn = psycopg2.connect(self.cadenaConexion)
    cur = conn.cursor()
    cur.execute(query)
    columns = [column[0] for column in cur.description]
    rows = cur.fetchall()  
    for row in rows:
        results.append(dict(zip(columns,row))) 
    conn.close()
    return results



