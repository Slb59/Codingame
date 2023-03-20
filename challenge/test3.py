from json import dumps, loads
from typing import List
from operator import itemgetter


def solve(grid: List[List[int]], rules: List[dict]) -> List[List[int]]:
    '''

    Args:

        - grid (List[List[int]]): The initial grid of elements
        - rules (List[dict]): Transition rules between elements
    '''
    size = len(grid[0])
    result=[ [0 for i in range(size-1)] for i in range(size-1)]
    for j in range(0, size-1):
        for i in range(0, size-1):
            subset = [grid[j][i], grid[j][i+1], grid[j+1][i], grid[j+1][i+1]]
            try:
                elem = next(item for item in rules if item["pattern"] == subset)
                result[j][i] = elem["result"]
            except:
                result[j][i] = 0
    return result

# Ignore and do not change the code below


def try_solution(new_grid: List[List[int]]):
    '''
    Try a solution
    '''
    json = new_grid
    print("" + dumps(json, separators=(',', ':')))

def main():
    res = solve(
        loads(input()),
        loads(input())
    )
    try_solution(res)


if __name__ == "__main__":
    main()
# Ignore and do not change the code above
