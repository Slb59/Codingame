from json import dumps, loads
from typing import List
import math

def collisions(particles: List[List[int]]) -> int:
    '''

    Args:

        - particles (List[List[int]]): the list of coordinates of the particles, in nm

    Returns:

        The number of potential collisions
    '''
    result = 0
    for i in range(0, len(particles)-1):
        for j in range(i+1, len(particles)):
            print(i)
            print(j)
            d = math.sqrt((particles[j][0] - particles[i][0])**2 + (particles[j][1] - particles[i][1])**2)
            print(d)
            if d < 1000:
                result +=1
    return result

# Ignore and do not change the code below


def try_solution(n_collisions: int):
    '''
    Try a solution

    Args:

        - int (int): The number of potential collisions
    '''
    json = n_collisions
    print("" + dumps(json, separators=(',', ':')))

def main():
    res = collisions(
        loads(input())
    )
    try_solution(res)


if __name__ == "__main__":
    main()
# Ignore and do not change the code above


