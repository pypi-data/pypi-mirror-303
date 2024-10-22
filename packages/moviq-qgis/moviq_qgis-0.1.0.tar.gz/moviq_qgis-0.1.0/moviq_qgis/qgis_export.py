import sys
import os
import logging
from PIL import Image
from pathlib import Path
# import warnings
# warnings.filterwarnings("ignore", category=DeprecationWarning)

from qgis.core import (
    QgsProject,
    QgsRasterLayer,
    QgsMapSettings,
    QgsRectangle,
    QgsMapRendererCustomPainterJob
)
from PyQt5.QtGui import QImage, QColor, QPainter
from PyQt5.QtCore import QSize
#
# https://qgis.org/pyqgis/3.0/index.html
# https://opensourceoptions.com/pyqgis-render-print-save-a-layer-as-an-image/
#

#
# list of supported colors to be used to mark the ground truth or the predicted fire
# you should use different colors!
#
colors = {
    "pink": (255, 32, 244, 255),
    "red": (227, 26, 28, 255),
    "yellow": (255, 255, 0, 255),
}


def save_layers_as_png(layer_names: list[str], output: str = None):
    """
        This function saves a QGIS layers as a PNG image.

        Parameters:
        layer_names (list[str]): A list of layer names to be rendered in the image.
        output (str, optional): The output file path for the image. If not provided, the image will be saved with a default name based on the first layer name.

        Returns:
        None
    """
    if not isinstance(layer_names, list):
        layer_names = [layer_names, ]

    # get the layers in the project
    maps = QgsProject.instance().mapLayers()
    name_map = layer_names[0]  # get the first layer as a template
    name_layer = maps[name_map].name()  #
    img_name = f'{name_layer}.png' if output is None else output

    logging.debug(f"Saving image `{img_name}` with layers: {' '.join(layer_names)}")
    w = maps[name_map].width()
    h = maps[name_map].height()

    img_size = (w, h)

    # create image
    img = QImage(QSize(*img_size), QImage.Format_ARGB32_Premultiplied)
    # set background color
    color = QColor(255, 255, 255, 255)
    img.fill(color.rgba())

    # create painter
    p = QPainter()
    p.begin(img)
    p.setRenderHint(QPainter.Antialiasing)

    # create map settings
    ms = QgsMapSettings()
    ms.setBackgroundColor(color)

    # set layers to render
    ms.setLayers([maps[k] for k in layer_names])

    # set extent
    rect = QgsRectangle(ms.fullExtent())
    rect.scale(1)  # if 1, it is not necessary
    ms.setExtent(rect)

    # set output size
    ms.setOutputSize(img.size())

    # setup qgis map renderer
    render = QgsMapRendererCustomPainterJob(ms, p)
    render.start()
    render.waitForFinished()
    p.end()

    # save the image
    img.save(img_name)
    logging.debug(f"Image `{img_name}` saved")


def save_base(base_tiff_file: str, output: str):
    """
    This function saves a base raster layer (real image in GeoTIFF format) to a specified output path (PNG image)

    Parameters:
        base_tiff_file (str): The path to the base raster layer (real image) in GeoTIFF format.
        output (str): The path where the output image will be saved.

    Returns:
    None

    Raises:
    Exception: If the provided raster layer is invalid.

    Note:
    This function uses QGIS to handle raster layers. It adds the base raster layer to the QGIS project,
    selects it for saving, and then saves it to the specified output path.
    """

    # Get the project instance
    project = QgsProject.instance()

    # Extract the name of the layer from the file path
    real_fname = os.path.basename(base_tiff_file)
    layer_name = str(Path(real_fname).with_suffix(''))

    # Create a QgsRasterLayer object from the base raster file
    real_layer = QgsRasterLayer(base_tiff_file, layer_name, "gdal")
    if real_layer.isValid():
        logging.debug(f"{layer_name} is a valid raster layer!")
    else:
        raise Exception(f"This raster layer is invalid! [{layer_name}]")

    # Add the raster layer to the QGIS project
    project.addMapLayer(real_layer)
    logging.debug(f"Real image layer name: {real_layer.name()}")

    # Get a dictionary of all map layers in the project
    maps = QgsProject.instance().mapLayers()

    # Select the layer we want to save in the image
    layers = [layer_name]
    mapLayerNames = [map_key for map_key in maps if maps[map_key].name() in layers]

    # Call the save_image function to save the selected layer to the output path
    save_layers_as_png(mapLayerNames, output)

    # Clear the project (remove all layers)
    project.clear()
    logging.info(f"Saved {output}")


def save_layers(base_tiff_file: str, transp_tiff_file: str, output: str, color: str = "pink"):
    """
    This function merges a base raster layer (real image) and a transparent raster layer (ground truth or predictions)
    into a new image, which will be placed in a specified output path.
    The transparent layer is rendered on top of the base layer.

    Parameters:
        base_tiff_file (str): The path to the base raster layer (real image) in GeoTIFF format.
        transp_tiff_file (str): The path to the transparent raster layer (ground truth or predictions) in GeoTIFF format.
        output (str): The path where the output image will be saved.
        color (str, optional): The color used to render the NoData value in the transparent layer. Default is "pink".

    Returns:
    None

    Raises:
    Exception: If either the base raster layer or the transparent raster layer is invalid.

    Note:
    This function uses QGIS to handle raster layers. It adds the base and transparent raster layers to the QGIS project,
    sets the NoData value and color for the transparent layer, selects the layers for saving, and then saves them to the specified output path.
    """

    assert color in colors.keys(), f"`{color}` is not a valid color name!"
    opacity = 0.0  # to set the transparent layer transparency

    # Get the project instance
    project = QgsProject.instance()

    # Extract the name of the layer from the file path
    real_fname = os.path.basename(base_tiff_file)
    layer_name = str(Path(real_fname).with_suffix(''))

    # Create a QgsRasterLayer object from the base raster file
    real_layer = QgsRasterLayer(base_tiff_file, layer_name, "gdal")
    if real_layer.isValid():
        logging.debug(f"{layer_name} is a valid raster layer!")
    else:
        raise Exception(f"This raster layer is invalid! [{layer_name}]")

    # Add the raster layer to the QGIS project
    project.addMapLayer(real_layer)
    logging.debug(f"Real image layer name: {real_layer.name()}")

    # Extract the name of the transparent layer, with the ground truth or predictions, from the file path
    transp_fname = os.path.basename(transp_tiff_file)
    transp_layer_name = str(Path(transp_fname).with_suffix(''))

    # Create a QgsRasterLayer object from the transparent raster file
    transp_layer = QgsRasterLayer(transp_tiff_file, transp_layer_name, "gdal")
    if transp_layer.isValid():
        logging.debug(f"{transp_layer_name} is a valid raster layer!")
    else:
        raise Exception(f"The transparent raster layer is invalid! [{transp_layer_name}]")
    logging.debug(f"Transparent layer name: {transp_layer.name()}")

    # Sets the opacity for the renderer, where opacity is a value between 0 (totally transparent) and 1.
    renderer = transp_layer.renderer()
    renderer.setOpacity(opacity)

    logging.debug(f"band count: {renderer.bandCount()}")
    if renderer.bandCount() > 1:
        raise Exception(f"Transparent layer should have only one band.")

    # TODO:
    # there is a reported (and random) problem with this SymbologyItems
    # according to Gabriel, sometimes the values (keys from legendSymbologyItems) are not '0.0' and '1.0'
    # so you have to manually adjust them to those limits
    # the code does not make this adjustment
    # print("SymbologyItems", renderer.legendSymbologyItems())  # raises DeprecationWarning if you call from layer

    band = 1
    # set the NoData value to 1 (the image is binary)
    transp_layer.dataProvider().setNoDataValue(bandNo=band, noDataValue=1)
    logging.debug(f"Has NoData value: {transp_layer.dataProvider().sourceHasNoDataValue(band)} - NoData value: {transp_layer.dataProvider().sourceNoDataValue(band)}")  # should return True
    # set the color used to render the NoData value
    renderer.setNodataColor(QColor(*colors[color]))
    transp_layer.triggerRepaint()
    logging.debug(f"NoData color: {transp_layer.renderer().nodataColor().getRgb()} <-> {color}")

    # Add the raster layer to the QGIS project
    project.addMapLayer(transp_layer)

    # Get a dictionary of all map layers in the project
    maps = QgsProject.instance().mapLayers()

    # Select the layer we want to save in the image
    # we need to force the order: first the transparent layer, then the real image layer
    mapLayerNames = []
    for layer in [transp_layer_name, layer_name]:
        k = [map_key for map_key in maps if maps[map_key].name() == layer]
        if len(k) > 0:
            # in principle, this is always true
            mapLayerNames.append(k[0])
    # save the layers
    save_layers_as_png(mapLayerNames, output)

    # Clear the project (remove all layers)
    project.clear()
    logging.info(f"Saved {output}")


def make_gif(list_images: list[str], output: str):
    """
        Generates an animated GIF from a list of PNG images.

        Parameters:
        - list_images (list[str]): A list of paths to the PNG images. This list contains the path to 3 PNG images [real hsi, gt, prediction]
        - output (str): The path to save the generated annimated GIF.

        Returns:
        None
    """
    if not output.endswith('.gif'):
        output += '.gif'
    frames = [Image.open(image) for image in list_images]
    frame_one = frames[0]
    frame_one.save(output,
                   format="GIF",
                   append_images=frames,
                   save_all=True,
                   duration=1000,
                   loop=0)
    logging.info(f"Saved {output}")
