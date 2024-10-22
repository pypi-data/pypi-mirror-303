# Copyright 2024 imec. All rights reserved.

__version__ = "0.1.0"

from .qgis_annimated import convert_tiff_images_to_png
from .qgis_export import make_gif

__all__ = ['convert_tiff_images_to_png', 'make_gif']
