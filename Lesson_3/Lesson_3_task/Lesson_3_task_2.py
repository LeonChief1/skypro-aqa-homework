from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 13", "+79161234567"),
    Smartphone("Samsung", "Galaxy S21", "+79161234568"),
    Smartphone("Google", "Pixel 6", "+79161234569"),
    Smartphone("OnePlus", "9 Pro", "+79161234570"),
    Smartphone("Xiaomi", "Mi 11", "+79161234571")
]

for self in catalog:
    print(f"{self.phone_brand} - {self.phone_model}. {self.subscriber_number}")