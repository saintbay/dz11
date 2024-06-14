import psycopg2
class Database_manager(): 
    def __init__(self, dbname, host, port, user, password): 
        self.dbname = dbname 
        self.host = host 
        self.port = port 
        self.user = user 
        self.password = password 
        self.connection = None 
        self.cursor = None 
 
    def connect(self): 
        try: 
            self.connection = psycopg2.connect(dbname=self.dbname, host=self.host, port=self.port, user=self.user, password=self.password) 
            print("Connected successfully") 
        except Exception as e: 
            print(f"Connection refused: {e}") 
        else: 
            self.cursor = self.connection.cursor() 
 
    def insert(self, table_name, **kwargs): 
        columns = ', '.join([column for column in kwargs.get('columns', [])]) 
        values = ', '.join([f"'{column}'" if type(column) == str else f"{column}" for column in kwargs.get('values', [])]) 
        print(columns) 
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})" 
        print(query) 
 
database = Database_manager('postgres', '127.0.0.1', 5432, user='postgres', password='123456') 
database.connect() 
database.insert('driver', columns=['name', 'car', 'color', 'number', 'class', 'phone_number'], values=['adil', 'toyota', 'black', '999', 'business', '77012276434'])
