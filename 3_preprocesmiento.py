import meshpy.tet as tet
from scipy.sparse import lil_matrix

# PREPROCESAMIENTO
points, facets = [ ... ], [ ... ]  # Define puntos y caras
mesh_info = tet.MeshInfo()
mesh_info.set_points(points)
mesh_info.set_facets(facets)
mesh = tet.build(mesh_info)


# ENSAMBLADO DE MATRICES
K_global = lil_matrix((nodos_totales, nodos_totales))
# Suma las matrices locales de rigidez al K_global en los índices correctos
