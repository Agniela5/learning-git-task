shopping_list = {
    "piekarnia": ["chelb", "bulki", "paczek"],
    "warzywniak": ["marchew", "seler", "rukola"]
}

for shop, product in shopping_list.items():
    product_capital = [p.title() for p in product]
    product_string = ", ".join(product_capital)

    print(f"Ide do {shop.title()}, kupuje tu nastepujace rzeczy: {product_string}")

