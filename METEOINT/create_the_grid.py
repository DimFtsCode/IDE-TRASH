import json

input_file = "grid.json"
output_file = "scatter.json"

# Choose one timestamp to extract the grid from
target_timestamp = "2026-04-27 12:00:00"

# Load the original GeoJSON file
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

features = data.get("features", [])

grid_features = []

# Keep only the points from the selected timestamp
for feature in features:
    timestamp = feature["properties"].get("time")

    if timestamp == target_timestamp:
        coordinates = feature["geometry"].get("coordinates", [])

        # Create a clean GeoJSON Feature with only coordinates
        grid_features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": coordinates
            },
            "properties": {}
        })

# Create a new GeoJSON FeatureCollection
grid_data = {
    "type": "FeatureCollection",
    "features": grid_features
}

# Save the new grid file
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(grid_data, f, indent=2)

print(f"Created {output_file}")
print(f"Total grid points saved: {len(grid_features)}")