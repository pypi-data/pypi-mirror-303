"""
Copyright CNRS/Inria/UniCA
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2018
SEE COPYRIGHT NOTICE BELOW
"""

import re as regx
import sys as sstm

from conf_ini_g.api.definition import missing_required_value_t, parameter_t, section_t
from obj_mpp.constant.config.definition import DEFINITION
from rich import print as rprint


def QueryResult(query: str, /) -> None:
    """"""
    query = query.lower()

    for section in DEFINITION:
        sct_name = section.name
        parameters = section.parameters
        if query in sct_name.lower():
            rprint(f"[blue]\\[{sct_name}][/]", end="")
            _PrintSectionDetails(section, query)
            for prm in parameters:
                _PrintParameterDetails(prm, query)
            rprint("")
        elif parameters is not None:
            for prm in parameters:
                if any(
                    query in _elm
                    for _elm in (prm.name, prm.definition, prm.description)
                    if isinstance(_elm, str)
                ):
                    rprint(f"[blue]\\[{sct_name}]", end="")
                    _PrintSectionDetails(section, query)
                    _PrintParameterDetails(prm, query)
                    rprint("")


def _PrintSectionDetails(section: section_t, query: str, /) -> None:
    """"""
    rprint(
        f" {_WithEmphasizedWord(section.definition, query)} / "
        f"cat={section.category} / "
        f"adv.opt={not section.basic}.{section.optional}"
    )


def _PrintParameterDetails(parameter: parameter_t, query: str, /) -> None:
    """"""
    if isinstance(parameter.default, missing_required_value_t):
        prm_default = "No defaults"
    else:
        prm_default = parameter.default
    rprint(
        f"\n    [magenta]{parameter.name}[/]: "
        f"{_WithEmphasizedWord(parameter.definition, query)}\n"
        f"        def={prm_default}\n"
        f"        type={parameter.type}\n"
        f"        adv.opt={not parameter.basic}.{parameter.optional}"
    )


def _WithEmphasizedWord(sentence: str, word: str, /) -> str:
    """"""
    return regx.sub(
        word, lambda wrd: f"[green]{wrd[0]}", sentence, flags=regx.IGNORECASE
    )


def Main() -> None:
    """"""
    if sstm.argv.__len__() > 1:
        QueryResult(sstm.argv[1])


if __name__ == "__main__":
    #
    Main()


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
