def oblicz_wielkanoc(rok):
    a = rok % 19
    b = rok // 100
    c = rok % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    miesiac = (h + l - 7 * m + 114) // 31
    dzien = ((h + l - 7 * m + 114) % 31) + 1

    return dzien, miesiac

rok = 2023
dzien, miesiac = oblicz_wielkanoc(rok)
print(f"Wielkanoc w roku {rok} przypada na {dzien} {miesiac}.")