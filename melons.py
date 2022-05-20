"""Classes for melon orders."""
class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""
    
    def __init__(self, name, species, qty):
        """Initialize melon order attributes."""
        self.name = name
        self.species = species
        self.qty = qty
        self.shipped = False
       
    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True
    
    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        
        total = (1 + self.tax) * self.qty * base_price

        return total

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    tax = 0.08
    order_type = "domestic"
    

       
        
class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    tax = 0.17
    order_type = "international"

    """Initialize melon order attributes."""

    def __init__(self, name, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(name, species, qty)

        self.country_code = country_code

    def get_total(self):
        
        if self.qty <10:
            total = super().get_total() + 3
        else:
            total = super().get_total()

        return total

        

    def get_country_code(self):
        """Return the country code."""
        
        return self.country_code
    
class GoverenmentMelonOrder(AbstractMelonOrder):  
      
    tax = 0
    
    def __init__(self, name, species, qty):
        super().__init__(name, species, qty)

        self.passed_inspection = False

    
    def mark_inspection(self, passed):

        self.passed_inspection = passed 


# Part 2

"""Because of changes in shipping costs, Ubermelon is updating its prices:

Now, Christmas melons will cost 1.5 times as much as the base price.
Also, a flat fee of $3 will be added to all international orders with less than 10 melons.
Update the get_total method to include these new prices."""
