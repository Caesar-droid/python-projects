filenames = ['text_files/cats.txt' , 'text_files/dogs.txt']
for filename in filenames:
    print("\nReading file: "+ filename)
    try:
        with open(filename,encoding='utf-8')as f:
            contents=f.read()
            print(contents)
    except FileNotFoundError:
        print("Sorry, I can't find that file.")
        