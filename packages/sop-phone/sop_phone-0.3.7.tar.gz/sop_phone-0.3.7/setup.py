from setuptools import setup, find_packages


setup(
    name='sop-phone',
    version='0.3.7',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'phonenumbers'
    ],
    description="Manage phone informations of each sites.",
    author="Leorevoir",
    author_email="leo.quinzler@epitech.eu",
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
    ],
    zip_safe=False,
)
