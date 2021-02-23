def count_words(filename):
    """Count the approximate number of words in the file."""
    try:
        with open(filename,encoding='utf-8') as f:
            contents=f.read()
    except FileNotFoundError:
        pass
        # print(f"Sorry,the file {filename} does not exist.")
    else:
        words=contents.split()
        num_words=len(words)
        print(f"the file {filename} has about {num_words} words.")
filenames=['text_files/alice.txt','text_files/siddhartha.txt','text_files/moby_dick.txt','text_files/little_women.txt']
for filename in filenames:
    count_words(filename)
        