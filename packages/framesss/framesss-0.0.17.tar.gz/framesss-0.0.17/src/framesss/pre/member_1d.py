from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np

from framesss.enums import BeamConnection
from framesss.enums import CoordinateDefinition
from framesss.enums import DistributedLoadLocation
from framesss.enums import Element1DType
from framesss.enums import LoadCoordinateSystem
from framesss.enums import SupportFixity
from framesss.fea.boundary_conditions.element_load import DistributedLoad
from framesss.fea.boundary_conditions.element_load import ThermalLoad
from framesss.fea.boundary_conditions.nodal_load import NodalLoad
from framesss.fea.element_1d import Element1D
from framesss.fea.node import Node
from framesss.post.member_1d_results import Member1DResults
from framesss.pre.member_load import DistributedLoadOnMember
from framesss.pre.member_load import PointLoadOnMember
from framesss.pre.member_load import ThermalLoadOnMember

if TYPE_CHECKING:
    import numpy.typing as npt

    from framesss.fea.analysis.analysis import Analysis
    from framesss.fea.models.model import Model
    from framesss.pre.cases import LoadCase
    from framesss.pre.section import Section

MAX_DISTANCE_BETWEEN_SAMPLING_POINTS = 0.1  # (m)
NUMERIC_GARBAGE = 1.0e-12

COORDINATE_DEFINITIONS = [CoordinateDefinition.ABSOLUTE, CoordinateDefinition.RELATIVE]


def cross(
    x: npt.NDArray[np.float64], y: npt.NDArray[np.float64]
) -> npt.NDArray[np.float64]:
    """
    Workaround function, because IDE marks the np.cross() as unreachable.

    See: https://github.com/numpy/numpy/issues/22146
    """
    # TODO: delete once numpy package gets fixed
    return np.cross(x, y)


class Member1D:
    """
    Class representing a 1D member.

    Represents a one-dimensional member, encapsulating all necessary attributes that define
    the member's physical and mechanical properties, as well as its loading conditions.

    The member is discretized into unique elements at points where discontinuities in the loading occur.

    :param label: A user-defined identifier for the member.
    :param element_type: Specifies the type of the element ('navier', 'timoshenko').
    :param nodes: The nodes at the ends of the member.
    :param section: The cross-section of the member.
    :param hinges: Defines the type of connections at the start and the end of the  member
                   (e.g., fixed, hinged, or semirigid) to model the rotational stiffness accurately.
    :param auxiliary_vector_xy_plane: An auxiliary vector in local xy-plane that defines the local
                                      coordinate system of the member.
    :param analysis: The :class:`Analysis` object.

    :ivar id: An automatically assigned unique identifier for the member within the model.
    :ivar direction_cosine_matrix: Calculated direction cosines for the member based on its geometry.
    :ivar transformation_matrix: A matrix used to transform displacements and forces between the local
                                 and global coordinate systems.
    :ivar distributed_loads: A collection of distributed loads applied to the member.
    :ivar thermal_loads: A collection of thermal loads affecting the member.
    :ivar point_loads: A collection of point forces and moments applied to the member.
    :ivar generated_nodes: A collection of user-defined and generated :class:`Node` objects
                           along the member in points of the loading discontinuities.
    :ivar generated_elements: A collection of :class:`Element1D` generated along the member for detailed analysis.
    :ivar x_user_defined_nodes: Positions along the member length where user-defined nodes are located.
    :ivar x_discontinuities: Positions along the member length where discontinuities (e.g., changes in loading) occur.
    :ivar results: An object to store analysis results related to the member.
    """

    TOLERANCE = 1e-6

    def __init__(
        self,
        label: str,
        element_type: str,
        nodes: list[Node],
        section: Section,
        hinges: list[str] | list[BeamConnection],
        auxiliary_vector_xy_plane: npt.NDArray[np.float64],
        analysis: Analysis,
    ) -> None:
        """Init the Member1D object."""
        self.id: None | int = None
        self.label = label
        self.element_type = Element1DType(element_type)
        self.analysis = analysis
        self.section: Section | None = section
        self.sections: dict[tuple[float, float], Section] | None = None
        self.nodes = nodes
        self.hinge_start, self.hinge_end = (BeamConnection(hng) for hng in hinges)
        self.auxiliary_vector_xy_plane = auxiliary_vector_xy_plane

        xi, yi, zi = nodes[0].coords
        xf, yf, zf = nodes[1].coords

        dx = xf - xi
        dy = yf - yi
        dz = zf - zi
        length = np.sqrt(dx**2 + dy**2 + dz**2)

        self.length = length

        # Member cosines with global axis
        cx = dx / length
        cy = dy / length
        cz = dz / length

        self.cosine_x = cx
        self.cosine_y = cy
        self.cosine_z = cz

        self.direction_cosine_matrix = self.get_direction_cosine_matrix()
        self.transformation_matrix = analysis.get_transformation_matrix(self)

        self.distributed_loads: list[DistributedLoadOnMember] = []
        self.thermal_loads: list[ThermalLoadOnMember] = []
        self.point_loads: list[PointLoadOnMember] = []

        self.generated_nodes: list[Node] = []
        self.generated_elements: list[Element1D] = []

        self.x_user_defined_nodes: npt.NDArray[np.float64] = np.array(
            [0.0, self.length]
        )
        self.x_discontinuities: npt.NDArray[np.float64] = np.array([0.0, self.length])

        self.results = Member1DResults(self)

    def __repr__(self) -> str:
        """Return a string representation of Member1D object."""
        node_labels = [node.label for node in self.nodes]
        hinge_descriptions = [hinge for hinge in [self.hinge_start, self.hinge_end]]
        aux_vector = ", ".join(
            f"{component:.2f}" for component in self.auxiliary_vector_xy_plane
        )
        return (
            f"{self.__class__.__name__}("
            f"label='{self.label}', "
            f"element_type='{self.element_type}', "
            f"nodes={node_labels}, "
            f"section='{self.section.label}', "
            f"length={self.length:.2f}, "
            f"hinges={hinge_descriptions}, "
            f"auxiliary_vector_xy_plane=[{aux_vector}])"
        )

    @property
    def x_local(self) -> npt.NDArray[np.float64]:
        """Return the x-coordinates along the local x-axis."""
        return np.concatenate(
            [
                element.x_start + element.sampling_points
                for element in self.generated_elements
            ]
        )

    def get_direction_cosine_matrix(self) -> npt.NDArray[np.float64]:
        """
        Return the direction cosine matrix representing the local axis of a member.

        This method calculates the local coordinate system vectors (x, y, z) for the member
        based on its nodal coordinates and the auxiliary vector. The local x-axis is aligned
        with the member axis, and the y and z-axes are perpendicular to it. The y-axis is
        determined by the cross product of the auxiliary vector and the x-axis, while the
        z-axis is the cross product of the x and y-axes. These vectors define the orientation
        of the member in 3D space and are normalized to unit vectors.

        :return: A 3x3 matrix containing the local coordinate system vectors [x, y, z] for
                 the member, where each vector is a row of the matrix.
        """
        # Get nodal coordinates
        xi, yi, zi = self.nodes[0].coords
        xf, yf, zf = self.nodes[-1].coords

        # Direction cosine for the local x-axis
        x = np.array([xf - xi, yf - yi, zf - zi])
        x = x / np.linalg.norm(x)

        # Direction cosine for the local z-axis
        z = cross(x, self.auxiliary_vector_xy_plane)
        z = z / np.linalg.norm(z)

        # Direction cosine for the local y-axis
        y = cross(z, x)

        return np.array([x, y, z])

    def _add_x_discontinuity(
        self,
        x: float,
        coordinate_definition: str | CoordinateDefinition = CoordinateDefinition.RELATIVE,
    ) -> float:
        """
        Helper method to append an x value to the x_discontinuities array if it's not already present within a tolerance.

        :param x: The x value to be added to the discontinuities array.
        :param coordinate_definition: Defines how the position 'x' is interpreted, either
                                        as 'relative' to the member's length or as an 'absolute'.
        :return: The exact x value that was added to the discontinuities array.
        """
        if coordinate_definition == CoordinateDefinition.RELATIVE:
            x_interpreted = x * self.length
        elif coordinate_definition == CoordinateDefinition.ABSOLUTE:
            x_interpreted = x
        else:
            raise ValueError(
                f"Unknown coordinate definition: '{coordinate_definition}.'"
                f"Valid options are: {COORDINATE_DEFINITIONS}."
            )

        # Validate that x_interpreted is withing the member's interval with tolerance
        if not (-self.TOLERANCE <= x_interpreted <= self.length + self.TOLERANCE):
            raise ValueError(
                f"Position of the x is outside the beam interval: [{0, self.length}], x: '{x_interpreted}'."
            )

        # Clamp x_interpreted within [0.0, self.length] if it's within tolerance
        if np.isclose(x_interpreted, 0.0, atol=self.TOLERANCE):
            x_interpreted = 0.0
        elif np.isclose(x_interpreted, self.length, atol=self.TOLERANCE):
            x_interpreted = self.length

        if not np.isclose(self.x_discontinuities, x_interpreted, atol=self.TOLERANCE).any():
            self.x_discontinuities = np.append(self.x_discontinuities, x_interpreted)

        return x_interpreted

    def define_sections(self, sections: dict[tuple[float, float], Section]) -> None:
        """
        Define sections along the member's length.

        This method allows the user to define multiple sections along the member's length,
        each with its own properties. The sections are defined by specifying the start and end
        positions along the member's length where the section applies, as well as the
        :class:`Section` object that defines the properties of the section.

        :param sections: A dictionary mapping tuples of start and end positions to :class:`Section` objects.
        """
        # Extract original start and end positions
        original_keys = list(sections.keys())
        original_sections = list(sections.values())

        original_x_start = original_keys[0][0]
        original_x_end = original_keys[-1][1]

        # Validate that the sections cover the entire member length
        if not np.isclose(original_x_start, 0.0, atol=self.TOLERANCE):
            raise ValueError("The first section must start at 'x=0.0'")
        if not np.isclose(original_x_end, self.length, atol=self.TOLERANCE):
            raise ValueError(f"The last section must end at the member's length, 'x={self.length}'")

        # Initialize new dictionary that hold updated sections with exact x values
        updated_sections = {}

        # Iterate over the original sections and update the start and end positions
        for (start, end), section in zip(original_keys, original_sections):
            exact_start = self._add_x_discontinuity(x=start, coordinate_definition=CoordinateDefinition.ABSOLUTE)
            exact_end = self._add_x_discontinuity(x=end, coordinate_definition=CoordinateDefinition.ABSOLUTE)

            updated_sections[(exact_start, exact_end)] = section

        # Assign updated sections to the member
        self.sections = updated_sections
        self.section = None

        # Sort the discontinuities
        self.x_discontinuities = np.unique(self.x_discontinuities)

    def get_section(self, x: float) -> Section:
        """
        Return the section at a specified position along the member.

        :param x: The position along the member's length.
        """
        if self.section and self.sections is None:
            return self.section

        elif self.sections and self.section is None:
            for (start, end), sec in self.sections.items():
                if start - self.TOLERANCE <= x <= end + self.TOLERANCE:
                    return sec
            else:
                # Section was not found
                raise ValueError(f"Section at 'x={x}' does not belong to any section.")

        else:
            raise ValueError("Sections are not defined correctly.")

    def _get_x_local(self, node: Node) -> float:
        """
        Calculate the local x-coordinate of a node by projecting it's global coordinates onto the member's local axis.

        :param node: Node for which to calculate the local x-coordinate.
        :return: The local x-coordinate of the node.
        """
        vector = np.array(node.coords) - np.array(self.nodes[0].coords)
        local_x_unit_axis = self.direction_cosine_matrix[0]
        return np.dot(vector, local_x_unit_axis)

    def _sort_nodes(self) -> None:
        """
        Sort the member's nodes based on their local x-coordinates.
        """
        if len(self.nodes) < 2:
            # No internal nodes to sort
            return

        # Extract internal nodes
        internal_nodes = self.nodes[1:-1]

        # Sort them based on x_local
        internal_nodes_sorted = sorted(
            internal_nodes, key=lambda node: self._get_x_local(node)
        )

        # Reconstruct the nodes list
        self.nodes = [self.nodes[0]] + internal_nodes_sorted + [self.nodes[-1]]

    def add_node(
        self,
        label: str,
        x: float,
        fixity: list[str] | tuple[str, ...] = ("free",) * 6,
        spring_stiffness: list[float] | tuple[float, ...] = (0.0,) * 6,
        coordinate_definition: (
            str | CoordinateDefinition
        ) = CoordinateDefinition.RELATIVE,
    ) -> Node:
        """
        Add a node to the member at a specified location.

        This method creates and adds a :class:`Node` object representing a point force
        applied to the :class:`Member1D`. The force is specified by its components, the position along
        the member where it is applied, the :class:`LoadCase` it belongs to, and its coordinate system.

        The position of the force can be defined relative to the member's length or as an
        absolute value, based on the ``coordinate_definition`` parameter. The method also records
        the position of the force as a discontinuity in the member's load distribution.

        :param label: A user-defined label for the node.
        :param x: The position along the member's length where the force is applied.
                  This can be a relative value (0 to 1) or an absolute value.
        :param fixity: A list specifying the essential boundary conditions for each degree of freedom (DoF)
                       at the node. Conditions can be 'free', 'fixed', or 'spring'.
        :param spring_stiffness: A list of spring stiffness coefficients applicable when the fixity is set
                                 to 'spring' for corresponding DoFs. The list should follow the order
                                 [kx, ky, kz, krx, kry, krz], representing translational and rotational spring
                                 stiffness values in the X, Y, and Z directions, respectively.`.
        :param coordinate_definition: Defines how the position 'x' is interpreted, either
                                      as 'relative' to the member's length or as an 'absolute'
                                      value. Can be an instance of :class:`CoordinateDefinition`.
                                      Default to ``RELATIVE``.
        """
        fixities = [SupportFixity(fix) for fix in fixity]
        spring_stiff = [stiff for stiff in spring_stiffness]
        coord_def = CoordinateDefinition(coordinate_definition)

        x_exact = self._add_x_discontinuity(x=x, coordinate_definition=coord_def)

        coords = self.nodes[0].coords + self.direction_cosine_matrix.T @ np.array(
            [x_exact, 0, 0]
        )

        new_node = Node(
            label=label,
            coords=coords,
            fixity=fixities,
            spring_stiffness=spring_stiff,
            is_user_defined=True,
        )

        self.x_user_defined_nodes = np.sort(np.append(self.x_user_defined_nodes, x_exact))
        self.nodes.insert(1, new_node)
        self._sort_nodes()

        return new_node

    def add_point_load(
        self,
        load_components: list[float] | npt.NDArray[np.float64],
        load_case: LoadCase,
        x: float,
        coordinate_system: str | LoadCoordinateSystem = LoadCoordinateSystem.GLOBAL,
        coordinate_definition: (
            str | CoordinateDefinition
        ) = CoordinateDefinition.RELATIVE,
    ) -> None:
        """
        Add a point load to the member at a specified location.

        This method creates and adds a :class:`PointLoadOnMember` object representing a point load
        applied to the :class:`Member1D`. The load is specified by its components, the position along
        the member where it is applied, the :class:`LoadCase` it belongs to, and its coordinate system.

        The position of the force can be defined relative to the member's length or as an
        absolute value, based on the ``coordinate_definition`` parameter. The method also records
        the position of the force as a discontinuity in the member's load distribution.

        :param load_components: The components of the point force in the format [Fx, Fy, Fz, Mx, My, Mz],
                                representing the force in the x, y, and z directions.
        :param load_case: The :class:`LoadCase` to which this point force belongs.
        :param x: The position along the member's length where the force is applied.
                  This can be a relative value (0 to 1) or an absolute value.
        :param coordinate_system: The coordinate system in which the force components are
                                  defined. Can be 'global' or 'local', or an instance
                                  of :class:`LoadCoordinateSystem`. Default to ``GLOBAL``.
        :param coordinate_definition: Defines how the position 'x' is interpreted, either
                                      as 'relative' to the member's length or as an 'absolute'
                                      value. Can be an instance of :class:`CoordinateDefinition`.
                                      Default to ``RELATIVE``.
        """
        x_exact = self._add_x_discontinuity(x=x, coordinate_definition=coordinate_definition)

        new_load = PointLoadOnMember(
            member=self,
            load_components=load_components,
            x=x_exact,
            load_case=load_case,
            coordinate_system=coordinate_system,
        )

        self.point_loads.append(new_load)

    def add_distributed_load(
        self,
        load_components: list[float] | npt.NDArray[np.float64],
        load_case: LoadCase,
        x_start: float = 0.0,
        x_end: float = 1.0,
        coordinate_system: str | LoadCoordinateSystem = LoadCoordinateSystem.GLOBAL,
        location: str | DistributedLoadLocation = DistributedLoadLocation.LENGTH,
        coordinate_definition: (
            str | CoordinateDefinition
        ) = CoordinateDefinition.RELATIVE,
    ) -> None:
        """
        Add a distributed load over a specified segment of the structural member.

        This method creates and adds a :class:`DistributedLoadOnMember` object, representing a
        distributed load that varies along a segment of the member. The load is defined by
        its components, the start and end positions of the load distribution, the :class:`LoadCase`
        it belongs to, and its coordinate system.

        :param load_components: The components of the distributed load in format [fx1, fy1, fz1, fx2, fy2, fz2].
        :param load_case: The :class:`LoadCase` to which this point force belongs.
        :param x_start: The start position of the load distribution along the member's
                        length. Defaults to 0. (start of the member).
        :param x_end: The end position of the load distribution along the member's
                      length. Defaults to 1. (end of the member).
        :param coordinate_system: The coordinate system in which the force components are
                                  defined. Can be 'global' or 'local', or an instance
                                  of :class:`LoadCoordinateSystem`. Default to ``GLOBAL``.
        :param location: Specifies whether the load is acting directly on an inclined :class:`Member1D`,
                         or on the projection into the global coordinate system.
                         For 'local' coordinate_system, the only option is 'length'.
                         For 'global' coordinate_system, the options are 'length' and 'projection'.
                         Default to ``LENGTH``.
        :param coordinate_definition: Defines how the position 'x' is interpreted, either
                                      as 'relative' to the member's length or as an 'absolute'
                                      value. Can be an instance of :class:`CoordinateDefinition`.
                                      Default to ``RELATIVE``.
        """
        x_exact_start = self._add_x_discontinuity(x=x_start, coordinate_definition=coordinate_definition)
        x_exact_end = self._add_x_discontinuity(x=x_end, coordinate_definition=coordinate_definition)

        new_udl = DistributedLoadOnMember(
            member=self,
            load_components=load_components,
            x_start=x_exact_start,
            x_end=x_exact_end,
            load_case=load_case,
            coordinate_system=coordinate_system,
            location=location,
        )

        self.distributed_loads.append(new_udl)

    def add_thermal_load(
        self,
        temperature_gradients: list[float] | npt.NDArray[np.float64],
        load_case: LoadCase,
        x_start: float = 0.0,
        x_end: float = 1.0,
        coordinate_definition: (
            str | CoordinateDefinition
        ) = CoordinateDefinition.RELATIVE,
    ) -> None:
        """
        Add a thermal load over a specified segment of the structural member.

        This method creates a :class:`ThermalLoadOnMember` object representing a thermal load,
        which is defined by temperature gradients along the member's local axes.
        The load is applied over a specified segment of the member, defined by the start and
        end positions.

        :param temperature_gradients: A list of the temperature gradients relative to local axis [tgx, tgy, tgz].
        :param load_case: The :class:`LoadCase` to which this point force belongs.
        :param x_start: The start position of the load distribution along the member's
                        length. Defaults to 0. (start of the member).
        :param x_end: The end position of the load distribution along the member's
                      length. Defaults to 1. (end of the member).
        :param coordinate_definition: Defines how the position 'x' is interpreted, either
                                      as 'relative' to the member's length or as an 'absolute'
                                      value. Can be an instance of :class:`CoordinateDefinition`.
                                      Default to ``RELATIVE``.
        """
        x_exact_start = self._add_x_discontinuity(x=x_start, coordinate_definition=coordinate_definition)
        x_exact_end = self._add_x_discontinuity(x=x_end, coordinate_definition=coordinate_definition)

        new_thermal_load = ThermalLoadOnMember(
            member=self,
            temperature_gradients=temperature_gradients,
            x_start=x_exact_start,
            x_end=x_exact_end,
            load_case=load_case,
        )

        self.thermal_loads.append(new_thermal_load)

    def discretize(self, model: Model, max_element_length: None | float = None) -> None:
        """
        Perform the discretization of the member based on its load discontinuities.

        This method is a key step in preparing the member for structural analysis. It starts
        by sorting and identifying unique discontinuities along the member's length. These
        discontinuities are used to generate intermediate nodes and elements to accurately
        represent the effects of point and distributed loads.

        The method then assigns point and distributed loads to these generated nodes and
        elements. Finally, it updates the model with these new nodes and elements,
        extending the model's global node and element lists.

        :param model: A reference to the :class:`Model` to which the member belongs.
        :param max_element_length: The maximum length of the finite elements to be used
                                   for discretization.
                                   If set to `None`, members will be divided only
                                   in discontinuities. Default is `None`.
        """
        if max_element_length:
            n_nodes = int(np.ceil(self.length / max_element_length)) + 1
            x_values = np.linspace(0, self.length, n_nodes)
            for xi in x_values[1:-1]:
                self._add_x_discontinuity(xi, CoordinateDefinition.ABSOLUTE)

        self.x_discontinuities = np.unique(self.x_discontinuities)

        self.generate_nodes()
        self.generate_elements()
        self.assign_point_loads()
        self.assign_distributed_loads()
        self.assign_thermal_loads()
        model.nodes.update(self.generated_nodes)
        model.elements.update(self.generated_elements)

    def generate_nodes(self) -> None:
        """
        Generate intermediate nodes at the locations of discontinuities along the member.

        This method creates new :class:`Node` at each discontinuity position along the member's
        local x-axis. The first and last nodes correspond to the existing start and end nodes
        of the member.
        """
        i = 0
        for x in self.x_discontinuities:
            if x in self.x_user_defined_nodes:
                idx = np.where(x == self.x_user_defined_nodes)[0][0]
                node = self.nodes[idx]
            else:
                coords = self.nodes[
                    0
                ].coords + self.direction_cosine_matrix.T @ np.array([x, 0, 0])
                node = Node(
                    f"{self.label}({i + 1})",
                    coords,
                    [SupportFixity(SupportFixity.FREE_DOF)] * 6,
                    [0.0] * 6,
                )
                i += 1

            self.generated_nodes.append(node)

    def generate_elements(self) -> None:
        """
        Generate elements between each pair of adjacent nodes along the member.

        This method is responsible for creating new elements (subdivisions of the original
        member) between each pair of adjacent nodes generated by `generate_nodes`. These
        sub-elements help to accurately represent and analyze the structural behavior in
        response to loads, particularly at points of discontinuity.

        The start and end hinges for each element are determined based on their positions:
        the first element gets the original member's start hinge setting, the last element
        gets the end hinge setting, and all intermediate elements are set to continuous.
        """
        for i, (node_1, node_2, x_1, x_2) in enumerate(
            zip(
                self.generated_nodes[:-1],
                self.generated_nodes[1:],
                self.x_discontinuities[:-1],
                self.x_discontinuities[1:],
            )
        ):
            hng = [BeamConnection(BeamConnection.CONTINUOUS_END)] * 2
            if i == 0:
                hng[0] = self.hinge_start
            if i == len(self.x_discontinuities) - 2:
                hng[1] = self.hinge_end

            section = self.section

            if self.sections:
                for (start, end), sec in self.sections.items():
                    if start <= x_1 < x_2 <= end:
                        section = sec
                        break
                else:
                    # Section was not found
                    raise ValueError(
                        f"Interval [{x_1, x_2}] does not belong to any section."
                    )

            new_element = Element1D(
                member=self,
                nodes=[node_1, node_2],
                section=section,
                x_start=x_1,
                x_end=x_2,
                hinges=hng,
            )
            self.generated_elements.append(new_element)

    def assign_point_loads(self) -> None:
        """
        Assign point loads (forces and moments), to the generated nodes of the member.

        This method iterates through each point load defined for the member and assigns
        it to the appropriate generated node based on the load's position.

        The method checks if a nodal load already exists for each node in the relevant load
        case. If not, it initializes a new :class:`NodalLoad` object. It then adds the load
        components from the point load to this nodal load.
        """
        # assign point loads (forces and moments) to generated nodes
        for point_load in self.point_loads:
            idx = np.where(self.x_discontinuities == point_load.x)[0][0]

            node = self.generated_nodes[idx]

            # Check if this node already has an associated NodalLoad in the given LoadCase
            if not point_load.load_case.nodal_loads.get(node):
                # If not, create a new NodalLoad instance for this node
                point_load.load_case.nodal_loads[node] = NodalLoad()

            nodal_load = point_load.load_case.nodal_loads[node]

            # Update the NodalLoad components for this node in the given LoadCase

            nodal_load.load_components += point_load.components_global

    def assign_distributed_loads(self) -> None:
        """
        Assign distributed loads to the appropriate elements generated along the member.

        This method iterates over each distributed load defined for the member. For each
        distributed load, it identifies the elements that fall within
        the load's span, based on the start and end positions of the load.

        For each relevant element, the method checks if a distributed load already exists
        for that element in the specified load case. If not, it initializes a new
        :class:`DistributedLoad` object for that element. It then calculates the
        distributed load values at the start and end of the element and adds these
        values to the existing load components.
        """
        for load in self.distributed_loads:
            mask = (load.x_start <= self.x_discontinuities[:-1]) * (
                self.x_discontinuities[1:] <= load.x_end
            )

            elements: list[Element1D] = np.array(self.generated_elements)[mask].tolist()

            for element in elements:
                # Check if this element already has an associated DistributedLoad in the given LoadCase
                if not load.load_case.element_distributed_loads.get(element):
                    # If not, create a new DistributedLoad instance for this element
                    load.load_case.element_distributed_loads[element] = DistributedLoad(
                        element
                    )

                load_components = np.zeros(6, dtype=np.float64)
                load_components[:3] = load.get_load_values_at_location(element.x_start)
                load_components[3:] = load.get_load_values_at_location(element.x_end)

                # Update the DistributedLoad components for this element in the given LoadCase
                load.load_case.element_distributed_loads[
                    element
                ].components_local += load_components

    def assign_thermal_loads(self) -> None:
        """
        Assign thermal loads to the appropriate elements generated along the member.

        This method iterates over each thermal load defined for the member. For each
        thermal load, it identifies the elements that fall within
        the load's span, based on the start and end positions of the load.

        For each relevant element, the method checks if a thermal load already exists
        for that element in the specified load case. If not, it initializes a new
        :class:`ThermalLoad` object for that element. It then adds the
        temperature gradients values to the existing temperature gradients.
        """
        for load in self.thermal_loads:
            mask = (load.x_start <= self.x_discontinuities[:-1]) * (
                self.x_discontinuities[1:] <= load.x_end
            )

            elements: list[Element1D] = np.array(self.generated_elements)[mask].tolist()

            for element in elements:
                # Check if this element already has an associated ThermalLoad in the given LoadCase
                if not load.load_case.element_thermal_loads.get(element):
                    # If not, create a new DistributedLoad instance for this element
                    load.load_case.element_thermal_loads[element] = ThermalLoad(element)

                # Update the ThermalLoad components for this element in the given LoadCase
                load.load_case.element_thermal_loads[
                    element
                ].temperature_gradients += load.temperature_gradients
