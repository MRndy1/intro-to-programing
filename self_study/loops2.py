cal_burn_permnt = 4.2

for mnt in range(10, 31, 5):
    total_cal = cal_burn_permnt * mnt
    print(f"after {mnt} minutes the total cal you burn is {int(total_cal)}")