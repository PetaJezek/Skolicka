def avoid_flood(N, M, forecast):
    last_rained = {}  # Dictionary to track the last day each lake rained
    dry_days = []  # Indices of days with no rain
    result = []  # Dragon's drinking schedule

    for day, lake in enumerate(forecast):
        if lake == 0:
            # No rain today, append to dry_days
            dry_days.append(day)
            result.append(0)  # Placeholder for dragon's action
        else:
            if lake in last_rained:
                # Check if there's a dry day available to empty this lake
                can_dry = False
                for i, dry_day in enumerate(dry_days):
                    if dry_day > last_rained[lake]:
                        # Use this dry day to empty the lake
                        result[dry_day] = lake  # Assign lake to be dried on this dry day
                        dry_days.pop(i)  # Remove this dry day from the list
                        can_dry = True
                        break
                if not can_dry:
                    return "FLOOD"  # Flood occurs
            # Update the last rained day for the lake
            last_rained[lake] = day

    # All rains handled without flooding, return the result
    output = [str(x) for x in result if x != 0]  # Filter out unnecessary zeros
    return "OK\n" + " ".join(output)

# Read input
N, M = map(int, input().split())
forecast = list(map(int, input().split()))

# Solve and print the result
print(avoid_flood(N, M, forecast))