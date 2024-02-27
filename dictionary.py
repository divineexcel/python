casts = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }


# for key in casts:
#     print(key)

for key in casts:
    print(casts[key])

for key, value in casts.items():
    print(f"{key} - {value}")

for key, value in casts.items():
    # print("Actor: {}    Role: {}".format(key, value))
    print(f"Actor: {key}   Role: {value}\n")

