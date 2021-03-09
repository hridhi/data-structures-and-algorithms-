jeanAndShoes=[3]
priceOfJeans=[4]
priceOfShoes=[3,4,1]
priceOfSkirts=[3,2]
priceOfTops=[4]
budgeted=10
for jean in priceOfJeans:
    for shoe in priceOfShoes:
        jeanAndShoes.append(jean+shoe)
skirtAndTops=[]
for skirt in priceOfSkirts:
    for top in priceOfTops:
        skirtAndTops.append(skirt+top)
jeanAndShoes.sort()
skirtAndTops.sort(reverse=True)
result=0
limit=0
for cost in jeanAndShoes:
    remaining=budgeted-cost
    while limit<len(skirtAndTops) and skirtAndTops[limit]>remaining:
        limit+=1
    if limit ==len(skirtAndTops):
        break
    result+=len(skirtAndTops)-limit
    
    

        
print(result)
