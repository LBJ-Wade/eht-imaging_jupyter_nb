# Running the Pipeline
__Before running the pipeline, please follow the INSTALLATION instructions [here](https://github.com/TauferLab/Src_EHT/blob/main/EHT-Imaging/docs/INSTALLATION.md)__

There is no need to worry about unpacking the data or where it is located before executing the pipeline because the `run-pipeline.sh` script will automatically ensure it is in the correct location.

Before running the pipeline, you can edit the `run-pipeline.sh` script to specify if you want the pipeline to save the images as `.pdf` files. Instructions are in the comments of the file on how to do this. By default, all outputs (`.fits` image, `.pdf` image, `.pdf` of image summary statistics) from the pipeline are saved. The output files will be saved in a new directory `EHT/EHT-Imaging/output`. This directory will be created automatically by the `run-pipeline.sh` script.

You can run the pipeline with the following command: (This assumes that you are currently in the `EHT/EHT-Imaging` directory, the `run-pipeline.sh` script must be executed from this directory in order to find the data properly)
```
bash scripts/run-pipeline.sh