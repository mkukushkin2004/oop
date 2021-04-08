A = [int(s) for s in input().split()]

for num in A:
    if len(str(num)) == 2:
        print('Двузначное есть')
        break
else:  # попадает в else только, если не случился break
    print('Двузначных нет')

