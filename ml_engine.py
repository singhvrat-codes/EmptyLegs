import math

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def compute_match(driver_dict, shipment_dict):
    # Driver origin -> Pickup
    detour = haversine(
        driver_dict['origin_lat'], driver_dict['origin_lng'],
        shipment_dict['pickup_lat'], shipment_dict['pickup_lng']
    )
    
    # Simple deterministic scoring
    score = max(0.3, 1 - detour / 500)
    
    # Pricing: Base $50 + $1.5/km detour
    price = 50 + detour * 1.5
    
    # CO2: Base assumption vs detour cost
    co2_saved = max(0, 800 - detour * 2)
    
    return {
        "score": score,
        "price": price,
        "co2_saved": co2_saved,
        "detour": detour
    }
