fruits = ['apple','banana','cherry','kiwi','mango']
newlist = []
for fruit in fruits:
    if 'a' in fruit:
        newlist.append(fruit)
print('Nueva lista a partir de recorrer la primera:',newlist)

newlist = [fruit for fruit in fruits if 'a' in fruit]
print('Nueva lista con LC',newlist)
