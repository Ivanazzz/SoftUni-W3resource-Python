bitcoins_count = int(input())
chinese_yuan_count = float(input())
commission = float(input())

bgn_lv = bitcoins_count * 1168
yuan_to_dollars = chinese_yuan_count * 0.15
dollar_to_lv = yuan_to_dollars * 1.76

euro = (bgn_lv + dollar_to_lv) / 1.95
total = euro - (euro * commission / 100)

print(f"{total:.2f}")