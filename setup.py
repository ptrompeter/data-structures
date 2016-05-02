from setuptools import setup

setup(
    name="data-structures",
    description="Collection of Classic Data Structures",
    version=0.1,
    author="Selena Flannery and Patrick Trompeter",
    license="MIT",
    py_modules=["linked_list",
                "stacks",
                "double_linked_list",
                "queue",
                "selena_parens",
                "patrick_parens",
                "deque"],
    package_dir={"": "src"},
    install_requires=["future"],
    extras_require={'test': ['pytest', 'pytest-xdist', 'tox']},
)
