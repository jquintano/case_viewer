import streamlit as st
import zipfile
from demo2_utils import *
from crowning2_utils import *
from casevwr_utils import *
from htmlTemplates import css, bot_template
import pyvista as pv
from stpyvista import stpyvista


# Function to handle zip file upload and processing
def upload_zip_file():
    uploaded_file = st.file_uploader("Upload a zip file", type=["stl"])

    if uploaded_file is not None:
        st.success("Zip file successfully uploaded!")

        # Add a submit button
        if st.button("Submit"):
        	mesh_prep_pv = load_prep_from_file(uploaded_file)
        	st.write(mesh_prep_pv)
        	return  mesh_prep_pv
        	

def main():
	st.set_page_config(page_title="Auto-Design Crown", page_icon=":tooth:")
	st.header('Auto-Design Crown :tooth:')

	with st.sidebar:
		uploaded_file = st.file_uploader("Upload a zip file", type=["stl"])
		if uploaded_file is not None:
			st.success("Zip file successfully uploaded!")
			if st.button("Submit"):
				# with st.spinner('Processing...'):
				# 	reader = pv.get_reader(uploaded_file)
				# 	mesh_prep_3m = reader.read()
					
				plotter = pv.Plotter(window_size=[400, 400])

				## Create a mesh with a cube
				mesh = pv.Cube(center=(0, 0, 0))

				## Add some scalar field associated to the mesh
				mesh["myscalar"] = mesh.points[:, 2] * mesh.points[:, 0]

				## Add mesh to the plotter
				plotter.add_mesh(mesh, scalars="myscalar", cmap="bwr", line_width=1)

				## Final touches
				plotter.background_color = "white"
				plotter.view_isometric()

				## Pass a key to avoid re-rendering at each time something changes in the page
				stpyvista(plotter, key="pv_cube")
					

if __name__ == "__main__":
	# upload_zip_file()
	main()
