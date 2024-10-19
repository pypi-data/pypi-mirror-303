from setuptools import setup, find_packages

setup(
    name='Oggyz',
    version='0.1',
    packages=find_packages(),
    author='oggy',
    author_email='tranthang20111@gmail.com',
    description='A custom text printing package with colors',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/Oggyz',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
