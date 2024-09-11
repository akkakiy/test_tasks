class TestUser:
    def test_user(self):
        user = {
            "username": "standard_user",
            "password": "secret_sauce"
        }
        return user


class DataUser:
    @staticmethod
    def data_user():
        data = {
            'first_name': "Alan",
            'last_name': "Po",
            'zip/postal_code': "1096"
        }
        return data
