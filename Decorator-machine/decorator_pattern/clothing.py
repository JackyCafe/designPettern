from decorator_pattern import ClothingDecorator


class CasualPantDecorator(ClothingDecorator):
    def __init__(self, person):
        super(CasualPantDecorator, self).__init__(person)

    def decorate(self):
        print("一條卡其褲")


class BeltDecorator(ClothingDecorator):
    def __init__(self, person):
        super(BeltDecorator, self).__init__(person)

    def decorate(self):
        print("粉紅色的腰帶")


class LeatherShoesDecorator(ClothingDecorator):

    def __init__(self, person):
        super(LeatherShoesDecorator, self).__init__(person)

    def decorate(self):
        print("辣妞皮鞋")


class WhiteTShirtDecorate(ClothingDecorator):
    def __init__(self, person):
        super(WhiteTShirtDecorate, self).__init__(person)

    def decorate(self):
        print("白 T Shirt")


class GlassesDecorate(ClothingDecorator):

    def __init__(self,person):
        super(GlassesDecorate, self).__init__(person)

    def decorate(self):
        print("鑲金框眼鏡")


