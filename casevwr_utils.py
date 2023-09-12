import trimesh
import zipfile
import io

def load_prep_from_file(my_file):
    mesh_3m = trimesh.load_mesh(my_file, file_type='stl')
    return mesh_3m

def load_prep_from_uploaded_zip(uploaded_file):
	stl_file_name = "PreparationScan.stl"
	with zipfile.ZipFile(uploaded_file, 'r') as zip_ref:
	    with zip_ref.open(stl_file_name) as file:
	        bytes_buffer = io.BytesIO(file.read())
	        mesh_3m = trimesh.load_mesh(bytes_buffer, file_type='stl')
	        return mesh_3m