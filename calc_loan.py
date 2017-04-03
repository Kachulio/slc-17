def interest_calc(amount,rate,time):
    amount = float(amount)
    rate = float(rate)
    time = float(time)

    return amount + (amount * (rate/100) *(time/12))


print interest_calc(100000,12,12)
