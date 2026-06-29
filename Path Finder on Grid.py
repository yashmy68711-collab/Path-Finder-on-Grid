class PathFinder:
    def __init__(self):
        self.grid = [
            ["S", ".", ".", "X"],
            [".", "X", ".", "."],
            [".", ".", ".", "E"]
        ]

        self.rows = len(self.grid)
        self.cols = len(self.grid[0])

    def show_grid(self):
        print("\nGrid:")
        for row in self.grid:
            print(" ".join(row))

    def find_positions(self):
        start = None
        end = None

        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == "S":
                    start = (i, j)
                elif self.grid[i][j] == "E":
                    end = (i, j)

        return start, end

    def dfs(self, x, y, end, visited):
        if (x, y) == end:
            return True

        if x < 0 or x >= self.rows or y < 0 or y >= self.cols:
            return False

        if self.grid[x][y] == "X" or (x, y) in visited:
            return False

        visited.add((x, y))

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        for dx, dy in directions:
            if self.dfs(x + dx, y + dy, end, visited):
                if self.grid[x][y] == ".":
                    self.grid[x][y] = "*"
                return True

        return False

    def find_path(self):
        start, end = self.find_positions()

        if start is None or end is None:
            print("Start or End missing")
            return

        visited = set()

        if self.dfs(start[0], start[1], end, visited):
            print("\nPath Found!")
        else:
            print("\nNo Path Found")

        self.show_grid()


finder = PathFinder()
finder.show_grid()
finder.find_path()