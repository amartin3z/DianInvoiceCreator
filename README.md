# Soriana | Portal Descarga Masiva SAT

El comando importpeppol extrae la informacion de https://docs.peppol.eu/poacc/billing/3.0/codelist/ para crear modelos, csv y fixtures

La manera de ejecutar este comando es la siguiente:

~~~
python manage.py importpeppol --settings=my.settings.path
~~~
De esta manera, obtendra todas las listas (18) de la url

Para realizar la descarga de los CSV es necesario contar con el driver del navegador a utilizar:

Chrome -> https://chromedriver.chromium.org/
Mozilla -> https://github.com/mozilla/geckodriver/releases
Opera -> https://github.com/operasoftware/operachromiumdriver/releases

Este driver debera colocarse en la ruta de la version python que se encuentre utilizando. Por ejemplo:
~~~
/usr/local/bin/python3.7

cp ~/Downloads/geckodriver /usr/local/bin/
chmod 755 /usr/local/bin/geckodriver
~~~

Los argumentos que componen este comando, son todos opcionales, y son los siguientes:
* -l 	(--list) 			--> 	Importa una lista de Peppol. Si no es especificada el nombre, se tomaran todas
* -o 	(--only-import) 	-->		Importa solamente la lista, sin descargar (IMPORTANTE: El archivo a importar debe existir)
* -ni (--no-import)			-->		No importa las listas a la Base de Datos
* -nf (--no-file)			-->		Crea solo CSV de las listas especificadas sin crear el modelo
* -nm (--no-model)			-->		Crea solo el modelo de las listas especificadas sin crear CSV (IMPORTANTE: El archivo CSV debe existir)
* -m 	('--no-migrate')	-->		Impide la migracion de los modelos descargados

~~~
LIST_CHOICES = {
	1: 'ICD',
	2: 'EAS',
	3: '3166',
	4: '4217',
	5: 'Recommendation 20',
	6: 'Recommendation 21',
	7: 'Duty',
	8: 'Item',
	9: 'Invoice',
	10: 'Credit',
	11: 'Invoiced',
	12: 'UNCL2005',
	13: 'UNCL4461',
	14: 'UNCL5189',
	15: 'UNCL7161',
	16: 'IANA',
	17: 'SEPA',
	18: 'VATEX',
}
~~~


Ejemplos:
* Descargar solo la lista VATEX realizando todas las acciones:
~~~
python manage.py importpeppol -l 18 --settings=my.settings.path
~~~

* Descargar archivo CSV:
~~~
python manage.py importpeppol -l 18 --no-models --no-import --no-migrate --settings=my.settings.path
~~~

* Importar CSV existente:
~~~
python manage.py importpeppol -l 18 --only-import --settings=my.settings.path

python manage.py importpeppol -l 18 --no-file --no-model --no-migrate --settings=my.settings.path
~~~

* Crear modelos sin migrarlos ni importarlos:
~~~
python manage.py importpeppol -l 18 --no-file --no-import --no-migrate --settings=my.settings.path
~~~

* Crear modelos, migrarlos e importar el contenido de los CSV:
~~~
python manage.py importpeppol -l 18 --no-file --settings=my.settings.path
~~~

NOTE IMPORTANTE:
Los archivos CSV ANNEXI.csv y ANNEXII_ANNEXIII.csv no son importandos a traves del comando debido a los caracteres especiales en su contenido. Para importarse, se recomienda hacer uso de lo siguiente:

~~~
import psycopg2
conn = psycopg2.connect('host=localhost dbname=databasename user=username password=password')

cursor = conn.cursor()
cursor.execute('ROLLBACK')

with open('/path/to/csv/ANNEXI.csv', 'r') as file:
	next(file)
	cursor.copy_from(file, 'peppol_annexi', sep=',')

cursor.execute('COMMIT')
cursor.close()
conn.close()

~~~