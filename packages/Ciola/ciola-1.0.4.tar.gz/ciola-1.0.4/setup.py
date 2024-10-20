from setuptools import setup, find_packages
 
setup(
    name='Ciola',
    version='1.0.4',
    author='Lapsus',
    author_email='',
    description='A personal library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'pyautogui',
    ],
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
