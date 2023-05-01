# MyCustomReviewers

Suite of reviewers for reviewing `<>`.

![MyCustomReviewers](<link to video>)

# Install

## Activate or Set up Conda Environment

This is **_highly_** recommended to manage different dependencies required by different reviewers.

See [Set up Conda Environment](https://github.com/getzlab/JupyterReviewer/blob/master/README.md#set-up-conda-environment) for details on how to download conda and configure an environment.
    
## Install PurityReviewers

Clone 
```
git clone git@github.com:<>/<MyCustomReviewer>.git 

# or in an existing repo
git submodule add git@github.com:<>/<MyCustomReviewer>.git 
```

Install
```
cd MyCustomReviewer
conda activate <your_env>
pip install -e .
```

# Basic usage

See `<MyCustomReviewer>/example_notebooks` for basic examples and demos of the purity reviewers.

See `<MyCustomReviewer>/Reviewers` to see available pre-built reviewer options.

See `<MyCustomReviewer>/DataTypes` to see pre-built data configurations for purity review.

# Custom and advanced usage

See `MyCustomReviewer/AppComponents` for pre-built components and their customizable parameters, and additional utility functions. 

For customizing annotations, adding new components, and other features, see [Intro_to_Reviewers.ipynb](https://github.com/getzlab/JupyterReviewer/blob/master/example_notebooks/Intro_to_Reviewers.ipynb).

For creating your own prebuilt reviewer, see [Developer_Jupyter_Reviewer_Tutorial.ipynb](https://github.com/getzlab/JupyterReviewer/blob/master/example_notebooks/Developer_Jupyter_Reviewer_Tutorial.ipynb).
