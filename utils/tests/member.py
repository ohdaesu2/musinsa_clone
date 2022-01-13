from member.models.user import User

MEMBER_API_URL = "/api/member/user/"

def create_test_user():
    user_data = {
        "username": "test_user",
        "email": "test_user@gmail.com",
        "password": "missing_voice_password",
    }
    user_obj = User(**user_data)
    user_obj.set_password(user_data["password"])
    user_obj.save()
    return user_obj

