from flask_app.config.mysqlconnection import connectToMySQL



class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod 
    def get_all(cls):
        query = """
            SELECT * FROM users
        """

        results = connectToMySQL("users_schema").query_db(query)

        users = []
        for row in results:
            new_user = cls(row)
            users.append(new_user)
        return users

    @classmethod
    def create(cls, form_data):
        query = """
            INSERT INTO users (first_name,last_name,email)
    		VALUES (%(first_name)s,%(last_name)s,%(email)s);
        """

        return connectToMySQL("users_schema").query_db(query,form_data)


    @classmethod
    def delete(cls, id):
            
        data = {
            "id":id
        }
        
        query = """
                DELETE FROM users WHERE id = %(id)s
            """ 

        connectToMySQL("users_schema").query_db(query, data)

    @classmethod
    def save_one(cls, id):

        data = {
            "id":id
        }

        query = """
            SELECT * FROM users WHERE id = %(id)s
        """

        results = connectToMySQL("users_schema").query_db(query, data)

        if results:
            row = results[0]
            
            new_user = cls(row)

            return new_user

    @classmethod
    def update(cls, data):
    
        query = """
            UPDATE users SET
            first_name = %(first_name)s,
            last_name = %(last_name)s,
            email = %(email)s
            WHERE id = %(id)s
        """

        connectToMySQL("users_schema").query_db(query, data)

    @classmethod
    def get_one(cls, id):
        query = """
            SELECT * FROM users WHERE id = %(id)s
        """
        results = connectToMySQL("users_schema").query_db(query, {"id":id})
        
        return cls(results[0])