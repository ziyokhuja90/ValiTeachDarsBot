import sqlite3


class Database:
    def __init__(self, path_to_db="db.sqlite3"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    # dars qo'shish
    def add_lesson(self, id: str, videoId:str , CountOfLesson: str, info: str , youtube: str , telegram: str , category:str , subcategory: str):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Lessons(id, CountOfLesson, videoId, info, youtube , telegram , category , subcategory) VALUES(?, ?,? , ?, ? ,? ,? ,?)
        """

        self.execute(sql, parameters=(id, videoId, CountOfLesson, info, youtube , telegram , category , subcategory), commit=True)
    
    
    
    def select_lesson(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM home_product WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchall=True)
    
    
    def select_all_lesson(self):
        return self.execute("SELECT DISTINCT CountOfLesson FROM Lessons",fetchall=True)

    

def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")
