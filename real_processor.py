import pandas as pd
import json
import time

def log_event(service, status, message):
    log = {
        "service": service,
        "status": status,
        "message": message,
        "timestamp": time.time()
    }

    with open("logs.json", "a") as file:
        file.write(json.dumps(log) + "\n")


def process_data():
    service_name = "data_pipeline"

    try:
        log_event(service_name, "INFO", "Starting data processing")

        df = pd.read_csv("data.csv")

        total = 0

        for index, row in df.iterrows():

            # -------------------------
            # VALUE VALIDATION
            # -------------------------
            try:
                value = int(row["value"])
            except:
                log_event(service_name, "ERROR", f"Invalid VALUE at row {index}: {row['value']}")
                continue

            # -------------------------
            # CATEGORY VALIDATION
            # -------------------------
            if str(row["category"]) == "INVALID":
                log_event(service_name, "WARNING", f"Invalid CATEGORY at row {index}")

            # -------------------------
            # STATUS VALIDATION
            # -------------------------
            if str(row["status"]).lower() == "failed":
                log_event(service_name, "ERROR", f"FAILED STATUS at row {index}")

            # -------------------------
            # NOTES VALIDATION
            # -------------------------
            if "corrupt" in str(row["notes"]).lower():
                log_event(service_name, "ERROR", f"Corrupted data at row {index}")

            total += value

        log_event(service_name, "INFO", f"Processing complete. Total = {total}")

    except Exception as e:
        log_event(service_name, "CRITICAL", str(e))


if __name__ == "__main__":
    process_data()