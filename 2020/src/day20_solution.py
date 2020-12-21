from collections import defaultdict
from dataclasses import field, dataclass
from pathlib import Path

from math import prod


@dataclass
class TilePuzzle:
    tiles: dict[int, dict] = field(default_factory=lambda: defaultdict(dict))
    edges: dict[str, set] = field(default_factory=lambda: defaultdict(set))
    images: dict[int, list[str]] = field(default_factory=lambda: defaultdict(list))
    corners: list[int] = field(default_factory=list)

    @property
    def corners_product(self) -> int:
        return prod(self.corners)

    def add_tile(self, tile: list[str]):
        tile_id = int(tile[0][5:-1])
        tile_image = tile[1:]
        self.images[tile_id] = tile_image
        self.store_tile(tile_id, tile_image)
        for edge in self.tiles[tile_id]:
            self.edges[edge].add(tile_id)
            self.edges[edge[::-1]].add(tile_id)

    def store_tile(self, tile_id, tile_image):
        transposed_tile = list(zip(*tile_image))
        right = "".join(transposed_tile[-1])
        left = "".join(transposed_tile[0])
        top = tile_image[0]
        bottom = tile_image[-1]
        tile_edges = {
            top: "top",
            bottom: "bottom",
            left: "left",
            right: "right",
        }
        self.tiles[tile_id] = tile_edges

    def _count_matching_edges(self, tile_id: int) -> int:
        return sum(1 for edge in self.tiles[tile_id] if len(self.edges[edge]) > 1)

    def _tile_neighbors(self, tile_id: int) -> set[int]:
        return {tid for edge in self.tiles[tile_id] for tid in self.edges[edge] if tid != tile_id}

    def read_tiles(self, tile_list: list[str]):
        for tile in tile_list:
            self.add_tile(tile.strip().split("\n"))
        corners = [tile_id for tile_id in self.tiles if self._count_matching_edges(tile_id) == 2]
        if corner_count := len(corners) == 4:
            self.corners = corners
        else:
            raise RuntimeError("Miscounted the number of corners, got %s" % corner_count)


if __name__ == '__main__':
    challenge_input = Path("../data/input_day20.txt").read_text().strip().split("\n\n")
    tiler = TilePuzzle()
    tiler.read_tiles(challenge_input)
    print(tiler.corners_product)
