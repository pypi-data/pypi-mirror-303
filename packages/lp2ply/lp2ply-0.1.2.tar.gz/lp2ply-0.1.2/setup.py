from setuptools import setup
from pathlib import Path

this_dir = Path(__file__).parent
long_description = (this_dir / "README.md").read_text() + "\n\n" + (this_dir / "CHANGELOG.md").read_text()


setup(
    name='lp2ply',
    version='0.1.2',
    description='Transform lamination parameters into stacking sequences.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Moritz Sprengholz',
    author_email='m.sprengholz@tu-bs.de',
    url="https://git.rz.tu-bs.de/m.sprengholz/publication-lamination-parameters",
    packages=['lp2ply'],
    install_requires=[
        'numpy',
        'DFO-LS',
        'numba',
        'pyDOE',
    ],
    license='GPLv3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
)

