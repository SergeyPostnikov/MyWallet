if __name__ == '__main__':
	from services import db_connect_decorator
else:
	from my_wallet.services import db_connect_decorator

from datetime import date
#----------------------User section-----------------------------------#

SQL_CREATE_NEW_USER = '''INSERT INTO user(firstname, lastname, email) 
						VALUES (%s, %s, %s)'''

SQL_SHOW_ALL_USERS = '''SELECT * FROM user'''

SQL_SHOW_USER_BY_PK = f'''{SQL_SHOW_ALL_USERS} WHERE id = %s'''

SQL_UPDATE_USER_INFO = '''UPDATE user 
						  SET firstname = %s, lastname = %s, email = %s
						  WHERE id = %s'''

SQL_DELETE_USER = 'DELETE FROM user WHERE id = %s'


@db_connect_decorator
def create_new_user(cursor, firstname, lastname, email):
	cursor.execute(SQL_CREATE_NEW_USER, (firstname, lastname, email))


@db_connect_decorator
def show_all_users(cursor):
	cursor.execute(SQL_SHOW_ALL_USERS)
	return cursor.fetchall()

@db_connect_decorator
def update_user_info(cursor, firstname, lastname, email, user_id):
	cursor.execute(SQL_UPDATE_USER_INFO, (firstname, lastname, email, user_id))


@db_connect_decorator
def show_user_by_pk(cursor, pk):
	cursor.execute(SQL_SHOW_USER_BY_PK, (pk,))
	return cursor.fetchall()

@db_connect_decorator
def show_user_by_(cursor, value, column):
	cursor.execute(f'{SQL_SHOW_ALL_USERS} WHERE {column} = "{value}"')	
	return cursor.fetchall()

@db_connect_decorator
def delete_user(cursor, pk):
	cursor.execute(SQL_DELETE_USER, (pk,))


#--------------------Transations section----------------------------------#

SQL_CREATE_TRANSACTION = '''INSERT INTO 
						  transaction(user_id, description, 
						  amount)
						  VALUES (%s, %s, %s)'''

SQL_DELETE_TRANSACTION = '''DELETE FROM transaction WHERE id = %s'''

SQL_SHOW_ALL_TRANSACTION = '''SELECT * FROM transaction'''

SQL_SHOW_ALL_USER_TRANSACTION = f'''{SQL_SHOW_ALL_TRANSACTION} 
									WHERE user_id = %s'''

SQL_UPDATE_TRANSACTION = '''UPDATE transaction
							SET description = %s, 
						    	amount = %s
						    WHERE id = %s'''

SQL_SUM_OF_TR = ''' SELECT SUM(amount), DATE(created_at)  
					FROM transaction
					WHERE created_at BETWEEN %s AND %s 
					AND user_id = %s  
					GROUP BY DATE(created_at)'''


@db_connect_decorator
def create_transaction(cursor, user_id, description, amount):
	cursor.execute(SQL_CREATE_TRANSACTION, (user_id, description, amount))

@db_connect_decorator
def delete_transaction(cursor, tr_id):
	cursor.execute(SQL_DELETE_TRANSACTION, (tr_id,))

@db_connect_decorator
def show_all_transactions(cursor):
	cursor.execute(SQL_SHOW_ALL_TRANSACTION)
	return cursor.fetchall()

@db_connect_decorator
def show_all_user_transactions(cursor, pk):
	cursor.execute(SQL_SHOW_ALL_USER_TRANSACTION, (pk,))
	return cursor.fetchall()

@db_connect_decorator
def update_transaction(cursor, tr_id, description, amount):
	cursor.execute(SQL_UPDATE_TRANSACTION, (description, amount, tr_id ))

@db_connect_decorator
def sum_transaction(cursor, user_id, since, till):
	cursor.execute(SQL_SUM_OF_TR, (since, till, user_id))
	return cursor.fetchall()


#--------------------- usability section --
SQL_MIN_DATE_TR ='''SELECT MIN(DATE(created_at)) 
					FROM transaction
					WHERE user_id = %s'''

@db_connect_decorator
def min_date(cursor, user_id):
	cursor.execute(SQL_MIN_DATE_TR, (user_id,))
	return str(cursor.fetchall()[0][0])


def sum_transaction_on_dur(user_id, since=None, till=None):
	'''rewrite'''
	since = min_date(user_id=user_id) if since is None else since
	till = date.today() if till is None else till
	return sum_transaction(user_id=user_id, since=since, till=till)


# TODO: fixit
@db_connect_decorator
def initialize(cursor, creation_schema):
	with open(creation_schema, 'r') as f:
		cursor.execute(f)







# todo: date instead of datetime : i think it's impossible with default
# todo: rewrite db_conf reader
