flour_price = float(input())
flour_kg = float(input())
sugar_kg = float(input())
egg_peels = int(input())
yeast_packs = int(input())

sugar_price = flour_price * 0.75
egg_peel_price = flour_price + (flour_price * 0.10)
yeast_pack_price = sugar_price * 0.20

total_price = flour_price * flour_kg + sugar_price * sugar_kg \
              + egg_peel_price * egg_peels + yeast_pack_price * yeast_packs

print(f"{total_price:.2f}")
