from setuptools import setup, find_packages

setup(
    name='Platts_eWindow_dashboard',  # Replace with your package name
    version='1.0.6',
    description='A Dash app for visualizing Platts eWindow data',
    author='Magnum35puc',
    packages=find_packages(where='src'),  # Include all Python packages inside src/
    package_dir={'': 'src'},  # Set src/ as the package directory
    include_package_data=True,  # Include non-python files like CSS
    install_requires=[  # List your dependencies
        'dash>=2.0.0',
        'plotly>=5.0.0',
        'pandas',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'start-dashboard=app.dashboard:main',  # The command to run the app
        ],
    },
)
