from json import dumps, loads
from typing import List
import sys


def solve(protons_start: int, neutrons_start: int, protons_target: int, neutrons_target: int) -> List[str]:
    '''

    Args:

        - protons_start (int): The initial number of protons
        - neutrons_start (int): The initial number of neutrons
        - protons_target (int): The desired number of protons
        - neutrons_target (int): The desired number of neutrons
    '''
    result = []
    nb_neutrons = neutrons_start
    nb_protons = protons_start
    while nb_neutrons != neutrons_target and nb_protons != protons_target:
        print(protons_target, file=sys.stderr, flush=True)
        print(nb_protons, file=sys.stderr, flush=True)
        if (neutrons_target - nb_neutrons)>2 and (protons_target-nb_protons)>2:
            result.append('ALPHA')
            nb_protons -= 2
            nb_neutrons -=2
        if nb_neutrons < neutrons_target:
            result.append('NEUTRON')
            nb_neutrons += 1
        if nb_protons < protons_target:
            result.append('PROTON')   
            nb_protons += 1 
    
    return result

# Ignore and do not change the code below


def try_solution(recipe: List[str]):
    '''
    Try a solution
    '''
    json = recipe
    print("" + dumps(json, separators=(',', ':')))

def main():
    res = solve(
        loads(input()),
        loads(input()),
        loads(input()),
        loads(input())
    )
    try_solution(res)


if __name__ == "__main__":
    main()
# Ignore and do not change the code above
