from setuptools import setup, find_packages

# Leer el contenido del archivo README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Configuración del paquete
setup(
    name="capibara-ent",
    version="1.1.0",
    author="Marco Durán",
    author_email="marco@anachroni.com",
    description="A flexible multimodal AI library for advanced contextual understanding and deployment.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Anachroni/capibara",
    packages=find_packages(include=[
                           "capibara_model", "capibara_model.*", "config", "data", "layers", "src", "tests"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    install_requires=[
        "tensorflow>=2.5.0",
        "docker",
        "nltk",
        "numpy",
        "pandas",
        "torch>=1.8.0",
        "torch-xla",
        "jax",
        "flax",
        "optax",
        "wandb",
        "tensorflow-hub",
        "tqdm",
        "PyYAML",
        "spacy",
        "transformers",
        "scipy",
        "matplotlib",
        "seaborn",
    ],
    extras_require={
        "dev": [
            "pytest",
            "pytest-cov",
            "sphinx",
            "sphinx-rtd-theme",
            "myst-parser",
            "black",
            "flake8",
        ],
        "gpu": [
            "tensorflow-gpu>=2.5.0",
            "torch>=1.8.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "capibaraent=capibara_model.cli.capibaraent_cli:main",
        ],
    },
    keywords="ai nlp multimodal machine-learning deep-learning language-models ethics tpu training deployment",
    include_package_data=True,
    zip_safe=False,
)
