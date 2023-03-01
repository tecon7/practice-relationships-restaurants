class Restaurant:
    def __init__(self, name):
        self.name = name
        self.reviews = []

    def get_name(self):
        return self.name
    
    def get_reviews(self):
        return self.reviews

    def average_rating(self):
        total = 0
        for review in self.reviews:
            total += review.rating
        return total / len(self.reviews)

        # List comprehension
        # sum([review.rating for review in self.reviews]) / len(self.reviews)
    
    # The value that you'll insert into the lists is the first part
    # The for loop is the second part
    def get_customers(self):
        return [review.customer for review in self.reviews]

    # Get the lowest review object
    def get_lowest_review(self):
        lowest_review = self.reviews[0]
        for current_review in self.reviews:
            if current_review.rating < lowest_review.rating:
                lowest_review = current_review
        return lowest_review

    # return min(self.reviews, key=lambda review: review)