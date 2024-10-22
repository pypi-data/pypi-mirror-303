import os
import sys
import logging
import click
logging.basicConfig(level=logging.DEBUG)

# notice that the path below changes depending on your QGIS version
# it also depends on the python version QGIS is installed
# the example here uses QGIS 3.36.3
# which uses Python 3.12.3
# installed at "C:\Program Files\QGIS 3.36.3\apps\Python312\python.exe"
if sys.platform == "win32":
    # you must check this path on your machine
    # because it is installation dependent
    path_to_qgis = "C:/Program Files/QGIS 3.36.3"
    logging.debug(f"adding to sys.path: {path_to_qgis}")
    # add QGIS api and other dependencies
    sys.path.append(os.path.join(path_to_qgis, "apps/Python312/Lib/site-packages"))
    sys.path.append(os.path.join(path_to_qgis, "apps/qgis/python"))

else:
    # on linux, just install QGIS
    # the libraries will be incorporated in the current python installation
    path_to_qgis = "/home/h3dema/.local/share/QGIS/QGIS3"
    sys.path.append("/usr/lib/python3/dist-packages")


# see refs. https://qgis.org/pyqgis/3.0/index.html
from qgis.core import QgsApplication  # type: ignore

try:
    from .qgis_export import save_base, save_layers, make_gif
except ImportError:
    from qgis_export import save_base, save_layers, make_gif


# ----------------------------------------------
#
# Constants
#
# ----------------------------------------------
level = logging.INFO
output = "results"  # path to output the results


def convert_tiff_images_to_png(base: str,
                               gt: str,
                               prediction: str,
                               output: str
                               ):
    """
    Converts GeoTIFF images to PNG format and saves them to the specified output directory.

    Args:
        base (str): Path to the real GeoTIFF image.
        gt (str): Path to the ground truth GeoTIFF image. Defaults to None.
        prediction (str): Path to the predictions GeoTIFF image. Defaults to None.
        output (str): Path to save the PNG images. Defaults to the current directory.

    Returns:
        tuple: A tuple containing the paths to the saved PNG images for the real, ground truth, and prediction images.
    """
    output_path = "." if output is None or len(output.strip()) == 0 else output
    try:
        os.makedirs(output_path, exist_ok=True)
    except FileNotFoundError:
        pass  # if path is '.'

    if gt is None:
        gt = base.replace("_hsi", "_gt")
    if prediction is None:
        prediction = base.replace("_hsi", "_prediction")

    # Supply path to qgis install location
    QgsApplication.setPrefixPath(path_to_qgis, True)

    # Create a reference to the QgsApplication.  Setting the
    # second argument to False disables the GUI.
    qgs = QgsApplication([], False)

    # Load providers
    qgs.initQgis()

    img_real = os.path.join(output_path, os.path.basename(base).replace(".tif", ".png"))
    img_gt = os.path.join(output_path, os.path.basename(gt).replace(".tif", ".png"))
    img_prediction = os.path.join(output_path, os.path.basename(prediction).replace(".tif", ".png"))
    # save real image (TIFF --> PNG)
    save_base(base, output=img_real)

    # save ground truth image and the predictions in two separate images
    save_layers(base, gt, output=img_gt, color="yellow")
    save_layers(base, prediction, output=img_prediction, color="red")

    # Finally, exitQgis() is called to remove the provider and layer registries from memory
    qgs.exitQgis()
    return img_real, img_gt, img_prediction


@click.command()
@click.option('--base', type=str, required=True, help='Path to the real geotiff image')
@click.option('--gt', type=str, required=True, help='Path to the ground truth geotiff image')
@click.option('--prediction', type=str, required=True, help='Path to the predictions geotiff image')
@click.option('--output', default=output, help='Path to save the png and gif images')
@click.option('--debug/--info', is_flag=True, default=False, help="set logging level to debug or info (default)")
def main(base: str,
         gt: str,
         prediction: str,
         output: str,
         debug: bool,
         ):
    # set logging for the application
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(level=level)
    logging.root.setLevel(level)

    img_real, img_gt, img_prediction = convert_tiff_images_to_png(base, gt, prediction, output)

    imgs = (img_real, img_gt, img_prediction)
    gif_fname = os.path.join(output, os.path.basename(base).replace("_hsi.tif", ".gif"))
    make_gif(imgs, gif_fname)


# Example:
# ========

# on Windows:
# & 'C:\Program Files\QGIS 3.36.3\apps\Python312\python.exe' qgis_annimated.py --base images/Spain_5_hsi.tif --gt images/Spain_5_gt.tif --prediction images/Spain_5_prediction.tif

if __name__ == "__main__":
    main()
