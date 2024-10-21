from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="flarchitect",
    version="0.0.8.48",  # Note the normalized version format
    packages=find_packages(include=[
        'flarchitect',
        'flarchitect.*',
        'flarchitect.html',
        'flarchitect.html.redoc_templates'
    ]),
    license="MIT",
    author="arched.dev (Lewis Morris)",
    author_email="hello@arched.dev",
    description="Automatic RESTful API generator with redoc",
    install_requires=requirements,
    package_data={
        "flarchitect": [
            "html/*",
            "html/redoc_templates/*",
        ],
    },
    include_package_data=True,
)
