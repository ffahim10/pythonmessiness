products = [
    ("A", "G1", 20.1),
    ("B", "G2", 98.4),
    ("C", "G1", 49.7),
    ("D", "G3", 35.8),
    ("E", "G3", 105.5),
    ("F", "G1", 55.2),
    ("G", "G1", 12.7),
    ("H", "G3", 88.6),
    ("I", "G1", 5.2),
    ("J", "G2", 72.4)
]

category = [
    ("C3", 50, 75),
    ("C4", 75, 100),
    ("C2", 25, 50),
    ("C5", 100, None),
    ("C1", 0, 25)
]

margins = {
    "C1": 0.2,
    "C2": 0.3,
    "C3": 0.4,
    "C4": 0.5,
    "CS": 0.6
}

def get_category(product):
    for cat in category:
        if cat[1] <= product[2] < cat[2]:
            return cat[0]

def get_price(product):
    margin = margins.get(get_category(product), 0.0)
    return product[2] * (1 + margin)

def calculate_average_price_per_group():
    result = {}
    group_counts = {}
    
    for product in products:
        group = product[1]
        price = get_price(product)
        
        if group not in result:
            result[group] = 0.0
            group_counts[group] = 0
        
        result[group] += price
        group_counts[group] += 1

    for group in result:
        result[group] /= group_counts[group]

    return result
    
def main():
    result = calculate_average_price_per_group()
    expected_result = {
        "G1": 32.68,
        "G2": 85.4,
        "G3": 76.3
    }

    assert result == expected_result

if __name__ == "__main__":
    main()
