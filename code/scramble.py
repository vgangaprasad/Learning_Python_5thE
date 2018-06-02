# file scramble.py

def scramble(seq):
    for i in range(len(seq)):                # Generator function
        yield seq[i:] + seq[:i]              # Yield one item per iteration

scramble2 = lambda seq: (seq[i:] + seq[:i] for i in range(len(seq)))
