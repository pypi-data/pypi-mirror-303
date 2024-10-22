"""
Copyright CNRS/Inria/UniCA
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2018
SEE COPYRIGHT NOTICE BELOW
"""

from multiprocessing.managers import DictProxy as dict_shared_t

from logger_36.content import LINE_INDENT
from obj_mpp.interface.console.progress.base import (
    NewProgressTracker as NewProgressTrackerBase,
)
from obj_mpp.interface.console.progress.base import (
    progress_tracker_h,
    progress_tracker_silent_t,
)
from obj_mpp.type.signal.domain import chunked_bounds_h
from rich.progress import TaskID as task_id_t


def NewProgressTracker(
    n_iterations: int,
    status_period: float,
    chunked_bounds: chunked_bounds_h,
    /,
    *,
    called_from_cli: bool = True,
) -> progress_tracker_h:
    """"""
    if called_from_cli:
        output = NewProgressTrackerBase(status_period)
        chunk_lengths = (_bnd[1] - _bnd[0] for _bnd in chunked_bounds[1])
        chunk_bounds = (
            f"{LINE_INDENT}{c_idx}: [{_frt}..{_lst}]#{_lgt}"
            for c_idx, ((_frt, _lst), _lgt) in enumerate(
                zip(chunked_bounds[1], chunk_lengths), start=1
            )
        )
        for chunk_bound in chunk_bounds:
            _ = output.add_task(
                chunk_bound,
                total=n_iterations,
                n_non_blank_its=0,
                n_instances=0,
                sampling_efficiency=0,
                refinement_efficiency=0,
            )
        output.start()
    else:
        output = progress_tracker_silent_t()

    return output


def UpdateProgressRecord(
    record: dict_shared_t | dict[task_id_t, tuple[int, int, int, int]],
    task_id: task_id_t,
    /,
    *,
    completed: int = 0,
    n_non_blank_its: int = 0,
    n_instances: int = 0,
    refinement_efficiency: int = 0,
) -> None:
    """
    Must follow the obj_mpp.interface.console.progress.base.update_progress_p protocol
    with the added progress record.
    """
    record[task_id] = (
        completed,
        n_non_blank_its,
        n_instances,
        refinement_efficiency,
    )


"""
COPYRIGHT NOTICE

This software is governed by the CeCILL  license under French law and
abiding by the rules of distribution of free software.  You can  use,
modify and/ or redistribute the software under the terms of the CeCILL
license as circulated by CEA, CNRS and INRIA at the following URL
"http://www.cecill.info".

As a counterpart to the access to the source code and  rights to copy,
modify and redistribute granted by the license, users are provided only
with a limited warranty  and the software's author,  the holder of the
economic rights,  and the successive licensors  have only  limited
liability.

In this respect, the user's attention is drawn to the risks associated
with loading,  using,  modifying and/or developing or reproducing the
software by the user in light of its specific status of free software,
that may mean  that it is complicated to manipulate,  and  that  also
therefore means  that it is reserved for developers  and  experienced
professionals having in-depth computer knowledge. Users are therefore
encouraged to load and test the software's suitability as regards their
requirements in conditions enabling the security of their systems and/or
data to be ensured and,  more generally, to use and operate it in the
same conditions as regards security.

The fact that you are presently reading this means that you have had
knowledge of the CeCILL license and that you accept its terms.

SEE LICENCE NOTICE: file README-LICENCE-utf8.txt at project source root.

This software is being developed by Eric Debreuve, a CNRS employee and
member of team Morpheme.
Team Morpheme is a joint team between Inria, CNRS, and UniCA.
It is hosted by the Centre Inria d'Université Côte d'Azur, Laboratory
I3S, and Laboratory iBV.

CNRS: https://www.cnrs.fr/index.php/en
Inria: https://www.inria.fr/en/
UniCA: https://univ-cotedazur.eu/
Centre Inria d'Université Côte d'Azur: https://www.inria.fr/en/centre/sophia/
I3S: https://www.i3s.unice.fr/en/
iBV: http://ibv.unice.fr/
Team Morpheme: https://team.inria.fr/morpheme/
"""
