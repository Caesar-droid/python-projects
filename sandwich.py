def make_sandwich(*slices):
    """we are going to make simple sandwich"""
    print("we are going to make the following sandwiches:")
    for slice in slices:
        print(slice)
make_sandwich('green pepper')
make_sandwich('plain','vegetable')
make_sandwich('mushroom','salad','fruit-salad')