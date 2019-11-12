import itertools
import random

from cached_property import cached_property


# TODO docs
# TODO do with processing


class QueenMatrix:
    """A class representing the N-Queens puzzle.

    Attributes:
        n (number): the amount of queens and the board size.
        combs (list): all possible combinations for swapping each two queens.
        steps (number): the amount of queens placed and removed.
    """

    def __init__(self, n):
        self.n = n
        # self.queens = list(range(self.n))
        # random.shuffle(self.queens)
        self.steps = 0
        self.combs = list(itertools.combinations(range(self.n), r=2))

    @cached_property
    def queens(self):
        """The current state of the queens on the board.

        The state is represented by a list of indices, each value represents the column index of a queen,
        and each spot index represents the row index of the queen.
        For example, the list [2,4,3,1,0] encodes the queens -> (0,2) (1,4) (2,3) (3,1) (4,0).

        Returns:
            list. the list representation of the queens.
        """
        new_queens = []
        columns = list(range(self.n))

        all_spots = {spot: True for spot in itertools.product(range(self.n), repeat=2)}

        def mark_spots(queen_x, queen_y):
            """Mark down all threatened spots in the board.

            Args:
                queen_x (number): row index of the threatening queen.
                queen_y (number): column index of the threatening queen.
            """
            for spot in all_spots:
                if self.is_threat(*spot, queen_x, queen_y):
                    all_spots[spot] = False

        for row in range(self.n):
            # calculate available (not threatened) spots in the board
            row_spots = [spot for spot in all_spots if spot[0] == row]
            available_spots = [spot[1] for spot in row_spots if all_spots[spot] is True]

            if len(available_spots) == 0:  # No available spots in the row -> choose random spot in the row
                queen = random.choice(columns)

            else:
                queen = random.choice(available_spots)

            new_queens.append(queen)
            self.steps += 1
            columns.remove(queen)
            mark_spots(row, queen)

        return new_queens

    @property
    def done(self):
        """Return whether all queens does not threat each other.

        Returns:
            bool. if all queens has no threat on them.
        """
        return all(self.cost(x, y) == 1 for x, y in enumerate(self.queens))

    @staticmethod
    def is_threat(x, y, i, j):
        """Return whether one spot is threatening other spot.

        Args:
            x (number): row index of the first spot.
            y (number): column index of the first spot.
            i (number): row index of the second spot.
            j (number): column index of the second spot.

        Returns:
            bool. whether the spots threat each other.
        """
        return x == i or y == j or abs(x - i) == abs(y - j)

    def cost(self, x, y):
        """Calculate the amount of queens threatening this spot.

        Args:
            x (number): row index of the spot.
            y (number): column index of the spot.

        Returns:
            number. the amount of queens threatening this spot.
        """
        return sum(self.is_threat(x, y, i, j) for i, j in enumerate(self.queens))

    def find_best_swap(self):
        """Find the best swap possible based on heuristic.

        To find which two queens is best to swap, the function calculates the `hit-map`, an array which holds for
        each spot how much queens threat it.
        Then, the functions iterates on all possible swaps and checks what are the values which the queens in this
        swap are going to land on and picks the maximum.
        The swap with the lowest maximum value is then picked, if there are more then one lowest, pick randomly.

        Returns:
            tuple. the best swap.
        """
        swap_costs = {}
        for x1, x2 in self.combs:
            y1 = self.queens[x1]
            y2 = self.queens[x2]
            swap_costs[x1, x2] = max(self.cost(x1, y2), self.cost(x2, y1))

        minimal_cost = swap_costs[min(swap_costs, key=swap_costs.get)]
        x, y = random.choice([swap for swap, cost in swap_costs.items() if cost == minimal_cost])
        return x, y

    def draw(self, queens_marker='X', empty_spot='*'):
        """Draw queens matrix board."""
        for x, y in itertools.product(range(self.n), repeat=2):
            if y == 0:
                print()

            if self.queens[x] == y:
                print(queens_marker, end=' ')

            else:
                print(empty_spot, end=' ')

        print()

    def solve(self, verbose=True):
        """Find spots for the queens such that no queen threats each other.

        The algorithm iterates over all two-rows-swap and for each swap maps to the maximum
        landing cost. Then it picks the swap with the lowest maximum cost, and swaps the queens.

        Args:
            verbose (bool): whether to print the board on each iteration.
        """
        last_swap = None

        while not self.done:

            x1, x2 = self.find_best_swap()
            if last_swap == (x1, x2):  # Avoid loops
                self.combs.remove(last_swap)
                x1, x2 = self.find_best_swap()
                self.combs.append(last_swap)

            last_swap = x1, x2

            if verbose:
                print(f'Swapping {x1} and {x2}')
                self.draw()

            self.queens[x1], self.queens[x2] = self.queens[x2], self.queens[x1]  # Swap queens
            self.steps += 4

        if verbose:
            print(self.queens)
            print(f'steps={self.steps}')
