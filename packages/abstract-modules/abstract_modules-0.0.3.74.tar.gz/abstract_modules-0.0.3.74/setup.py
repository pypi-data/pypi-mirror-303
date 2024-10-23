from time import time
import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
    name='abstract_modules',
    version='0.0.3.74',
    author='putkoff',
    author_email='partners@abstractendeavors.com',
    description='abstract_modules allows you to easily upload your Python module to the Python Package Index (PyPI) using Twine. It automates several steps of the packaging and distribution process, making it easier to share your module with the Python community..',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/AbstractEndeavors/abstract_modules',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
    ],
    install_requires=['module_utils', 'pkg_resources', 'abstract_utilities', 'upload_utils', 'setuptools', 'requests', 'abstract_gui'],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    # Add this line to include wheel format in your distribution
    setup_requires=['wheel'],
)
