from setuptools import setup

setup(
    name             = "enigma",
    version          = "0.0.1",
    author           = "JMP",
    author_email     = "",
    description      = "",
    long_description = "",
    license          = "BSD",
    keywords         = "",
    classifiers = [
        "Development Status :: 2 - Pre-Alpha",
    ],
    packages  = [
        "enigma", 
        "tests"
    ],
    entry_points = {
        'console_scripts' : [
            'enigma-encipher = enigma.__main__:encipher',
            'enigma-decipher = enigma.__main__:decipher',
            'enigma-decrypt  = enigma.__main__:decrypt'
        ]
    },
)
