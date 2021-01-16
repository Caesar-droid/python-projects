current_users=['moonwalker','cishet','ambivert','hoe','winetaster']
new_users=['cishet','caesar','hoe','sidechic']
for new_user in new_users:
    if new_user in current_users:
        print("you need to enter a new username")
    else:
        print("the new username is available for use")
#checking case...
current_users=['moonwalker','cishet','ambivert','hoe','winetaster']
new_users=['CISHET','caesar','HOE','sidechic']
for new_user in new_users:
    if new_user in current_users:
        print("you need to enter a new username")
    else:
        print("the new username is available for use")