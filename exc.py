def computepay(h,r):
    if h <= 40:
        pago= h * r
    else:
        pago= 1.5 * r * (h - 40) + (40 *r)
    return pago


hrs = input("Enter Hours:")
rate = input("Enter Rate:")
fhrs = float(hrs)
frate = float(rate)
p = computepay(fhrs,frate)
print("Pay", p)
