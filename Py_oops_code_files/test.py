exp = 0
level = 1

amount = int(input('Enter gained exp:'))
if exp+amount<100:
    exp += amount
    print(f'Exp gained:{amount}, Level:{level}')
else:
    level_up = (exp+amount)//100
    rem_exp = (exp+amount)%100
    level += level_up
    exp = rem_exp

    print(f'Exp gained:{amount},Total Exp:{exp},Remining exp:{rem_exp}, Level:{level}')
