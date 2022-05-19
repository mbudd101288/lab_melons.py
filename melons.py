"""Classes for melon orders."""
class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""
    
    def __init__(self, name, species, qty, order_type):
        """Initialize melon order attributes."""
        self.name = name
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type

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

    def __init__(self, name):
        """Initialize melon order attributes."""
        super().__init__(name)
       
        
class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    tax = 0.17
    order_type = "international"

    def __init__(self, name):
        """Initialize melon order attributes."""
        super().__init__(name)


    def get_country_code(self):
        """Return the country code."""

        return self.country_code
