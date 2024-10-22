"""
Copyright CNRS/Inria/UniCA
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2018
SEE COPYRIGHT NOTICE BELOW
"""

import typing as h

from rich.progress import BarColumn as column_bar_t
from rich.progress import Progress as progress_tracker_t
from rich.progress import TaskID as task_id_t
from rich.progress import TextColumn as column_text_t
from rich.progress import TimeRemainingColumn as column_time_remaining_t


class progress_tracker_silent_t:
    def start(self) -> None:
        pass

    def update(self, *_, **__) -> None:
        pass

    def stop(self) -> None:
        pass


progress_tracker_h = progress_tracker_t | progress_tracker_silent_t


def NewProgressTracker(status_period: float, /) -> progress_tracker_t:
    """"""
    columns = (
        column_text_t("{task.description}", markup=False),
        column_bar_t(),
        column_text_t(
            "{task.fields[n_non_blank_its]}/{task.completed}",
            justify="right",
            markup=False,
        ),
        column_text_t(
            "#{task.fields[n_instances]}[{task.fields[refinement_efficiency]}%]",
            markup=False,
        ),
        column_time_remaining_t(elapsed_when_finished=True),
    )

    return progress_tracker_t(*columns, refresh_per_second=1.0 / status_period)


class update_progress_p(h.Protocol):
    """
    Must be compatible with the rich.progress.Progress.update signature with added
    custom progress parameters.
    """

    def __call__(
        self,
        task_id: task_id_t,
        /,
        *,
        completed: int = 0,
        n_non_blank_its: int = 0,
        n_instances: int = 0,
        refinement_efficiency: int = 0,
    ) -> None: ...


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
