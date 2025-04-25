from datetime import datetime

date1 = datetime(2025, 2, 1, 12, 0, 0)
date2 = datetime(2025, 2, 10, 14, 30, 0)
delta = date2 - date1
print(delta.total_seconds())