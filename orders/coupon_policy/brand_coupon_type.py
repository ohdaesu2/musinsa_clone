from orders.coupon_policy.base_coupon_type import BaseCouponType

from member.models.user import User
from orders.models.discount_coupon import DiscountCoupon
from shop.models.clothes import Clothes


class BrandCouponType(BaseCouponType):

    def brand_verified(self, clothes_obj=Clothes):
        discount_coupon_obj = self.discount_coupon_obj
        clothes_obj = clothes_obj

        # 쿠폰 브랜드와 orderitem의 brand가 같은지 비교
        coupon_brand = discount_coupon_obj.brand
        clothes_brand = clothes_obj.brand

        if coupon_brand == clothes_brand:
            return True
        else:
            print("이 쿠폰을 사용할 수 없습니다.")
            return False


