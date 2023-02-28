from review import Review
from customer import Customer
from restaurant import Restaurant


def test_review_init_customer_restaurant_rating():
    """
    Should be able to initialize a review object with
    a customer, restaurant, and rating
    """
    restaurant = Restaurant('Applebees')
    customer = Customer('Jane', 'Doe')
    review = Review(customer, restaurant, 5)
    assert review.customer == customer
    assert review.restaurant == restaurant
    assert review.rating == 5

def test_review_rating():
    """
    Should return the review for the rating
    """
    restaurant = Restaurant('Applebees')
    customer = Customer('Jane', 'Doe')
    review = Review(customer, restaurant, 5)
    assert review.get_rating() == 5

def test_review_get_restaurant():
    """
    get_restaurant() should return the Restaurant object
    associated with the review
    """
    restaurant = Restaurant('Applebees')
    customer = Customer('Jane', 'Doe')
    review = Review(customer, restaurant, 5)
    assert review.get_restaurant() == restaurant

def test_review_get_customer():
    """
    get_customer() should return the Customer object
    associated with the review
    """
    restaurant = Restaurant('Applebees')
    customer = Customer('Jane', 'Doe')
    review = Review(customer, restaurant, 5)
    assert review.get_customer() == customer
