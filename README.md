#  Modelling Kakuro as CSP and Solving Kakuro Puzzles
**Kakuro** or Kakkuro or Kakoro is a kind of logic puzzle that is often referred to as a mathematical transliteration of the crossword.

We model Kakuro as a **CSP** and solve Kakuro puzzles with various algorithms. Our goal is to show how different algorithms for CSP behave during the solution of these puzzles.

## Algorithms for CSP
The algorithms tested are combinations of:
- BT (Backtracking-Search)
- FC (Forward-Checking)
- AC3 (Maintaining-Arc-Consistency)
- MRV (Minimum-Remaining-Values)
- LCV (Least-Constraining-Value)

## Usage
`$ python3 kakuro.py`

## Implementation

The **kakuro.py** file is written by me and it's the modelization of Kakuro as a CSP and the main function. 

## Kakuro Puzzles
The Kakuro puzzles are taken from [here](https://www.kakuroconquest.com/) and [here](https://www.menneske.no/kakuro/eng/).

## Kakuro puzzle: kakuro_given4x3

| *    | *   | *    | 6\\ | 3\\ |
|------|-----|------|-----|-----|
|   *  | 4\\ | 3\\3 |  2  |  1  |
| \\10 |  3  |  1   |  4  |  2  |
| \\3  |  1  |  2   |  *  |  *  |

        Heuristic and CSP algorithms: BT
        Solved in 0.012365341186523438 seconds.
        Made 219 assignments.

        Heuristic and CSP algorithms: BT + FC
        Solved in 0.0 seconds.
        Made 179 assignments.

        Heuristic and CSP algorithms: BT + FC + MRV
        Solved in 0.0 seconds.
        Made 18 assignments.

        Heuristic and CSP algorithms: BT + FC + MRV + LCV
        Solved in 0.014313936233520508 seconds.
        Made 17 assignments.

        Heuristic and CSP algorithms: BT + AR3
        Solved in 0.0009548664093017578 seconds.
        Made 16 assignments.

        Heuristic and CSP algorithms: BT + AR3 + MRV
        Solved in 0.0 seconds.
        Made 15 assignments.

        Heuristic and CSP algorithms: BT + AR3 + MRV + LCV
        Solved in 0.0 seconds.
        Made 16 assignments.


## Kakuro puzzle: kakuro_intermediate6x6

|  * | 11\\ | 16\\ | 30\\ |  *  | 24\\ | 11\\ |
|----|------|------|------|-----|------|------|
| \\24 |  8   |  9   |  7   | \\9 |  7   |  2   |
| \\16 |  3   |  7   |  6   |14\\17|  8   |  9   |
|  *  |  *   |22\\20|  8   |  3  |  9   |  *   |
|  *  | 3\\24|  7   |  9   |  8  |10\\  |13\\  |
| \\7 |  1   |  6   | \\19 |  2  |  8   |  9   |
| \\11|  2   |  9   |  \\7 |  1  |  2   |  4   |

        Heuristic and CSP algorithms: BT
        Solved in 8.171801328659058 seconds.
        Made 203638 assignments.

        Heuristic and CSP algorithms: BT + FC
        Solved in 1.8245935440063477 seconds.
        Made 180149 assignments.

        Heuristic and CSP algorithms: BT + FC + MRV
        Solved in 0.0 seconds.
        Made 99 assignments.

        Heuristic and CSP algorithms: BT + FC + MRV + LCV
        Solved in 0.0009984970092773438 seconds.
        Made 72 assignments.

        Heuristic and CSP algorithms: BT + AR3
        Solved in 0.01970195770263672 seconds.
        Made 52 assignments.

        Heuristic and CSP algorithms: BT + AR3 + MRV
        Solved in 0.005637168884277344 seconds.
        Made 46 assignments.

        Heuristic and CSP algorithms: BT + AR3 + MRV + LCV
        Solved in 0.01735234260559082 seconds.
        Made 46 assignments.

## Kakuro puzzle: kakuro_hard8x8

|  *  | 28\\ | 15\\ |  *  | 9\\  | 15\\ |  *  | 9\\  | 12\\ |
|-----|------|------|-----|------|------|-----|------|------|
| \\10 |  8   |  2   | 15\\6 |  4   |  2   | 10\\4 |  1   |  3   |
| \\38 |  4   |  3   |  6   |  5   |  1   |  2   |  8   |  9   |
| \\17 |  7   |  1   |  9   |  \\4  |  3   |  1  | 27\\  |  *   |
| \\13 |  9   |  4   | 7\\  | 17\\19 |  9   |  7   |  3   | 15\\ |
|  *  | \\8  |  5   |  2   |  1   |  *  | 16\\3 |  1   |  2   |
|  *  | 11\\ |  4\\4  |  1   |  3   | 3\\24 |  9   |  8   |  7   |
| \\44 |  9   |  3   |  4   |  8   |  2   |  7   |  6   |  5   |
| \\3  |  2   |  1   |  \\6  |  5   |  1   | \\10  |  9   |  1   |

        Heuristic and CSP algorithms: BT + FC + MRV
        Solved in 22.311200618743896 seconds.
        Made 452 assignments.

        Heuristic and CSP algorithms: BT + FC + MRV + LCV
        Solved in 7.967247247695923 seconds.
        Made 213 assignments.

        Heuristic and CSP algorithms: BT + AR3
        Solved in 38.182045698165894 seconds.
        Made 108 assignments.

        Heuristic and CSP algorithms: BT + AR3 + MRV
        Solved in 6.239919424057007 seconds.
        Made 81 assignments.

        Heuristic and CSP algorithms: BT + AR3 + MRV + LCV
        Solved in 7.183613300323486 seconds.
        Made 81 assignments.