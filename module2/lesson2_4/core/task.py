matn = "broker_connection_retry_on_startup"
l=""
for i in matn:
    if i.isalpha():
        l+=i.upper()
    else:
        l+=i

print(l)