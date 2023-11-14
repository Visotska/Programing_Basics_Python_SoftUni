from math import pi


figure = str(input())

if figure == "square":
    duljina_na_strana_na_kvadrat = float(input())
    lice_na_kvadrat = duljina_na_strana_na_kvadrat * duljina_na_strana_na_kvadrat
    print("{:.3f}".format(lice_na_kvadrat))
elif figure == "rectangle":
    strana_1_rect = float(input())
    strana_2_rect = float(input())
    lice_na_pravougulnik = strana_1_rect * strana_2_rect
    print("{:.3f}".format(lice_na_pravougulnik))
elif figure == "circle" :
    radius_circle = float(input())
    lice_na_krug = pi * (radius_circle * radius_circle)
    print("{:.3f}".format(lice_na_krug))
elif figure == "triangle" :
    strana_triangle = float(input())
    visochina_triangle = float(input())
    lice_na_triugulnik = (strana_triangle * visochina_triangle) / 2
    print("{:.3f}".format(lice_na_triugulnik))
