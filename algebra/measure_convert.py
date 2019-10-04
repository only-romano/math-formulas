# Length

def convert_length(value, from_l, to_l):
    lengths = {
        'm': 1, 'dm': 0.1, 'cm': 0.01, 'mm': 0.001, 'km': 1000,
        'in': 0.0254, 'ft': 0.3048, 'yd': 0.9144, 'mile': 1609.3, 'nmile': 1853,
        'ha': 100, 'acre': 63.6152,
        'litre': 0.1, 'oz': 0.030925, 'pt': 0.07793, 'gal': 0.15585,
    }
    return lengths[from_l] * value / lengths[to_l]


def convert_area(value, from_a, to_a):
    return value * convert_length(1, from_a, to_a) ** 2


def convert_volume(value, from_a, to_a):
    return value * convert_length(1, from_a, to_a) ** 3


def convert_weight(value, from_w, to_w):
    weights = {
        'mg': 0.000001, 'g': 0.001, 'kg': 1, 't': 1000,
        'grain': 0.0000648, 'oz': 0.02835, 'lb': 0.4536,
        'cwt': 50.802, 'st': 907.2, 'lt': 1016,
    }
    return weights[from_w] * value / weights[to_w]


def to_celsius(fahr):
    return (fahr - 32) / 1.8

def to_fahr(cels):
    return cels * 1.8 + 32

def temp_change(temp, farh):
    if farh == 1:
        return temp * 1.8
    else:
        return temp / 1.8


def pl(a, b, c):
    print(convert_length(a, b, c))

def pa(a, b, c):
    print(convert_area(a, b, c))

def pv(a, b, c):
    print(convert_volume(a, b, c))

def pw(a, b, c):
    print(convert_weight(a, b, c))

def pt(t, f):
    if f == 1:
        print(to_fahr(t))
    else:
        print(to_celsius(t))

def pc(t, f):
    print(temp_change(t, f))


if __name__ == '__main__':
    pl(5, 'ft', 'm')
    pl(8, 'km', 'mile')
    pl(12, 'cm', 'in')
    pl(7, 'nmile', 'km')
    pl(800, 'cm', 'yd')
    pl(440, 'yd', 'm')
    pl(8.5, 'in', 'cm')
    pl(20, 'km', 'nmile')
    pl(5.5, 'mile', 'm')
    pl(42.1955, 'km', 'yd')

    print()

    pa(50, 'ft', 'm')
    pa(24, 'ha', 'acre')
    pa(18, 'cm', 'in')
    pa(9, 'mile', 'km')
    pa(20, 'm', 'yd')
    pa(0.2, 'acre', 'm')
    pa(720, 'in', 'm')
    pa(5, 'km', 'acre')
    pa(5351, 'm', 'acre')
    pa(10368, 'in', 'cm')

    print()

    pv(70, 'ft', 'm')
    pv(260, 'litre', 'pt')
    pv(600, 'cm', 'in')
    pv(35, 'oz', 'litre')
    pv(45, 'm', 'yd')
    pv(0.25, 'in', 'cm')
    pv(5, 'litre', 'pt')
    pv(88000, 'ft', 'litre')
    pv(159, 'litre', 'ft')

    print()

    pl(5000, 'yd', 'm')
    pl(40, 'ft', 'm')
    pa(250, 'ft', 'm')
    pv(35, 'in', 'cm')
    pw(120, 'lb', 'kg')
    pv(44, 'gal', 'litre')
    pa(175, 'yd', 'm')
    pa(0.25, 'acre', 'm')
    pw(300, 'st', 't')
    pw(200, 'cwt', 't')

    print()

    pl(3000, 'm', 'mile')
    pa(200, 'm', 'yd')
    pv(5000, 'cm', 'in')
    pw(2250, 'g', 'oz')
    pv(20000, 'litre', 'gal')
    pa(770, 'ha', 'acre')
    pl(720, 'cm', 'ft')
    pa(50000, 'km', 'mile')
    pw(3.75, 't', 'lt')
    pw(75, 'kg', 'lb')

    print()
    pt(32, 1)
    pt(11, 1)
    pt(68, 0)
    pt(18, 0)
    pt(57.8, 1)
    pt(101.3, 0)
    pc(49, 0)
    pc(280, 1)
    pt(-460, 0)
    pt(-89.2, 1)
    pa(15 * 16, 'ft', 'm')
    pw(170, 'lb', 'kg')
