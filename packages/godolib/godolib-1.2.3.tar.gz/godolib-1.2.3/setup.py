from setuptools import setup, find_packages

setup(
    name='godolib',
    version='1.2.3',
    packages=find_packages(),
    install_requires=['statsmodels', 'numpy', 'scikit-learn', 'pandas', 'boto3', 'chardet', 'psutil', 'plotly', 'matplotlib', 'requests', 'h5py', 'tensorflow'],
    description='Machine/Deep learning and preprocessing oriented library',
    author='Sergio Montes',
    author_email='ss.montes.jimenez@gmail.com',
    url='',
)
