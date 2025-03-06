import datetime

now = datetime.now()
without_micro = now.replace(microsecond=0)
print(without_micro)