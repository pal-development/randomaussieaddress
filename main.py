import requests

postcode = str(input("Post Code: "))

a = requests.get(f"https://www.property.com.au/buy/in-{postcode}/list-1?source=location-search").text

if ("Street, " in a):
    n = a.index("Street, ") + 6
    split_strings = [a[index : index + n] for index in range(0, len(a), n)]
    address = split_strings[0].split(">")[split_strings[0].count(">")]
elif ("Road, " in a):
    n = a.index("Road, ") + 6
    split_strings = [a[index : index + n] for index in range(0, len(a), n)]
    address = split_strings[0].split(">")[split_strings[0].count(">")]
elif ("Parade, " in a):
    n = a.index("Parade, ") + 6
    split_strings = [a[index : index + n] for index in range(0, len(a), n)]
    address = split_strings[0].split(">")[split_strings[0].count(">")]
elif ("Lane, " in a):
    n = a.index("Lane, ") + 6
    split_strings = [a[index : index + n] for index in range(0, len(a), n)]
    address = split_strings[0].split(">")[split_strings[0].count(">")]
elif ("Avenue, " in a):
    n = a.index("Avenue, ") + 6
    split_strings = [a[index : index + n] for index in range(0, len(a), n)]
    address = split_strings[0].split(">")[split_strings[0].count(">")]
else:
    print("Sorry! We couldn't find an address for that postcode, try again later.")




print(address)
