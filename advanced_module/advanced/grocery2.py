def grocery_store(**kwargs):
    sorted_products = sorted(kwargs.items(), key= lambda x: (-x[1], len(x[0]), x[0]))
    result = []
    for product, quantity in sorted_products:
        result.append(f"{product}: {quantity}")

    return "\n".join(result)

print(grocery_store(

bread=5,

pasta=12,

eggs=12,

))