def build_person(first_name,last_name,age=None):
    """return a dictinary about a person"""
    person={'first': first_name,'last': last_name}
    if age:
        person['age']=age
    return person
musician = build_person('Kyle','caesar',age=17)
print(musician)
