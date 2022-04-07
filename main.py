
#__int__py

from flask import Flask,request
import json
from flaskext.mysql import MySQL

#import mysql.connector 
#conexion = mysql.connector.connect(user='enrique',password='enrique22',
#                                    host='tallerMecanicohdz.com',
#                                    database='taller_mecanico',
#                                    port='3306')
app= Flask (__name__)
app.config['MYSQL_DATABASE_HOST']="localhost"
app.config['MYSQL_DATABASE_PORT']=3306
app.config['MYSQL_DATABASE_USER']="root"
app.config['MYSQL_DATABASE_DB']="taller_mecanico"

mysql = MySQL()
mysql.init_app(app)
##@app.get('/')
#---------------------------------------------------------------------
@app.get('/registro')
def index():

   #nombre_cliente=request.args.get("nombre_cliente")
   #telefono=request.args.get("telefono")
   modelo=request.args.get("modelo")
   #servicio=request.args.get("servicio")
   #placas=request.args.get("placas")
   print (modelo)
   if not modelo:
      return "parametros inclompletos",400
   
   cursor = mysql.get_db().cursor()

   cursor.execute('''
         INSERT INTO `cliente`(`modelo`) 
         VALUES (%s)
      ''',(modelo))
      
 #cursor.execute('''
 #        INSERT INTO `cliente`(`nombre_cliente`,`telefono`,`modelo`,`servicio`,`placas`) 
 #        VALUES (%s,%s,%s,%s,%s)
 #     ''',(nombre_cliente,telefono,modelo,servicio,placas))


   mysql.get_db().commit()


   #print(clientes)
   return "cliente registrado"
#---------------------------------------------------------------------
##consutas de clientes
@app.get('/clientess')
def index1():
   cursor = mysql.get_db().cursor()
   #sirve base de datos
   cursor.execute('SELECT nombre_cliente FROM taller_mecanico.cliente')
   clientes=cursor.fetchall()
   print(clientes)
   clientes_json=json.dumps(clientes)
   clientes_str="Estos son los clientes: "+str(clientes_json).replace("[","").replace("]","")
   return clientes_str

#---------------------------------------------------------------------
##consutas de mecanicos
@app.get('/mecanicos')
def index2():
   cursor = mysql.get_db().cursor()
   cursor.execute('SELECT nombre FROM taller_mecanico.mecanicos')
   mecanico=cursor.fetchall()
   print(mecanico)
   mecanico_json=json.dumps(mecanico)
   mecanico_str="Estos son los mecanicos de nuestro taller: "+str(mecanico_json).replace("[","").replace("]","")
   return mecanico_str

#---------------------------------------------------------------------
##consutas de servicio
@app.get('/servicio')
def servicio():
   cursor = mysql.get_db().cursor()
   cursor.execute("SELECT servicio FROM taller_mecanico.servicio where taller_mecanico.servicio.tamaño = 'Compacto'")
   servicio=cursor.fetchall()
   print(servicio)
   servicio_json=json.dumps(servicio)
   servicio_str="Estos son los servicio de nuestro taller: "+str(servicio_json).replace("[","").replace("]","")
   return servicio_str
#---------------------------------------------------------------------

