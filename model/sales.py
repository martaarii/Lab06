from dataclasses import dataclass
from datetime import date
@dataclass
class Sale:
    retailer_code: int
    product_number: int
    orther_method_code: int
    date: date
    quantity: int
    unit_price: float
    unit_sale_price: float
