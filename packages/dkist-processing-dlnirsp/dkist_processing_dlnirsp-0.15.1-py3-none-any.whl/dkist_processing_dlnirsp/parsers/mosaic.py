"""Bud to parse the number of subloops making up a mosaic."""
from collections import defaultdict
from collections import namedtuple
from typing import Literal
from typing import Type

from dkist_processing_common.models.flower_pot import SpilledDirt
from dkist_processing_common.models.flower_pot import Stem
from dkist_processing_common.models.task_name import TaskName

from dkist_processing_dlnirsp.models.constants import DlnirspBudName
from dkist_processing_dlnirsp.parsers.dlnirsp_l0_fits_access import DlnirspL0FitsAccess


class NumMosaicPieceBase(Stem):
    """
    Base class for identifying the number of dither steps, mosaic repeats, X tiles, and Y tiles in a dataset.

    Header keys exist for all of these loop levels; this class exists to handle the logic of datasets that are aborted
    at different levels of the instrument loops.

    Each "piece" of the mosaic loop (dither, mosaic repeats, X tiles, Y tiles) is recorded for all OBSERVE frames so
    that derived classes can use this information to figure out how many pieces there are.
    """

    MosaicPieces = namedtuple("MosaicPieces", ["dither_step", "mosaic_num", "X_tile", "Y_tile"])
    observe_task_name = TaskName.observe.value.casefold()

    # This only here so type-hinting of this complex dictionary will work.
    key_to_petal_dict: dict[str, MosaicPieces]

    def __init__(self, constant_name: str):
        super().__init__(stem_name=constant_name)

    def setter(self, fits_obj: DlnirspL0FitsAccess) -> Type[SpilledDirt] | tuple:
        """
        Extract the mosaic piece information from each frame and package in a tuple.

        Only OBSERVE frames are considered.
        """
        if fits_obj.ip_task_type.casefold() != TaskName.observe.value.casefold():
            return SpilledDirt

        dither_step = fits_obj.dither_step
        mosaic_num = fits_obj.mosaic_num
        X_tile = fits_obj.X_tile_num
        Y_tile = fits_obj.Y_tile_num

        return self.MosaicPieces(
            dither_step=dither_step, mosaic_num=mosaic_num, X_tile=X_tile, Y_tile=Y_tile
        )

    def multiple_pieces_attempted_and_at_least_one_completed(
        self, piece_name: Literal["dither_step", "mosaic_num", "X_tile", "Y_tile"]
    ) -> bool:
        """Return `True` if more than one of the requested pieces was attempted and at least one completed."""
        num_files_per_piece = self.num_files_per_mosaic_piece(piece_name)
        complete_piece_nums = self.complete_piece_list(num_files_per_piece)
        num_attempted_pieces = len(num_files_per_piece.keys())
        num_completed_pieces = len(complete_piece_nums)

        return num_attempted_pieces > 1 and num_completed_pieces > 0

    def num_files_per_mosaic_piece(
        self, piece_name: Literal["dither_step", "mosaic_num", "X_tile", "Y_tile"]
    ) -> dict[int, int]:
        """
        Compute the number of files per each unique mosaic piece.

        For example, if each mosaic num usually has 4 files, but an abort resulted in the last one only having 2 then
        the output of this method would be `{0: 4, 1: 4, 2: 4, 3: 2}`.
        """
        num_files_per_piece = defaultdict(int)
        for mosaic_pieces in self.key_to_petal_dict.values():
            num_files_per_piece[getattr(mosaic_pieces, piece_name)] += 1

        return num_files_per_piece

    def complete_piece_list(self, num_files_per_piece_dict: dict[int, int]) -> list[int]:
        """
        Identify the index numbers of all complete mosaic pieces.

        "Completed" pieces are assumed to be those that have a number of files equal to the maximum number of files
        in any mosaic piece. This is a good assumption for now.
        """
        complete_piece_size = max(num_files_per_piece_dict.values())
        return [
            piece_num
            for piece_num, piece_size in num_files_per_piece_dict.items()
            if piece_size == complete_piece_size
        ]


class NumMosaicRepeatsBud(NumMosaicPieceBase):
    """
    Bud for determining the number of mosaic repeats.

    Only completed mosaics are considered.
    """

    def __init__(self):
        super().__init__(constant_name=DlnirspBudName.num_mosaic_repeats.value)

    def getter(self, key: str) -> int:
        """
        Return the number of *completed* mosaic repeats.

        A check is also made that the list of completed repeats is continuous from 0 to the number of completed repeats.
        """
        num_files_per_mosaic = self.num_files_per_mosaic_piece("mosaic_num")
        complete_mosaic_nums = self.complete_piece_list(num_files_per_mosaic)

        num_mosaics = len(complete_mosaic_nums)
        sorted_complete_mosaic_nums = sorted(complete_mosaic_nums)
        if sorted_complete_mosaic_nums != list(range(num_mosaics)):
            raise ValueError(
                f"Not all sequential mosaic repeats could be found. Found {sorted_complete_mosaic_nums}"
            )

        return num_mosaics


class NumDitherStepsBud(NumMosaicPieceBase):
    """
    Bud for determining the number of dither steps.

    If there are multiple mosaic repeats and any of them are complete then *all* dither steps are expected to exist.
    Otherwise the number of completed dither steps is returned.
    """

    def __init__(self):
        super().__init__(constant_name=DlnirspBudName.num_dither_steps.value)

    def getter(self, key: str) -> int:
        """
        Return the number of *completed* dither steps.

        Also check that the set of completed dither steps is either `{0}` or `{0, 1}` (because the max number of dither
        steps is 2).
        """
        num_files_per_dither = self.num_files_per_mosaic_piece("dither_step")
        if self.multiple_pieces_attempted_and_at_least_one_completed("mosaic_num"):
            # Only consider complete dither steps
            all_dither_steps = sorted(list(num_files_per_dither.keys()))
            num_dither_steps = len(all_dither_steps)
            if all_dither_steps != list(range(num_dither_steps)):
                raise ValueError(
                    f"Whole dither steps are missing. This is extremely strange. Found {all_dither_steps}"
                )
            return num_dither_steps

        complete_dither_nums = self.complete_piece_list(num_files_per_dither)

        num_dither = len(complete_dither_nums)

        if sorted(complete_dither_nums) != list(range(num_dither)):
            raise ValueError(
                f"Not all sequential dither steps could be found. Found {set(complete_dither_nums)}."
            )

        return num_dither


class NumXTilesBud(NumMosaicPieceBase):
    """
    Bud for determining the number of X tiles.

    If the dataset includes multiple attempted mosaic repeats or dithers then all found X tiles are expected to be
    completed. If only a single mosaic repeat and dither was attempted then the number of complete X tiles is returned.
    This allows for the case where the mosaic repeat and dither loops were unused.
    """

    def __init__(self):
        super().__init__(constant_name=DlnirspBudName.num_spatial_steps_X.value)

    def getter(self, key: str) -> int:
        """
        Return the number of X tiles.

        If multiple mosaic repeats or dithers were attempted and at least one is completed then all X tiles are required
        to be complete, but if only a single mosaic repeat and dither was attempted then the total number of X tiles
        is considered to be the number of *completed* X tiles.

        We also check that the set of X tiles is continuous from 0 to the number of X tiles.
        """
        num_files_per_X_tile = self.num_files_per_mosaic_piece("X_tile")
        if (
            self.multiple_pieces_attempted_and_at_least_one_completed("mosaic_num")  # fmt: skip
            or self.multiple_pieces_attempted_and_at_least_one_completed("dither_step")
        ):
            # The logic of this conditional is pretty subtle so here's an explanation:
            # If ANY higher-level loop has more than one iteration then ALL lower-level loops will be required
            # to be complete. This is why this is `or` instead of `and`. For example if num_dithers=2 but the mosaic
            # loop was not used (num_mosaic = 1) we still need all X tiles.
            all_X_tiles = sorted(list(num_files_per_X_tile.keys()))
            num_X_tiles = len(all_X_tiles)
            if all_X_tiles != list(range(num_X_tiles)):
                raise ValueError(
                    f"Whole X tiles are missing. This is extremely strange. Found {all_X_tiles}"
                )
            return num_X_tiles

        # Otherwise (i.e., there are no completed mosaics, or we only observed a single mosaic) all X tiles are valid
        completed_X_tiles = self.complete_piece_list(num_files_per_X_tile)

        num_X_tiles = len(completed_X_tiles)
        sorted_complete_X_tiles = sorted(completed_X_tiles)
        if sorted_complete_X_tiles != list(range(num_X_tiles)):
            raise ValueError(
                f"Not all sequential X tiles could be found. Found {sorted_complete_X_tiles}"
            )

        return num_X_tiles


class NumYTilesBud(NumMosaicPieceBase):
    """
    Bud for determining the number of Y tiles.

    If the dataset includes multiple attempted mosaic repeats, dithers, or X tiles then all found Y tiles are expected
    to be completed. If only a single mosaic repeat AND dither AND X tile were attempted then the number of complete
    Y tiles is returned. This allows for the case where the mosaic repeat, dither, and X tile loops were unused.
    """

    def __init__(self):
        super().__init__(constant_name=DlnirspBudName.num_spatial_steps_Y.value)

    def getter(self, key: str) -> int:
        """
        Return the number of Y tiles.

        If multiple mosaic repeats, dithers, or X tiles were attempted and at least one complete one exists then all Y
        tiles are required to be complete, but if only a single mosaic repeat AND dither AND X tile were attempted then
        the total number of Y tiles is considered to be the number of *completed* Y tiles.

        We also check that the set of Y tiles is continuous from 0 to the number of Y tiles.
        """
        num_files_per_Y_tile = self.num_files_per_mosaic_piece("Y_tile")
        if (
            self.multiple_pieces_attempted_and_at_least_one_completed("mosaic_num")
            or self.multiple_pieces_attempted_and_at_least_one_completed("dither_step")
            or self.multiple_pieces_attempted_and_at_least_one_completed("X_tile")
        ):
            # The logic of this conditional is pretty subtle so here's an explanation:
            # If ANY higher-level loop has more than one iteration then ALL lower-level loops will be required
            # to be complete. This is why this is `or` instead of `and`. For example if num_mosaics = 3 but the X tile
            # loop was not used (num_X_tiles = 1) we still need all Y tiles.
            all_Y_tiles = sorted(list(num_files_per_Y_tile.keys()))
            num_Y_tiles = len(all_Y_tiles)
            if all_Y_tiles != list(range(num_Y_tiles)):
                raise ValueError(
                    f"Whole Y tiles are missing. This is extremely strange. Found {all_Y_tiles}"
                )
            return num_Y_tiles

        completed_Y_tiles = self.complete_piece_list(num_files_per_Y_tile)
        num_Y_tiles = len(completed_Y_tiles)
        sorted_complete_Y_tiles = sorted(completed_Y_tiles)
        if sorted_complete_Y_tiles != list(range(num_Y_tiles)):
            raise ValueError(
                f"Not all sequential Y tiles could be found. Found {sorted_complete_Y_tiles}"
            )

        return num_Y_tiles
