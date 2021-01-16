favorite_languages={
    'domie' : 'python',
    'paul' : 'react js',
    'hilda' : 'android',
    'barry' : 'php'
    }
language=favorite_languages['paul'].title()
print(f"Paul's favorite languange is {language}")
# #looping through dictionary
favorite_languages={
    'domie' : 'python',
    'paul' : 'react js',
    'hilda' : 'android',
    'barry' : 'php'
    }
for name,language in favorite_languages.items():
    print(f"{name.title()}'s  favorite language is {language.title()}")
# #looping through keys in a dictionary
favorite_languages={
    'domie' : 'python',
    'paul' : 'react js',
    'hilda' : 'android',
    'barry' : 'php'
    }
for name in favorite_languages:
    print(name.title())
#using list together with dictionary 
favorite_languages={
    'domie' : 'python',
    'paul' : 'react js',
    'hilda' : 'android',
    'barry' : 'php'
    }
friends=[]
friends.append('domie')
friends.append('barry')
print(friends)
for name in favorite_languages:
    print( f"Hi {name.title()}.")
    if name in friends:
        language=favorite_languages[name].title()
        print(f"\t{name.title()}, i see you love {language.title()}!")
#looping thru the dictionary
favorite_languages={
    'domie' : 'python',
    'paul' : 'react js',
    'hilda' : 'android',
    'barry' : 'php'
    }
if 'erin' not in favorite_languages.keys():
    print("Erin, please our poll!")
#nesting
favorite_languages={
    'domie' : ['python','java'],
    'paul' : ['react js','javaScript'],
    'hilda' : ['android','c','javascript'],
    'barry' : ['php'],
    }
for name,languages in favorite_languages.items():
    if len(languages) >= 1:
        print(f"\n{name.title()}'s favorite languages are: ")
        for language in languages:
            print(language) 
    elif len(languages)== 1:
        print(f"\n{name.title()}'s favorite language is: ")
        for language in languages:
            print(language)