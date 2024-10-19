import numpy as np
import tifffile
import skimage.measure

def write_ome_tiff(data, output_filename, channel_names=[], pixel_size_x=1, pixel_size_y=1, physical_size_z=1, imagej=False, create_pyramid=True, compression='zlib', Unit='µm', downsample_count=4):
    """
    Write an array to an OME-TIFF file with optional pyramid creation.

    Parameters:
    data (numpy.ndarray): The image data (must be in ZCYX format).
    channel_names (list of str): Names of the channels.
    output_filename (str): Path to save the OME-TIFF file.
    pixel_size_x (float): Pixel size in the X dimension in microns.
    pixel_size_y (float): Pixel size in the Y dimension in microns.
    physical_size_z (float): Physical size in the Z dimension in microns (for 3D data).
    imagej (bool): Flag to use ImageJ compatibility mode.
    create_pyramid (bool): Flag to create a pyramid if the dimensions are suitable.
    compression (str): Compression method, defaults to 'zlib'.
    Unit (str): Unit for physical sizes, defaults to 'µm' (micrometers).
    downsample_count (int): Number of pyramid downsample levels, defaults to 4.
    """
    
    # Ensure the data is in ZCYX format (4D array: Z-slices, Channels, Y, X)
    if len(data.shape) != 4:
        raise ValueError(f"Input data must have 4 dimensions (ZCYX). Found {len(data.shape)} dimensions.")
    
    if channel_names and data.shape[1] != len(channel_names):
        raise ValueError(f"Number of channels in the data ({data.shape[1]}) does not match the length of 'channel_names' ({len(channel_names)}).")
    
    # Provide default channel names if none are provided
    if not channel_names:
        channel_names = [f"Channel {i+1}" for i in range(data.shape[1])]

    # Handle unit conversion for ImageJ compatibility (ImageJ expects 'um' instead of 'µm')
    if Unit == 'µm' and imagej:
        Unit = 'um'
        
    # Validate compression options
    valid_compressions = [None, 'zlib', 'lzma', 'jpeg']
    if compression not in valid_compressions:
        raise ValueError(f"Invalid compression option '{compression}'. Valid options are: {valid_compressions}.")

    # Handle 3D data (ZCYX format)
    if data.shape[0] > 1:
        
        if data.shape[1] == 3 and data.dtype == np.uint8:
            print("Detected 3D color data")
            data = np.transpose(data, (0, 2, 3, 1))
            metadata = {
                'axes': 'ZYXC',
                'PhysicalSizeX': pixel_size_x,
                'PhysicalSizeXUnit': Unit,
                'PhysicalSizeY': pixel_size_y,
                'PhysicalSizeYUnit': Unit,
                'PhysicalSizeZ': physical_size_z,
                'PhysicalSizeZUnit': Unit,
                'Photometric': 'RGB',
                'Planarconfig': 'contig',
            }
            
            # Handle pyramid creation
            if create_pyramid:
                print(f"Writing with pyramid, {downsample_count} downsample levels")
                with tifffile.TiffWriter(output_filename, bigtiff=True, imagej=imagej) as tif:
                    tif.write(data, subifds=downsample_count, metadata=metadata, compression=compression)
                    for level in range(1, downsample_count + 1):
                        data = skimage.measure.block_reduce(data, block_size=(1, 2, 2, 1), func=np.mean).astype(data.dtype)  # Average pooling
                        metadata['PhysicalSizeX'] *= 2  # Update pixel size for each level
                        metadata['PhysicalSizeY'] *= 2
                        tif.write(data, subfiletype=1, metadata=metadata, compression=compression)
            else:
                print("Writing without pyramid")
                with tifffile.TiffWriter(output_filename, bigtiff=True, imagej=imagej) as tif:
                    tif.write(data, subifds=0, metadata=metadata, compression=compression)
        else:
            print("Detected 3D data")
            metadata = {
                'axes': 'ZCYX',
                'Channel': [{'Name': name, 'SamplesPerPixel': 1} for name in channel_names],
                'PhysicalSizeX': pixel_size_x,
                'PhysicalSizeXUnit': Unit,
                'PhysicalSizeY': pixel_size_y,
                'PhysicalSizeYUnit': Unit,
                'PhysicalSizeZ': physical_size_z,
                'PhysicalSizeZUnit': Unit,
                'Photometric': 'minisblack',
            }
        
            # Handle pyramid creation
            if create_pyramid:
                print(f"Writing with pyramid, {downsample_count} downsample levels")
                with tifffile.TiffWriter(output_filename, bigtiff=True, imagej=imagej) as tif:
                    tif.write(data, subifds=downsample_count, metadata=metadata, compression=compression)
                    for level in range(1, downsample_count + 1):
                        data = skimage.measure.block_reduce(data, block_size=(1, 1, 2, 2), func=np.mean).astype(data.dtype)  # Average pooling
                        metadata['PhysicalSizeX'] *= 2  # Update pixel size for each level
                        metadata['PhysicalSizeY'] *= 2
                        tif.write(data, subfiletype=1, metadata=metadata, compression=compression)
            else:
                print("Writing without pyramid")
                with tifffile.TiffWriter(output_filename, bigtiff=True, imagej=imagej) as tif:
                    tif.write(data, subifds=0, metadata=metadata, compression=compression)

    # Handle 2D data (CYX format)
    else:
        # Remove the z-dimension (since it's a single z-slice)
        data = data[0, ...]  # Now data has shape (C, Y, X)
            
        # Check if data is RGB (3 channels and uint8 type)
        if data.shape[0] == 3 and data.dtype == np.uint8:
            print("Detected 2D color data")
            data = np.transpose(data, (1, 2, 0))
            metadata = {
                'axes': 'YXC',
                'PhysicalSizeX': pixel_size_x,
                'PhysicalSizeXUnit': Unit,
                'PhysicalSizeY': pixel_size_y,
                'PhysicalSizeYUnit': Unit,
                'Photometric': 'RGB',
                'Planarconfig': 'contig',
            }
            
            # Handle pyramid creation
            if create_pyramid:
                print(f"Writing with pyramid, {downsample_count} downsample levels")
                with tifffile.TiffWriter(output_filename, bigtiff=True, imagej=imagej) as tif:
                    tif.write(data, subifds=downsample_count, metadata=metadata, compression=compression)
                    for level in range(1, downsample_count + 1):
                        data = skimage.measure.block_reduce(data, block_size=(2, 2, 1), func=np.mean).astype(data.dtype)  # Average pooling
                        metadata['PhysicalSizeX'] *= 2  # Update pixel size for each level
                        metadata['PhysicalSizeY'] *= 2
                        tif.write(data, subfiletype=1, metadata=metadata, compression=compression)
            else:
                print("Writing without pyramid")
                with tifffile.TiffWriter(output_filename, bigtiff=True, imagej=imagej) as tif:
                    tif.write(data, subifds=0, metadata=metadata, compression=compression)
        else:
            print("Detected 2D data")
            metadata = {
                'axes': 'CYX',
                'Channel': [{'Name': name, 'SamplesPerPixel': 1} for name in channel_names],
                'PhysicalSizeX': pixel_size_x,
                'PhysicalSizeXUnit': Unit,
                'PhysicalSizeY': pixel_size_y,
                'PhysicalSizeYUnit': Unit,
                'Photometric': 'minisblack',
                'Planarconfig': 'separate',
            }

            # Handle pyramid creation
            if create_pyramid:
                print(f"Writing with pyramid, {downsample_count} downsample levels")
                with tifffile.TiffWriter(output_filename, bigtiff=True, imagej=imagej) as tif:
                    tif.write(data, subifds=downsample_count, metadata=metadata, compression=compression)
                    for level in range(1, downsample_count + 1):
                        data = skimage.measure.block_reduce(data, block_size=(1, 2, 2), func=np.mean).astype(data.dtype)  # Average pooling
                        metadata['PhysicalSizeX'] *= 2  # Update pixel size for each level
                        metadata['PhysicalSizeY'] *= 2
                        tif.write(data, subfiletype=1, metadata=metadata, compression=compression)
            else:
                print("Writing without pyramid")
                with tifffile.TiffWriter(output_filename, bigtiff=True, imagej=imagej) as tif:
                    tif.write(data, subifds=0, metadata=metadata, compression=compression)

    print(f"OME-TIFF file written successfully: {output_filename}")
