sandwich_orders=['vegetable','pastrami','tuna','beef','pastrami','cheese&onion','pastrami']
finished_sandwiches=[]
print("the deli has run out of 'pastrami'")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    sandwich=sandwich_orders.pop()
    print(f"i have made you a {sandwich} sandwich")
    finished_sandwiches.append(sandwich)
print(finished_sandwiches)
