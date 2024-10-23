import itertools
from abc import ABC, abstractmethod

import chess
import numpy as np

from .chess_features import get_unified_valued_bitboard, to_valued_attack_map


class FeatureExtractionFactory:
    def __init__(self) -> None:
        self._feature_extraction_map = self.get_feature_extraction_map()

    def get_feature_extraction_map(self) -> dict:
        map_ = {}
        for subclass in AbstractFeature.__subclasses__():
            map_[subclass.__name__.replace("Extract", "")] = subclass
        return map_


class AbstractFeature(ABC):
    def __init__(
        self,
        board: chess.Board,
        *,
        is_midgame: bool | None = None,
        color: bool = chess.WHITE,
    ) -> None:
        self.board = board
        self.is_midgame = is_midgame
        self.color = chess.WHITE if color is None else color

    @abstractmethod
    def extract_feature(self, board: chess.Board, *, is_midgame: bool, color: bool) -> float | int:
        pass


class ExtractNonPawnMaterial(AbstractFeature):
    def __init__(
        self,
        board: chess.Board,
        *,
        is_midgame: bool | None = None,
        color: bool = chess.WHITE,
    ) -> None:
        super().__init__(board, is_midgame=is_midgame, color=color)

        self.values = [0, 781, 825, 1276, 2538] if self.is_midgame else [0, 854, 915, 1380, 2682]

    def extract_feature(self) -> float:
        values = dict(
            zip(
                ["pawn", "knight", "bishop", "rook", "queen", "king"],
                [*self.values, 0],
                strict=False,
            )
        )
        return np.sum(get_unified_valued_bitboard(self.board, values=values))


class ExtractPieceValue(AbstractFeature):
    def __init__(
        self,
        board: chess.Board,
        *,
        is_midgame: bool | None = None,
        color: bool = chess.WHITE,
    ) -> None:
        super().__init__(board, is_midgame=is_midgame, color=color)

        self.piece_values = [124, 781, 825, 1276, 2538] if self.is_midgame else [206, 854, 915, 1380, 2682]

    def extract_feature(self) -> int:
        values = dict(
            zip(
                ["pawn", "knight", "bishop", "rook", "queen", "king"],
                [*self.piece_values, 0],
                strict=False,
            )
        )
        return np.sum(get_unified_valued_bitboard(self.board, values=values))


class ExtractPsqt(AbstractFeature):
    def __init__(
        self,
        board: chess.Board,
        *,
        is_midgame: bool | None = None,
        color: bool = chess.WHITE,
    ) -> None:
        super().__init__(board, is_midgame=is_midgame, color=color)
        if self.is_midgame:
            self.piece_bonus = np.array(
                [
                    [
                        [-175, -92, -74, -73],
                        [-77, -41, -27, -15],
                        [-61, -17, 6, 12],
                        [-35, 8, 40, 49],
                        [-34, 13, 44, 51],
                        [-9, 22, 58, 53],
                        [-67, -27, 4, 37],
                        [-201, -83, -56, -26],
                    ],
                    [
                        [-53, -5, -8, -23],
                        [-15, 8, 19, 4],
                        [-7, 21, -5, 17],
                        [-5, 11, 25, 39],
                        [-12, 29, 22, 31],
                        [-16, 6, 1, 11],
                        [-17, -14, 5, 0],
                        [-48, 1, -14, -23],
                    ],
                    [
                        [-31, -20, -14, -5],
                        [-21, -13, -8, 6],
                        [-25, -11, -1, 3],
                        [-13, -5, -4, -6],
                        [-27, -15, -4, 3],
                        [-22, -2, 6, 12],
                        [-2, 12, 16, 18],
                        [-17, -19, -1, 9],
                    ],
                    [
                        [3, -5, -5, 4],
                        [-3, 5, 8, 12],
                        [-3, 6, 13, 7],
                        [4, 5, 9, 8],
                        [0, 14, 12, 5],
                        [-4, 10, 6, 8],
                        [-5, 6, 10, 8],
                        [-2, -2, 1, -2],
                    ],
                    [
                        [271, 327, 271, 198],
                        [278, 303, 234, 179],
                        [195, 258, 169, 120],
                        [164, 190, 138, 98],
                        [154, 179, 105, 70],
                        [123, 145, 81, 31],
                        [88, 120, 65, 33],
                        [59, 89, 45, -1],
                    ],
                ]
            )
            self.pawn_bonus = np.array(
                [
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [3, 3, 10, 19, 16, 19, 7, -5],
                    [-9, -15, 11, 15, 32, 22, 5, -22],
                    [-4, -23, 6, 20, 40, 17, 4, -8],
                    [13, 0, -13, 1, 11, -2, -13, 5],
                    [5, -12, -7, 22, -8, -5, -15, -8],
                    [-7, 7, -3, -13, 5, -16, 10, -8],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                ]
            )
        else:
            self.piece_bonus = np.array(
                [
                    [
                        [-96, -65, -49, -21],
                        [-67, -54, -18, 8],
                        [-40, -27, -8, 29],
                        [-35, -2, 13, 28],
                        [-45, -16, 9, 39],
                        [-51, -44, -16, 17],
                        [-69, -50, -51, 12],
                        [-100, -88, -56, -17],
                    ],
                    [
                        [-57, -30, -37, -12],
                        [-37, -13, -17, 1],
                        [-16, -1, -2, 10],
                        [-20, -6, 0, 17],
                        [-17, -1, -14, 15],
                        [-30, 6, 4, 6],
                        [-31, -20, -1, 1],
                        [-46, -42, -37, -24],
                    ],
                    [
                        [-9, -13, -10, -9],
                        [-12, -9, -1, -2],
                        [6, -8, -2, -6],
                        [-6, 1, -9, 7],
                        [-5, 8, 7, -6],
                        [6, 1, -7, 10],
                        [4, 5, 20, -5],
                        [18, 0, 19, 13],
                    ],
                    [
                        [-69, -57, -47, -26],
                        [-55, -31, -22, -4],
                        [-39, -18, -9, 3],
                        [-23, -3, 13, 24],
                        [-29, -6, 9, 21],
                        [-38, -18, -12, 1],
                        [-50, -27, -24, -8],
                        [-75, -52, -43, -36],
                    ],
                    [
                        [1, 45, 85, 76],
                        [53, 100, 133, 135],
                        [88, 130, 169, 175],
                        [103, 156, 172, 172],
                        [96, 166, 199, 199],
                        [92, 172, 184, 191],
                        [47, 121, 116, 131],
                        [11, 59, 73, 78],
                    ],
                ]
            )
            self.pawn_bonus = np.array(
                [
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [-10, -6, 10, 0, 14, 7, -5, -19],
                    [-10, -10, -10, 4, 4, 3, -6, -4],
                    [6, -2, -8, -4, -13, -12, -10, -9],
                    [10, 5, 4, -5, -5, -5, 14, 9],
                    [28, 20, 21, 28, 30, 7, 6, 13],
                    [0, -11, 12, 21, 25, 19, 4, 7],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                ]
            )

    def extract_feature(self) -> float:
        piece_map = np.append(self.piece_bonus, np.flip(self.piece_bonus, -1), axis=2)

        opponent_piece_map = np.append(np.expand_dims(self.pawn_bonus, 0), piece_map, axis=0)
        own_piece_map = np.flip(opponent_piece_map, axis=1)

        values = dict(
            zip(
                ["pawn", "knight", "bishop", "rook", "queen", "king"],
                range(1, 7),
                strict=False,
            )
        )
        valued_board = get_unified_valued_bitboard(self.board, values)

        own_piece_bonus_sum = 0
        for i in range(1, 7):
            current_piece_mask = valued_board == i
            own_piece_bonus_sum += own_piece_map[i - 1][current_piece_mask].sum()

        opponent_piece_bonus_sum = 0
        for i in range(-1, -7, -1):
            current_piece_mask = valued_board == i
            opponent_piece_bonus_sum += opponent_piece_map[abs(i) - 1][current_piece_mask].sum()

        return own_piece_bonus_sum - opponent_piece_bonus_sum


class ExtractMobilityArea(AbstractFeature):
    def extract_feature(self) -> float:
        own_mobility_area = self.get_mobility_area(self.board, color=self.color)
        opponent_mobility_area = self.get_mobility_area(self.board.mirror(), color=self.color)
        return own_mobility_area.sum() - opponent_mobility_area.sum()

    @classmethod
    def get_mobility_area(cls, board: chess.Board, *, color: bool) -> np.ndarray:
        values = dict(
            zip(
                ["pawn", "knight", "bishop", "rook", "queen", "king"],
                range(1, 7),
                strict=False,
            )
        )
        valued_board = get_unified_valued_bitboard(board, values)
        valued_attack_map = to_valued_attack_map(board)

        mobility_area = np.ones((8, 8))
        # own king and queen
        mobility_area -= (valued_board == 6) + (valued_board == 5)
        # own pawns in own 3 ranks
        mobility_area[5:] -= valued_board[5:] == 1
        # attacked by opponent pawns
        mobility_area -= valued_attack_map[6]
        # own blocked pawns
        mobility_area[1:] -= (((valued_board[:7] == 1).astype("int") + (valued_board[1:] == 1).astype("int")) > 1).astype("int")
        # own blockers for king

        pins = cls.get_pinned(board, color=color)
        for pin in pins:
            index, _ = pin
            row_index = (63 - index) // 8
            col_index = index % 8
            mobility_area[row_index, col_index] = 0

        return (mobility_area == 1).astype("int")

    @classmethod
    def get_pinned(cls, board: chess.Board, *, color: bool) -> np.ndarray:
        """Get the pinned squares and the direction.
        1 - horizontal, 2 - topleft to bottomright, 3 - vertical, 4 - topright to bottomleft
        board is bottom up, left right

        Parameters
        ----------
        board : chess.Board
            the board

        Returns
        -------
        list
            contains tuples with (square index, direction)
        """
        result = []

        for i in chess.SQUARES:
            if len(a := board.pin(color, i)) < 64:
                mask = np.array(a.tolist())
                if i < 8:
                    if mask[i + 8]:
                        result.append((i, 3))  # vertical
                    elif mask[i + 7]:
                        result.append((i, 2))  # topleft to bottomright

                    elif mask[i + 9]:
                        result.append((i, 4))  # topright to bottomleft
                elif mask[i - 8]:
                    result.append((i, 3))  # vertical
                elif mask[i - 9]:
                    result.append((i, 4))  # topright to bottomleft
                elif mask[i - 7]:
                    result.append((i, 2))  # topleft to bottomright

                if (i % 8) < 1:
                    if mask[i + 1]:
                        result.append((i, 1))  # horizontal
                elif mask[i - 1]:
                    result.append((i, 8))  # horizontal
        return result


class ExtractMobility(AbstractFeature):
    def __init__(
        self,
        board: chess.Board,
        *,
        is_midgame: bool | None = None,
        color: bool = chess.WHITE,
    ) -> None:
        super().__init__(board, is_midgame=is_midgame, color=color)

        if self.is_midgame:
            self.bonus = [
                [-62, -53, -12, -4, 3, 13, 22, 28, 33],
                [-48, -20, 16, 26, 38, 51, 55, 63, 63, 68, 81, 81, 91, 98],
                [-60, -20, 2, 3, 3, 11, 22, 31, 40, 40, 41, 48, 57, 57, 62],
                [
                    -30,
                    -12,
                    -8,
                    -9,
                    20,
                    23,
                    23,
                    35,
                    38,
                    53,
                    64,
                    65,
                    65,
                    66,
                    67,
                    67,
                    72,
                    72,
                    77,
                    79,
                    93,
                    108,
                    108,
                    108,
                    110,
                    114,
                    114,
                    116,
                ],
            ]
        else:
            self.bonus = [
                [-81, -56, -31, -16, 5, 11, 17, 20, 25],
                [-59, -23, -3, 13, 24, 42, 54, 57, 65, 73, 78, 86, 88, 97],
                [-78, -17, 23, 39, 70, 99, 103, 121, 134, 139, 158, 164, 168, 169, 172],
                [
                    -48,
                    -30,
                    -7,
                    19,
                    40,
                    55,
                    59,
                    75,
                    78,
                    96,
                    96,
                    100,
                    121,
                    127,
                    131,
                    133,
                    136,
                    141,
                    147,
                    150,
                    151,
                    168,
                    168,
                    171,
                    182,
                    182,
                    192,
                    219,
                ],
            ]

    def extract_feature(self) -> float:
        mobility_area = ExtractMobilityArea.get_mobility_area(self.board, color=self.color)[::-1].reshape(-1)
        mob = []
        for square in range(64):
            if self.board.color_at(square) == chess.WHITE and self.board.piece_type_at(square) not in [None, 1, 6]:
                if not self.board.is_pinned(chess.WHITE, square):
                    t = self.board.attacks(square)
                    if self.board.piece_type_at(square) in [2, 3]:
                        t = t ^ self.board.pieces(5, chess.WHITE)
                    t = t.tolist() & mobility_area.astype("bool")
                    mob.append((square, self.board.piece_type_at(square), sum(t.tolist())))
                else:
                    mob.append((square, self.board.piece_type_at(square), 0))
        all_ = 0
        for _, ind, val in mob:
            all_ += self.bonus[ind - 2][val]
        return all_


class ExtractPawnlessFlank(AbstractFeature):
    def extract_feature(self) -> float:
        """1 if only black is in danger, 0 when both or neither, -1 if only white is in danger

        Parameters
        ----------
        board : chess.Board
            chess board

        Returns
        -------
        int
            who is in favor
        """
        return self.pawnless_flank_colored(color=chess.BLACK) - self.pawnless_flank_colored(color=chess.WHITE)

    def pawnless_flank_colored(self, *, color: bool) -> float:
        """Whether the given color's king is on a pawnless flank

        Parameters
        ----------
        board : chess.Board
            position
        color : bool, optional
            _description_, by default chess.WHITE

        Returns
        -------
        _type_
            _description_
        """
        pawn_columns = np.zeros((8, 1))
        for i in range(64):
            if self.board.piece_type_at(i) == 1:
                pawn_columns[i % 8] += 1
            elif self.board.piece_type_at(i) == 6 and self.board.color_at(i) == color:
                king_column = i % 8
        if king_column == 0:
            pawn_sum = pawn_columns[0] + pawn_columns[1] + pawn_columns[2]
        elif king_column < 3:
            pawn_sum = pawn_columns[0] + pawn_columns[1] + pawn_columns[2] + pawn_columns[3]
        elif king_column < 5:
            pawn_sum = pawn_columns[2] + pawn_columns[3] + pawn_columns[4] + pawn_columns[5]
        elif king_column < 7:
            pawn_sum = pawn_columns[4] + pawn_columns[5] + pawn_columns[6] + pawn_columns[7]
        else:
            pawn_sum = pawn_columns[5] + pawn_columns[6] + pawn_columns[7]

        return 1 if pawn_sum == 0 else 0


class ExtractStrengthSquare(AbstractFeature):
    def extract_feature(self) -> float:
        flipped_board = self.board.transform(chess.flip_vertical)
        return self.get_strength_square(self.board, color=self.color) - self.get_strength_square(flipped_board, color=(not self.color))

    def get_strength_square(self, board: chess.Board, *, color: bool) -> float:
        debug = np.zeros((8, 8))

        for square_x, square_y in itertools.product(range(8), repeat=2):
            v = 5
            kx = min(6, max(1, square_x))
            weakness = [
                [-6, 81, 93, 58, 39, 18, 25],
                [-43, 61, 35, -49, -29, -11, -63],
                [-10, 75, 23, -2, 32, 3, -45],
                [-39, -13, -29, -52, -48, -67, -166],
            ]
            for x_ in range(kx - 1, kx + 2):
                us = 0
                for y in range(square_y + 1):
                    if (
                        (board.piece_type_at((x_) + y * 8) == 1 and board.color_at((x_) + y * 8) == (not color))
                        and not (board.piece_type_at((x_ - 1) + (y - 1) * 8) == 1 and board.color_at((x_ - 1) + (y - 1) * 8) == color)
                        and not (board.piece_type_at((x_ + 1) + (y - 1) * 8) == 1 and board.color_at((x_ + 1) + (y - 1) * 8) == color)
                    ):
                        us = 7 - y
                f = min(x_, 7 - x_)
                v += weakness[f][us]
            debug[square_y][square_x] = v

        return debug.sum()


class ExtractStormSquare(AbstractFeature):
    def extract_feature(self, board: chess.Board, *, is_midgame: bool, color: bool) -> float:
        raise NotImplementedError
