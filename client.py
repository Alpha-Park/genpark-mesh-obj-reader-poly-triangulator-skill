"""3D Polygon Mesh Triangulation & OBJ Parsing Engine
100% Python Standard Library.
"""

class MeshProcessor:
    """Wavefront OBJ reader with polygon fan triangulation."""
    def parse_obj(self, obj_text):
        vertices = []
        faces = []
        for line in obj_text.strip().splitlines():
            parts = line.strip().split()
            if not parts:
                continue
            if parts[0] == "v":
                vertices.append([float(parts[1]), float(parts[2]), float(parts[3])])
            elif parts[0] == "f":
                idx = [int(p.split("/")[0]) - 1 for p in parts[1:]]
                for i in range(1, len(idx) - 1):
                    faces.append([idx[0], idx[i], idx[i + 1]])

        return {
            "vertex_count": len(vertices),
            "triangle_count": len(faces),
            "vertices": vertices[:10],
            "triangles": faces[:10]
        }
