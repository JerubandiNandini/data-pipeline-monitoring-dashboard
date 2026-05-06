import pandas as pd

df = pd.read_json("logs.json", lines=True)

print("=== First Logs ===")
print(df.head())

print("\n=== Status Count ===")
print(df["status"].value_counts())

print("\n=== Error Logs ===")
errors = df[df["status"] == "ERROR"]
print(errors[["message"]])

print("\n=== Processing Summary ===")
info_logs = df[df["status"] == "INFO"]
print(info_logs[["message"]])