from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "S22 Ultra", "+79990001122"),
    Smartphone("POCO", "X22", "+73330001144"),
    Smartphone("Apple", "Iphone 17", "+71112221122"),
    Smartphone("Huawei", "Mate", "+75550001134"),
    Smartphone("Nokia", "N90", "+76660001114"),
]

for i in catalog:
    print(f"{i.brand} - {i.model}, {i.phone_number}")
