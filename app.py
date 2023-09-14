import streamlit as st
# import zipfile
from demo2_utils import *
# from crowning2_utils import *
# from casevwr_utils import *
from htmlTemplates import css, bot_template
import pyvista as pv
from stpyvista import stpyvista
import trimesh



def main():
	def callback2(point):
		mesh = pv.Sphere(center=point, radius=10)
		plotter.add_mesh(mesh, style='wireframe', color='r')
		plotter.add_point_labels(point, [f"{point[0]:.2f}, {point[1]:.2f}, {point[2]:.2f}"])
		print(point)

	mesh_list = []
	# st.header('Auto-Design Crown :tooth:')
	st.write(css, unsafe_allow_html=True)

	with st.sidebar:
		uploaded_file = st.file_uploader("Upload STL", type=["stl"], accept_multiple_files=True)

		if st.button("Submit"):
			with st.spinner('Processing...'):
				if uploaded_file:
					for i,file in enumerate(uploaded_file):
						mesh_prep_3m = load_prep_from_file(file)
						mesh_list.append(mesh_prep_3m)
	lowest_vol = 900000000
	lowest_vol_idx = None
	if mesh_list:
		plotter = pv.Plotter()
		for i,mesh in enumerate(mesh_list):
			if int(mesh.volume) < int(lowest_vol):
				lowest_vol = mesh.volume
				lowest_vol_idx = i

		for i,mesh in enumerate(mesh_list):
			if i == lowest_vol_idx:
				plotter.add_mesh(pv.wrap(mesh), color='w')
			else:
				plotter.add_mesh(pv.wrap(mesh))
			plotter.background_color = "white"
			plotter.camera_position = 'zx'
			plotter.window_size = [600, 400]

		plotter.enable_surface_point_picking(callback=callback2, show_point=True)
		stpyvista(plotter, key='test')
					

if __name__ == "__main__":
	# upload_zip_file()
	main()
