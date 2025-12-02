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

    def add_new_tile(self, tile: list[str]) -> None:
        tile_id = int(tile[0][5:-1])
        tile_image = tile[1:]
        self.store_tile(tile_id, tile_image)
        for edge in self.tiles[tile_id]:
            self.edges[edge].add(tile_id)
            self.edges[edge[::-1]].add(tile_id)

    def store_tile(self, tile_id, tile_image) -> None:
        right = "".join(row[-1] for row in tile_image)
        left = "".join(row[0] for row in tile_image)
        top = tile_image[0]
        bottom = tile_image[-1]
        tile_edges = {
            top: "top",
            bottom: "bottom",
            left: "left",
            right: "right",
        }
        self.images[tile_id] = tile_image
        self.tiles[tile_id] = tile_edges

    def _count_matching_edges(self, tile_id: int) -> int:
        return sum(1 for edge in self.tiles[tile_id] if len(self.edges[edge]) > 1)

    def _tile_neighbors(self, tile_id: int) -> set[int]:
        return {tid for edge in self.tiles[tile_id] for tid in self.edges[edge] if tid != tile_id}

    @staticmethod
    def _flip_horizontal(image: list[str]) -> list[str]:
        """Reverse the order of character in each string"""
        return [row[::-1] for row in image]

    @staticmethod
    def _flip_vertical(image: list[str]) -> list[str]:
        """Reverse the order of the rows, leave each string in the same order"""
        return image[::-1]

    @staticmethod
    def _rotate_image(image: list[str]) -> list[str]:
        """Rotate the image 90 degrees clockwise"""
        return ["".join(row) for row in zip(*image[::-1])]

    def read_tiles(self, tile_list: list[str]):
        for tile in tile_list:
            self.add_new_tile(tile.strip().split("\n"))
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
