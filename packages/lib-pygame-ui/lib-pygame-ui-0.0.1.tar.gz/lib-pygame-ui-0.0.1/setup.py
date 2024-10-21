from distutils.core import setup

with open('README.md', 'r') as README:
    README_md = README.read()

setup(
    name = 'lib-pygame-ui',
    version = '0.0.1',
    author = 'azzammuhyala',
    author_email = 'azzammuhyala@gmail.com',
    description = 'gui for pygame. (UNOFFICIAL)',
    install_requires = [
        "pygame>=2.5.0",
        "pillow>=10.1.0"
    ],
    keywords = [
        'pyg_ui', 'pygameui', 'pygamegui', 'pygame gui'
    ],
    packages = [
        'pyg_ui', 'pyg_ui.__private'
    ],
    long_description_content_type = 'text/markdown',
    long_description = README_md,
    python_requires ='>=3.10',
    classifiers = [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)