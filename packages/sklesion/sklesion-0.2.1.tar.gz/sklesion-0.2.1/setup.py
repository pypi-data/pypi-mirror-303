from setuptools import setup, find_packages

setup(
    name="sklesion",
    version="0.2.1",
    # Automatically find python packages (they need to have a __init__.py file in them)
    packages=find_packages(),
    install_requires=[
        "tensorflow==2.17.0",
        "pandas==2.2.3",
        "numpy==1.26.4",
        ],
    package_data={
        "sklesion": [
            "model.keras",
            "model_props.pkl",
            "cr_test.pkl",
            "prob_to_label.py",
            "cl_info.pkl",
        ],
    },
    include_package_data=True,
    description="A Keras model for diagnosing skin lesions.",
    long_description="A Keras model for diagnosing skin lesions.",
    long_description_content_type="text/markdown",
    author="Elio Pereira",
    author_email="eliocpereira@hotmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # Minimum Python version
    python_requires=">=3.11",
)
