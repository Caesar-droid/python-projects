def create_user(last,first,**user_info):
    """we are going to create an empty dictionary and populate it with personal informtion."""
    user_info['last_name']=last
    user_info['first_name']=first
    return user_info
build_profile=create_user('Kyle','Caesar',city='nairobi',education='undergraduate',status='single')
print(build_profile)
    