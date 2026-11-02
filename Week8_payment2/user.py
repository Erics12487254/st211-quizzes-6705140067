class UserService:
    def __init__(self, database):
        self.database = database

    def get_username(self, user_id):
        return self.database.find_user(user_id)

from unittest.mock import Mock

from Week8_payment2.user import UserService

def test_get_username():
    db = Mock()
    db.find_user.return_value = "Alice"
    service = UserService(db)
    assert service.get_username(1) == "Alice"