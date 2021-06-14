import sqlite3
db = sqlite3.connect('data.sqlite')

cur = db.cursor()

if db:
    print('Successfully connect')
else:
    print('Fail')

def create_table():
    # Create User table
    query = '''
        CREATE TABLE USERS(
            user_id varchar(255),
            user_name varchar(255),
            tokens int,
            primary key(user_id)
        )
    '''
    cur.execute(query)
    db.commit()

    # Create TRANS table
    query = '''
        CREATE TABLE TRANS(
            trans_id integer primary key autoincrement,
            from_user_id varchar(255),
            to_user_id varchar(255),
            trans_type varchar(50),
            trans_amount INT,
            foreign key(from_user_id) references USERS(user_id) on delete cascade,
            foreign key(to_user_id) references USERS(user_id) on delete cascade
        )
    '''
    cur.execute(query)
    db.commit()

def create_user(user_id,username,token=0):
    exec = "INSERT INTO USERS(user_id,user_name,tokens) values('{}', '{}', {}); ".format(user_id,username,token)
    # print(exec)
    cur.execute(exec)
    db.commit()

def add_token(user_id, tokens):
    # select current left tokens
    exec = "Select tokens from users where user_id = '{}'".format(user_id)
    res = cur.execute(exec).fetchone()
    if res:
        res = res[0]
    update_exec = "Update users set tokens={} where user_id ='{}'".format(res+int(tokens), user_id)
    
    try:
        cur.execute(update_exec)
        db.commit()
        return "Successfully Update"
    except Exception as e: 
        return e

    # then add

def select_token(user_id):
    exec = "Select tokens from users where user_id = '{}'".format(user_id)
    res = cur.execute(exec).fetchone()
    if res:
        res = res[0]

    return res


def create_transaction():
    pass

def delete_user():
    pass


