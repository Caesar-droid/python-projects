#looping through all the keys in a dictionary
favorite_languages={
    'domie' : 'python',
    'paul' : 'react js',
    'hilda' : 'android',
    'barry' : 'php'
    }
for name in sorted(favorite_languages.keys()):
    language=favorite_languages[name].title()
    print(f"{name.title()} taking {language}, thank you for taking poll!")
#looping through all the values in a dictionary
favorite_languages={
    'domie' : 'python',
    'paul' : 'react js',
    'hilda' : 'python',
    'barry' : 'php'
    }
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())