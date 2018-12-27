from setuptools import setup, find_packages


setup(
    name='wallpaper_app',
    version='0.0.1',

    description='A macOS statusbar app for wallpaper switching',

    setup_requires=['setuptools-markdown'],
    long_description_markdown_filename='README.md',

    url='https://github.com/kpj/wallpaper_app',

    author='kpj',
    author_email='kpjkpjkpjkpjkpjkpj@gmail.com',

    license='MIT',
    packages=find_packages(exclude=['tests']),

    install_requires=[
        'rumps', 'pync',
        'requests'
    ],

    entry_points={
        'console_scripts': [
            'wallpaper_app=wallpaper_app:launch_app',
        ],
    }
)
