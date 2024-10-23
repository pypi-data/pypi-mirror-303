from itertools import product

import chess
import numpy as np

from .neighborhood_transform import get_neighborhood


class StockfishExtractor:
    def extract(self, feature_names: list[str] | None = None) -> list[float | int]:
        pass


def to_white_moving(board: chess.Board) -> chess.Board:
    if not board.turn:
        board.mirror()
    return board


def to_fen(board: chess.Board) -> str:
    return board.fen()


def bitboards_to_array(bb: np.ndarray) -> np.ndarray:
    bb = np.asarray(bb, dtype=np.uint64)[:, np.newaxis]
    s = 8 * np.arange(7, -1, -1, dtype=np.uint64)
    b = (bb >> s).astype(np.uint8)
    b = np.unpackbits(b, bitorder="little")
    return b.reshape((-1, 8, 8))


def bitboard_to_array(bb: int) -> np.ndarray:
    s = 8 * np.arange(7, -1, -1, dtype=np.uint64)
    print(bb.shape, s.shape)
    b = (bb >> s).astype(np.uint8)
    b = np.unpackbits(b, bitorder="little")
    return b.reshape(8, 8)


def to_bitboard(board: chess.Board) -> np.ndarray:
    values = {"queen": 1, "king": 1, "rook": 1, "bishop": 1, "knight": 1, "pawn": 1}
    return to_valued_bitboard(board, values)


def to_unified_neg_bitboard(board: chess.Board) -> np.ndarray:
    bitboards = to_bitboard(board).astype(np.int16)
    return bitboards[:6] - bitboards[6:]


def to_unified_bitboard(board: chess.Board) -> np.ndarray:
    bitboards = np.array(
        [
            board.pawns,
            board.knights,
            board.bishops,
            board.rooks,
            board.queens,
            board.kings,
        ],
        dtype=np.uint64,
    )
    return bitboards_to_array(bitboards)


def to_valued_bitboard(board: chess.Board, values: dict | None = None) -> np.ndarray:
    if values is None:
        values = {
            "queen": 9,
            "king": 500,
            "rook": 5,
            "bishop": 3,
            "knight": 3,
            "pawn": 1,
        }
    black, white = board.occupied_co

    values_array = np.array(
        [
            values["pawn"],
            values["knight"],
            values["bishop"],
            values["rook"],
            values["queen"],
            values["king"],
            values["pawn"],
            values["knight"],
            values["bishop"],
            values["rook"],
            values["queen"],
            values["king"],
        ]
    )

    bitboards = np.array(
        [
            white & board.pawns,
            white & board.knights,
            white & board.bishops,
            white & board.rooks,
            white & board.queens,
            white & board.kings,
            black & board.pawns,
            black & board.knights,
            black & board.bishops,
            black & board.rooks,
            black & board.queens,
            black & board.kings,
        ],
        dtype=np.uint64,
    )
    bitboard = bitboards_to_array(bitboards)
    return bitboard * values_array.reshape((-1, 1, 1))


def bitboard_to_bitvector(bitboard: chess.Board) -> np.ndarray:
    return bitboard.reshape(-1)


def get_unified_valued_bitboard(board: chess.Board, values: dict | None = None) -> np.ndarray:
    valued_board = to_valued_bitboard(board, values)
    valued_board[-6:] = -valued_board[-6:]
    return np.sum(valued_board, axis=0)


def to_chess_neighborhoods(board: chess.Board, *, clockwise: bool = False) -> np.ndarray:
    valued_board = get_unified_valued_bitboard(board)
    neighborhoods = []
    for x, y in product(range(8), repeat=2):
        neighborhoods.append(get_neighborhood(valued_board, x, y, clockwise=clockwise))
    return np.array(neighborhoods)


def to_san(board: chess.Board) -> str:
    san_board = chess.Board()
    move_stack = []

    for move in board.move_stack:
        move_stack.append(san_board.san(move))
        san_board.push(move)

    return " ".join(move_stack)


def to_bit_attack_map(board: chess.Board) -> np.ndarray:
    attack_map = np.zeros((2, 64))
    for square in chess.SQUARES:
        white_attackers = board.attackers(chess.WHITE, square)
        black_attackers = board.attackers(chess.BLACK, square)
        if white_attackers:
            attack_map[0, square] = 1
        if black_attackers:
            attack_map[1, square] = 1

    return np.flip(attack_map.reshape((2, 8, 8)), axis=1)


def to_valued_attack_map(board: chess.Board, values: dict | None = None) -> np.ndarray:
    if values is None:
        values = {
            "queen": 9,
            "king": 500,
            "rook": 5,
            "bishop": 3,
            "knight": 3,
            "pawn": 1,
        }
    values_array = np.array(
        [
            values["pawn"],
            values["knight"],
            values["bishop"],
            values["rook"],
            values["queen"],
            values["king"],
            values["pawn"],
            values["knight"],
            values["bishop"],
            values["rook"],
            values["queen"],
            values["king"],
        ]
    )

    attack_map = np.zeros((2 * 6, 64))
    for square in chess.SQUARES:
        white_attackers = board.attackers(chess.WHITE, square)
        black_attackers = board.attackers(chess.BLACK, square)

        white_min_attacker = min(
            (board.piece_type_at(white_attacker) for white_attacker in white_attackers),
            default=-1,
        )
        if white_min_attacker >= 0:
            attack_map[white_min_attacker - 1, square] = 1

        black_min_attacker = min(
            (board.piece_type_at(black_attacker) for black_attacker in black_attackers),
            default=-1,
        )
        if black_min_attacker >= 0:
            attack_map[5 + black_min_attacker, square] = 1

    return np.flip(attack_map.reshape((12, 8, 8)), axis=1) * values_array.reshape((-1, 1, 1))


def to_bit_defend_map(board: chess.Board) -> np.ndarray:
    attack_map = np.zeros((2, 64))
    for square in chess.SQUARES:
        white_defenders = board.attackers(chess.BLACK, square)
        black_defenders = board.attackers(chess.WHITE, square)
        if white_defenders:
            attack_map[0, square] = 1
        if black_defenders:
            attack_map[1, square] = 1

    return np.flip(attack_map.reshape((2, 8, 8)), axis=1)


def to_valued_defend_map(board: chess.Board, values: dict | None = None) -> np.ndarray:
    if values is None:
        values = {
            "queen": 9,
            "king": 500,
            "rook": 5,
            "bishop": 3,
            "knight": 3,
            "pawn": 1,
        }

    values_array = np.array(
        [
            values["pawn"],
            values["knight"],
            values["bishop"],
            values["rook"],
            values["queen"],
            values["king"],
            values["pawn"],
            values["knight"],
            values["bishop"],
            values["rook"],
            values["queen"],
            values["king"],
        ]
    )

    defend_map = np.zeros((2 * 6, 64))
    for square in chess.SQUARES:
        white_defenders = board.attackers(chess.BLACK, square)
        black_defenders = board.attackers(chess.WHITE, square)

        white_min_defender = min(
            (board.piece_type_at(white_attacker) for white_attacker in white_defenders),
            default=-1,
        )
        if white_min_defender >= 0:
            defend_map[white_min_defender - 1, square] = 1

        black_min_defender = min(
            (board.piece_type_at(black_attacker) for black_attacker in black_defenders),
            default=-1,
        )
        if black_min_defender >= 0:
            defend_map[5 + black_min_defender, square] = 1

    return np.flip(defend_map.reshape((12, 8, 8)), axis=1) * values_array.reshape((-1, 1, 1))
