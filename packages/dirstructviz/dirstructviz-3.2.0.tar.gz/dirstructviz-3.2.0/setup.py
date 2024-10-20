from setuptools import setup, find_packages

setup(
    name='dirstructviz',
    version='3.2.0',
    description='A versatile directory structure visualizer and exporter utility for Python projects.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Abhinav Hudda',
    author_email='upstage.barrier_0x@icloud.com',
    packages=find_packages(),
    install_requires=[
        'click>=8.0',
        'rich',
        'matplotlib>=3.5',
        'networkx>=2.5',
    ],
    entry_points={
        'console_scripts': [
            'dirviz=visualizer.cli:visualize',
            'visualizer=visualizer.cli:visualize',
            'visualiser=visualizer.cli:visualize',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    python_requires='>=3.7',
    include_package_data=True,
)
