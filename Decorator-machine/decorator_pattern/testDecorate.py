from decorator_pattern import Engineer,BeltDecorator,CasualPantDecorator,LeatherShoesDecorator\
    ,GlassesDecorate,WhiteTShirtDecorate



def main():
    jimmy = Engineer("Jimmy","哭")
    pant = CasualPantDecorator(jimmy)
    belt = BeltDecorator(pant)
    shoes = LeatherShoesDecorator(belt)
    shirt = WhiteTShirtDecorate(shoes)
    glasses = GlassesDecorate(shirt)
    glasses.wear()
    print("Done!!!")

if __name__ == '__main__':
    main()