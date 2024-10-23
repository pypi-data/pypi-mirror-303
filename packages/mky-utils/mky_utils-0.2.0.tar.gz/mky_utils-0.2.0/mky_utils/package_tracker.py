import argparse
import os
import time
import json
import requests

from utils import notify


def track_package(tracking_num: str, freq: int):

    url = "https://api-eu.dhl.com/track/shipments"
    key = os.getenv("DHL_API_KEY")
    headers = {"Accept": "application/json", "DHL-API-Key": key}
    params = {"trackingNumber": tracking_num, "service": "express"}

    prev_events = []
    prev_status = ""
    while True:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()

            events = data["shipments"][0]["events"]
            status = data["shipments"][0]["status"]["status"]

            data_to_dump = {
                "estimatedTimeOfDelivery": (
                    data["shipments"][0]["estimatedTimeOfDelivery"]
                    if "estimatedTimeOfDelivery" in data["shipments"][0]
                    else None
                ),
                "estimatedTimeOfDeliveryRemark": (
                    data["shipments"][0]["estimatedTimeOfDeliveryRemark"]
                    if "estimatedTimeOfDeliveryRemark" in data["shipments"][0]
                    else None
                ),
                "status": data["shipments"][0]["status"],
                "last_event": data["shipments"][0]["events"][0],
            }

            if len(events) > len(prev_events) or status != prev_status:
                notify(
                    f"UPDATE ON PACKAGE {tracking_num}:\n{json.dumps(data_to_dump, indent=2)}"
                )
                prev_events = events
                prev_status = status

            with open("package_status.json", "w") as f:
                json.dump(data_to_dump, f, indent=2)
        else:
            print(f"Error: {response.status_code}, {response.text}")
        time.sleep(freq)


tnum = "6071204683"
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--tracking_num",
        default=tnum,
        help="tracking number of the package",
    )
    parser.add_argument(
        "--freq",
        default="30",
        help=(
            "How often to update package status "
            "(freq < 6 will results in rate_limit being hit)"
        ),
    )
    args = parser.parse_args()
    track_package(args.tracking_num, int(args.freq))
