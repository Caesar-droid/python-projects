guest=['jessie','jason','june','marvin','jade']
print(f"Hey {guest[0].title()},you are invited for supper.")
print(f"Hey {guest[1].title()},you are invited for supper.")
print(f"Hey {guest[2].title()},you are invited for supper.")
print(f"Hey {guest[3].title()},you are invited for supper.")
print(f"Hey {guest[4].title()},you are invited for supper.")
guest=['jessie','jason','june','marvin','jade']
print(f"Due to unavoidable circumstances, {guest[2].title()} wont be joining us anytime soon")
guest[2]='gerald'
print(f"Hey {guest[0].title()},you are invited for supper.")
print(f"Hey {guest[1].title()},you are invited for supper.")
print(f"Hey {guest[2].title()},you are invited for supper.")
print(f"Hey {guest[3].title()},you are invited for supper.")
print(f"Hey {guest[4].title()},you are invited for supper.")
guest=['jessie','jason','june','marvin','jade']
print("hello everyone, we have all be summoned here to inform you that we have reserved a bigger table.")
guest.insert(0,'caesar')
guest.insert(3,'doodleshot')
guest.append('jellyBean')
print(f"Hey {guest[0].title()},you are invited for supper.")
print(f"Hey {guest[1].title()},you are invited for supper.")
print(f"Hey {guest[2].title()},you are invited for supper.")
print(f"Hey {guest[3].title()},you are invited for supper.")
print(f"Hey {guest[4].title()},you are invited for supper.")
print(f"Hey {guest[5].title()},you are invited for supper.")
print(f"Hey {guest[6].title()},you are invited for supper.")
print(f"Hey {guest[7].title()},you are invited for supper.")
print(guest)
print("unfortunately, the was only reservation for two guest")
popped_guest=guest.pop()
print(f"Sorry {popped_guest},you are not invited for the supper")
popped_guest=guest.pop()
print(f"Sorry {popped_guest},you are not invited for the supper")
popped_guest=guest.pop()
print(f"Sorry {popped_guest},you are not invited for the supper")
popped_guest=guest.pop()
print(f"Sorry {popped_guest},you are not invited for the supper")
popped_guest=guest.pop()
print(f"Sorry {popped_guest},you are not invited for the supper")
popped_guest=guest.pop()
print(f"Sorry {popped_guest},you are not invited for the supper")
print(f"i would like to inform you; {guest[0].title()} that you have been invited")
print(f"i would like to inform you; {guest[1].title()} that you have been invited")
del guest[0]
# del guest[1]
print(guest)
guest=['jessie','jason','june','marvin','jade']
print(len(guest))