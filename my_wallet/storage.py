from services import db_connect_decorator
# __all__ = [
# 		'initialize'
# 		]

SQL_CREATE_NEW_USER = '''INSERT INTO user(firstname, lastname, email) 
						VALUES (%s, %s, %s)'''

SQL_SHOW_ALL_USERS = '''SELECT * FROM user'''

SQL_SHOW_USER_BY_PK = f'''{SQL_SHOW_ALL_USERS} WHERE id = %s'''

SQL_UPDATE_USER_INFO = '''UPDATE user 
						  SET firstname = %s, lastname = %s, email = %s'''

SQL_DELETE_USER = 'DELETE FROM user WHERE id = %s'


def initialize(cursor, creation_schema):
	with open(creation_schema, 'r') as f:
		cursor.execute(f)

@db_connect_decorator
def create_new_user(cursor, firstname, lastname, email):
	cursor.execute(SQL_CREATE_NEW_USER, (firstname, lastname, email))

@db_connect_decorator
def show_all_users(cursor):
	cursor.execute(SQL_SHOW_ALL_USERS)
	result = cursor.fetchall()
	for line in result:
		print(line)

@db_connect_decorator
def update_user_info(cursor, firstname, lastname, email):
	cursor.execute(SQL_UPDATE_USER_INFO, (firstname, lastname, email))

@db_connect_decorator
def show_user_by_pk(cursor, pk):
	cursor.execute(SQL_SHOW_USER_BY_PK, (pk,))
	result = cursor.fetchall()
	for line in result:
		print(line)


@db_connect_decorator
def delete_user(cursor, pk):
	cursor.execute(SQL_DELETE_USER, (pk,))

if __name__ == '__main__':
	create_new_user(firstname='Neko', lastname="San", email='Yanix2x2')
	show_all_users()	

