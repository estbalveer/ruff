ORCHESTRA = {
    "violin": "strings",
    "oboe": "woodwind",
    "tuba": "brass",
    "gong": "percussion",
}

# Errors
for instrument in ORCHESTRA:
    print(f"{instrument}: {ORCHESTRA[instrument]}")

for instrument in ORCHESTRA:
    ORCHESTRA[instrument]

for instrument in ORCHESTRA.keys():
    print(f"{instrument}: {ORCHESTRA[instrument]}")

for instrument in ORCHESTRA.keys():
    ORCHESTRA[instrument]

for instrument in (temp_orchestra := {"violin": "strings", "oboe": "woodwind"}):
    print(f"{instrument}: {temp_orchestra[instrument]}")

for instrument in (temp_orchestra := {"violin": "strings", "oboe": "woodwind"}):
    temp_orchestra[instrument]

# # OK
for instrument, section in ORCHESTRA.items():
    print(f"{instrument}: {section}")

for instrument, section in ORCHESTRA.items():
    section

for instrument, section in (
    temp_orchestra := {"violin": "strings", "oboe": "woodwind"}
).items():
    print(f"{instrument}: {section}")

for instrument, section in (
    temp_orchestra := {"violin": "strings", "oboe": "woodwind"}
).items():
    section

for instrument in ORCHESTRA:
    ORCHESTRA[instrument] = 3


# Shouldn't trigger for non-dict types
items = {1, 2, 3, 4}
for i in items:
    items[i]

items = [1, 2, 3, 4]
for i in items:
    items[i]


# A case with multiple uses of the value to show off the secondary annotations
for instrument in ORCHESTRA:
    data = json.dumps(
        {
            "instrument": instrument,
            "section": ORCHESTRA[instrument],
        }
    )

    print(f"saving data for {instrument} in {ORCHESTRA[instrument]}")

    with open(f"{instrument}/{ORCHESTRA[instrument]}.txt", "w") as f:
        f.write(data)


# This should still suppress the error
for (  # noqa: PLC0206
    instrument
) in ORCHESTRA:
    print(f"{instrument}: {ORCHESTRA[instrument]}")


# Assigning to the dictionary should suppress the diagnostic: `.items()` would
# not remove the need to index by key, and the value can be stale after a write.
for instrument in ORCHESTRA.keys():
    if ORCHESTRA[instrument]:
        ORCHESTRA[instrument] = "strings"

for instrument in ORCHESTRA:
    ORCHESTRA[instrument] = ORCHESTRA[instrument].upper()

for instrument in ORCHESTRA:
    if ORCHESTRA[instrument] == "strings":
        ORCHESTRA[instrument] = "woodwind"
    elif ORCHESTRA[instrument] == "brass":
        ORCHESTRA[instrument] = "percussion"

for instrument in (temp_orchestra := {"violin": "strings"}):
    temp_orchestra[instrument] = temp_orchestra[instrument].upper()

for instrument in ORCHESTRA:
    ORCHESTRA[instrument] += "!"


# Assigning to a different key or dictionary should still be flagged.
for instrument in ORCHESTRA:
    print(ORCHESTRA[instrument])
    ORCHESTRA["violin"] = "strings"

for instrument in ORCHESTRA:
    print(ORCHESTRA[instrument])
    other = {"violin": "strings"}
    other[instrument] = "woodwind"


# Mutating the value without assigning to the subscript should still be flagged.
for instrument in ORCHESTRA:
    ORCHESTRA[instrument].pop("__name__", None)
