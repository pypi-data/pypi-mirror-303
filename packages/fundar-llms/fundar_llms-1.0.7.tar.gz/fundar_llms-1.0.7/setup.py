from setuptools import setup, find_packages # type: ignore

setup(
    version = '1.0.7',
    name='fundar_llms',
    author='Fundar',
    description="LLM utilities created for Fundar's dev projects.",
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.10',
    setup_requires=['setuptools-git-versioning'],
    version_config={
       "dirty_template": "{tag}",
   }
)