from collections import defaultdict
from dataclasses import field, dataclass
from pathlib import Path

from math import prod


@dataclass
class TilePuzzle:
    tiles: dict[int, list] = field(default_factory=lambda: defaultdict(list))
    edges: dict[str, set] = field(default_factory=lambda: defaultdict(set))
    corners: list[int] = field(default_factory=list)

    @property
    def corners_product(self) -> int:
        return prod(self.corners)

    def add_tile(self, tile: list[str]):
        tile_id = int(tile[0][5:-1])
        tile_image = tile[1:]
        transposed_tile = list(zip(*tile_image))
        right = "".join(transposed_tile[-1])
        left = "".join(transposed_tile[0])

        edges = []
        edges.extend([
            tile_image[0],
            tile_image[-1],
            left,
            right,
        ])

        self.tiles[tile_id] = edges
        for edge in edges:
            self.edges[edge].add(tile_id)
            self.edges[edge[::-1]].add(tile_id)

    def _count_matching_edges(self, tile_id: int) -> int:
        return sum(1 for edge in self.tiles[tile_id] if len(self.edges[edge]) > 1)

    def read_tiles(self, tile_list: list[str]):
        for tile in tile_list:
            self.add_tile(tile.strip().split("\n"))
        corners = [tile_id for tile_id in tiler.tiles if tiler._count_matching_edges(tile_id) == 2]
        if corner_count := len(corners) == 4:
            self.corners = corners
        else:
            raise RuntimeError("Miscounted the number of corners, got %s" % corner_count)


if __name__ == '__main__':
    challenge_input = Path("../data/input_day20.txt").read_text().strip().split("\n\n")
    tiler = TilePuzzle()
    tiler.read_tiles(challenge_input)
    print(tiler.corners_product)
