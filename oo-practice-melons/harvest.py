############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    cas = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    cas.add_pairing('strawberries')
    cas.add_pairing('mint')
    all_melon_types.append(cas)

    cren = MelonType('cren', 1996, 'green', False, False, 'Crenshaw')
    cren.add_pairing('proscuitto')
    all_melon_types.append(cren)

    yw = MelonType('yw', 2013, 'yellow', False, True, 'Yellow Watermelon')
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(melon.name, "pairs with:")
        for pair in melon.pairings:
            print("-", pair)

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    #dictionary[key]=value
    melon_dict = {}
    for melon in melon_types:
        if melon not in melon_dict:
            melon_dict[melon.code] = melon
    return melon_dict

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Needs __init__ and is_sellable methods
    def __init__(self, melon_type, shape_rating, color_rating, harvested_from, harvested_by):
        self.melon_type = melon_type 
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_from = harvested_from
        self.harvested_by = harvested_by

    def is_sellable(self):
        is_good_shape = self.shape_rating > 5
        is_good_color = self.color_rating > 5
        is_good_field = self.harvested_from != "Field 3"
        return (is_good_shape and is_good_color and is_good_field)

def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melon_obj_list = []

    melons_by_id = make_melon_type_lookup(melon_types)
    melon_1 = Melon(melons_by_id['yw'], 8, 7, 'Field 2', 'Sheila')
    melon_obj_list.append(melon_1)

    melon_2 = Melon(melons_by_id['yw'], 3, 4, 'Field 2', 'Sheila')
    melon_obj_list.append(melon_2)

    melon_3 = Melon(melons_by_id['yw'], 9, 8, 'Field 3', 'Sheila')
    melon_obj_list.append(melon_3)

    melon_4 = Melon(melons_by_id['cas'], 10, 6, 'Field 35', 'Sheila')
    melon_obj_list.append(melon_4)

    return melon_obj_list

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
