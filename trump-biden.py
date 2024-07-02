#!/usr/bin/env python3

# Data from:
#   https://www.270towin.com/2024-presidential-election-polls/
# Last taken 2024-07-02

from data import data
from electoral_college import electoral_college

def main():
    no_polls = []
    cand = [0, 0, 0]
    undecided_states = []
    popular_vote = [0.0, 0.0]

    for key, t in data.items():
        if not t:
            no_polls.append(key)
        else:
            (votes, trump, biden) = t
            i = (
                0 if biden > trump else
                1 if trump > biden else
                2
            ) 
            popular_vote[0] += votes * biden / (biden + trump)
            popular_vote[1] += votes * trump / (biden + trump)
            cand[i] += votes
            if i == 2:
                undecided_states.append(key)

    print(f"biden {cand[0]}")
    print(f"trump {cand[1]}")
    print(f"{no_polls = }: {sum(electoral_college[state] for state in no_polls)}")
    print(f"undecided states = {undecided_states}: {sum(electoral_college[s] for s in undecided_states)}")
    print(f"biden vote {popular_vote[0]}")
    print(f"trump vote {popular_vote[1]}")

    x = [(k, d[1] - d[2]) for k, d in data.items() if d]
    sorted_states = sorted(
        x,
        key=lambda x: x[1],
    )
    print(f"{sorted_states}")
        

if __name__ == '__main__':
    main()
