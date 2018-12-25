import mysql.connector

class usuario:

    def abrir(self):
        conexion=mysql.connector.connect(host="localhost", 
                                              user="root", 
                                              passwd="", 
                                              database="bd3",
                                              use_unicode=True, 
                                              raw=False, 
                                              buffered=True, 
                                              connection_timeout=300)
        return conexion

    def Insertar(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into registrar(Nombre, Apellido, Cedula, Edad) values (%s,%s,%s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consultar(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select Nombre, Apellido, Cedula, Edad from registrar where Cedula = %s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall()   

    def ListaDeDatos(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select Cedula, Nombre, Apellido, Edada from registrar"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()
               


   

    