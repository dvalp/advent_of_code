from src.day03_solution import tree_count_deluxe, check_all_slopes, tree_count, parse_input

TMAP = """..##.......\n
#...#...#..\n
.#....#..#.\n
..#.#...#.#\n
.#...##..#.\n
..#.##.....\n
.#.#.#....#\n
.#........#\n
#.##...#...\n
#...##....#\n
.#..#...#.#\n""".split()


class TestDay03:
    def test_tree_count(self):
        result = sum(tree_count())
        assert result == 145

    def test_tree_count_deluxe(self):
        result = sum(tree_count_deluxe(tree_map=TMAP, offsets=(3, 1)))
        assert result == 7

    def test_check_all_slopes(self):
        result = check_all_slopes(TMAP)
        assert result == 336

    def test_parse_input(self):
        tree_map = parse_input()
        assert len(tree_map) == 323
        assert len(tree_map[0]) == 31
