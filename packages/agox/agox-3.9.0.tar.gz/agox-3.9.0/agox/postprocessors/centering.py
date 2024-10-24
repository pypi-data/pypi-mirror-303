import numpy as np

from agox.postprocessors.ABC_postprocess import PostprocessBaseClass


class CenteringPostProcess(PostprocessBaseClass):
    """
    Centers a candidate object to the middle of the cell.

    Should not be used for periodic systems.
    """

    name = "CenteringPostProcess"

    def postprocess(self, candidate):
        """
        Centers a candidate object to the middle of the cell.

        Parameters
        ----------
        candidate : Candidate
            Candidate object to be centered.

        Returns
        -------
        candidate : Candidate
            Centered candidate object.

        """
        if candidate.pbc.any():
            self.writer.writer("CenteringPostProcess used on a periodic system, won't have any effect. Consider removing from script.")
            return candidate

        com = candidate.get_center_of_mass()
        cell_middle = np.sum(candidate.get_cell(), 0) / 2
        candidate.positions = candidate.positions - com + cell_middle
        return candidate
