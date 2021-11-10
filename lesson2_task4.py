goods = [20.13, 11.20, 15.15, 56.65, 22.90, 55.50, 90.96, 1.22, 2.43, 4.88]

for good in goods:
    rub = int(good)
    kk = (good - rub) * 100
    print(f'{rub} руб {kk:02.0f} коп')

goods = [20.13, 11.20, 15.15, 56.65, 22.90, 55.50, 90.96, 1.22, 2.43, 4.88]
print(id(goods))
goods.sort()
print(id(goods))
for good in goods:
    rub = int(good)
    kk = (good - rub) * 100
    print(f'{rub} руб {kk:02.0f} коп', end=', ')


goods = [20.13, 11.20, 15.15, 56.65, 22.90, 55.50, 90.96, 1.22, 2.43, 4.88]
for good in sorted(goods)[::-1][:5]:
    rub = int(good)
    kk = (good - int(good)) * 100
    print(f'{rub} руб {kk:02.0f}коп', end=', ')



