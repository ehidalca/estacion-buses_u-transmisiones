import pymysql
import sys

class ConexionMy():
    
    servidor ="192.168.11.150"
    usuario = "root"
    password ="stp.2019"
    baseDatos = "stp_estacionamiento"

    def ConsultaQuery_(self, query):
        results =[]
        db = pymysql.connect(self.servidor,self.usuario,self.password,self.baseDatos)
        cursor = db.cursor()
        cursor.execute(query)
        datos = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        for row in datos:
            results.append(dict(zip(columns,row))) 
        db.close()
        return results
    
    def ConsultaQuery(self, query, data):
    
        results =[]
        db = pymysql.connect(self.servidor,self.usuario,self.password,self.baseDatos)
        cursor = db.cursor()
        cursor.execute(query, data)
        datos = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        for row in datos:
            results.append(dict(zip(columns,row))) 
        db.close()
        return results

    def ConsultaQueryId(self, query):
        db = pymysql.connect(self.servidor,self.usuario,self.password,self.baseDatos)
        cursor = db.cursor()
        cursor.execute(query)
        db.commit()
        datos = cursor.fetchall()
        db.close()
        return db.insert_id() 
    #versioon parametros evita sql inyect
    def EjecutaQuery(self, query, datos):
        db =pymysql.connect(self.servidor,self.usuario,self.password,self.baseDatos)
        cursor = db.cursor()
        try:
            cursor.execute(query,datos)
            db.commit()
            return True
        except Exception as inst:
                db.rollback
                print (inst)
                raise ValueError(str(inst))
        db.close()
      
    def EjecutaQueryN(self, query):
        db =pymysql.connect(self.servidor,self.usuario,self.password,self.baseDatos)
        cursor = db.cursor()
        try:
            cursor.execute(query)
            db.commit()
            return True
        except Exception as inst:
                db.rollback
                print (inst)
                raise ValueError(str(inst))
        db.close()
        
    def EjecutaQueryId(self, query, datos):
        db =pymysql.connect(self.servidor,self.usuario,self.password,self.baseDatos)
        cursor = db.cursor()
        try:
            cursor.execute(query,datos)
            db.commit()
            return cursor.lastrowid
        except Exception as inst:
                db.rollback
                print (inst)
                raise ValueError(str(inst))
        db.close()

