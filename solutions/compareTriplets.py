def compareTriplets(a, b):
    score_bob = 0
    score_alice = 0
    for i in range(3):
        if a[i] > b[i]:
            score_alice+=1
        elif b[i]>a[i]:
            score_bob+=1
        else:
            continue
    return [score_alice, score_bob]