
class RGBColour(object):

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def print(self):
        print('({} / 255, {} / 255, {} / 255)'.format(self.r, self.g, self.b))


class HexColour(object):

    def __init__(self, un, deux, trois):
        # three bytes
        self.un = un
        self.deux = deux
        self.trois = trois

    def print(self):
        hex_str = '#{}{}{}'.format(self.un, self.deux, self.trois)
        print(hex_str.upper())


def make_hex_byte(div, rem):
    hex_div = hex(div)
    hex_rem = hex(rem)

    str_div = str(hex_div)
    str_rem = str(hex_rem)

    # append division hex to remainder hex to make hex byte
    return str_div.replace("0x", "") + str_rem.replace("0x", "")


def rgb_to_hex(rgb):
    hex_base = 16
    # get division, remainder of colour
    red = divmod(rgb.r, hex_base)
    green = divmod(rgb.g, hex_base)
    blue = divmod(rgb.b, hex_base)

    one = make_hex_byte(red[0], red[1])
    two = make_hex_byte(green[0], green[1])
    three = make_hex_byte(blue[0], blue[1])

    return HexColour(one, two, three)


# test
my_rgb = RGBColour(33, 223, 101)
my_rgb.print()
my_hex = rgb_to_hex(my_rgb)
my_hex.print()

