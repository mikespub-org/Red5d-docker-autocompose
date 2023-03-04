from setuptools import find_packages, setup

setup(
    name="docker-autocompose",
    version="1.2.0",
    description="Generate a docker-compose yaml definition from a running container",
    url="https://github.com/Red5d/docker-autocompose",
    author="Red5d",
    license="GPLv2",
    keywords="docker yaml container",
    packages=find_packages(),
    install_requires=["pyaml>=21.10.1", "docker>=6.0.1"],
    scripts=["autocompose.py"],
    entry_points={
        "console_scripts": [
            "autocompose = autocompose:main",
        ]
    },
)
