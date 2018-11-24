"""Specify the number of records that you want to group in 'val'
'id' - a field containing sequential numbers or even random
numbers.
The number in 'id' is divided by 'val' and incremented if the
modulus == 0
"""
cnt = 0
def seq_group(id, val):
    global cnt
    if id % val == 0 :
        cnt += 1
    return cnt
