import re

non_decimal = re.compile(r'[^\d.,]+')

a = ','
print(non_decimal.sub(',', a))

st = "565701	342265	16360	1979	504	182	82			12	8	5		3"
st2 = non_decimal.sub(',', st)
print(st2)
