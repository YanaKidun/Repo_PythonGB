# задание 6 День достижения желаемого результата спортсменом
numberofday = 1
startresult = 2
waitresult = 3

while True:
    if waitresult > startresult:
        numberofday = numberofday + 1
        startresult = startresult + startresult * 0.1
        continue
    print("День достижения результата {}". format(numberofday))
    break