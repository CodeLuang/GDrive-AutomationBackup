import datetime

now = datetime.datetime.now()

slice = now.strftime("%Y-%m-%d")
dayS = int(slice[8:]) + 10

dp = slice[:8] + f"{dayS}" 


if dp == now:
    print("running the script")
else:
    print("failed to run")