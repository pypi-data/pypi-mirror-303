
# numpy2ometiff

`numpy2ometiff` is a Python library designed to convert NumPy arrays into OME-TIFF files. This library facilitates exporting scientific imaging data to the OME-TIFF format, which is ideal for microscopy and bioimaging applications.

## Features

- **Simple API**: Convert NumPy arrays to OME-TIFF with a single function call.
- **Flexible Input**: Supports single and multi-dimensional arrays (2D, 3D, 4D) representing multiple channels and z-slices.
- **Customizable Metadata**: Allows users to specify pixel sizes and channel information.
- **Optional Pyramid Creation**: Enable pyramid OME-TIFF files for large datasets, improving performance in compatible viewers.

## Installation

You can install `numpy2ometiff` directly via pip:

```bash
pip install numpy2ometiff
```
## Example Usage

This example demonstrates how to convert a NumPy array into an OME-TIFF file using the `numpy2ometiff` library. It assumes you have already installed `numpy2ometiff` as described in the installation section.

```python
import numpy as np
from numpy2ometiff import write_ome_tiff

# Generate a dummy numpy array
data = np.random.rand(1, 3, 256, 256).astype(np.float32)  # 1 z-slice, 3 channels, 256x256 pixels

# Define channel names
channel_names = ['DAPI', 'GFP', 'RFP']

# Define pixel sizes and physical size in Z
pixel_size_x = 0.65  # micron
pixel_size_y = 0.65  # micron
physical_size_z = 0.2  # micron

# Specify the output filename
output_filename = 'output_test_image.ome.tiff'

# Write the OME-TIFF file
write_ome_tiff(data=data,
               output_filename=output_filename,
               channel_names=channel_names,
               pixel_size_x=pixel_size_x,
               pixel_size_y=pixel_size_y,
               physical_size_z=physical_size_z,
               Unit='µm',
               imagej=False, 
               create_pyramid=True,
               compression='zlib')

print("The OME-TIFF file has been successfully written.")
```

## Contributing

Contributions to `numpy2ometiff` are welcome! Feel free to fork the repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the BSD 3-Clause License - see the [LICENSE](LICENSE) file for details.
