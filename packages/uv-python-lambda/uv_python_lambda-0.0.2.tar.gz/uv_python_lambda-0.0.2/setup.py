import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "uv-python-lambda",
    "version": "0.0.2",
    "description": "uv-python-lambda",
    "license": "Apache-2.0",
    "url": "https://github.com/fourTheorem/uv-python-lambda",
    "long_description_content_type": "text/markdown",
    "author": "Eoin Shanaghy<eoin.shanaghy@fourtheorem.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/fourTheorem/uv-python-lambda"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "uv_python_lambda",
        "uv_python_lambda._jsii"
    ],
    "package_data": {
        "uv_python_lambda._jsii": [
            "uv-python-lambda@0.0.2.jsii.tgz"
        ],
        "uv_python_lambda": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.8",
    "install_requires": [
        "aws-cdk-lib>=2.161.1, <3.0.0",
        "constructs>=10.3.0, <11.0.0",
        "jsii>=1.104.0, <2.0.0",
        "publication>=0.0.3",
        "typeguard>=2.13.3,<4.3.0"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
