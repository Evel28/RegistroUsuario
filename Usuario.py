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

    def Actualizar(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="update registrar set Nombre = %s, Apellido = %s, Edad = %s where Cedula = %s"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        return cursor.rowcount # retornamos la cantidad de filas modificadas

    def consultar(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select Nombre, Apellido, Cedula, Edad from registrar where Cedula = %s" # Corrección en edad por ortografía.
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall()   

    def ListaDeDatos(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select Cedula, Nombre, Apellido, Edad from registrar" 
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()
               


   

    