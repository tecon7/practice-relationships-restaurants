from restaurant import Restaurant


def test_restaurant_init_name():
    """
    Should be able to initialize a restaurant with a name
    """
    restaurant = Restaurant("Monk's Cafe")
    assert restaurant.name == "Monk's Cafe"

def test_restaurant_get_name():
    """
    get_name() should return the restaurant's name
    """
    restaurant = Restaurant("Monk's Cafe")
    restaurant.get_name() == "Monk's Cafe"
