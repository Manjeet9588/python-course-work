details = {"Name": "Manjeet", "Age": 20}
new = list(details.items())

print(new)

for i in range(len(new)):
    key,detail = new[i]
    print(f"key {key}")
    print(f"detail {detail}")
