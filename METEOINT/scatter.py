import json
import matplotlib.pyplot as plt


input_file = "grid.json"

# Choose one timestamp to extract the grid from

# Load the original GeoJSON file
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

features = data.get("features", [])
target_timestamp = "2026-04-27 12:00:00"

grid_features_lat = []
grid_features_lon = []

# Keep only the points from the selected timestamp
for feature in features:
    timestamp = feature["properties"].get("time")

    if timestamp == target_timestamp:
        coordinates = feature["geometry"].get("coordinates", [])

        grid_features_lat.append(coordinates[0])
        grid_features_lon.append(coordinates[1])


plt.scatter(grid_features_lat, grid_features_lon, marker='o', label='Circle')
plt.title("Scatter Plot with Different Markers")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.legend()
plt.show()
