# Invite some people to dinner
guests = ["Date Mike", "Prison Mike", "Michael Scarn"]

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

name = guests[0].title()
print(f"\nSorry,  {name} can't make it to dinner.")

# Date Mike can't make it! invite Blind Guy McSqueezy instead
del guests[0]
guests.insert(0, "blind guy mcsqueezy")

# Print invitations again
name = guests[0].title()
print(f"\n{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")
