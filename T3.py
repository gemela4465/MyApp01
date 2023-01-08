def calculate_number(*first):
    total=10
    for f in first:
        if f %2 == 0:
            total += f
    return(total)

result = calculate_number(9,11,35,40)
print (result)

def app_log(name,func_id,date="2022/12/25"):
    print(f"{name} use the {func_id} on {date}")

app_log(name="mike",func_id="func_A01",date="2023/01/10")

def app_log1(**info):
    print(info)

app_log1(name="mike",func_id="func_A01",date="2023/01/10")
