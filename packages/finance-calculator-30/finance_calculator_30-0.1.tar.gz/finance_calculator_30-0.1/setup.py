from setuptools import setup, find_packages

setup(
    name='finance-calculator-30',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'finance-calculater=finance_calculater.__main__:main',
        ],
    },
    description='A package for calculating net profit and ROI.',
    author='grisha123invent',
    author_email='grig.perev@gamil.com',
)