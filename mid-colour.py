
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


def not_divmod(div, rem, base): 
	return div * base + rem


def hex_to_rgb(hex):
	hex_base = 16
	# break hex into parts
	one_pt_one = int(hex.un[0], 16)
	one_pt_two = int(hex.un[1], 16)
	two_pt_one = int(hex.deux[0], 16)
	two_pt_two = int(hex.deux[1], 16)
	three_pt_one = int(hex.trois[0], 16)
	three_pt_two = int(hex.trois[1], 16)
	# reverse the divmod
	red = not_divmod(one_pt_one, one_pt_two, hex_base)
	green = not_divmod(two_pt_one, two_pt_two, hex_base)
	blue = not_divmod(three_pt_one, three_pt_two, hex_base)

	return RGBColour(red, green, blue)


def find_mid_rgb(rgb_one, rgb_two):
	mid_r = int((rgb_one.r + rgb_two.r) / 2)
	mid_g = int((rgb_one.g + rgb_two.g) / 2)
	mid_b = int((rgb_one.b + rgb_two.b) / 2)

	return RGBColour(mid_r, mid_g, mid_b)


def hex_from_str(hex_str):
	# split into bytes
	split_hex = [hex_str[i : i + 2] for i in range(0, len(hex_str), 2)]
	# check len
	if len(split_hex) != 3:
		return HexColour(0, 0, 0)
	else:
		return HexColour(split_hex[0], split_hex[1], split_hex[2])


# actual program
while(1):
	in_one = input("input first hex (#xxxxxx): ")
	in_two = input("input second hex (#xxxxxx): ")

	clean_one = in_one.replace("#", "")
	clean_two = in_two.replace("#", "")
	# check len
	hex_len = 6
	if len(clean_one) != hex_len or len(clean_two) != hex_len:
		print("bad input, try again")
		continue
	# create hex objs
	hex_one = hex_from_str(clean_one)
	hex_two = hex_from_str(clean_two)
	# convert to rgb objs
	rgb_one = hex_to_rgb(hex_one)
	rgb_two = hex_to_rgb(hex_two)

	mid_rgb = find_mid_rgb(rgb_one, rgb_two)
	mid_hex = rgb_to_hex(mid_rgb)
	print("mid hex is:")
	mid_hex.print()

	in_cont = input("would you like to go again (y or n): ")
	if in_cont.lower() != 'y':
		break
