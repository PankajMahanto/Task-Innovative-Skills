# Initial Data
readings = [12.5, "Error", 18.2, 15.0, "Error", 22.1, 10.8]
print(f"Original List: {readings}")
print("-" * 30)

# --- Task 1: The Cleaner (Search and Replace) ---
# We loop through the list by index to find strings and replace them.
for i in range(len(readings)):
    if readings[i] == "Error":
        readings[i] = 0.0

print(f"After Cleaning: {readings}")


# --- Task 2: The Multiplier (In-place Modification) ---
# We loop through the indices to modify the existing values by 10%.
for i in range(len(readings)):
    readings[i] = readings[i] * 1.1

print(f"After Calibration (+10%): {readings}")


# --- Task 3: The Filter (Selective Removal) ---
# We check the modified values. If < 15.0, we add them to the new list.
low_quality_log = []

for i in range(len(readings)):
    if readings[i] < 15.0:
        low_quality_log.append(readings[i])

print("-" * 30)
print(f"Final Main List: {readings}")
print(f"Low Quality Log: {low_quality_log}")