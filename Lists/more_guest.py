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

# Got a bigger table so we can add more guest
print("\nWe got a bigger table!")
guests.insert(0, "caleb crawdad")
guests.insert(2, "willy wonka")
guests.insert(3, "santa bond")

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

name = guests[3].title()
print(f"{name}, please come to dinner.")

name = guests[4].title()
print(f"{name}, please come to dinner.")

name = guests[5].title()
print(f"{name}, please come to dinner.")
