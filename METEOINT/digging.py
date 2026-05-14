import json
from collections import defaultdict, Counter

file_path = "grid.json"

# Load GeoJSON file
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

features = data.get("features", [])

# Group coordinates by timestamp
coords_by_time = defaultdict(list)

for feature in features:
    timestamp = feature["properties"].get("time")
    coordinates = tuple(feature["geometry"].get("coordinates", []))  # (longitude, latitude)

    coords_by_time[timestamp].append(coordinates)

print(f"The file has {len(features)} records.")
print(f"Unique timestamps found: {len(coords_by_time)}")
print()

# Analyze each timestamp separately
for timestamp, coords in coords_by_time.items():
    total_records = len(coords)
    unique_coords = set(coords)
    unique_count = len(unique_coords)
    duplicate_count = total_records - unique_count

    print(f"Timestamp: {timestamp}")
    print(f"  Total records: {total_records}")
    print(f"  Unique coordinates: {unique_count}")
    print(f"  Duplicate coordinates: {duplicate_count}")

    if duplicate_count == 0:
        print("  Result: All coordinates are different for this timestamp.")
    else:
        print("  Result: Some coordinates are duplicated for this timestamp.")

    print()