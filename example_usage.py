from client import MeshProcessor

def main():
    processor = MeshProcessor()
    sample_obj = """
    v 0.0 0.0 0.0
    v 1.0 0.0 0.0
    v 1.0 1.0 0.0
    v 0.0 1.0 0.0
    f 1 2 3 4
    """
    res = processor.parse_obj(sample_obj)
    print("Mesh Processor Verification:")
    print(f"Parsed Vertices: {res['vertex_count']}")
    print(f"Triangles Created: {res['triangle_count']}")

if __name__ == "__main__":
    main()
