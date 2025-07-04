import sqlite3


class person():

    def add_email(self, email):
        self.email = email

    def add_password(self, password):
        self.password = password


class Database():
    def __init__(self):
        self.conn = sqlite3.connect('datapool.db')
        self.c = self.conn.cursor()
        try:
            self.c.execute("""CREATE TABLE info(
							email text,
							password text
							)""")
            self.conn.commit()
        except:
            print('table already exists !!')

    def add_entry(self, person_obj):
        with self.conn:
            self.c.execute('INSERT into info values(:email, :password)',
                           ({'email': person_obj.email, 'password': person_obj.password}))
        self.conn.commit()

    def select_by_email(self, person_obj=None, email=None):
        if person_obj is not None:
            with self.conn:
                self.c.execute('SELECT * from info where email = (:email)', ({'email': person_obj.email}))
                return self.c.fetchone()
        else:
            with self.conn:
                self.c.execute('SELECT * from info where email = (:email)', ({'email': email}))
                return self.c.fetchone()