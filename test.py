url = "https://bookstore.toolsqa.com/"
header = {'accept': 'application/json'}
my_book = {"isbn": 1, "title": "my_book", "subTitle": "my life", "author": "me", "publish_date": "1.1.2000",
           "publisher": "him", "pages": 200, "description": "cool book about me", "website": "www.google.com/me"}
my_user = {"userId": 10, "username": "Me", "books": my_book}
my_user_list = """[{"id": 10, "username": "Me", "firstName": "Noam", "lastName": "Barkai",
                 "email": "barkai@email.com", "password": "12345", "phone": "12345", "userStatus": 2},
                {"id": 11, "username": "theUser", "firstName": "John", "lastName": "James",
                 "email": "john@email.com", "password": "12345", "phone": "12345", "userStatus": 1}]"""