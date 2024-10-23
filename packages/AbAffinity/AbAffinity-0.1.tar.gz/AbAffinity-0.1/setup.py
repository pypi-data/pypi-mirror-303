from setuptools import setup, find_packages 

setup(
    name='AbAffinity',
    version='0.1', 
    description='Predict Affinity against SARS-CoV-2 HR2 peptide',
    author='Faisal Bin Ashraf',
    packages=find_packages(),
    include_package_data=True, 
    package_data={
        '': ['ESM2/*.py'],             # Include all .py files in EM2 folder
    },
    install_requires=[
        'torch',              # PyTorch
        'numpy',              # For numerical operations
        'matplotlib',         # For plotting graphs
        'textwrap3',           # For wrapping text
    ],
)