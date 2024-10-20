from setuptools import setup, find_packages

setup(
    name='reissvd_imgcompress',
    version='0.2.0',
    packages=find_packages(),
    description='Image compression using REIS-SVD with evaluation metrics like MSE, PSNR, and SSIM.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'numpy',
        'Pillow',
        'matplotlib',
        'scipy',
        'scikit-image',
    ],
    author='Katie Wen-Ling Kuo',
    author_email='katie20030705@gmail.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    python_requires='>=3.6',
)

