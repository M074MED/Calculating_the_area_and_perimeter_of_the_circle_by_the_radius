while True:
    try:
        the_radius = float(input("enter the radius: "))
        the_area = float(pow(the_radius, 2) * 2 * (22 / 7))
        the_perimeter = float(2 * (22 / 7) * the_radius)
        if the_radius <= 0:
            print("""error!!
            the number is negative.
            please, enter root positive number!""")
        else:
            print("the area = " + str(the_area))
            print("the perimeter = " + str(the_perimeter))
    except ValueError:
        print("""error!!
        wrong input.
        please, enter root correct input!""")
