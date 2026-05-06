import random
import time
import json

services = ["network", "compute", "storage", "database"]

def generate_log():
    service = random.choice(services)

    if random.random() < 0.1:
        status = "ERROR"
        latency = random.randint(300, 1000)
    elif random.random() < 0.2:
        status = "WARNING"
        latency = random.randint(100, 300)
    else:
        status = "OK"
        latency = random.randint(10, 100)

    return {
        "service": service,
        "status": status,
        "latency": latency,
        "timestamp": time.time()
    }

if __name__ == "__main__":
    with open("logs.json", "a") as file:
        for _ in range(20):
            log = generate_log()
            print(log)

            # save as JSON line
            file.write(json.dumps(log) + "\n")

            time.sleep(1)