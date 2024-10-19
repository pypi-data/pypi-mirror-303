from setuptools import setup, find_packages

setup(
    name='tse_motion',  
    version='0.2.8.6',
    packages=find_packages(), 
    install_requires=[
        'torch',
        'monai',
        'nibabel',
        'torchvision',
        'argparse'  # Add argparse to the requirements
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'rate-motion=tse_motion.rate:main',
            'gen-motion=tse_motion.motion2d:main',
            'translate-t1=tse_motion.translate_t1:main',  # Uses argparse for command-line options
            'recon-tse=tse_motion.reconstruction:main',
            'nii2mp4=tse_motion.nii2mp4:main',
            'rembg-nii=tse_motion.remove_background:main'
        ],
    },
    author='Jinghang Li',
    author_email='jinghang.li@pitt.edu',
    description='A package to rate motion artifacts in medical images.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/jinghangli98/tse-rating',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)