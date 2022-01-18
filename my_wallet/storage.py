

if __name__ == '__main__':
	from services import db_connect_decorator
else:
	from my_wallet.services import db_connect_decorator

#----------------------User section-----------------------------------#

SQL_CREATE_NEW_USER = '''INSERT INTO user(firstname, lastname, email) 
						VALUES (%s, %s, %s)'''

SQL_SHOW_ALL_USERS = '''SELECT * FROM user'''

SQL_SHOW_USER_BY_PK = f'''{SQL_SHOW_ALL_USERS} WHERE id = %s'''

SQL_UPDATE_USER_INFO = '''UPDATE user 
						  SET firstname = %s, lastname = %s, email = %s
						  WHERE id = %s'''

SQL_DELETE_USER = 'DELETE FROM user WHERE id = %s'

#--------------------Transations section----------------------------------#

SQL_CREATE_TRANSACTION = '''INSERT INTO 
						  transaction(user_id, description, 
						  amount,	tr_type)
						  VALUES (%s, %s, %s, %s)'''

SQL_DELETE_TRANSACTION = '''DELETE FROM transaction WHERE id = %s'''

SQL_SHOW_ALL_TRANSACTION = '''SELECT * FROM transaction'''

SQL_SHOW_ALL_USER_TRANSACTION = f'''{SQL_SHOW_ALL_TRANSACTION} 
									WHERE user_id = %s'''

SQL_UPDATE_TRANSACTION = '''UPDATE transaction
							SET description = %s, 
						    	amount = %s,
						    	tr_type = %s
						    WHERE id = %s'''

SQL_SUM_OF_TR = ''' SELECT SUM(amount) 
					FROM transaction
					WHERE created_at BETWEEN %s AND %s
					AND user_id = %s
					AND tr_type = %s
					GROUP BY user_id'''



def handler(cursor):
	for user in cursor.fetchall():
		print(user)

# TODO: fixit
@db_connect_decorator
def initialize(cursor, creation_schema):
	with open(creation_schema, 'r') as f:
		cursor.execute(f)

@db_connect_decorator
def create_new_user(cursor, firstname, lastname, email):
	cursor.execute(SQL_CREATE_NEW_USER, (firstname, lastname, email))


@db_connect_decorator
def show_all_users(cursor):
	cursor.execute(SQL_SHOW_ALL_USERS)
	handler(cursor)

@db_connect_decorator
def update_user_info(cursor, firstname, lastname, email, user_id):
	cursor.execute(SQL_UPDATE_USER_INFO, (firstname, lastname, email, user_id))

@db_connect_decorator
def show_user_by_pk(cursor, pk):
	cursor.execute(SQL_SHOW_USER_BY_PK, (pk,))
	handler(cursor)


@db_connect_decorator
def delete_user(cursor, pk):
	cursor.execute(SQL_DELETE_USER, (pk,))
# -------

@db_connect_decorator
def create_transaction(cursor, user_id, description, amount, tr_type):
	cursor.execute(SQL_CREATE_TRANSACTION, (user_id, description, amount, tr_type))


@db_connect_decorator
def delete_transaction(cursor, tr_id):
	cursor.execute(SQL_DELETE_TRANSACTION, (tr_id,))

@db_connect_decorator
def show_all_transactions(cursor):
	cursor.execute(SQL_SHOW_ALL_TRANSACTION)
	handler(cursor)

@db_connect_decorator
def show_all_user_transactions(cursor, pk):
	cursor.execute(SQL_SHOW_ALL_USER_TRANSACTION, (pk,))
	handler(cursor)


@db_connect_decorator
def update_transaction(cursor, tr_id, description, amount, tr_type):
	cursor.execute(SQL_UPDATE_TRANSACTION, (description, amount, tr_type, tr_id ))

@db_connect_decorator
def sum_transaction(cursor, user_id, since, till, tr_type):
	cursor.execute(SQL_SUM_OF_TR, (since, till, user_id, tr_type))
	handler(cursor)




#-----------

# if __name__ == '__main__':
	# create_new_user(firstname='Neko', lastname="San", email='Yanix2x2')
	# update_user_info(firstname='Nekinator', lastname="Shinigami", email='Yanix2x2', user_id='2')
	# show_user_by_pk(pk=2)
	# delete_user(pk=7)
	# show_all_users()
	# create_transaction(user_id=2, description='salary', amount=200, tr_type='income')
	# show_all_transactions()
	# show_all_user_transactions(pk=1)
	# sum_transaction(user_id=2, since='2022-01-17 21:07:20',
	# 				till='2022-01-17 21:20:22',
	# 				tr_type='outcome')
	# update_transaction(tr_id=2, description='bread', amount=0.8, tr_type='outcome')

# todo: date instead of datetime
# todo: return cursor not empty
