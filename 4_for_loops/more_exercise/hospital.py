DOCTORS = 7

period = int(input())

treated_patients = untreated_patients = 0

for day in range(1, period + 1):
    patients = int(input())

    if patients <= DOCTORS:
        treated_patients += patients
    else:
        treated_patients += DOCTORS
        untreated_patients += patients - DOCTORS

    if (day + 1) % 3 == 0:
        if treated_patients < untreated_patients:
            DOCTORS += 1

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")

