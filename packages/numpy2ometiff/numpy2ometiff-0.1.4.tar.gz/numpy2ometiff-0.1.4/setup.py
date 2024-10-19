from setuptools import setup, find_packages
import pathlib

# Get the long description from the README.md file
here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='numpy2ometiff',
    version='0.1.4',
    description='Convert NumPy arrays to OME-TIFF',
    long_description=long_description,  # Add this to include the README.md content
    long_description_content_type='text/markdown',  # Specify the content type as Markdown
    author='Tristan Whitmarsh',
    author_email='tw401@cam.ac.uk',
    url='https://github.com/TristanWhitmarsh/numpy2ometiff',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'tifffile',
        'scikit-image',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],
    python_requires='>=3.6',
)
