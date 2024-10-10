restaurants = [
    {
        "restaurant_name": "Sands of Flavor", 
        "cuisine_type": "Middle Eastern", 
        "location": "789 Oasis Drive, Shurima Desert, Runeterra", 
        "restaurant_owner": "Omah D. Azir", 
        "average_price_range": "$15-35 per person"
    },
    {
        "restaurant_name": "The Iron Fork", 
        "cuisine_type": "Rustic European", 
        "location": "456 Warpath Lane, Noxus City, Runeterra", 
        "restaurant_owner": "Dar D. Ius", 
        "average_price_range": "$20-$50 per person"
    },
    {
        "restaurant_name": "Valor's Bounty", 
        "cuisine_type": "Traditional American", 
        "location": "123 Honor Road, Demacia City, Runeterra", 
        "restaurant_owner": "Garen D. Crownguard", 
        "average_price_range": "$10-$25 per person"
    },
    {
        "restaurant_name": "Serenity Garden", 
        "cuisine_type": "Asian Fusion", 
        "location": "234 Tranquil Path, Ionia Village, Runeterra", 
        "restaurant_owner": "Karma I. Ionian", 
        "average_price_range": "$12-$30 per person"
    },
    {
        "restaurant_name": "Celestial Cuisine", 
        "cuisine_type": "Mediterranean", 
        "location": "321 Starfall Avenue, Targon Peaks, Runeterra", 
        "restaurant_owner": "Tar G. On", 
        "average_price_range": "$18-$40 per person"
    }
]

for restaurant in restaurants:
    print(f"Restaurant Name: {restaurant['restaurant_name']} | Cuisine Type: {restaurant['cuisine_type']} | Location: {restaurant['location']} | Restaurant Owner: {restaurant['restaurant_owner']} | Average Price Range: {restaurant['average_price_range']}")
