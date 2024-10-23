import json
import os
from cs_ai_common.logging.internal_logger import InternalLogger
import re

from cs_ai_common.seed_data.seed_data_resolver import SeedDataResolver

class LambdaEventSeedDataResolver(SeedDataResolver):
    def __init__(self, event: dict):
        self.event = event

    def get_seed_data(self) -> dict:
        InternalLogger.LogDebug("Getting seed data from lambda event. {}".format(json.dumps(self.event)))        
        seed_data = self.event["seed_data"]
        task_id = self.event["task_id"]
        created_date = self.event["created_date"]
        return {
            "seed_data": {
                "Type": "osobowe",
                "Make": transform(seed_data["Make"]),
                "Model": seed_data["Model"],
                "ProductionYear": seed_data["ProductionYear"],
                "FuelType": seed_data["FuelType"],
                "Mileage": seed_data["Mileage"],
                "Capacity": seed_data["Capacity"],
                "Transmission": seed_data["Transmision"],
                "HorsePower": seed_data["HorsePower"],
                "Generation": ""
            },
            "task_id": task_id,
            "created_date": created_date
        }

def transform(make: str) -> str:
    _val = make.replace(" ", "")
    return re.sub(r'(?<!^)(?=[A-Z])', '-', _val).lower()

     