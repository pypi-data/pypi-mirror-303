
import enum
from typing import ( 
    List,
    Tuple
)

from .fcscore_core import *
from .fcscore_geometry import *

class ElementDimension(enum.Enum):
	ZERO: ElementDimension
	ONE: ElementDimension
	TWO: ElementDimension
	THREE: ElementDimension

class SpecificElementType(enum.Enum):
	"""
	Specific element types that follow the GMSH convention.
	"""
	LINE_2NODE = 1
	TRIANGLE_3NODE = 2
	QUADRANGLE_4NODE = 3
	TETRAHEDRON_4NODE = 4
	HEXAHEDRON_8NODE = 5
	PRISM_6NODE = 6
	PYRAMID_5NODE = 7
	LINE_3NODE_SECOND_ORDER = 8
	TRIANGLE_6NODE_SECOND_ORDER = 9
	QUADRANGLE_9NODE_SECOND_ORDER = 10
	TETRAHEDRON_10NODE_SECOND_ORDER = 11
	HEXAHEDRON_27NODE_SECOND_ORDER = 12
	PRISM_18NODE_SECOND_ORDER = 13
	PYRAMID_14NODE_SECOND_ORDER = 14
	POINT_1NODE = 15
	QUADRANGLE_8NODE_SECOND_ORDER = 16
	HEXAHEDRON_20NODE = 17
	PRISM_15NODE_SECOND_ORDER = 18

class MeshElementOrder(enum.Enum):
	FIRST: MeshElementOrder
	SECOND: MeshElementOrder
      
class Target2DElementType(enum.Enum):
    """
	Available easy-to-understand 2D element type choice for meshing.
	"""
    TRIA: Target2DElementType
    QUAD: Target2DElementType

class Mesh2DAlgorithmChoice(enum.Enum):
	MESH_ADAPT: Mesh2DAlgorithmChoice
	DELAUNAY: Mesh2DAlgorithmChoice
	FRONTAL: Mesh2DAlgorithmChoice
	BAMG: Mesh2DAlgorithmChoice
	DELAUNAY_QUAD: Mesh2DAlgorithmChoice
      
class Target3DElementType(enum.Enum):
    """
	Available easy-to-understand 3D element type choice for meshing.
	"""
    TETRA: Target3DElementType
    HEXA: Target3DElementType
	
class Mesh3DAlgorithmChoice(enum.Enum):
	BASE_TETRAHEDRALIZATION: Mesh3DAlgorithmChoice

class Mesh2DSettings:
    def __init__(self,
                 element_size: float, 
				 element_type: Target2DElementType, 
				 algorithm_choice: Mesh2DAlgorithmChoice, 
				 element_order: MeshElementOrder):
        """
        Initializes the Mesh2DSettings with the given parameters.

        :param element_size: Size of the elements.
        :param element_type: Type of the 2D elements.
        :param algorithm_choice: Choice of 2D mesh algorithm.
        :param element_order: Order of the elements.
        """
        ...

    def set_element_size(self, element_size: float):
        """
        Sets the size of the elements.

        :param element_size: Size of the elements.
        """
        ...

    def set_element_type(self, element_type: Target2DElementType):
        """
        Sets the type of the 2D elements.

        :param element_type: Type of the 2D elements.
        """
        ...

    def set_element_order(self, element_order: MeshElementOrder):
        """
        Sets the order of the elements.

        :param element_order: Order of the elements.
        """
        ...

    def get_element_size(self) -> float:
        """
        Gets the size of the elements.

        :return: Size of the elements.
        """
        ...

    def get_element_type(self) -> Target2DElementType:
        """
        Gets the type of the 2D elements.

        :return: Type of the 2D elements.
        """
        ...

    def get_element_order(self) -> MeshElementOrder:
        """
        Gets the order of the elements.

        :return: Order of the elements.
        """
        ...

    def get_mesh_algorithm(self) -> Mesh2DAlgorithmChoice:
        """
        Gets the choice of 2D mesh algorithm.

        :return: Choice of 2D mesh algorithm.
        """
        ...

class Mesh3DSettings:
    def __init__(self, 
                 element_size: float, 
                 element_type: Target3DElementType, 
                 algorithm_choice: Mesh3DAlgorithmChoice, 
                 element_order: MeshElementOrder):
        """
        Initializes the Mesh3DSettings with the given parameters.

        :param element_size: Size of the elements.
        :param element_type: Type of the 3D elements.
        :param algorithm_choice: Choice of 3D mesh algorithm.
        :param element_order: Order of the elements.
        """
        ...

    def set_element_size(self, element_size: float):
        """
        Sets the size of the elements.

        :param element_size: Size of the elements.
        """
        ...

    def set_element_type(self, element_type: Target3DElementType):
        """
        Sets the type of the 3D elements.

        :param element_type: Type of the 3D elements.
        """
        ...

    def set_element_order(self, element_order: MeshElementOrder):
        """
        Sets the order of the elements.

        :param element_order: Order of the elements.
        """
        ...

    def get_element_size(self) -> float:
        """
        Gets the size of the elements.

        :return: Size of the elements.
        """
        ...

    def get_element_type(self) -> Target3DElementType:
        """
        Gets the type of the 3D elements.

        :return: Type of the 3D elements.
        """
        ...

    def get_element_order(self) -> MeshElementOrder:
        """
        Gets the order of the elements.

        :return: Order of the elements.
        """
        ...

    def get_mesh_algorithm(self) -> Mesh3DAlgorithmChoice:
        """
        Gets the choice of 3D mesh algorithm.

        :return: Choice of 3D mesh algorithm.
        """
        ...

class MeshFactory:
    def __init__(self): ...
    @staticmethod
    def set_export_directory(export_path: str): ...
    @staticmethod
    def get_export_directory() -> str: ...
    def create_2d_mesh(self, geom_object_face: GEOM_Object, mesh_settings: Mesh2DSettings) -> Mesh: ...
    def create_2d_mesh_fixed_boundary(self, geom_object_face: GEOM_Object, mesh_settings: Mesh2DSettings) -> Mesh: ...

class Mesher3D:
	@staticmethod
	def generate_3d_mesh(boundary_element_ids: set, mesh_settings: Mesh3DSettings) -> Mesh: ...
	
class MeshReferenceType(enum.Enum):
	UNDETERMINED: MeshReferenceType
	ELEMENT_SET: MeshReferenceType
	NODE_SET: MeshReferenceType


class ElementReferences:
     ElementId: int
     ComponentMeshId: int
     ElementSetStorageID: int
     WasFound: bool

class Node:
    def __init__(self, node_id: int, position: XYZ):
        """
        Initializes the Node with the given ID and position.

        :param node_id: ID of the node.
        :param position: Position of the node.
        """

    NodeId: int
    Position: XYZ


class Element:
    def __init__(self, element_id: int, nodes: list[Node], element_type: SpecificElementType):
        """
        Initializes the Element with the given ID, nodes, and element type.

        :param element_id: ID of the element.
        :param nodes: List of nodes in the element.
        :param element_type: Type of the element.
        """

    ElementId: int
    NodeIDs: list[int]
    ElementReferencesSnapshot: ElementReferences
    ElementType: SpecificElementType

class MeshFileFormat(enum.Enum):
	MSH: MeshFileFormat
	MED: MeshFileFormat
	STL: MeshFileFormat
	INP: MeshFileFormat
	
class Mesh:
    def __init__(self, open_new_mesh_model: bool = False):
        """
        Initializes the Mesh class, optionally opening a new mesh model.
        :param open_new_mesh_model: A boolean to specify if a new mesh model should be opened.
        """
        ...

    def set_file_name(self, file_name: str) -> None:
        """
        Sets the name of the mesh file.
        :param file_name: The file name to set.
        """
        ...

    def get_file_name(self) -> str:
        """
        Retrieves the name of the mesh file.
        :return: The name of the mesh file as a string.
        """
        ...

    def load_mesh(self, mesh_directory: str, mesh_file_format: MeshFileFormat) -> bool:
        """
        Loads a mesh from the specified directory and file format.
        :param mesh_directory: The directory where the mesh file is located.
        :param mesh_file_format: The format of the mesh file.
        :return: True if the mesh is successfully loaded, otherwise False.
        """
        ...

    def write_mesh(self, export_directory: str, mesh_file_format: MeshFileFormat) -> str:
        """
        Writes the mesh to the specified directory in the given file format.
        :param export_directory: The directory where the mesh will be exported.
        :param mesh_file_format: The format in which the mesh will be exported.
        :return: The path of the exported mesh file as a string.
        """
        ...

    def get_source_mesh_path(self) -> str:
        """
        Retrieves the path of the source mesh.
        :return: The source mesh path as a string.
        """
        ...

    def get_source_mesh_format(self) -> MeshFileFormat:
        """
        Retrieves the format of the source mesh.
        :return: The source mesh format.
        """
        ...
        
    def get_all_elements(self) -> List[Element]:
        """
        :return: All elements that comprise the mesh.
        """
        ...

    def get_node_definition(self, node_id: int) -> Node:
        """
        Retrieves the definition of a specific node.
        :param node_id: The ID of the node.
        :return: The definition of the node.
        """
        ...

    def get_element_definition(self, element_id: int, compute_references: bool) -> Element:
        """
        Retrieves the definition of a specific element.
        :param element_id: The ID of the element.
        :param compute_references: If set to true, will also compute what component mesh-es reference it.
        This only makes sense for master mesh queries.
        :return: The definition of the element.
        """
        ...

    def get_elements_associated_with_node(self, node_id: int) -> List[Element]:
        """
        Retrieves the elements associated with a given node ID.
        :param node_id: The ID of the node.
        :return: A list of elements associated with the node.
        """
        ...

    def get_elements_near_position(self, position: XYZ) -> List[Element]:
        """
        Retrieves the elements that are near a specific position in space.
        :param position: The position in space as an XYZ object.
        :return: A list of elements near the position.
        """
        ...

    def get_boundary_node_ids(self, element_ids: List[int]) -> List[int]:
        """
        Retrieves the boundary node IDs for a given list of element IDs.
        :param element_ids: A list of element IDs.
        :return: A list of boundary node IDs.
        """
        ...
        
    def get_bounding_wires_for_elements(self, element_ids: List[int]) -> List[GEOM_Object]:
        """
        Constructs wires that bound the element. If an empty list is returned it means the mesh 
        is enclosed completely.
        
        :param element_ids: A list of element IDs.
        :return: A list of closed wires that bound the mesh.
        """
        ...

	
class MasterMesh:
    @staticmethod
    def run_local_debug_viewer() -> None:
        """
        Only works locally in a development environment. Spawns a simple UI,
        to quick check the mesh. 
        """
        ...

    @staticmethod
    def is_node_orphan(node_id: int) -> bool:
        """
        Places a standalone mesh and inserts it into the master mesh.
        :return: True, if the node is orphan.
        """
        ...

    @staticmethod
    def create_node_set(comp_id: int, node_ids: set[int]) -> NodeSet:
        """
        Constructs a node set from the provided node IDs.

        :param comp_id: Unique identifier of the mesh instance.
        :param node_ids: Element IDs that we need to group together.
        :return: Pointer to newly constructed node set.
        """
        ...

    @staticmethod
    def create_element_set(comp_id: int, element_ids: set[int]) -> ElementSet:
        """
        Constructs an element set from the provided element IDs.

        :param comp_id: Unique identifier of the mesh instance.
        :param element_ids: Element IDs that we need to group together.
        :return: Pointer to newly constructed element set.
        """
        ...

    @staticmethod
    def insert_mesh_reference(mesh_reference: MeshReference) -> bool:
        """
        Inserts a mesh reference into the master mesh.

        :param mesh_reference: Reference mesh to be inserted.
        :return: True if insertion was successful.
        """
        ...

    @staticmethod
    def delete_mesh_set(comp_id: int) -> bool:
        """
        Deletes the mesh reference for a given component ID.

        :param comp_id: Unique identifier of the mesh reference.
        :return: True if deletion was successful.
        """
        ...

    @staticmethod
    def add_node(xyz: XYZ) -> Node:
        """
        Adds a new node to the master mesh.

        :param XYZ: position of the node to be placed
        :return: Newly placed Node's definition
        """
        ...

    @staticmethod
    def get_all_elements() -> List[Element]:
        """
        :return: All element definitions that comprise the mesh.
        """
        ...
        
    @staticmethod
    def get_node_definition(node_id: int) -> Node: ...
        
    @staticmethod
    def get_element_definition(element_id: int, compute_refences: bool) -> Element: ...
    
    @staticmethod
    def get_elements_associated_with_node(node_id: int) -> List[Element]:
        """
        Retrieves the elements associated with a given node ID.
        :param node_id: The ID of the node.
        :return: A list of elements associated with the node.
        """
        ...

    @staticmethod
    def get_elements_near_position(position: XYZ) -> List[Element]:
        """
        Retrieves the elements that are near a specific position in space.
        :param position: The position in space as an XYZ object.
        :return: A list of elements near the position.
        """
        ...

    @staticmethod
    def get_boundary_node_ids(element_ids: List[int]) -> List[int]:
        """
        Retrieves the boundary node IDs for a given list of element IDs.
        :param element_ids: A list of element IDs.
        :return: A list of boundary node IDs.
        """
        ...
        
    @staticmethod
    def get_bounding_wires_for_elements(element_ids: List[int]) -> List[GEOM_Object]:
        """
        Constructs wires that bound the element. If an empty list is returned it means the mesh 
        is enclosed completely.
        
        :param element_ids: A list of element IDs.
        :return: A list of closed wires that bound the mesh.
        """
        ...
        
    @staticmethod
    def get_boundary_node_pairs(element_ids: List[int]) -> List[Tuple[int,int]]:
        """
        Retrieves the boundary node IDs as pairs that represent free edges for a given 
        list of element IDs.
        :param element_ids: A list of element IDs.
        :return: A list of boundary node IDs pairs.
        """
        ...

    @staticmethod
    def delete_nodes(
          node_ids: set[int],
          removed_associated_elements: set[int],
          removed_orphaned_node_ids: set[int]) -> bool:
        """
        Deletes nodes from the master mesh.

        :param mesh_component_id: Helper ID of the mesh component from which nodes were deleted.
        :param node_ids: Node IDs to be deleted.
        :param removed_associated_elements: Set to store IDs of removed associated elements.
        :param removed_orphaned_node_ids: Populates this empty list with the orphaned node IDs.
        :return: True if deletion was successful.
        """
        ...

    @staticmethod
    def add_element(mesh_component_id: int, spec_elem_type: SpecificElementType, node_ids: list[int]) -> Element:
        """
        Adds an element to the master mesh.

        :param mesh_component_id: The mesh component that was active when the element was created.
        :param spec_elem_type: Specific element type for the element.
        :param node_ids: Collection of node IDs used to construct the element.
        :return: Newly placed element information
        """
        ...

    @staticmethod
    def delete_elements(
		  element_ids: set[int],
          removed_orphaned_ids: list[int]) -> bool:
        """
        Deletes elements from the master mesh.

        :param element_ids: Element IDs to be deleted.
        :param removed_orphaned_ids: Will populate this list with NodeIDs that were removed
        :return: True if deletion was successful.
        """
        ...

    @staticmethod
    def merge_nodes(
        slave_node_id: int, 
        master_node_id: int, 
        removed_element_ids: list[int], 
        remove_duplicates: bool
    ) -> list[Element]:
        """
        Merges the slave node with the master node. Optionally removes duplicates and modifies elements accordingly.

        :param slave_node_component_id: Component ID of the slave node.
        :param slave_node_id: ID of the slave node.
        :param master_node_component_id: Component ID of the master node.
        :param master_node_id: ID of the master node.
        :param removed_element_ids: List to store IDs of removed elements.
        :param remove_duplicates: Flag to indicate whether to remove duplicates.
        :return: List of added elements.
        """
        ...
        
    @staticmethod
    def merge_by_elements(
         selected_element_ids: List[int],
         tolerance: float,
         removed_element_ids: List[int],
         merge_same_element_nodes: bool = True) -> List[Element]:
        """
        Within tolerance, closest node pairs are found and are merged.

        :param selected_element_ids: IDs of the elements to whose nodes the merging will be applied.
        :param tolerance: The tolerance within which any two nodes need to be merged
        :param removed_element_ids: This list will be populated with element IDs that were removed.
        :param merge_same_element_nodes: By default, we may merge nodes of the same elements and thus
        degrading the element or completely removing it.
        :return: List of added elements.
        """

    @staticmethod
    def copypaste_cutpaste_elements_nodes(
        source_node_ids: set[int], 
        source_element_ids: set[int],
        target_component_id: int, 
        perform_cut_paste: bool
    ) -> tuple[list[Node], list[Element], list[int]]:
        """
        Reassigns elements and nodes from the source component to the target component.

        :param source_node_ids: Set of source node IDs.
        :param source_element_ids: Set of source element IDs.
        :param source_component_id: ID of the source component.
        :param target_component_id: ID of the target component.
        :param perform_cut_paste: Flag to indicate whether to perform cut-paste operation.
        :return: A tuple containing a list of new nodes, a list of new elements, 
            and a list of orphaned node IDs
        """
        ...

    @staticmethod
    def export_mesh_file(mesh_file_format: MeshFileFormat, mesh_component_id: int = -1) -> bool:
        """
        Exports a MED file with the sets defined there.

		:param mesh_file_format: The desired output format that we want to export the mesh as.
        :param mesh_component_id: If specified, writes out a mesh file for the corresponding component mesh ID.
        :return: True if the file export was successful.
        """
        ...
        
    @staticmethod
    def get_element_dimension_by_type(elem_type: SpecificElementType) -> int:
        """
        Returns the element dimension based on its type.
        :param: elem_type: A GMSH definition of an element type.
        """
        ...

class MeshReference:
	def get_component_id(self) -> int: ...
	def add_node_id(self, node_id: int) -> None: ...
	def add_element_id(self, element_id: int) -> None: ...
	def get_node_ids(self) -> set: ...
	def set_node_ids(self, node_ids: set) -> None: ...
	def get_element_ids(self) -> set: ...
	def set_element_ids(self, element_ids: set) -> None: ...
	def get_mesh_reference_type(self) -> MeshReferenceType: ...
	def modify_constituent_ids(self, 
							added_element_ids: set,
							removed_element_ids: set,
							added_node_ids: set,
							removed_node_ids: set) -> bool: ...

class ComponentMesh(Mesh):
    def write_mesh_asset_file(self) -> None: ...
    def get_component_mesh_id(self) -> int: ...
    def is_component_mesh_empty(self) -> bool: ...
    def get_elements_by_dimension(self, dimension: ElementDimension) -> ElementSet: ...


class ElementSet(MeshReference): ...
class NodeSet(MeshReference): ...