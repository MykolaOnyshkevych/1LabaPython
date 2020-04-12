from Lab1 import *


def main():
    combine1 = Combine(500)
    combine2 = Combine(2000, 2500, 120)
    combine3 = Combine(1000, 1500,2300,"Our Super Model", 230)
    combines = [combine1, combine2, combine3]
    [(print(str(quantity)), print(quantity)) for quantity in combines]

    print(combine1.priceStaticMethod())
    print(combine1.numberOfSeatsStaticMethod())

    print(combine1.colorGetter())
    combine1.colourSetter("Red")
    print(combine1.colorGetter())


if __name__ == "__main__":
    main()