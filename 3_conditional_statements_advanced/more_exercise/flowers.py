CHRYSANTHEMUM_SPRING_SUMMER = 2
CHRYSANTHEMUM_AUTUMN_WINTER = 3.75
ROSE_SPRING_SUMMER = 4.10
ROSE_AUTUMN_WINTER = 4.50
TULIP_SPRING_SUMMER = 2.50
TULIP_AUTUMN_WINTER = 4.15
ARRANGEMENT_BOUQUET = 2

chrysanthemum_quantity = int(input())
rose_quantity = int(input())
tulip_quantity = int(input())
season = input()
holiday = input()

bouquet_price = 0

if season == "Spring" or season == "Summer":
    bouquet_price += (chrysanthemum_quantity * CHRYSANTHEMUM_SPRING_SUMMER) \
                     + (rose_quantity * ROSE_SPRING_SUMMER) + (tulip_quantity * TULIP_SPRING_SUMMER)
elif season == "Autumn" or season == "Winter":
    bouquet_price += (chrysanthemum_quantity * CHRYSANTHEMUM_AUTUMN_WINTER) \
                     + (rose_quantity * ROSE_AUTUMN_WINTER) + (tulip_quantity * TULIP_AUTUMN_WINTER)

if holiday == "Y":
    bouquet_price += bouquet_price * 0.15

if season == "Spring" and tulip_quantity > 7:
    bouquet_price -= bouquet_price * 0.05
if season == "Winter" and rose_quantity >= 10:
    bouquet_price -= bouquet_price * 0.10
if chrysanthemum_quantity + rose_quantity + tulip_quantity > 20:
    bouquet_price -= bouquet_price * 0.20

total_bouquet_price = bouquet_price + ARRANGEMENT_BOUQUET

print(f"{total_bouquet_price:.2f}")


