from config.dbconfig import pg_config
from psycopg2.extras import RealDictCursor
import psycopg2

class SupplierDAO:
    def getConn(self):
        #Using RealDictCursor, the result set now is retreived in form of a dict, instead of a tuple
        return psycopg2.connect(**pg_config, cursor_factory=RealDictCursor) #**pg_config unpacks
        # the dictionary into the parameters required by psycopg

    def getAllSuppliers(self):
        conn = self.getConn()
        cursor = conn.cursor()
        query = "select * from supplier;"
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()
        return result

    def getSupplierById(self, sid):
        conn = self.getConn()
        cursor = conn.cursor()
        query = "select * from supplier where sid = %s;"
        cursor.execute(query, (sid,))
        result = cursor.fetchone()
        conn.close()
        return result

    def getPartsBySupplierId(self, sid):
        conn = self.getConn()
        cursor = conn.cursor()
        query = "select pid, pname, pmaterial, pcolor, pprice, qty from parts natural inner join supplier natural inner join supplies where sid = %s;"
        cursor.execute(query, (sid,))
        result = cursor.fetchone()
        conn.close()
        return result

    def getSuppliersByCity(self, city):
        conn = self.getConn()
        cursor = conn.cursor()
        query = "select * from supplier where scity = %s;"
        cursor.execute(query, (city,))
        result = cursor.fetchall()
        conn.close()
        return result

    def insert(self, sname, scity, sphone):
        conn = self.getConn()
        cursor = conn.cursor()
        query = "insert into supplier(sname, scity, sphone) values (%s, %s, %s) returning sid;"
        cursor.execute(query, (sname, scity, sphone))
        sid = cursor.fetchone()["sid"]
        conn.commit()
        conn.close()
        return sid