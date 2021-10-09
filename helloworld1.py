price = 1000000
has_goodcredit = True
if has_goodcredit:
    down_payment=(0.1 * price)
else:
    down_payment=(0.2 * price)

print(f"Down Payment:${down_payment}")
