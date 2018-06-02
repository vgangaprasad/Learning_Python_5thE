def countdown(N):
    if N == 0:
        print('stop')                 # 2.X: print 'stop'
    else:
        print(N, end=' ')             # 2.X: print N,
        countdown(N-1)


def countdown2(N):                          # Generator function, recursive
    if N == 0:
        yield 'stop'
    else:
        yield N
        for x in countdown2(N-1): yield x   # 3.3+: yield from countdown2(N-1)