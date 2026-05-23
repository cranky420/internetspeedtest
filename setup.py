from setuptools import setup

setup(

    name='internetspeed',

    version='0.1',

    py_modules=[

        'cli',
        'speed'

    ],

    install_requires=[

        'click',
        'requests',
        'rich'

    ],

    entry_points={

        'console_scripts': [

            'internetspeed=cli:cli'

        ]

    }

)