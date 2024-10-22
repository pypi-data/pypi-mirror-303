"""
Copyright CNRS/Inria/UniCA
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2018
SEE COPYRIGHT NOTICE BELOW
"""

import typing as h

from conf_ini_g.api.definition import parameter_t
from conf_ini_g.api.definition import section_controller_t as controller_t
from conf_ini_g.api.definition import section_t
from obj_mpp.constant.config.label import label_e
from str_to_obj.api.catalog import (
    callable_t,
    collection_t,
    number_t,
    path_purpose_e,
    path_t,
    path_type_e,
)

DEFINITION = (
    section_t(
        name=label_e.sct_mpp.value,
        category=label_e.cat_optimization.value,
        definition="Main Obj.MPP parameters",
        description="Algorithmic parameters of Obj.MPP.",
        basic=True,
        optional=False,
        parameters=[
            parameter_t(
                name="n_iterations",
                definition="Number of iterations",
                description="Number of rounds (or iterations) of random candidate object generation. "
                "There is no default value.",
                basic=True,
                type=h.Annotated[int, number_t(min=1)],
            ),
            parameter_t(
                name="n_new_per_iteration",
                definition='Number of object "births" at each iteration',
                description="Number of new, random candidate objects generated at each iteration. "
                "This could be set equal to the expected number of objects in the signal "
                "although there is no guarantee that this order of magnitude is optimal "
                "in terms of detection_performance-vs-computation_time trade-off. "
                "The total number of candidate objects generated will be "
                '"n_iterations x n_new_per_iteration". '
                "The default value is 20.",
                basic=False,
                type=h.Annotated[int, number_t(min=1)],
                default=100,
            ),
            parameter_t(
                name="seed",
                definition="Seed for pseudo-random number generation",
                description="The seed used to initialize the pseudo-random number generator "
                "used to build random candidate objects. This parameter should usually be ignored. "
                'It is mainly used to make the randomness in Obj.MPP "predictable" '
                "when testing or debugging. "
                "If None, there is no specific seeding."
                "The default value is None.",
                basic=False,
                type=h.Annotated[int, number_t(min=0, max=2**32 - 1)] | None,
                default=None,
            ),
            parameter_t(
                name="n_parallel_workers",
                definition="Number of parallel detection subtasks",
                description="Number of subtasks the detection task will be split into to be run in parallel. "
                "If equal to 1, the detection task will be run sequentially. "
                "If > 1, that number of subtasks will be used. "
                "If <= 0, Obj.MPP will choose the number of subtasks based on the number of CPU cores. "
                "Note that this parameter is ignored on Windows, falling back to sequential processing "
                '(see the documentation of the "fork" start method in the "multiprocessing" Python module). '
                "The default value is 0.",
                basic=False,
                type=int,
                default=0,
            ),
            parameter_t(
                name="use_history",
                definition="Whether to use a previous detection result",
                basic=False,
                type=bool,
                default=False,
            ),
            parameter_t(
                name="fixed_history",
                definition="Whether to make the previous detection result immutable and unremovable",
                basic=False,
                type=bool,
                default=False,
            ),
        ],
    ),
    section_t(
        name=label_e.sct_refinement.value,
        category=label_e.cat_optimization.value,
        definition="Refinement parameters",
        basic=False,
        optional=True,
        parameters=[
            parameter_t(
                name="interval",
                basic=False,
                type=h.Annotated[int, number_t(min=0)] | None,
                default=None,
            ),
            parameter_t(
                name="n_attempts",
                basic=False,
                type=h.Annotated[int, number_t(min=1)],
                default=10,
            ),
            parameter_t(
                name="max_variation",
                basic=False,
                type=h.Annotated[float, number_t(min=0.0, min_inclusive=False)],
                default=0.1,
            ),
        ],
    ),
    section_t(
        name=label_e.sct_feedback.value,
        category=label_e.cat_optimization.value,
        basic=False,
        optional=True,
        parameters=[
            parameter_t(
                name="status_period",
                definition="Time in seconds between two status feedback (0 -> no feedback)",
                basic=False,
                type=h.Annotated[float, number_t(min=0.0)],
                default=2.0,
            )
        ],
    ),
    section_t(
        name=label_e.sct_object.value,
        category=label_e.cat_object.value,
        definition="Object type and common properties",
        basic=True,
        optional=False,
        parameters=[
            parameter_t(
                name="definition",
                definition="[Object module:]Object type",
                description="Before the colon: Object module path (absolute or relative to ini file) "
                "or object module name in brick/marked_point/(oneD|twoD|threeD), "
                'with "py" extension chopped off. '
                "E.g. circle for circle.py. "
                "This part, including the colon, is optional. "
                "Since when this part is omitted, a module is searched for in several folders, "
                "these modules should have different names to avoid masking modules in subsequently visited folders. "
                'After the colon: An object type defined in the object module with "_t" suffix chopped off. '
                "E.g. circle for class circle_t",
                basic=True,
                type=callable_t.NewAnnotatedType(kind="class", allow_external=True),
            ),
            parameter_t(
                name="center",
                description="- None = No constraint on position: it can be anywhere inside image domain"
                "- Precision(s): a precision common to all dimensions, or a list/tuple of per-axis precisions"
                "- Path to an image representing a map (image containing 2 distinct values, "
                "the locii of the max being valid points) or "
                "a PDF (image of positive values summing to 1 used to draw points).",
                basic=False,
                type=int
                | float
                | h.Annotated[tuple, collection_t(items_types=int | float)]
                | path_t.NewAnnotatedType(path_type_e.any, path_purpose_e.input)
                | None,
                default=None,
            ),
            parameter_t(
                name="only_un_cropped",
                definition="Only retain objects that do not cross domain border",
                basic=False,
                type=bool,
                default=True,
            ),
        ],
    ),
    section_t(
        name=label_e.sct_mark_ranges.value,
        category=label_e.cat_object.value,
        definition="Specific to the selected object type",
        basic=True,
        optional=False,
        controller=controller_t(
            section=label_e.sct_object.value, parameter="definition"
        ),
    ),
    section_t(
        name=label_e.sct_quality.value,
        category=label_e.cat_object.value,
        definition="Common to any object quality",
        basic=True,
        optional=False,
        parameters=[
            parameter_t(
                name="definition",
                definition="[Quality module:]Quality class",
                description="Before the colon: Quality module path (absolute or relative to ini file) "
                "or object module name in brick/quality/(oneD|twoD|threeD), "
                'with "py" extension chopped off. '
                "E.g. contrast for contrast.py. "
                "This part, including the colon, is optional. "
                "Since when this part is omitted, a module is searched for in several folders, "
                "these modules should have different names to avoid masking modules in subsequently visited folders. "
                'After the colon: A quality class defined in the quality module with "_t" suffix chopped off. '
                "E.g. bright_on_dark_contrast for class contrast_bright_on_dark_t",
                basic=True,
                type=str,
            ),
            parameter_t(name="min_value", basic=True, type=int | float),
        ],
    ),
    section_t(
        name=label_e.sct_quality_prm.value,
        category=label_e.cat_object.value,
        definition="Specific to the selected object quality",
        basic=False,
        optional=True,
        controller=controller_t(
            section=label_e.sct_quality.value, parameter="definition"
        ),
    ),
    # section_t(
    #     name=label_e.sct_incentives.value,
    #     category=label_e.cat_object.value,
    #     definition="Incentives on Generated Objects",
    #     basic=False,
    #     optional=True,
    # ),
    section_t(
        name=label_e.sct_constraints.value,
        category=label_e.cat_object.value,
        definition="Constraints on Generated Objects",
        basic=False,
        optional=True,
        parameters=[
            parameter_t(
                name="max_overlap",
                definition="As a percentage (0.0 => no overlap allowed)",
                basic=False,
                type=h.Annotated[float, number_t(min=0.0, max=100.0)],
                default=20.0,
            )
        ],
    ),
    section_t(
        name=label_e.sct_signal.value,
        category=label_e.cat_input.value,
        definition="Common to any signal loading function",
        basic=True,
        optional=False,
        parameters=[
            parameter_t(
                name="path",
                definition="Image path or image folder path",
                description="Path to raw signal (either a single file or a folder (absolute or relative to ini file) "
                "that will be scanned w/o recursion)",
                basic=True,
                type=path_t.NewAnnotatedType(path_type_e.any, path_purpose_e.input),
            ),
            parameter_t(
                name="loading_function",
                description="Raw signal loading module in given folder (absolute or relative to ini file) or "
                "in helper with py extension chopped off. E.g. signal_loading for signal_loading.py. "
                "Optional = signal_loading module in helper. "
                "It must accept a parameter named signal_path",
                basic=False,
                type=str,
                default="ImageChannelBySkimage",
            ),
        ],
    ),
    section_t(
        name=label_e.sct_signal_loading_prm.value,
        category=label_e.cat_input.value,
        definition="Specific to the selected signal loading function",
        basic=False,
        optional=True,
    ),
    section_t(
        name=label_e.sct_signal_processing_prm.value,
        category=label_e.cat_input.value,
        definition="Specific to the selected object quality: parameters for the function converting "
        "loaded raw signal into signal used by object quality",
        basic=False,
        optional=True,
    ),
    section_t(
        name=label_e.sct_output.value,
        category=label_e.cat_output.value,
        basic=True,
        optional=True,
        parameters=[
            parameter_t(
                name="console",
                definition="Whether to print the result in the console",
                basic=False,
                type=bool,
                default=True,
            ),
            parameter_t(
                name="base_folder",
                definition="Base output folder",
                basic=True,
                type=path_t.NewAnnotatedType(path_type_e.folder, path_purpose_e.output)
                | None,
                default=None,
            ),
            parameter_t(
                name="what",
                definition="Which results should be output. Comma-separated list of keywords among: "
                "csv (detected marked points in a CSV file),"
                "json (detected marked points in a file with a format that can be used to recreate them),"
                "contour (contours of the detected marked points in an image file),"
                "region (regions of the detected marked points in an image file),"
                "region_numpy (regions of the detected marked points in a Numpy file (.npz)).",
                basic=True,
                type=str | None,
                default=None,
            ),
            parameter_t(
                name="output_function",
                description="Result output module in given folder (absolute or relative to ini file) or "
                'in helper with "py" extension chopped off. '
                "E.g. result_output for result_output.py. Optional  =  result_output module in helper. "
                "Result output function: Output2DObjects if processing a single "
                "datum, or None if processing a signal folder",
                basic=False,
                type=str | None,
                default=None,
            ),
            parameter_t(
                name="marks_separator",
                definition="Marks separator for the CSV format",
                basic=True,
                type=str,
                default=",",
            ),
        ],
    ),
    section_t(
        name=label_e.sct_output_prm.value,
        category=label_e.cat_output.value,
        definition="Specific to the select result output function",
        basic=False,
        optional=True,
    ),
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
