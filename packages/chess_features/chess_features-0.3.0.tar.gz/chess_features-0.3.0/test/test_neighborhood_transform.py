import chess
import numpy as np

from src.chess_features.chess_features import to_valued_bitboard
from src.chess_features.neighborhood_transform import (
    get_diagonal_neighbor,
    get_file_rank_neighbor,
    get_horse_neighbor,
    get_neighborhood,
)


class TestChessNeighborhoods:
    @classmethod
    def setup_class(cls) -> None:
        board = chess.Board("rnbqkb1r/ppppp2p/6p1/3n4/3R4/8/8/4K3 b Qkq - 3 4")
        valued_board = to_valued_bitboard(board)
        valued_board[-6:] = -valued_board[-6:]
        valued_board = np.sum(valued_board, axis=0)
        cls.board = valued_board

    def test_get_horse_neighbors(self):
        assert (
            get_horse_neighbor(
                self.board,
                2,
                1,
                under_square=True,
                right_of_square=True,
                closer_to_vertical=True,
            )
            == -3
        )
        assert (
            get_horse_neighbor(
                self.board,
                2,
                1,
                under_square=True,
                right_of_square=True,
                closer_to_vertical=False,
            )
            == 0
        )
        assert (
            get_horse_neighbor(
                self.board,
                2,
                1,
                under_square=True,
                right_of_square=False,
                closer_to_vertical=True,
            )
            == 0
        )
        assert (
            get_horse_neighbor(
                self.board,
                2,
                1,
                under_square=True,
                right_of_square=False,
                closer_to_vertical=False,
            )
            == 0
        )
        assert (
            get_horse_neighbor(
                self.board,
                2,
                1,
                under_square=False,
                right_of_square=True,
                closer_to_vertical=True,
            )
            == 0
        )
        assert (
            get_horse_neighbor(
                self.board,
                2,
                1,
                under_square=False,
                right_of_square=True,
                closer_to_vertical=False,
            )
            == -500
        )
        assert (
            get_horse_neighbor(
                self.board,
                2,
                1,
                under_square=False,
                right_of_square=False,
                closer_to_vertical=True,
            )
            == 0
        )
        assert (
            get_horse_neighbor(
                self.board,
                2,
                1,
                under_square=False,
                right_of_square=False,
                closer_to_vertical=False,
            )
            == -5
        )

    def test_get_file_rank_neighbor(self):
        assert get_file_rank_neighbor(self.board, x=2, y=1, down_right_of_square=1, file_wise=True) == 0
        assert get_file_rank_neighbor(self.board, x=2, y=1, down_right_of_square=1, file_wise=False) == -1
        assert get_file_rank_neighbor(self.board, x=2, y=1, down_right_of_square=-1, file_wise=True) == -3
        assert get_file_rank_neighbor(self.board, x=2, y=1, down_right_of_square=-1, file_wise=False) == -1

    def test_get_diagnoal_neighbor(self):
        assert get_diagonal_neighbor(self.board, 2, 1, 1, 1) == 0
        assert get_diagonal_neighbor(self.board, 2, 1, 1, -1) == 0
        assert get_diagonal_neighbor(self.board, 2, 1, -1, 1) == -9
        assert get_diagonal_neighbor(self.board, 2, 1, -1, -1) == -3

    def test_get_neighborhood_unordered(self):
        neighborhood = get_neighborhood(self.board, x=2, y=1, clockwise=False)
        np.testing.assert_equal(neighborhood, [-1, -3, 0, 0, 0, 0, -500, 0, -5, 0, -1, -3, -1, 0, 0, -9, -3])

    def test_get_neighborhood_clockwise(self):
        neighborhood = get_neighborhood(self.board, x=2, y=1, clockwise=True)
        np.testing.assert_equal(neighborhood, [-1, -1, -9, -3, -3, -1, 0, 0, 0, 0, -500, 0, 0, -5, 0, 0, -3])
        np.testing.assert_equal(neighborhood, [-1, -1, -9, -3, -3, -1, 0, 0, 0, 0, -500, 0, 0, -5, 0, 0, -3])
