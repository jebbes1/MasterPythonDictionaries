products = [
    {
        "product_name": "Gaming Console", 
        "price": 2500, 
        "discount": "5%", 
        "category": "Video Games", 
        "stock": 10
    },
    {
        "product_name": "Shampoo", 
        "price": 6, 
        "discount": "0%", 
        "category": "Personal Care", 
        "stock": 7
    },
    {
        "product_name": "Smartphone", 
        "price": 7600, 
        "discount": "20%", 
        "category": "Electronics", 
        "stock": 50
    },
    {
        "product_name": "Laptop", 
        "price": 65000, 
        "discount": "20%", 
        "category": "Electronics", 
        "stock": 99
    },
    {
        "product_name": "Book", 
        "price": 750, 
        "discount": "5%", 
        "category": "Books", 
        "stock": 20
    }
]

for product in products:
    print(f"Product: {product['product_name']} | Price: {product['price']} | Discount: {product['discount']} | Category: {product['category']} | Stock: {product['stock']}")
