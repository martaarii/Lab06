from dataclasses import dataclass
@dataclass
class Product:
    product_number: int
    product_line: str
    product_type: str
    product: int
    product_brand: str
    product_color: str
    product_cost: float
    product_price:float

    def __eq__(self, other):
        return self.product_number == other.product_number

    def __hash__(self):
        return hash(self.product_number)

    def __str__(self):
        return f"{self.product},{self.product_brand} ({self.product_number})"