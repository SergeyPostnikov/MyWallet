from configparser import ConfigParser
from mysql.connector import connect, Error


def read_db_config(filename='config.ini', section='mysql'):
	""" Read database configuration file and return a dictionary object
	:param filename: name of the configuration file
	:param section: section of database configuration
	:return: a dictionary of database parameters
	"""
	# create parser and read ini configuration file
	parser = ConfigParser()
	parser.read(filename)
 
	# get section, default to mysql
	db = {}
	if parser.has_section(section):
		items = parser.items(section)
		for item in items:
			db[item[0]] = item[1]
	else:
		raise Exception(f'{section} not found in the {filename} file')
	return db

def db_connect_decorator(func):
	def wrapper(*args, **kwargs):
		config = read_db_config()
		try:
			print('Connecting to MySQL database...')
			with connect(**config) as conn:
				if conn.is_connected():
					print('connection established.')
					with conn.cursor() as cursor:
						res = func(cursor=cursor,  *args, **kwargs)						
						conn.commit()
						return res

				else:
					print('connection failed.')
		except Error as e:
			print(e)
	return wrapper

