#calling the function using positional argument
def make_shirt(size,message):
    print(f"the t-shirt will be of size {size}")
    print(f"written {message}")
make_shirt('26','Doodleshot')

#calling the function using keyword arguments
def make_shirt(size,message):
    print(f"\nthe t-shirt will be of size {size}")
    print(f"written {message}")
make_shirt(message='Doodleshot',size='26')
#using default values
def make_shirt(size='large',message='i love python'):
    print(f" i want a {size} written {message}")
make_shirt()
make_shirt(size='medium')
make_shirt(size='small',message='YOLO')
    
