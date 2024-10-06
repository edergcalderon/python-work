# Invite some people to dinner. 
guests = ['Kobe Bryant', 'Lionel Messi', 'Lebron James', 'Eder Calderon']

name = guests[0].title()
print(f"{name}, are you available to come to the party tonight?")
name = guests[1].title()
print(f"{name}, are you available to come to the party tonight?")
name = guests[2].title()
print(f"{name}, are you available to come to the party tonight?")

name = guests[-1].title()
print(f"\nSorry, {name}, I can't make it to dinner tonight.")

# Lionel can't make it to dinner. Let's invite someone else.
del(guests[1])
guests.insert(1, 'Luis Diaz')

# Print the invitations again.
name = guests[0].title()
print(f"\n{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

# Letting guests know we got a bigger table.
print("\nWe got a bigger table!")
guests.insert(0, 'Lamar Jackson')
guests.insert(2, 'Cristiano Ronaldo')
guests.append('Neymar Jr')

# Print the invitations again.

name = guests[0].title()
print(f"\n{name}, please come to dinner.")

name = guests[1].title()
print(f"\n{name}, please come to dinner.")

name = guests[2].title()
print(f"\n{name}, please come to dinner.")

name = guests[3].title()
print(f"\n{name}, please come to dinner.")

name = guests[4].title()
print(f"\n{name}, please come to dinner.")

name = guests[5].title()
print(f"\n{name}, please come to dinner.")