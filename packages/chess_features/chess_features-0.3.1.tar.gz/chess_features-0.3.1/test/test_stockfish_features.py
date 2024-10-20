import chess

from src.chess_features.stockfish_features import (
    ExtractMobility,
    ExtractMobilityArea,
    ExtractNonPawnMaterial,
    ExtractPawnlessFlank,
    ExtractPieceValue,
    ExtractPsqt,
    ExtractStormSquare,
    ExtractStrengthSquare,
)


class TestNonPawnMaterial:
    def test_non_pawn_material_starting_position(self):
        board = chess.Board()
        assert ExtractNonPawnMaterial(board, is_midgame=True).extract_feature() == 0

    def test_non_pawn_material_no_queen(self):
        board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
        assert ExtractNonPawnMaterial(board, is_midgame=True).extract_feature() == -2538

    def test_non_pawn_material_random_position(self):
        board = chess.Board("r1bqk1n1/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
        assert ExtractNonPawnMaterial(board, is_midgame=True).extract_feature() == 344


class TestPieceValue:
    def test_piece_value_mg_starting_position(self):
        board = chess.Board()
        assert ExtractPieceValue(board, is_midgame=True).extract_feature() == 0

    def test_piece_value_mg_no_queen(self):
        board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
        assert ExtractPieceValue(board, is_midgame=True).extract_feature() == -2786

    def test_piece_value_mg_random_position(self):
        board = chess.Board("r1bqk1n1/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
        assert ExtractPieceValue(board, is_midgame=True).extract_feature() == 96

    def test_piece_value_eg_starting_position(self):
        board = chess.Board()
        assert ExtractPieceValue(board, is_midgame=False).extract_feature() == 0

    def test_piece_value_eg_no_queen(self):
        board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
        assert ExtractPieceValue(board, is_midgame=False).extract_feature() == -3094

    def test_piece_value_eg_random_position(self):
        board = chess.Board("r1bqk1n1/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
        assert ExtractPieceValue(board, is_midgame=False).extract_feature() == 55


class TestPsqtBonus:
    def test_psqt_bonus_mg_starting_position(self):
        board = chess.Board()
        assert ExtractPsqt(board, is_midgame=True).extract_feature() == 0

    def test_psqt_bonus_mg_no_queen(self):
        board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
        assert ExtractPsqt(board, is_midgame=True).extract_feature() == -33

    def test_psqt_bonus_mg_random_position(self):
        board = chess.Board("r1bqk1n1/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
        assert ExtractPsqt(board, is_midgame=True).extract_feature() == -164

    def test_psqt_bonus_eg_starting_position(self):
        board = chess.Board()
        assert ExtractPsqt(board, is_midgame=True).extract_feature() == 0

    def test_psqt_bonus_eg_no_queen(self):
        board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
        assert ExtractPsqt(board, is_midgame=False).extract_feature() == 16

    def test_psqt_bonus_eg_random_position(self):
        board = chess.Board("r1bqk1n1/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
        assert ExtractPsqt(board, is_midgame=False).extract_feature() == -95


class TestMobilityArea:
    def test_mobility_area_starting_position(self):
        board = chess.Board()
        assert ExtractMobilityArea(board).extract_feature() == 0

    def test_mobility_area_no_queen(self):
        board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
        assert ExtractMobilityArea(board).extract_feature() == 3

    def test_mobility_area_random_position(self):
        board = chess.Board("r1bqk1n1/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
        assert ExtractMobilityArea(board).extract_feature() == 3

    def test_mobility_area_random_position_with_pins(self):
        board = chess.Board("b2rk1n1/p1p1pp2/pP1p2b1/1P1N1P1p/2qBK3/4B3/7P/RN2r2R w KQkq - 2 5")
        assert ExtractMobilityArea(board).extract_feature() == -3


class TestMobility:
    def test_mobility_mg_random_starting_position(self):
        board = chess.Board()
        assert ExtractMobility(board, is_midgame=True).extract_feature() == -172

    def test_mobility_mg_random_no_queen(self):
        board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
        assert ExtractMobility(board, is_midgame=True).extract_feature() == -66

    def test_mobility_mg_random_random_position(self):
        board = chess.Board("r1bqk1n1/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
        assert ExtractMobility(board, is_midgame=True).extract_feature() == -66

    def test_mobility_mg_random_position_with_pins(self):
        board = chess.Board("b2rk1n1/p1p1pp2/pP1p2b1/1P1N1P1p/2qBK3/4B3/7P/RN2r2R w KQkq - 2 5")
        assert ExtractMobility(board, is_midgame=True).extract_feature() == -137

    def test_mobility_eg_starting_position(self):
        board = chess.Board()
        assert ExtractMobility(board, is_midgame=False).extract_feature() == -244

    def test_mobility_eg_no_queen(self):
        board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
        assert ExtractMobility(board, is_midgame=False).extract_feature() == -116

    def test_mobility_eg_random_position(self):
        board = chess.Board("r1bqk1n1/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
        assert ExtractMobility(board, is_midgame=False).extract_feature() == -116

    def test_mobility_eg_random_position_with_pins(self):
        board = chess.Board("b2rk1n1/p1p1pp2/pP1p2b1/1P1N1P1p/2qBK3/4B3/7P/RN2r2R w KQkq - 2 5")
        assert ExtractMobility(board, is_midgame=False).extract_feature() == -73


class TestPawnlessFlankColored:
    def test_pawnless_flank_colored_starting_position(self):
        board = chess.Board()
        assert ExtractPawnlessFlank(board).pawnless_flank_colored(color=chess.WHITE) == 0

    def test_pawnless_flank_colored_no_queen(self):
        board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
        assert ExtractPawnlessFlank(board).pawnless_flank_colored(color=chess.WHITE) == 0

    def test_pawnless_flank_colored_random_position(self):
        board = chess.Board("r1bqk1n1/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
        assert ExtractPawnlessFlank(board).pawnless_flank_colored(color=chess.WHITE) == 0

    def test_pawnless_flank_colored_random_position_with_pins(self):
        board = chess.Board("b2rk1n1/p1p1pp2/pP1p2b1/1P1N1P1p/2qBK3/4B3/7P/RN2r2R w KQkq - 2 5")
        assert ExtractPawnlessFlank(board).pawnless_flank_colored(color=chess.WHITE) == 0

    def test_pawnless_flank_colored_endgame(self):
        board = chess.Board("1k6/4pp1p/8/8/4B3/8/4PP1P/5K2 w - - 2 2")
        assert ExtractPawnlessFlank(board).pawnless_flank_colored(color=chess.WHITE) == 0

    def test_pawnless_flank_colored_endgame_black(self):
        board = chess.Board("1k6/4pp1p/8/8/4B3/8/4PP1P/5K2 w - - 2 2")
        assert ExtractPawnlessFlank(board).pawnless_flank_colored(color=chess.BLACK) == 1


class TestPawnlessFlank:
    def test_pawnless_flank_starting_position(self):
        board = chess.Board()
        assert ExtractPawnlessFlank(board).extract_feature() == 0

    def test_pawnless_flank_no_queen(self):
        board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
        assert ExtractPawnlessFlank(board).extract_feature() == 0

    def test_pawnless_flank_random_position(self):
        board = chess.Board("r1bqk1n1/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
        assert ExtractPawnlessFlank(board).extract_feature() == 0

    def test_pawnless_flank_random_position_with_pins(self):
        board = chess.Board("b2rk1n1/p1p1pp2/pP1p2b1/1P1N1P1p/2qBK3/4B3/7P/RN2r2R w KQkq - 2 5")
        assert ExtractPawnlessFlank(board).extract_feature() == 0

    def test_pawnless_flank_endgame(self):
        board = chess.Board("1k6/4pp1p/8/8/4B3/8/4PP1P/5K2 w - - 2 2")
        assert ExtractPawnlessFlank(board).extract_feature() == 1

    def test_pawnless_flank_endgame_2(self):
        board = chess.Board("6k1/4pp1p/8/8/4B3/8/4PP1P/1K6 w - - 2 2")
        assert ExtractPawnlessFlank(board).extract_feature() == -1


class TestStrengthSquare:
    def test_strength_square_starting_position(self):
        board = chess.Board()
        assert ExtractStrengthSquare(board, color=chess.WHITE).extract_feature() == 0

    def test_strength_square_no_queen(self):
        board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
        assert ExtractStrengthSquare(board).extract_feature() == 836

    def test_strength_square_random_position(self):
        board = chess.Board("r1bqk1n1/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
        assert ExtractStrengthSquare(board).extract_feature() == 836

    def test_strength_square_random_position_with_pins(self):
        board = chess.Board("b2rk1n1/p1p1pp2/pP1p2b1/1P1N1P1p/2qBK3/4B3/7P/RN2r2R w KQkq - 2 5")
        assert ExtractStrengthSquare(board).extract_feature() == 250

    def test_strength_square_endgame(self):
        board = chess.Board("1k6/4pp1p/8/8/4B3/8/4PP1P/5K2 w - - 2 2")
        assert ExtractStrengthSquare(board).extract_feature() == 0

    def test_strength_square_endgame_2(self):
        board = chess.Board("6k1/4pp1p/8/8/4B3/8/4PP1P/1K6 w - - 2 2")
        assert ExtractStrengthSquare(board).extract_feature() == 0


class TestStormSquare:
    def test_storm_square_starting_position(self):
        board = chess.Board()
        assert ExtractStormSquare(board).extract_feature() == 0

    def test_storm_square_no_queen(self):
        board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
        assert ExtractStormSquare(board).extract_feature() == 518

    def test_storm_square_random_position(self):
        board = chess.Board("r1bqk1n1/pppppppp/8/8/8/8/PP2PPPP/RNB1KBNR b KQkq - 1 1")
        assert ExtractStormSquare(board).extract_feature() == 518

    def test_storm_square_random_position_with_pins(self):
        board = chess.Board("b2rk1n1/p1p1pp2/pP1p2b1/1P1N1P1p/2qBK3/4B3/7P/RN2r2R w KQkq - 2 5")
        assert ExtractStormSquare(board).extract_feature() == 2473

    def test_storm_square_endgame(self):
        board = chess.Board("1k6/4pp1p/8/8/4B3/8/4PP1P/5K2 w - - 2 2")
        assert ExtractStormSquare(board).extract_feature() == 0

    def test_storm_square_endgame_2(self):
        board = chess.Board("6k1/4pp1p/8/8/4B3/8/4PP1P/1K6 w - - 2 2")
        assert ExtractStormSquare(board).extract_feature() == 0
