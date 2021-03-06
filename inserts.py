from pymongo import MongoClient

client = MongoClient()

db = client.Served

"""
data = [
    {"name": "Angelica Pizza", "address": "332 Livingston St", "neighborhood": "Downtown Brooklyn", "category": "Italian", "pictures": [], "ratings": []},
    {"name": "Ani Sushi Bar", "address": "142 Montague St", "neighborhood": "Downtown Brooklyn", "category": "Japanese", "pictures": [], "ratings": []},
    {"name": "Antonio's", "address": "32 Court St", "neighborhood": "Downtown Brooklyn", "category": "Deli Food", "pictures": [], "ratings": []},
    {"name": "Archway Cafe", "address": "57 B Pearl St", "neighborhood": "Downtown Brooklyn", "category": "Coffee & Tea", "pictures": [], "ratings": []},
    {"name": "Armando's", "address": "143 Montague St", "neighborhood": "Downtown Brooklyn", "category": "Italian", "pictures": [], "ratings": []},
    {"name": "Atlantic ChipShop", "address": "129 Atlantic Ave", "neighborhood": "Downtown Brooklyn", "category": "British (Traditional)", "pictures": [], "ratings": []},
    {"name": "Authentic Indian Food, Chicken & Pizza", "address": "547 Fulton St", "neighborhood": "Downtown Brooklyn", "category": "Indian", "pictures": [], "ratings": []},
    {"name": "Boomwich", "address": "311 Atlantic Ave", "neighborhood": "Downtown Brooklyn", "category": "Sandwiches", "pictures": [], "ratings": []},
    {"name": "Brooklyn Brewhouse", "address": "229 Duffield St", "neighborhood": "Downtown Brooklyn", "category": "American", "pictures": [], "ratings": []},
    {"name": "Brooklyn Brewhouse", "address": "229 Duffield St", "neighborhood": "Downtown Brooklyn", "category": "American", "pictures": [], "ratings": []},
    {"name": "Brooklyn Bridge Cafe", "address": "235 Adams St", "neighborhood": "Downtown Brooklyn", "category": "Diner", "pictures": [], "ratings": []},
    {"name": "Brooklyn Heights Deli", "address": "292 Henry St", "neighborhood": "Downtown Brooklyn", "category": "Deli Food", "pictures": [], "ratings": []},
    {"name": "Buffalo Boss Two", "address": "400 Jay St", "neighborhood": "Downtown Brooklyn", "category": "Wings", "pictures": [], "ratings": []},
    {"name": "Buffalo Boss Two", "address": "400 Jay St", "neighborhood": "Downtown Brooklyn", "category": "Wings", "pictures": [], "ratings": []},
    {"name": "Cafe Metro", "address": "15 Metrotech Ctr", "neighborhood": "Downtown Brooklyn", "category": "Deli Food", "pictures": [], "ratings": []},
    {"name": "Caffe Buon Gusto - Brooklyn", "address": "151 Montague St", "neighborhood": "Downtown Brooklyn", "category": "Italian", "pictures": [], "ratings": []},
    {"name": "Checkers", "address": "111 Court St", "neighborhood": "Downtown Brooklyn", "category": "Burgers", "pictures": [], "ratings": []},
    {"name": "Chu's Gourmet", "address": "82 Livingston St", "neighborhood": "Downtown Brooklyn", "category": "Chinese", "pictures": [], "ratings": []},
    {"name": "Chu's Gourmet", "address": "82 Livingston St", "neighborhood": "Downtown Brooklyn", "category": "Chinese", "pictures": [], "ratings": []},
    {"name": "Clark's Restaurant", "address": "80 Clark St", "neighborhood": "Downtown Brooklyn", "category": "Diner", "pictures": [], "ratings": []},
    {"name": "Concord Market", "address": "91 Tillary St", "neighborhood": "Downtown Brooklyn", "category": "Deli Food", "pictures": [], "ratings": []},
    {"name": "Court Order", "address": "52 Court St", "neighborhood": "Downtown Brooklyn", "category": "Deli Food", "pictures": [], "ratings": []},
    {"name": "Court Order", "address": "52 Court St", "neighborhood": "Downtown Brooklyn", "category": "Deli Food", "pictures": [], "ratings": []},
    {"name": "Court Street Fresco Tortilla", "address": "113 Court St", "neighborhood": "Downtown Brooklyn", "category": "Southwestern", "pictures": [], "ratings": []},
    {"name": "Curry Heights", "address": "151 Remsen St", "neighborhood": "Downtown Brooklyn", "category": "Indian", "pictures": [], "ratings": []},
    {"name": "Custom House", "address": "139 Montague St", "neighborhood": "Downtown Brooklyn", "category": "American", "pictures": [], "ratings": []},
    {"name": "Dallas BBQ", "address": "180 Livingston St", "neighborhood": "Downtown Brooklyn", "category": "Barbecue", "pictures": [], "ratings": []},
    {"name": "Dining Room", "address": "56 Willoughby St", "neighborhood": "Downtown Brooklyn", "category": "American", "pictures": [], "ratings": []},
    {"name": "Dumbo Kitchen", "address": "108 Jay St", "neighborhood": "Downtown Brooklyn", "category": "Pizza", "pictures": [], "ratings": []},
    {"name": "Fatoosh Pitza & BBQ", "address": "330 Hicks St", "neighborhood": "Downtown Brooklyn", "category": "Middle Eastern", "pictures": [], "ratings": []},
    {"name": "Five Guys", "address": "2 Metrotech Center", "neighborhood": "Downtown Brooklyn", "category": "Burgers", "pictures": [], "ratings": []},
    {"name": "Five Guys", "address": "2 Metrotech Center", "neighborhood": "Downtown Brooklyn", "category": "Burgers", "pictures": [], "ratings": []},
    {"name": "Front Street Pizza", "address": "80 Front St", "neighborhood": "Downtown Brooklyn", "category": "Deli Food", "pictures": [], "ratings": []},
    {"name": "Garden of Eden", "address": "180 Montague St", "neighborhood": "Downtown Brooklyn", "category": "Deli Food", "pictures": [], "ratings": []},
    {"name": "Hale & Hearty Soups", "address": "32 Court St", "neighborhood": "Downtown Brooklyn", "category": "Sandwiches", "pictures": [], "ratings": []},
    {"name": "Hanco's", "address": "147 Montague St", "neighborhood": "Downtown Brooklyn", "category": "Vietnamese", "pictures": [], "ratings": []},
    {"name": "Happy Days Diner", "address": "148 Montague St", "neighborhood": "Downtown Brooklyn", "category": "Diner", "pictures": [], "ratings": []},
    {"name": "Harry O's", "address": "120 Lawrence St", "neighborhood": "Downtown Brooklyn", "category": "American", "pictures": [], "ratings": []},
    {"name": "Hill Country Barbecue Market", "address": "345 Adams St", "neighborhood": "Downtown Brooklyn", "category": "Barbecue", "pictures": [], "ratings": []},
    {"name": "Hill Country Chicken", "address": "345 Adams St", "neighborhood": "Downtown Brooklyn", "category": "Soul Food", "pictures": [], "ratings": []},
    {"name": "Ignazio's Pizza", "address": "4 Water St", "neighborhood": "Downtown Brooklyn", "category": "Pizza", "pictures": [], "ratings": []},
    {"name": "InfiniTEA Cafe", "address": "150 Lawrence St", "neighborhood": "Downtown Brooklyn", "category": "Japanese", "pictures": [], "ratings": []},
    {"name": "Iron Chef House", "address": "92 Clark St", "neighborhood": "Downtown Brooklyn", "category": "Japanese", "pictures": [], "ratings": []},
    {"name": "Just Salad", "address": "210 State St", "neighborhood": "Downtown Brooklyn", "category": "Sandwiches", "pictures": [], "ratings": []},
    {"name": "La Defense", "address": "2 Metrotech Ctr", "neighborhood": "Downtown Brooklyn", "category": "Mediterranean", "pictures": [], "ratings": []},
    {"name": "La Flor Del Paraiso", "address": "491 Atlantic Ave", "neighborhood": "Downtown Brooklyn", "category": "Puerto Rican", "pictures": [], "ratings": []},
    {"name": "Lantern Thai", "address": "101 Montague St", "neighborhood": "Downtown Brooklyn", "category": "Thai", "pictures": [], "ratings": []},
    {"name": "Lichee Nut", "address": "162 Montague St", "neighborhood": "Downtown Brooklyn", "category": "Chinese", "pictures": [], "ratings": []},
    {"name": "Lichee Nut", "address": "162 Montague St", "neighborhood": "Downtown Brooklyn", "category": "Chinese", "pictures": [], "ratings": []},
    {"name": "Livingston Diner", "address": "372 Livingston St", "neighborhood": "Downtown Brooklyn", "category": "Mexican", "pictures": [], "ratings": []},
    {"name": "Luciano's", "address": "15 Metrotech Ctr", "neighborhood": "Downtown Brooklyn", "category": "Italian", "pictures": [], "ratings": []},
    {"name": "Luke's Lobster", "address": "11 Water St", "neighborhood": "Downtown Brooklyn", "category": "Seafood", "pictures": [], "ratings": []},
    {"name": "Luzzo's", "address": "145 Atlantic Ave", "neighborhood": "Downtown Brooklyn", "category": "Italian", "pictures": [], "ratings": []},
    {"name": "Mamma Mia Pizza", "address": "435 Fulton St", "neighborhood": "Downtown Brooklyn", "category": "Pizza", "pictures": [], "ratings": []},
    {"name": "Masala Grill", "address": "501B Atlantic Ave", "neighborhood": "Downtown Brooklyn", "category": "Indian", "pictures": [], "ratings": []},
    {"name": "Montague Street Bagels", "address": "108 Montague St", "neighborhood": "Downtown Brooklyn", "category": "Deli Food", "pictures": [], "ratings": []},
    {"name": "Montague Street Bagels", "address": "108 Montague St", "neighborhood": "Downtown Brooklyn", "category": "Deli Food", "pictures": [], "ratings": []},
    {"name": "Monty Q's", "address": "158 Montague St", "neighborhood": "Downtown Brooklyn", "category": "Italian", "pictures": [], "ratings": []},
    {"name": "My Little Pizzeria", "address": "114 Court St", "neighborhood": "Downtown Brooklyn", "category": "Pizza", "pictures": [], "ratings": []},
    {"name": "Nanatori", "address": "162 Montague St", "neighborhood": "Downtown Brooklyn", "category": "Japanese", "pictures": [], "ratings": []},
    {"name": "Nanatori", "address": "162 Montague St", "neighborhood": "Downtown Brooklyn", "category": "Japanese", "pictures": [], "ratings": []},
    {"name": "Nevins Gourmet Deli", "address": "455 Atlantic Ave", "neighborhood": "Downtown Brooklyn", "category": "Deli Food", "pictures": [], "ratings": []},
    {"name": "New Apollo Diner", "address": "155 Livingston St", "neighborhood": "Downtown Brooklyn", "category": "Diner", "pictures": [], "ratings": []},
    {"name": "No. 7 Sub", "address": "11 Water St", "neighborhood": "Downtown Brooklyn", "category": "Sandwiches", "pictures": [], "ratings": []},
    {"name": "Park Plaza Restaurant", "address": "220 Cadman Plz W", "neighborhood": "Downtown Brooklyn", "category": "Diner", "pictures": [], "ratings": []},
    {"name": "Pedro's Restaurant", "address": "73 Jay St", "neighborhood": "Downtown Brooklyn", "category": "Mexican", "pictures": [], "ratings": []},
    {"name": "Pinkberry", "address": "117 Front St", "neighborhood": "Downtown Brooklyn", "category": "Desserts", "pictures": [], "ratings": []},
    {"name": "Pio Bagels", "address": "136 Lawrence St", "neighborhood": "Downtown Brooklyn", "category": "Deli Food", "pictures": [], "ratings": []},
    {"name": "Piz-zetta", "address": "90 Livingston St", "neighborhood": "Downtown Brooklyn", "category": "Italian", "pictures": [], "ratings": []},
    {"name": "Potbelly Sandwich Shop", "address": "345 Adams St", "neighborhood": "Downtown Brooklyn", "category": "Sandwiches", "pictures": [], "ratings": []},
    {"name": "Red Gravy", "address": "151 Atlantic Ave", "neighborhood": "Downtown Brooklyn", "category": "Italian", "pictures": [], "ratings": []},
    {"name": "Rocco's Tacos", "address": "339 Adams St", "neighborhood": "Downtown Brooklyn", "category": "Mexican", "pictures": [], "ratings": []},
    {"name": "Saketumi Asian Bistro", "address": "118 Montague St", "neighborhood": "Downtown Brooklyn", "category": "Japanese", "pictures": [], "ratings": []},
    {"name": "Skyline Gourmet", "address": "64 Willoughby St", "neighborhood": "Downtown Brooklyn", "category": "Deli Food", "pictures": [], "ratings": []},
    {"name": "Sophie's", "address": "27 Smith St", "neighborhood": "Downtown Brooklyn", "category": "Cuban", "pictures": [], "ratings": []},
    {"name": "Table 87", "address": "87 Atlantic Ave", "neighborhood": "Downtown Brooklyn", "category": "Italian", "pictures": [], "ratings": []},
    {"name": "The Bridges", "address": "66 Water St", "neighborhood": "Downtown Brooklyn", "category": "American", "pictures": [], "ratings": []},
    {"name": "The Bridges", "address": "66 Water St", "neighborhood": "Downtown Brooklyn", "category": "American", "pictures": [], "ratings": []},
    {"name": "Tio Pio", "address": "119 Court St", "neighborhood": "Downtown Brooklyn", "category": "Deli Food", "pictures": [], "ratings": []},
    {"name": "Tio Pio", "address": "78 Willoughby St", "neighborhood": "Downtown Brooklyn", "category": "Diner", "pictures": [], "ratings": []},
    {"name": "Tutt Cafe", "address": "47 Hicks St", "neighborhood": "Downtown Brooklyn", "category": "Middle Eastern", "pictures": [], "ratings": []},
    {"name": "Vanity Sweets", "address": "300 Cadman Plaza", "neighborhood": "Downtown Brooklyn", "category": "Desserts", "pictures": [], "ratings": []},
    {"name": "Vanity Sweets", "address": "300 Cadman Plaza", "neighborhood": "Downtown Brooklyn", "category": "Desserts", "pictures": [], "ratings": []},
    {"name": "Vegetarian Ginger", "address": "128 Montague St", "neighborhood": "Downtown Brooklyn", "category": "Vegetarian", "pictures": [], "ratings": []},
    {"name": "Willowtown Store #7", "address": "16 Columbia Pl", "neighborhood": "Downtown Brooklyn", "category": "Coffee & Tea", "pictures": [], "ratings": []},
    {"name": "7 Old Fulton", "address": "7 Old Fulton St", "neighborhood": "Downtown Brooklyn", "category": "Eclectic & International", "pictures": [], "ratings": []},
    {"name": "7 Stars Deli", "address": "59 Front St", "neighborhood": "Downtown Brooklyn", "category": "Deli Food", "pictures": [], "ratings": []},
    {"name": "99 Cent Fresh Hot Pizza", "address": "51-D Willoughby St", "neighborhood": "Downtown Brooklyn", "category": "Pizza", "pictures": [], "ratings": []},
    {"name": "Absolute Coffee", "address": "327 Atlantic Ave", "neighborhood": "Downtown Brooklyn", "category": "Coffee & Tea", "pictures": [], "ratings": []},
    {"name": "AlMar", "address": "111 Front St", "neighborhood": "Downtown Brooklyn", "category": "Italian", "pictures": [], "ratings": []},
    {"name": "Almondine Bakery", "address": "85 Water St", "neighborhood": "Downtown Brooklyn", "category": "Bakery & Pastries", "pictures": [], "ratings": []},
    {"name": "Ample Hills Creamery", "address": "360 Furman St", "neighborhood": "Downtown Brooklyn", "category": "Desserts", "pictures": [], "ratings": []},
    {"name": "Annies First Wok", "address": "155 York St", "neighborhood": "Downtown Brooklyn", "category": "Chinese", "pictures": [], "ratings": []},
    {"name": "Asian City", "address": "148 Lawrence St", "neighborhood": "Downtown Brooklyn", "category": "Chinese", "pictures": [], "ratings": []},
    {"name": "Asya", "address": "46 Henry St", "neighborhood": "Downtown Brooklyn", "category": "Indian", "pictures": [], "ratings": []},
    {"name": "Atrium Dumbo", "address": "15 Main St", "neighborhood": "Downtown Brooklyn", "category": "American", "pictures": [], "ratings": []},
    {"name": "Au Bon Pain", "address": "70 Myrtle Ave", "neighborhood": "Downtown Brooklyn", "category": "Bakery & Pastries", "pictures": [], "ratings": []},
    {"name": "Bacchus Bistro", "address": "409 Atlantic Ave", "neighborhood": "Downtown Brooklyn", "category": "French", "pictures": [], "ratings": []},
    {"name": "Barnes & Noble Cafe", "address": "106 Court St", "neighborhood": "Downtown Brooklyn", "category": "Coffee & Tea", "pictures": [], "ratings": []},
    {"name": "Bed-Stuy Fish Fry", "address": "193 Schermerhorn St", "neighborhood": "Downtown Brooklyn", "category": "Seafood", "pictures": [], "ratings": []},
    {"name": "Bevacco", "address": "60 Henry St", "neighborhood": "Downtown Brooklyn", "category": "Italian", "pictures": [], "ratings": []},
    {"name": "Bijan's", "address": "81 Hoyt St", "neighborhood": "Downtown Brooklyn", "category": "Persian", "pictures": [], "ratings": []},
    {"name": "Blue Cafe", "address": "50 Hoyt St", "neighborhood": "Downtown Brooklyn", "category": "Deli Food", "pictures": [], "ratings": []},
    {"name": "Bolivian LLAMA Party", "address": "Location Varies", "neighborhood": "Downtown Brooklyn", "category": "South American", "pictures": [], "ratings": []},
    {"name": "Bridge Coffee Shop", "address": "73 Bridge St", "neighborhood": "Downtown Brooklyn", "category": "Diner", "pictures": [], "ratings": []},
    {"name": "Bridge Fresh", "address": "68 Jay St", "neighborhood": "Downtown Brooklyn", "category": "Deli Food", "pictures": [], "ratings": []},
    {"name": "Brooklyn Beach Shack", "address": "Brooklyn Bridge Park", "neighborhood": "Downtown Brooklyn", "category": "Burgers", "pictures": [], "ratings": []},
    {"name": "Brooklyn Bread Express", "address": "100 Henry St", "neighborhood": "Downtown Brooklyn", "category": "Bakery & Pastries", "pictures": [], "ratings": []},
    {"name": "Brooklyn Bridge Garden Bar", "address": "3 Old Fulton St", "neighborhood": "Downtown Brooklyn", "category": "American", "pictures": [], "ratings": []},
    {"name": "Brooklyn Heights Wine Bar", "address": "50 Henry St", "neighborhood": "Downtown Brooklyn", "category": "American", "pictures": [], "ratings": []},
    {"name": "Brooklyn Roasting Company", "address": "25 Jay St", "neighborhood": "Downtown Brooklyn", "category": "Coffee & Tea", "pictures": [], "ratings": []},
    {"name": "Cafe Plymouth", "address": "90 Henry St", "neighborhood": "Downtown Brooklyn", "category": "Diner", "pictures": [], "ratings": []},
    {"name": "Casella", "address": "66 Willoughby St", "neighborhood": "Downtown Brooklyn", "category": "Sandwiches", "pictures": [], "ratings": []},
    {"name": "Chang Heng", "address": "54 Willoughby St", "neighborhood": "Downtown Brooklyn", "category": "Chinese", "pictures": [], "ratings": []},
    {"name": "Chef's Table at Brooklyn Fare", "address": "200 Schemerhorn St", "neighborhood": "Downtown Brooklyn", "category": "Seafood", "pictures": [], "ratings": []},
    {"name": "Chez Moi", "address": "135 Atlantic Ave", "neighborhood": "Downtown Brooklyn", "category": "French", "pictures": [], "ratings": []},
    {"name": "Chipotle", "address": "1 MetroTech Center", "neighborhood": "Downtown Brooklyn", "category": "Mexican", "pictures": [], "ratings": []},
    {"name": "Chipotle", "address": "185 Montague St", "neighborhood": "Downtown Brooklyn", "category": "Mexican", "pictures": [], "ratings": []},
    {"name": "ChocoBolo", "address": "68 Jay St", "neighborhood": "Downtown Brooklyn", "category": "Bakery & Pastries", "pictures": [], "ratings": []},
    {"name": "Chuang Hing II", "address": "48 Hoyt St", "neighborhood": "Downtown Brooklyn", "category": "Chinese", "pictures": [], "ratings": []},
    {"name": "Cobble Hill Canteen", "address": "331 Henry St", "neighborhood": "Downtown Brooklyn", "category": "Sandwiches", "pictures": [], "ratings": []},
    {"name": "Colonie", "address": "127 Atlantic Ave", "neighborhood": "Downtown Brooklyn", "category": "American", "pictures": [], "ratings": []},
    {"name": "Connecticut Muffin", "address": "115 Montague St", "neighborhood": "Downtown Brooklyn", "category": "Bakery & Pastries", "pictures": [], "ratings": []},
    {"name": "D-Town Deli", "address": "26 Nevins St", "neighborhood": "Downtown Brooklyn", "category": "Deli Food", "pictures": [], "ratings": []},
    {"name": "Damascus Pastry", "address": "195 Atlantic Ave", "neighborhood": "Downtown Brooklyn", "category": "Middle Eastern", "pictures": [], "ratings": []},
    {"name": "Dellarocco's", "address": "214 Hicks St", "neighborhood": "Downtown Brooklyn", "category": "Pizza", "pictures": [], "ratings": []},
    {"name": "Dish", "address": "81 Washington St", "neighborhood": "Downtown Brooklyn", "category": "Mediterranean", "pictures": [], "ratings": []},
    {"name": "DLO Infusion Bar", "address": "145 Front St", "neighborhood": "Downtown Brooklyn", "category": "Other", "pictures": [], "ratings": []},
    {"name": "Don Nico's", "address": "9 Dekalb Ave Ste 43", "neighborhood": "Downtown Brooklyn", "category": "Mexican", "pictures": [], "ratings": []},
    {"name": "Fascati Pizza", "address": "80 Henry St", "neighborhood": "Downtown Brooklyn", "category": "Italian", "pictures": [], "ratings": []},
    {"name": "Fast & Fresh Burrito Deli", "address": "84 Hoyt St", "neighborhood": "Downtown Brooklyn", "category": "Mexican", "pictures": [], "ratings": []},
    {"name": "Five Guys", "address": "138 Montague St", "neighborhood": "Downtown Brooklyn", "category": "Burgers", "pictures": [], "ratings": []},
    {"name": "Foragers Market", "address": "56 Adams St", "neighborhood": "Downtown Brooklyn", "category": "Deli Food", "pictures": [], "ratings": []},
    {"name": "Fornino", "address": "Brooklyn Bridge Park", "neighborhood": "Downtown Brooklyn", "category": "Pizza", "pictures": [], "ratings": []},
    {"name": "Fortune House", "address": "82 Henry St", "neighborhood": "Downtown Brooklyn", "category": "Chinese", "pictures": [], "ratings": []},
    {"name": "FrozenPeaks", "address": "115 Court St", "neighborhood": "Downtown Brooklyn", "category": "Desserts", "pictures": [], "ratings": []},
    {"name": "Gallitos Kitchen", "address": "140 Montague St", "neighborhood": "Downtown Brooklyn", "category": "Mexican", "pictures": [], "ratings": []},
    {"name": "Ganso Ramen", "address": "25 Bond St", "neighborhood": "Downtown Brooklyn", "category": "Japanese", "pictures": [], "ratings": []},
    {"name": "Golden Fried Dumplings", "address": "192 Duffield St", "neighborhood": "Downtown Brooklyn", "category": "Chinese", "pictures": [], "ratings": []},
    {"name": "Golden Krust", "address": "139 Lawrence Ave", "neighborhood": "Downtown Brooklyn", "category": "Jamaican", "pictures": [], "ratings": []},
    {"name": "Govinda's", "address": "305 Schermerhorn St", "neighborhood": "Downtown Brooklyn", "category": "Indian", "pictures": [], "ratings": []},
    {"name": "Gran Electrica", "address": "5 Front St", "neighborhood": "Downtown Brooklyn", "category": "Mexican", "pictures": [], "ratings": []},
    {"name": "Great Wall", "address": "60 Henry St", "neighborhood": "Downtown Brooklyn", "category": "Chinese", "pictures": [], "ratings": []},
    {"name": "Green Power Cafe", "address": "194 Joralemon St", "neighborhood": "Downtown Brooklyn", "category": "Smoothies & Juices", "pictures": [], "ratings": []},
    {"name": "Grimaldi's", "address": "1 Front St", "neighborhood": "Downtown Brooklyn", "category": "Pizza", "pictures": [], "ratings": []},
    {"name": "Haagen-Dazs", "address": "120 Montague St", "neighborhood": "Downtown Brooklyn", "category": "Desserts", "pictures": [], "ratings": []},
    {"name": "Heights Cafe", "address": "84 Montague St", "neighborhood": "Downtown Brooklyn", "category": "American", "pictures": [], "ratings": []},
    {"name": "Heights Falafel", "address": "78 Henry St", "neighborhood": "Downtown Brooklyn", "category": "Middle Eastern", "pictures": [], "ratings": []},
    {"name": "Henry Street Ale House", "address": "62 Henry St", "neighborhood": "Downtown Brooklyn", "category": "American", "pictures": [], "ratings": []},
    {"name": "Henry's End Restaurant", "address": "44 Henry St", "neighborhood": "Downtown Brooklyn", "category": "American", "pictures": [], "ratings": []},
    {"name": "Hillside", "address": "70 Hudson Ave", "neighborhood": "Downtown Brooklyn", "category": "American", "pictures": [], "ratings": []},
    {"name": "Iris Cafe", "address": "20 Columbia Pl", "neighborhood": "Downtown Brooklyn", "category": "American", "pictures": [], "ratings": []},
    {"name": "Jack The Horse Tavern", "address": "66 Hicks St", "neighborhood": "Downtown Brooklyn", "category": "American", "pictures": [], "ratings": []},
    {"name": "Jacques Torres Chocolate", "address": "66 Water St", "neighborhood": "Downtown Brooklyn", "category": "Desserts", "pictures": [], "ratings": []},
    {"name": "Jeni's Splendid Ice Cream", "address": "Location Varies", "neighborhood": "Downtown Brooklyn", "category": "Desserts", "pictures": [], "ratings": []},
    {"name": "Jimi's", "address": "52 Jay St", "neighborhood": "Downtown Brooklyn", "category": "Chinese", "pictures": [], "ratings": []},
    {"name": "Juliana's", "address": "19 Old Fulton St", "neighborhood": "Downtown Brooklyn", "category": "Pizza", "pictures": [], "ratings": []},
    {"name": "June Wine Bar", "address": "31 Court St", "neighborhood": "Downtown Brooklyn", "category": "Alcohol", "pictures": [], "ratings": []},
    {"name": "Kaya NYC", "address": "Location Varies", "neighborhood": "Downtown Brooklyn", "category": "Asian Fusion", "pictures": [], "ratings": []},
    {"name": "Kung Fu Tea", "address": "40 Hoyt St", "neighborhood": "Downtown Brooklyn", "category": "Teahouses", "pictures": [], "ratings": []},
    {"name": "La Bagel Delight", "address": "104 Front St", "neighborhood": "Downtown Brooklyn", "category": "Deli Food", "pictures": [], "ratings": []},
    {"name": "La Bagel Delight", "address": "90 Court St", "neighborhood": "Downtown Brooklyn", "category": "Deli Food", "pictures": [], "ratings": []},
    {"name": "La Colombe", "address": "50 Washington St", "neighborhood": "Downtown Brooklyn", "category": "Coffee & Tea", "pictures": [], "ratings": []},
    {"name": "Lait Cafe", "address": "129 Livingston Street", "neighborhood": "Downtown Brooklyn", "category": "Coffee & Tea", "pictures": [], "ratings": []},
    {"name": "Lassen & Hennigs", "address": "114 Montague St", "neighborhood": "Downtown Brooklyn", "category": "Bakery & Pastries", "pictures": [], "ratings": []},
    {"name": "Le Pain Quotidien", "address": "121 Montague St", "neighborhood": "Downtown Brooklyn", "category": "Belgian", "pictures": [], "ratings": []},
    {"name": "Lee's Villa", "address": "152 Lawrence St", "neighborhood": "Downtown Brooklyn", "category": "Chinese", "pictures": [], "ratings": []},
    {"name": "Liddabit Sweets", "address": "Location Varies", "neighborhood": "Downtown Brooklyn", "category": "Desserts", "pictures": [], "ratings": []},
    {"name": "Little Muenster Tiny Takeout", "address": "145 Front St", "neighborhood": "Downtown Brooklyn", "category": "Sandwiches", "pictures": [], "ratings": []},
    {"name": "Livingston Manor", "address": "42 Hoyt St", "neighborhood": "Downtown Brooklyn", "category": "Cocktails", "pictures": [], "ratings": []},
    {"name": "Lizzmonade Brooklyn", "address": "Old Fulton St", "neighborhood": "Downtown Brooklyn", "category": "Other", "pictures": [], "ratings": []},
    {"name": "Long Island", "address": "110 Atlantic Ave", "neighborhood": "Downtown Brooklyn", "category": "Cocktails", "pictures": [], "ratings": []},
    {"name": "M.O.B.", "address": "525 Atlantic Ave", "neighborhood": "Downtown Brooklyn", "category": "Vegetarian", "pictures": [], "ratings": []},
    {"name": "Mamselles Teas and Tarts", "address": "145 Front St", "neighborhood": "Downtown Brooklyn", "category": "Jamaican", "pictures": [], "ratings": []},
    {"name": "Metro Deli", "address": "115 Willoughby St", "neighborhood": "Downtown Brooklyn", "category": "Deli Food", "pictures": [], "ratings": []},
    {"name": "Metro King", "address": "538 Fulton Mall", "neighborhood": "Downtown Brooklyn", "category": "Japanese", "pictures": [], "ratings": []},
    {"name": "Metro Star Cafe", "address": "369 Jay St", "neighborhood": "Downtown Brooklyn", "category": "Italian", "pictures": [], "ratings": []},
    {"name": "Misdemeanor", "address": "85 Smith St", "neighborhood": "Downtown Brooklyn", "category": "Cocktails", "pictures": [], "ratings": []},
    {"name": "Miso Restaurant", "address": "40 Main St", "neighborhood": "Downtown Brooklyn", "category": "Japanese", "pictures": [], "ratings": []},
    {"name": "Mocha Hookah", "address": "183 Atlantic Ave", "neighborhood": "Downtown Brooklyn", "category": "Middle Eastern", "pictures": [], "ratings": []},
    {"name": "Noodle Pudding", "address": "38 Henry St", "neighborhood": "Downtown Brooklyn", "category": "Italian", "pictures": [], "ratings": []},
    {"name": "O'Keefe's Bar & Grill", "address": "62 Court St", "neighborhood": "Downtown Brooklyn", "category": "American", "pictures": [], "ratings": []},
    {"name": "One Girl Cookies", "address": "33 Main St", "neighborhood": "Downtown Brooklyn", "category": "Bakery & Pastries", "pictures": [], "ratings": []},
    {"name": "One Way Deli", "address": "26 Court St", "neighborhood": "Downtown Brooklyn", "category": "Cheesesteaks", "pictures": [], "ratings": []},
    {"name": "Orange Leaf", "address": "345 Adams St", "neighborhood": "Downtown Brooklyn", "category": "Desserts", "pictures": [], "ratings": []},
    {"name": "Ozu Japanese Restaurant", "address": "78 Clark St", "neighborhood": "Downtown Brooklyn", "category": "Japanese", "pictures": [], "ratings": []},
    {"name": "Pair", "address": "140 Atlantic Ave", "neighborhood": "Downtown Brooklyn", "category": "Alcohol", "pictures": [], "ratings": []},
    {"name": "Panera Bread", "address": "345 Adams Street", "neighborhood": "Downtown Brooklyn", "category": "Bakery & Pastries", "pictures": [], "ratings": []},
    {"name": "Pardes", "address": "497 Atlantic Ave", "neighborhood": "Downtown Brooklyn", "category": "American", "pictures": [], "ratings": []},
    {"name": "Patty Plus", "address": "324 Livingston St", "neighborhood": "Downtown Brooklyn", "category": "Jamaican", "pictures": [], "ratings": []},
    {"name": "Potpuri", "address": "Location Varies", "neighborhood": "Downtown Brooklyn", "category": "Indian", "pictures": [], "ratings": []},
    {"name": "Punto Bianco Cafe", "address": "20 Jay St", "neighborhood": "Downtown Brooklyn", "category": "Mediterranean", "pictures": [], "ratings": []},
    {"name": "Queen Italian Restaurant", "address": "84 Court St", "neighborhood": "Downtown Brooklyn", "category": "Italian", "pictures": [], "ratings": []},
    {"name": "Red Mango", "address": "123 Court St", "neighborhood": "Downtown Brooklyn", "category": "Smoothies & Juices", "pictures": [], "ratings": []},
    {"name": "Rice & Miso Everyday", "address": "Location Varies", "neighborhood": "Downtown Brooklyn", "category": "Japanese", "pictures": [], "ratings": []},
    {"name": "River Deli", "address": "32 Joralemon St", "neighborhood": "Downtown Brooklyn", "category": "Italian", "pictures": [], "ratings": []},
    {"name": "Roebling Inn", "address": "97 Atlantic Ave", "neighborhood": "Downtown Brooklyn", "category": "Bar Food", "pictures": [], "ratings": []},
    {"name": "Seattle's Best", "address": "253 Livingston St", "neighborhood": "Downtown Brooklyn", "category": "Coffee & Tea", "pictures": [], "ratings": []},
    {"name": "Shake Shack", "address": "1 Old Fulton St", "neighborhood": "Downtown Brooklyn", "category": "Burgers", "pictures": [], "ratings": []},
    {"name": "Shake Shack", "address": "409 Fulton St", "neighborhood": "Downtown Brooklyn", "category": "Burgers", "pictures": [], "ratings": []},
    {"name": "Siz-In-Pan", "address": "318 Livingston St", "neighborhood": "Downtown Brooklyn", "category": "Asian Fusion", "pictures": [], "ratings": []},
    {"name": "Smith Food Express", "address": "21 Smith St", "neighborhood": "Downtown Brooklyn", "category": "Deli Food", "pictures": [], "ratings": []},
    {"name": "Sociale", "address": "72 Henry St", "neighborhood": "Downtown Brooklyn", "category": "Italian", "pictures": [], "ratings": []},
    {"name": "Souvlaki House", "address": "158 Lawrence St", "neighborhood": "Downtown Brooklyn", "category": "Greek", "pictures": [], "ratings": []},
    {"name": "St. Ann's Warehouse", "address": "45 Water St", "neighborhood": "Downtown Brooklyn", "category": "Coffee & Tea", "pictures": [], "ratings": []},
    {"name": "St. Gambrinus Beer Shoppe", "address": "533 Atlantic Ave", "neighborhood": "Downtown Brooklyn", "category": "Other", "pictures": [], "ratings": []},
    {"name": "Super Taco Plus", "address": "51B Willoughby St", "neighborhood": "Downtown Brooklyn", "category": "Mexican", "pictures": [], "ratings": []},
    {"name": "Super Taco", "address": "54 Willoughby St", "neighborhood": "Downtown Brooklyn", "category": "Southwestern", "pictures": [], "ratings": []},
    {"name": "Superfine", "address": "126 Front St", "neighborhood": "Downtown Brooklyn", "category": "Mediterranean", "pictures": [], "ratings": []},
    {"name": "Sushi Gallery", "address": "71 Clark St", "neighborhood": "Downtown Brooklyn", "category": "Japanese", "pictures": [], "ratings": []},
    {"name": "Sushi Ganso", "address": "31 3rd Ave", "neighborhood": "Downtown Brooklyn", "category": "Sushi", "pictures": [], "ratings": []},
    {"name": "Tazza", "address": "311 Henry St", "neighborhood": "Downtown Brooklyn", "category": "Coffee & Tea", "pictures": [], "ratings": []},
    {"name": "Tazza", "address": "72 Clark St", "neighborhood": "Downtown Brooklyn", "category": "Italian", "pictures": [], "ratings": []},
    {"name": "Teresa's", "address": "80 Montague St", "neighborhood": "Downtown Brooklyn", "category": "Polish", "pictures": [], "ratings": []},
    {"name": "The Archives", "address": "333 Adams St", "neighborhood": "Downtown Brooklyn", "category": "American", "pictures": [], "ratings": []},
    {"name": "The Brazen Head", "address": "228 Atlantic Ave", "neighborhood": "Downtown Brooklyn", "category": "Wings", "pictures": [], "ratings": []},
    {"name": "The Brooklyn Ice Cream Factory", "address": "1 Water St", "neighborhood": "Downtown Brooklyn", "category": "Desserts", "pictures": [], "ratings": []},
    {"name": "The Landing", "address": "20 Old Fulton St", "neighborhood": "Downtown Brooklyn", "category": "Hot Dogs", "pictures": [], "ratings": []},
    {"name": "The River Cafe", "address": "1 Water St", "neighborhood": "Downtown Brooklyn", "category": "American", "pictures": [], "ratings": []},
    {"name": "Tony's Famous Pizza", "address": "2 Dekalb Ave", "neighborhood": "Downtown Brooklyn", "category": "Pizza", "pictures": [], "ratings": []},
    {"name": "Uncle Louie G", "address": "40 Hoyt St", "neighborhood": "Downtown Brooklyn", "category": "Desserts", "pictures": [], "ratings": []},
    {"name": "Vinegar Hill House", "address": "72 Hudson Ave", "neighborhood": "Downtown Brooklyn", "category": "American", "pictures": [], "ratings": []},
    {"name": "Wingstop", "address": "289 Livingston St", "neighborhood": "Downtown Brooklyn", "category": "Wings", "pictures": [], "ratings": []},
    {"name": "Wok & Roll", "address": "1 MetroTech Center N", "neighborhood": "Downtown Brooklyn", "category": "Chinese", "pictures": [], "ratings": []},
    {"name": "Yummy Taco", "address": "52 Willoughby St", "neighborhood": "Downtown Brooklyn", "category": "Mexican", "pictures": [], "ratings": []}
    ]
"""




#db.restaurants.remove()
#db.rating.remove()
#for x in data:
#    db.restaurants.insert(x)

#    {"name": "Yummy Taco", "address": "52 Willoughby St", "neighborhood": "Downtown Brooklyn", "category": "Mexican", "pictures": [], "ratings": []}



RESTAURANTS = [

    ["Roccos Tacos", "339 Adams St, Brooklyn, NY 11201", "Downtown Brooklyn", "Mexican", [
            "http://travelupdate.boardingarea.com/wp-content/uploads/2014/08/IMG_8681.jpg",
            "http://cdn.chilledmagazine.com/wp-content/uploads/2015/07/Fresh-Dishes-from-Roccos-Tacos.jpg",
            "https://media-cdn.tripadvisor.com/media/photo-s/0e/89/cd/91/exterior-shot-of-rocco.jpg" ]
     ,"Andrew"],



        ["Juniors Restaurant", "386 Flatbush Ave Ext, Brooklyn, NY 11201", "Downtown Brooklyn", "Diner", [
            "http://vp.cdn.cityvoterinc.com/GetImage.ashx?img=00/00/00/02/25/75/22575-556377.jpg",
            "https://blankslatepages.s3.amazonaws.com/54d8d6d95b7d6-4fc5c4dafc853d23410f6a706700cd7f.jpg",
            "http://www4.pictures.zimbio.com/gi/Brooklyn+Famous+Junior+Restaurant+Sold+Developer+YzQbBj6bSwZl.jpg" ]
         ],

        ["Yaso Tangbao", "148 Lawrence St, Brooklyn, NY 11201", "Downtown Brooklyn", "Shanghainese", [
            "http://s3.amazonaws.com/downtownbrooklyn/imgr/listings/yaso-tangbao.jpg",
            "http://yasotangbao.com/img/slide_small1.png",
            "https://brklynhospitality.files.wordpress.com/2016/05/7461c866-4d3d-4523-8412-5dc83c93782b.jpg",
            "https://s3-media2.fl.yelpcdn.com/bphoto/YVrNtlNJd3pciib539PV1Q/o.jpg" ]
         ],

        ["Hill Country Barbecue Market", "345 Adams Street (on Willoughby Plaza), Brooklyn, NY 11201", "Downtown Brooklyn", "Barbecue", [
            "https://resizer.otstatic.com/v2/photos/large/24005275.jpg",
            "https://www.giltcity.com/images/share/uploads/0000/0001/5532/155324236/orig.jpg",
            "http://s3.amazonaws.com/downtownbrooklyn/imgr/listings/hill-country-barbecue-market.jpg" ]
         ],

        ["Myrtle & Gold", "343 Gold St, Brooklyn, NY 11201", "Downtown Brooklyn", "American", [
            "http://3f60kb4wap2qw7kd14ry4wy1.wpengine.netdna-cdn.com/wp-content/uploads/2015/06/20150611_160642.jpg",
            "https://s3-media1.fl.yelpcdn.com/bphoto/vz4xwOUZJsXDhoAxCryorQ/348s.jpg",
            "http://blog.whereyoueat.com/wp-content/uploads/2015/10/American-Cafe-in-Downtown-Brooklyn-300x225.jpg",
            "https://s3-media2.fl.yelpcdn.com/bphoto/V1lmHXW1rvP3yhYAokHdhg/348s.jpg" ]
         ],

        ["Pollo Doro", "306 Gold St, Brooklyn, NY 11201", "Downtown Brooklyn", "Peruvian", [
            "https://media-cdn.tripadvisor.com/media/photo-s/06/ce/c9/2e/pollo-d-oro.jpg",
            "https://media-cdn.tripadvisor.com/media/photo-s/08/46/92/1d/pollo-d-oro.jpg",
            "https://s3-media1.fl.yelpcdn.com/bphoto/KyrnVWlXLFKkgdt5RoJ6cA/348s.jpg" ]
         ],

        ["Forno Rosso", "327 Gold St, Brooklyn, NY 11201", "Downtown Brooklyn", "Italian", [
            "http://nebula.wsimg.com/808673d579f82b714c8817a42932d75d?AccessKeyId=0F80301A12A3736C97F6&disposition=0&alloworigin=1",	"http://79eeea381619f313d82e-993cdc17da461fcae971e861a6f98752.r94.cf1.rackcdn.com/chicago/venue/image/1000004377/30341-Forno.jpg",
            "http://nebula.wsimg.com/6c3ec0979618bfaf11f6c252e21f8dd4?AccessKeyId=0F80301A12A3736C97F6&disposition=0&alloworigin=1" ]
         ],

        ["Bijans", "81 Hoyt St, Brooklyn, NY 11201", "Downtown Brooklyn", "Italian", [
            "https://resizer.otstatic.com/v2/profiles/legacy/147940.jpg",
            "https://s3-media1.fl.yelpcdn.com/bphoto/XiVzej2h25d60cq370d-sA/348s.jpg",
            "http://pages.blankslate.com/scripts/timthumb.php?w=450&h=400&zc=1&src=https://blankslatepages.s3.amazonaws.com/bijan%27s-6b79a77180e9ec3a7ca351ebe54641a2-1400791524-bijan%27s-4.jpg" ]
         ],

        ["The Wei", "30 Dekalb Ave, Brooklyn, NY 11201", "Downtown Brooklyn", "Chinese", [
            "https://s3-media1.fl.yelpcdn.com/bphoto/bAsLn1UuUhornsm0h-_3sQ/348s.jpg",
            "https://s3-media2.fl.yelpcdn.com/bphoto/fkjzVN8tYAeZ1PFe8oMW9A/348s.jpg",
            "https://s3-media3.fl.yelpcdn.com/bphoto/MAN5ru1Y6Lz9AEJafNPL5g/348s.jpg",
            "http://thewei.nyc/wp-content/uploads/2014/05/front-2048x853.jpg" ]
         ],

        ["Broccolino", "213 Smith St, Brooklyn, NY 11201", "Downtown Brooklyn", "Italian", [
            "https://assets.dnainfo.com/photo/2016/10/1476298988-276921/larger.jpg",
            "https://pbs.twimg.com/media/C7J-rmsXUAI3X--.jpg",
            "https://resizer.otstatic.com/v2/photos/large/24910496.jpg",
            "https://pbs.twimg.com/media/C8CacXZXUAELvBj.jpg" ]
         ],

        ["Jun Shokudo", "306 Gold St, Brooklyn, NY 11201", "Downtown Brooklyn", "Japanese", [
            "https://media-cdn.tripadvisor.com/media/photo-s/0a/45/c7/eb/side.jpg",
            "https://s3-media3.fl.yelpcdn.com/bphoto/BMzkEBtZNnvTbIm4vyA51w/348s.jpg",
            "http://www.asianfusion-mag.com/wp-content/uploads/2016/12/Jun_Shokudo_1773_spicy_miso_seafood_udon.jpg",
            "http://www.asianfusion-mag.com/wp-content/uploads/2016/12/Jun_Shokudo_1814_all_dishes.jpg" ]
         ],

        ["Domo Taco", "66 Willoughby St, Brooklyn, NY 11201", "Downtown Brooklyn", "Asian", [
            "https://s3-media1.fl.yelpcdn.com/bphoto/HOY94WqrdSmVwxBeoiy54A/348s.jpg",
            "http://smartassdesign.imgix.net/imgr/Domo-Taco-2-2x.jpg?fm=jpg&auto=compress,enhance,format&w=1200",
            "https://s3-media2.fl.yelpcdn.com/bphoto/GLMHpzPubW-mpfRkix5QvA/348s.jpg" ]
         ,"Andrew"],

        ["Brooklyn Brewhouse", "229 Duffield St, Brooklyn, NY 11201", "Downtown Brooklyn", "American", [
            "http://s3.amazonaws.com/downtownbrooklyn/imgr/listings/brooklyn-brewhouse.jpg",
            "https://s3-media2.fl.yelpcdn.com/bphoto/z7kQSJTLBDnOhPbZb6D26Q/ls.jpg",
            "https://s3-media1.fl.yelpcdn.com/bphoto/0x1si1-hPNxuSN95BqTvPg/o.jpg" ]
         ],

        ["The Juice Box", "114 Dekalb Ave, Brooklyn, NY 11201", "Downtown Brooklyn", "Cafe", [
            "https://s3-media4.fl.yelpcdn.com/bphoto/pu_kXHGzSkQ2ijMOa4ZmpA/348s.jpg",
            "https://res.cloudinary.com/grubhub/image/upload/w_264,h_198,f_auto,fl_lossy,q_80,b_rgb:000,o_80,c_fill/umh9ibqcp2ufzhavvehe",
            "https://s3-media3.fl.yelpcdn.com/bphoto/M-MH7oSfqgJoxB0q3Fwtsw/348s.jpg" ]
         ],

        ["Amarachi Restaurant", "189 Bridge St, Brooklyn, NY 11201", "Downtown Brooklyn", "Grill", [
            "https://s3-media4.fl.yelpcdn.com/bphoto/2slDZhvAVXunPhN4h_2NOA/ls.jpg",
            "http://www.reachfolk.com/wp-content/uploads/2016/09/0_0_0_0_539_303_csupload_67676720.jpg",
            "https://rdc.rdcimage.com/partner-images/226313/micrositeimage_photo1.jpg" ]
         ],

        ["Golden Fried Dumpling", "192 Duffield St, Brooklyn, NY 11201", "Downtown Brooklyn", "Chinese", [
            "https://s3-media3.fl.yelpcdn.com/bphoto/zuvdJyknn5vGElyxkbyh2Q/348s.jpg",
            "https://media-cdn.tripadvisor.com/media/photo-s/03/2b/b8/60/golden-fried-dumplings.jpg",
            "https://b.zmtcdn.com/data/pictures/9/17763779/df75b2bfa96de0e882912c8884fefb75.jpg" ]
         ],

        ["Ganso Ramen", "25 Bond St, Brooklyn, NY 11201", "Downtown Brooklyn", "Japanese", [
            "http://gansonyc.com/wordpress/wp-content/gallery/photos/ganso-kakuni-ramen.jpg",
            "http://smartassdesign.imgix.net/imgr/ganso-ramen.jpg?fm=jpg&auto=compress,enhance,format&w=1200",
            "https://s3-media3.fl.yelpcdn.com/bphoto/LQtFPZrtPPrTBYdlE4qszQ/348s.jpg" ]
         ],

        ["Kimoto Rooftop Bar & Lounge", "216 Duffield St, Brooklyn, NY 11201", "Downtown Brooklyn", "Asian", [
            "https://media-cdn.tripadvisor.com/media/photo-s/0d/74/dd/1a/summer-movie-nights.jpg",
            "http://images1.villagevoice.com/imager/u/745xauto/7762992/kimoto_spam_sushi_dog_ext_lo_by_michael_tulipan.jpg",
            "https://d3tv8y14ogpztx.cloudfront.net/pulses/images/000/029/226/wide_product/kimoto-inside.jpg" ]
         ],

        ["La Defense Bistro", "2 MetroTech Center, Brooklyn, NY 11201", "Downtown Brooklyn", "French", [
            "https://s3-media4.fl.yelpcdn.com/bphoto/048D1Jgt7c_mJ8cwCbBbyg/348s.jpg",
            "http://assets.nydailynews.com/polopoly_fs/1.1980623.1413826995!/img/httpImage/image.jpg_gen/derivatives/article_750/aline26f-13-web.jpg",
            "https://media-api.xogrp.com/images/4dd0c4c7-3121-4f11-b7d1-41b840e80997~rs_2001.480.fit.jpg" ]
         ],

        ["SUBWAY Restaurants", "391 Jay St, Brooklyn, NY 11201", "Downtown Brooklyn", "Sandwich", [
            "https://igx.4sqi.net/img/general/600x600/s4pLQXrlBkUGsJMSnqyoya6tB5-kj__NRSiN28XVP_U.jpg",
            "https://igx.4sqi.net/img/general/600x600/14FCWPATN1K13OFQ4VF5ZIHXDC45NDHIYQV4LKWU051YBP25.jpg",
            "https://s3-media3.fl.yelpcdn.com/bphoto/aV6V0yZlOi_wUbjXaZDS7A/ls.jpg" ]
         ],  

        ["Brasserie Seoul", " 300 Schermerhorn St, Brooklyn, NY 11217", "Downtown Brooklyn", "French", [
            "https://static1.squarespace.com/static/57055938c6fc08c6df557ec4/57055f5ca3360cc2b0dc52cc/57354ccdc2ea51b32cf79a55/1469476036398/IMG_0956a.jpg?format=1500w",
            "http://www.nycgo.com/images/venues/13211/brasserie-seoul-han-gyeol-lyu-006__x_large.jpg",
            "http://www.nycgo.com/images/venues/13211/brasserie-seoul-han-gyeol-lyu-001__x_large.jpg" ]
         ],

        ["Lucianos", "15 MetroTech Center, Brooklyn, NY 11201", "Downtown Brooklyn", "Italian", [
            "https://s3-media4.fl.yelpcdn.com/bphoto/2PZiAhNjA2-YDHtPdHQlGA/o.jpg",
            "https://s3-media3.fl.yelpcdn.com/bphoto/joQiqtacsSFWOaeS1pq5EQ/348s.jpg",
            "https://s3-media1.fl.yelpcdn.com/bphoto/-Ms_ARIrnIA9lkgqlgKChQ/180s.jpg" ]
         ],

        ["Sophies Cuban Cuisine", "27 Smith St, Brooklyn, NY 11201", "Downtown Brooklyn", "Cuban", [
            "http://dcdiningguide.com/wp-content/uploads/2014/02/Sophies.jpg",
            "http://s3.amazonaws.com/downtownbrooklyn/imgr/listings/sophies-cuban-cuisine.jpg",
            "http://ot-foodspotting-production.s3.amazonaws.com/reviews/1633196/thumb_600.jpg?1335126399" ]
         ],

        ["Buffalo Boss", "400 Jay St, Brooklyn, NY 11201", "Downtown Brooklyn", "Chicken Wings", [
            "http://whereyoueat.com/images/restaurants/8053/gallery/0001-BG.jpg",
            "https://s3-media2.fl.yelpcdn.com/bphoto/8I3Fbt5TDQDfolh-WVw2wQ/ls.jpg",	"http://static.wixstatic.com/media/fa0f75_4f0a7fefa2be45d8b240276bd5d93416.jpg_srz_917_300_85_22_0.50_1.20_0.00_jpg_srz" ]
         ],

        ["Souvlaki House", "158 Lawrence St, Brooklyn, NY 11201", "Downtown Brooklyn", "Gyro", [
            "https://s3-media4.fl.yelpcdn.com/bphoto/AJZ1CAqFXsvKhR66w8Mvug/348s.jpg",
            "http://cdn2.vox-cdn.com/uploads/chorus_asset/file/968372/jurybrooksouvlaki.0.jpg",
            "http://www.brooklynpaper.com/assets/photos/38/35/dtg-souvlaki-house-go-there-now-2015-09-04-bk02_z.jpg",
            "http://assets.nydailynews.com/polopoly_fs/1.2256670.1434148068!/img/httpImage/image.jpg_gen/derivatives/article_750/2line21f-21-web.jpg" ]
         ]
    ]


"""
    # Name, Address, Neighborhood, Category, Pictures {}, Ratings {}
    ["Rocco's Tacos", "339 Adams St, Brooklyn, NY 11201", "Downtown Brooklyn", "Mexican", [
            "http://travelupdate.boardingarea.com/wp-content/uploads/2014/08/IMG_8681.jpg",
            "http://cdn.chilledmagazine.com/wp-content/uploads/2015/07/Fresh-Dishes-from-Roccos-Tacos.jpg"
            ]
     ]
    #["Taco Bell", "18 E 14th St, New York, NY 10003", "Union Square", "Mexican", {

    ]
"""


db.restaurants.remove()
db.ratings.remove()
for x in RESTAURANTS:
    if len(x) == 6:
        db.restaurants.insert({ "name": x[0],
                                "address": x[1],
                                "neighborhood": x[2],
                                "category": x[3],
                                "pictures": x[4],
                                "ratings": [],
                                "creator": x[5]
                                })
    else:
        db.restaurants.insert({ "name": x[0],
                                "address": x[1],
                                "neighborhood": x[2],
                                "category": x[3],
                                "pictures": x[4],
                                "ratings": []
                                })

