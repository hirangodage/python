import pyodbc 
import json
con = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=localhost;"
                      "Database=xxx;"
                      "Trusted_Connection=yes;")


cursor = con.cursor()
cursor.execute('SELECT ServerName,ID, ServerName as SN FROM Server')
rows = cursor.fetchall()
field_names = [i[0] for i in cursor.description]
fr=open("D:\\files\\jdata.json","w")
json.dump([
{description: value for description, value in zip(field_names, row)}
for row in rows],fr,indent=4)
#print(rows)
cursor.close()
con.close()
