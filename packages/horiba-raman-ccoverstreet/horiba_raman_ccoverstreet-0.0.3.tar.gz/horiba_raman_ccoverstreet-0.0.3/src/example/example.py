from horiba_raman_ccoverstreet import mapping
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


img, extent_camera = mapping.parse_image_comb("Gd2O3_AlN_map.bmp", "Gd2O3_AlN_map.txt")
shift, pos, counts = mapping.parse_data_txt("Gd2O3_AlN_map_data.txt")

dim = mapping.determine_rectangular_map_dim(pos)
extent = mapping.extract_extent_from_pos_rect(pos, dim)

# Create an array and reshape based on rectangular mesh
# of peak maxes corresponding to Gd2O3
maxes = []
for c in counts:
    m = mapping.extract_max_from_range(shift, c, 300, 500)
    maxes.append(m)

maxes = np.reshape(np.array(maxes), dim)
print(maxes)

# Throw everything into a plot to taste
plt.figure(figsize=(10, 4))
plt.subplot(121)
plt.title(r"Overlay of Gd$_2$O$_3$ Raman peak", fontsize=16)
plt.imshow(img, extent=extent_camera)
plt.imshow(maxes, extent=extent, alpha=0.4, interpolation="bilinear")
plt.annotate("AlN", (-280, 0), fontsize=16, ha="center")
plt.annotate(r"Gd$_2$O$_3$", (295, 0), fontsize=16, ha="center")
print(extent_camera)
plt.xlim(extent_camera[0], extent_camera[1])
plt.ylim(extent_camera[2], extent_camera[3])
plt.xlabel(r"X [$\mu$m]", fontsize=16)
plt.ylabel(r"Y [$\mu$m]", fontsize=16)

plt.subplot(122)
plt.imshow(img, extent=extent_camera, cmap=plt.get_cmap("gist_grey"))
plt.imshow(maxes, extent=extent, alpha=0.4, cmap=plt.get_cmap("gist_heat"))
plt.xlim(extent_camera[0], extent_camera[1])
plt.ylim(extent_camera[2], extent_camera[3])

plt.xlabel(r"X [$\mu$m]", fontsize=16)
plt.ylabel(r"Y [$\mu$m]", fontsize=16)

plt.tight_layout()

plt.savefig("Raman_mapping_postprocessing_demo.png")
plt.show()


