season = input()
type_of_group = input()
number_of_students = int(input())
number_of_nights = int(input())

school_camp_price = 0
sport = ""

if season == "Winter":
    if type_of_group == "girls":
        school_camp_price += (number_of_nights * 9.60) * number_of_students
        sport = "Gymnastics"
    elif type_of_group == "boys":
        school_camp_price += (number_of_nights * 9.60) * number_of_students
        sport = "Judo"
    elif type_of_group == "mixed":
        school_camp_price += (number_of_nights * 10) * number_of_students
        sport = "Ski"
if season == "Spring":
    if type_of_group == "girls":
        school_camp_price += (number_of_nights * 7.20) * number_of_students
        sport = "Athletics"
    elif type_of_group == "boys":
        school_camp_price += (number_of_nights * 7.20) * number_of_students
        sport = "Tennis"
    elif type_of_group == "mixed":
        school_camp_price += (number_of_nights * 9.50) * number_of_students
        sport = "Cycling"
if season == "Summer":
    if type_of_group == "girls":
        school_camp_price += (number_of_nights * 15) * number_of_students
        sport = "Voleyball"
    elif type_of_group == "boys":
        school_camp_price += (number_of_nights * 15) * number_of_students
        sport = "Football"
    elif type_of_group == "mixed":
        school_camp_price += (number_of_nights * 20) * number_of_students
        sport = "Swimming"

if number_of_students >= 50:
    school_camp_price -= school_camp_price * 0.50
elif number_of_students >= 20:
    school_camp_price -= school_camp_price * 0.15
elif number_of_students >= 10:
    school_camp_price -= school_camp_price * 0.05

print(f"{sport} {school_camp_price:.2f} lv.")
