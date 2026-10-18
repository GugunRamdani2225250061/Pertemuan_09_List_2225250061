
# Latihan 5: Filter Kelulusan

nilai = [75, 55, 80, 60, 45, 90]
lulus = []

for x in nilai:
    if x >= 60:
        lulus.append(x)

print("Nilai lulus:", lulus)
print(f"Jumlah lulus = {len(lulus)}")