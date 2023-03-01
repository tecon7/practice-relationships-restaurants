# practice-relationships-restaurants

## Deliverables

### Initializers, Readers, and Writers

#### Customer

- `Customer __init__(self, first_name, last_name)`
  - Customer should be initialized with a first and last name, both strings
- `Customer get_first_name()`
  - returns the customer's first name
- `Customer get_last_name()`
  - returns the customer's last name
- `Customer full_name()`
  - returns the full name of the customer

#### Restaurant

- `Restaurant __init__(self, name)`
  - Restaurants should be initialized with a name (string)
- `Restaurant get_name()`
  - returns the restaurant's name

#### Review

- `Review __init__(self, customer, restaurant, rating)`
  - Reviews should be initialized with a customer (Customer), restaurant (Restaurant), and a rating (int)
- `Review get_rating()`
  - returns the rating for a restaurant

### Object Relationship Methods

#### Customer
- `Customer get_reviews()`
  - returns the list of `Review` objects associated with the `Customer` instance
- `Customer add_review(restaurant, rating)`
  - creates a new `Review` objects with the given rating and adds it to both the `Customer` instance and the `Restaurant` object

#### Restaurant
- `Restaurant get_reviews()`
  - returns the list of `Review` objects associated with the `Restaurant` instance

#### Review
- `Review get_restaurant()`
  - returns the `Restaurant` object associated with the `Review` instance
- `Review get_customer()`
  - returns the `Customer` object associated with the `Review` instance

### Aggregate and Association Methods

#### Customer
- `Customer review_count()`
  - returns the total number of reviews associated with the `Customer` instance

#### Restaurant
- `Restaurant average_rating()`
  - returns the average rating for the `Restaurant` instance
  - HINT: can calculate the average by adding up all the ratings and diviging by the total number of ratings