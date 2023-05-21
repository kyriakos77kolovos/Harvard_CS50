def main():
    """Convert matter to energy"""
    mass = input("Enter a mass in kg: ").strip()
    print(convert(int(mass)))


def convert(mass):
    """Convert kg to J"""
    joules = mass * (300000000**2)
    return joules


main()