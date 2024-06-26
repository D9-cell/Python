def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")
        
print_kwargs(name="IronMan",power="IronSuit")
print_kwargs(name="Thor")
print_kwargs(name="Captain America",power="Shield",enemy="Thanos")