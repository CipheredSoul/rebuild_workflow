I made this to pull the metadata and then rebuild the workflow from an image saved by ComfyUI.

This script uses the PIL (Pillow) library to directly read metadata from PNG image files.

Single file : rebuild_workflow.py your_image.png

Batch files : rebuild_workflow.py *.png

Multiple Files : rebuild_workflow.py image1.png image2.png

Specific Folder with Wildcard : rebuild_workflow.py "C:\images\\*.png"

Mixed Input : rebuild_workflow.py  image1.png "C:\images\\*.png" image2.png



