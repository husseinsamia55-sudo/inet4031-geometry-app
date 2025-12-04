import math

def volume(radius):
    """
    Compute the volume of a sphere given its radius.
    """
    return (4/3) * math.pi * (radius ** 3)

def main():
    print("Geometry App - Sphere Volume Calculator")
    r = float(input("Enter radius: "))
    v = volume(r)
    print(f"Volume of sphere: {v}")

if __name__ == "__main__":
    main()
