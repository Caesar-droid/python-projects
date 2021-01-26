#specifying a list of items to be printed
unprinted_designs=['phone case','robot pandant','dodecoheran']
completed_models=[]

#simulate printing each design,until none are left
#move each design to completed_models after printing
while unprinted_designs:
    current_design=unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)
#display all completed models.
print("\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_model)
#modifying a list in a function
def printing_models(unprinted_designs,completed_models):
    """
    simulate printing each design, until none are left.
    move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design=unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
def show_completed_models(completed_models):
    """show completed models that have been printed"""
    print("the following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs=['phone case','robot pendant','dodecahedron']
completed_models=[]
printing_models(unprinted_designs,completed_models)
show_completed_models(completed_models)
