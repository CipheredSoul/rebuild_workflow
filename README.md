I made this to pull the metadata and then rebuild the workflow from an image saved by ComfyUI.

This script uses the PIL (Pillow) library to directly read metadata from PNG image files.

Single file 

rebuild_workflow.py your_image.png

Batch files 

rebuild_workflow.py *.png
