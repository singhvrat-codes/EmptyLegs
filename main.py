import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
import models
import ml_engine

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory stores
drivers = []
shipments = []
matches = []

# Global state for scoping
latest_active_shipment_id = None

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/drivers/register")
def register_driver(driver: models.DriverRoute):
    driver_dict = driver.dict()
    # Simulate DB ID
    driver_dict["id"] = len(drivers) + 1
    drivers.append(driver_dict)
    return driver_dict

@app.post("/shipments/create")
def create_shipment(shipment: models.Shipment):
    global latest_active_shipment_id
    shipment_dict = shipment.dict()
    shipment_dict["id"] = len(shipments) + 1
    shipments.append(shipment_dict)
    
    latest_active_shipment_id = shipment_dict["id"]
    
    # Recompute matches
    current_matches = []
    
    # Simple deterministic matching against all available drivers
    # In a real app, availability logic would be more complex
    for d in drivers:
        res = ml_engine.compute_match(d, shipment_dict)
        if res["score"] > 0:
            match_obj = {
                "id": len(matches) + len(current_matches) + 1,
                "match_id": len(matches) + len(current_matches) + 1, # Frontend compat
                "shipment_id": shipment_dict["id"],
                "driver_name": d["driver_name"],
                "score": res["score"],
                "price": res["price"],
                "co2_saved": res["co2_saved"],
                "accepted": False
            }
            current_matches.append(match_obj)
            
    matches.extend(current_matches)
    
    return {
        "shipment_id": shipment_dict["id"], 
        "matches_count": len(current_matches)
    }

@app.get("/matches")
def get_matches(shipment_id: Optional[int] = None):
    # Scope to latest active shipment if not specified (Frontend compat)
    target_id = shipment_id or latest_active_shipment_id
    
    if not target_id:
        return []
        
    return [
        m for m in matches 
        if m["shipment_id"] == target_id and not m.get("accepted")
    ]

@app.post("/matches/{match_id}/accept")
def accept_match(match_id: int):
    # Find match
    match = next((m for m in matches if m["id"] == match_id), None)
    if not match:
        raise HTTPException(status_code=404, detail="Match not found")
    
    if match.get("accepted"):
        raise HTTPException(status_code=400, detail="Match already accepted")
        
    # Mark accepted
    match["accepted"] = True
    
    # Cleanup competing matches for this shipment
    # (In-memory, we can just mark them or filter them out next time)
    # For strict compat with frontend logic:
    for m in matches:
        if m["shipment_id"] == match["shipment_id"] and m["id"] != match_id:
             # Effectively remove or invalidate
             # In this simple store, we leave them but get_matches filters accepted
             pass

    return match

@app.get("/metrics")
def get_metrics():
    accepted = [m for m in matches if m.get("accepted")]
    total_co2 = sum(m["co2_saved"] for m in accepted)
    
    return {
        "total_co2_saved_kg": total_co2,
        "active_matches": len(accepted)
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
