import setuptools


setuptools.setup(
    long_description_content_type="text/markdown",
    entry_points={
        'console_scripts': [
            'parser=src.DlmsSPODES.setting:version'
        ]
    },
)
