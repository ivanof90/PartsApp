from config.dbconfig import pg_config
import psycopg2
from psycopg2.extras import RealDictCursor

class PartsDAO:
    def getConn(self):
        return psycopg2.connect(**pg_config, cursor_factory=RealDictCursor)

    def getAllParts(self):
        conn = self.getConn()
        cursor = conn.cursor()
        query = "select pid, pname, pmaterial, pcolor, pprice from parts;"
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()
        return result

    def getPartById(self, pid):
        conn = self.getConn()
        cursor = conn.cursor()
        query = "select pid, pname, pmaterial, pcolor, pprice from parts where pid = %s;"
        cursor.execute(query, (pid,))
        result = cursor.fetchone()
        conn.close()
        return result

    def getPartsByColor(self, color):
        conn = self.getConn()
        cursor = conn.cursor()
        query = "select * from parts where pcolor = %s;"
        cursor.execute(query, (color,))
        result = cursor.fetchall()
        conn.close()
        return result

    def getPartsByMaterial(self, material):
        conn = self.getConn()
        cursor = conn.cursor()
        query = "select * from parts where pmaterial = %s;"
        cursor.execute(query, (material,))
        result = cursor.fetchall()
        conn.close()
        return result

    def getPartsByColorAndMaterial(self, color, material):
        conn = self.getConn()
        cursor = conn.cursor()
        query = "select * from parts where pmaterial = %s and pcolor = %s;"
        cursor.execute(query, (material,color))
        result = cursor.fetchall()
        conn.close()
        return result

    def getSuppliersByPartId(self, pid):
        conn = self.getConn()
        cursor = conn.cursor()
        query = "select sid, sname, scity, sphone from parts natural inner join supplier natural inner join supplies where pid = %s;"
        cursor.execute(query, (pid,))
        result = cursor.fetchall()
        conn.close()
        return result

    def insert(self, pname, pcolor, pmaterial, pprice):
        conn = self.getConn()
        cursor = conn.cursor()
        query = "insert into parts(pname, pcolor, pmaterial, pprice) values (%s, %s, %s, %s) returning pid;"
        cursor.execute(query, (pname, pcolor, pmaterial, pprice,))
        pid = cursor.fetchone()["pid"]
        conn.commit()
        conn.close()
        return pid

    def delete(self, pid):
        conn = self.getConn()
        cursor = conn.cursor()
        query = "delete from parts where pid = %s;"
        cursor.execute(query, (pid,))
        conn.commit()
        conn.close()
        return pid

    def update(self, pid, pname, pcolor, pmaterial, pprice):
        conn = self.getConn()
        cursor = conn.cursor()
        query = "update parts set pname = %s, pcolor = %s, pmaterial = %s, pprice = %s where pid = %s;"
        cursor.execute(query, (pname, pcolor, pmaterial, pprice, pid,))
        conn.commit()
        conn.close()
        return pid

    def getCountByPartId(self):
        conn = self.getConn()
        cursor = conn.cursor()
        query = "select pid, pname, sum(stock) from parts natural inner join supplies group by pid, pname order by pname;"
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()
        return result

