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

# Plans changed! They cancelled the larger table and can only invite two people.
print("\nSorry, the restaurant just called and they no longer have the table.")

name = guests.pop(0)
print(f"Sorry, {name.title()} it looks like we can only invite two poeple for dinner now!")

name = guests.pop(1)
print(f"Sorry, {name.title()} the plans changed and you are no longer invited.")

name = guests.pop(2)
print(f"Sorry, {name.title()} but you are no longer invited! I changed my mind.")

name = guests.pop(3)
print(f"Sorry, {name.title()} I have decided to invite someone else in your place. Take care!")

# Two people invited to dinner only.
name = guests[0].title()
print(f"{name}, please get to the dinner table!")

name = guests[1].title()
print(f"{name}, please get to the dinner table!")

# Empty what is remaining in the list.
del(guests[0])
del(guests[1])

# Prove the list is now empty
print(guests)

del(guests[0])

print(guests)