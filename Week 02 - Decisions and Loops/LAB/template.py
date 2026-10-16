"""
RECORD CHECK  -  my version
===========================

Name  : Nicole 
Lane  :  AI 
Date  : 30/09/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
over_limit_no = 0

while True:

    label = input("Enter label: ")    

    if label == "quit":
        break

    value = float(input("Enter a value: "))     
    limit = float(input("Enter a limit: "))     


    difference = limit - value 
    percent = (value / limit) * 100       

    if value >= limit:
        status = "OVER LIMIT"
        over_limit_no +=1 

    elif percent >= 90:
        status = "WARNING"

    else:
        status = "OK"



    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f" Used  : {value:>8.2f}")
    print(f" Total : {limit:>8.2f}")
    print(f" Free  : {difference:>8.2f}")
    print(f" Percent : {percent:.2f}%")
    print(f" Status : {status:>8}")


    print("=" * 34)

    print()
    print(f"OVER LIMIT records = {over_limit_no}")


