from setuptools import setup, find_packages

setup(
    name='PiQR',
    version='0.1.1',
    author='PimpDiCaprio',
    author_email='info@aperturesoftware.us',
    description='A Python library for displaying QR codes.',
    long_description=open('README.md').read(),  # Make sure you have a README.md file
    long_description_content_type='text/markdown',
    url='https://github.com/PimpDiCaprio/PiQR',  # Update with your repository URL
    packages=find_packages(),  # Automatically find packages in the current directory
    scripts=['PiQR.py'],
    install_requires=[
        'opencv-contrib-python',  # Dependency for image processing
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Specify your license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify your Python version requirements
)