from copy import deepcopy
def solution(S):
    # strip 
    So = deepcopy(S)
    for i in range(len(S)):
        if S[i] == 'X':
            break

    So = So[i:]

    if So == '.':
        return 0 
    else:
        for i in range(len(S)):
            if S[len(S) - i - 1] == 'X':
                break

        So = So[:-i ]

    # iter 
    p_cnt = 0
    loc = 0 
    maxloc = len(So)

    # loop start to end
    while loc < maxloc:
        if So[loc] == 'X': # cur location is X -> p_cnt + 1 & go 3 step 
            loc = loc + 3
            p_cnt += 1
        else:
            loc = loc + 1

        # cur location is not X -> go 1 step

    return p_cnt

solution('XXXX')