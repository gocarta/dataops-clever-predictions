# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "datablob",
#     "requests",
#     "simple-env",
# ]
# ///
import datablob
import requests
import simple_env as se
from time import sleep

AWS_BUCKET_NAME = se.get("AWS_BUCKET_NAME")
AWS_BUCKET_PATH = se.get("AWS_BUCKET_PATH")
CLEVER_BUS_TIME_API_KEY = se.get("CLEVER_BUS_TIME_API_KEY")

client = datablob.DataBlobClient(
    bucket_name=AWS_BUCKET_NAME, bucket_path=AWS_BUCKET_PATH
)

vehicles = client.get_dataset_as_json(name="clever_vehicle_locations", version="1")

results = []

for vehicle in vehicles:
    sleep(0.1)
    vid = vehicle["vehicle_id"]
    pred_url = f"https://bustracker.gocarta.org/bustime/api/v3/getpredictions?key={CLEVER_BUS_TIME_API_KEY}&vid={vid}&format=json"

    resp = requests.get(pred_url).json().get("bustime-response", {})

    # skip if there are no predictions (sometimes 'error' is returned instead of 'prd')
    if "prd" not in resp:
        continue

    predictions = resp["prd"]

    # sometimes only 1 prediction is returned
    if isinstance(predictions, dict):
        results.append(predictions)
    else:
        results += predictions

client.update_dataset(
    name="clever_predictions",
    version="1",
    data=results,
    description="Clever Predictions",
)
print(f"[dataops-clever-predictions] updated {len(results)} rows")
