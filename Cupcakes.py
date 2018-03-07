def pluralize(amount, singular, plural):
    """Return the pluralized form of a word.

    Arguments:
        amount (float): The amount of the item.
        singular (str): The singular form of the word.
        plural (str): The plural form of the word.

    Returns:
        str: The correct form of the word depending on the amount.

    Examples:

        >>> print(pluralize(1, 'octopus', 'octopi'))
        octopus

        >>> print(pluralize(1.5, 'octopus', 'octopi'))
        octopi

        >>> print(pluralize(2, 'octopus', 'octopi'))
        octopi

    """
    if amount == 1:
        return singular
    else:
        return plural

def ceil(number):
    """Round up to the next integer.

    Arguments:
        number (float): The number to round.

    Returns:
        int: The next integer up from the argument.

    Examples:

        >>> print(ceil(1))
        1

        >>> print(ceil(1.4))
        2

        >>> print(ceil(1.5))
        2
    """
    from math import ceil as math_ceil
    return math_ceil(number)


def two_decimal_places(number):
    """Convert a number to two-decimal places.

    Arguments:
        number (float): The number to convert.

    Returns:
        str: The number rounded to two decimal places.

    Examples:

        >>> print(two_decimal_places(3))
        3.00

        >>> print(two_decimal_places(3.14159))
        3.14

        >>> print(two_decimal_places(3.516))
        3.52
    """
    return '{:.2f}'.format(number)

people_serve = int(input("How many people do you need to serve?\n"))
batches_needed = (ceil((people_serve/12)))
print("You need to make:", str(batches_needed), pluralize(batches_needed, "batch", "batches"), "of cupcakes\n")
print("Shopping List for Vanilla Cupcakes")
print("----------------------------------")

CUPS_FLOUR_PER_BATCH = 1.5
CUPS_G_SUGAR_PER_BATCH = 1
CUPS_BUTTER_PER_BATCH = 1.5
CUPS_SOUR_CREAM_PER_BATCH = 0.5
EGGS_PER_BATCH = 3
CUPS_P_SUGAR_PER_BATCH = 2.5
TEASPOONS_VANILLA_PER_BATCH = 4.5

flour = batches_needed * CUPS_FLOUR_PER_BATCH
g_sugar = batches_needed * CUPS_G_SUGAR_PER_BATCH
butter = batches_needed * CUPS_BUTTER_PER_BATCH
sour_cream = batches_needed * CUPS_SOUR_CREAM_PER_BATCH
eggs = batches_needed * EGGS_PER_BATCH
p_sugar = batches_needed * CUPS_P_SUGAR_PER_BATCH
vanilla = batches_needed * TEASPOONS_VANILLA_PER_BATCH

FLOUR_CUPS_PER_BAG = 20
G_SUGAR_CUPS_PER_BAG = 10
BUTTER_CUPS_PER_BOX = 2
SOUR_CREAM_CUPS_PER_TUB = 1
EGGS_PER_DOZEN = 12
P_SUGAR_CUPS_PER_BAG = 5.5
VANILLA_TEASPOONS_PER_BOTTLE = 12

shop_flour = ceil(flour / FLOUR_CUPS_PER_BAG)
shop_g_sugar = ceil(g_sugar / G_SUGAR_CUPS_PER_BAG)
shop_butter = ceil(butter / BUTTER_CUPS_PER_BOX)
shop_sour_cream = ceil(sour_cream / SOUR_CREAM_CUPS_PER_TUB)
shop_eggs = ceil(eggs / EGGS_PER_DOZEN)
shop_p_sugar = ceil(p_sugar / P_SUGAR_CUPS_PER_BAG)
shop_vanilla = ceil(vanilla / VANILLA_TEASPOONS_PER_BOTTLE)

print(str(shop_flour) + " " + pluralize(shop_flour, "bag", "bags") + " of flour")
print(str(shop_g_sugar) + " " + pluralize(shop_g_sugar, "bag", "bags") + " of granulated sugar")
print(str(shop_butter) + " " + pluralize(shop_butter, "box", "boxes") + " of butter")
print(str(shop_sour_cream) + " " + pluralize(shop_sour_cream, "tub", "tubs") + " of sour cream")
print(str(shop_eggs) + " dozen eggs")
print(str(shop_p_sugar) + " " + pluralize(shop_p_sugar, "bag", "bags") + " of powdered sugar")
print(str(shop_vanilla) + " " + pluralize(shop_vanilla, "bottle", "bottles") + " of vanilla extract\n")

PRICE_FLOUR_PER_BAG = 3.09
PRICE_G_SUGAR_PER_BAG = 2.98
PRICE_BUTTER_PER_BOX = 2.50
PRICE_SOUR_CREAM_PER_TUB = 1.29
PRICE_EGGS_PER_DOZEN = 2.68
PRICE_P_SUGAR_PER_BAG = 1.18
PRICE_VANILLA_PER_BOTTLE = 4.12

cost_flour = (shop_flour * PRICE_FLOUR_PER_BAG)
cost_g_sugar = (shop_g_sugar * PRICE_G_SUGAR_PER_BAG)
cost_butter = (shop_butter * PRICE_BUTTER_PER_BOX)
cost_sour_cream = (shop_sour_cream * PRICE_SOUR_CREAM_PER_TUB)
cost_eggs = (shop_eggs * PRICE_EGGS_PER_DOZEN)
cost_p_sugar = (shop_p_sugar * PRICE_P_SUGAR_PER_BAG)
cost_vaniila = (shop_vanilla * PRICE_VANILLA_PER_BOTTLE)
total_cost = two_decimal_places(cost_flour + cost_g_sugar + cost_butter + cost_sour_cream + cost_eggs + cost_p_sugar + cost_vaniila)

print("Total expected cost of ingredients: $" + str(total_cost) + "\n")
print("Have a great party!")