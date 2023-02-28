from customer import Customer


def test_customer_init_first_and_last_name():
    """
    Should be able to initialize a customer with a first and last name
    """
    customer = Customer('Jane', 'Doe')
    assert customer.first_name == 'Jane'
    assert customer.last_name == 'Doe'

def test_customer_get_first_name():
    """
    get_first_name() should return the customer's first name
    """
    customer = Customer('Jane', 'Doe')
    assert customer.get_first_name() == 'Jane'

def test_customer_get_last_name():
    """
    get_last_name() should return the customer's last name
    """
    customer = Customer('Jane', 'Doe')
    assert customer.get_last_name() == 'Doe'

def test_customer_get_full_name():
    """
    get_full_name() should return the customer's full name
    """
    customer = Customer('Jane', 'Doe')
    assert customer.get_full_name() == 'Jane Doe'
