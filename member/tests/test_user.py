from rest_framework.test import APITestCase

from member.models.user import User
from utils.tests.member import create_test_user, MEMBER_API_URL


class UserTestCase(APITestCase):
    def setUp(self) -> None:
        create_test_user()

        self.create_user_data ={
            "username": "test_user",
            "email": "test_user@gmail.com",
            "password": "missing_voice_password",
            "phone_number": "010-1234-5678",
            "address": "Seoul",
            "gender": "M",
        }

    def test_필수_필드_이용하여_user_생성(self):
        user_data ={
            "username": "test_user",
            "email": "test_user@gmail.com",
            "password": "missing_voice_password",
        }
        response = self.client.post(f"{MEMBER_API_URL}", data=user_data)


        # user_obj = User.objects.create(**user_data)
        # self.assertTrue(isinstance(user_obj, User))
        # self.assertEqual(user_obj.total_point, 0)
        # self.assertEqual(user_obj.user_level.level_name, 1)
        # self.assertEqual(user_obj.user_level.discount_rate, 1)
        # self.assertEqual(user_obj.user_level.current_level_minimum_point, 0)
        # self.assertEqual(user_obj.user_level.next_level_minimum_point, 2000)
        # self.assertEqual(user_obj.user_level.monthly_discount_coupon_rate, 2)
        # self.assertEqual(user_obj.user_level.monthly_discount_coupon_count, 3)



