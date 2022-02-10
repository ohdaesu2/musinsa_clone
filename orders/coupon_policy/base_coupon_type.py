from abc import *

from datetime import datetime

from member.models.user import User
from orders.models.discount_coupon import DiscountCoupon


class BaseCouponType(metaclass=ABCMeta):

    def __init__(self,
                 user_obj: User,
                 discount_coupon_obj: DiscountCoupon,
                 ):
        self.user_obj = user_obj
        self.discount_coupon_obj = discount_coupon_obj

    def is_verified(self):
        user_obj = self.user_obj
        discount_coupon_obj = self.discount_coupon_obj

        # user가 가지고 있는 쿠폰 중에 현재 쿠폰이 있는지 확인
        user_coupon_list = user_obj.user_in_discount_coupon.all()
        if discount_coupon_obj in user_coupon_list:
            # user가 쿠폰을 가지고 있다면, 유효기간이 남았는지 확인
            current_time = datetime.now()
            disabled_time = discount_coupon_obj.disabled_at

            # Boolean 형태로 아웃풋
            available = disabled_time > current_time
            if available is True:
                return available
            else:
                print(f"이 쿠폰은 유효기간이 지났습니다.")
                return False

        else:
            print(f"{user_obj}가 가지고 있는 쿠폰이 아닙니다. ")
            return False

    def calculate_remaining_period(self):
        discount_coupon_obj = self.discount_coupon_obj

        current_time = datetime.now()
        disabled_time = discount_coupon_obj.disabled_at
        remaining_period = disabled_time - current_time
        return remaining_period