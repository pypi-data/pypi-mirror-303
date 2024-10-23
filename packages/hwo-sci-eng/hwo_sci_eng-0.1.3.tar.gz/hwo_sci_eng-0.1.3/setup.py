from setuptools import setup

setup(name="hwo_sci_eng",
      version="0.1.3",
      description="HWO Science Engineering Interface", 
      author="Breann Sitarski (NASA/GSFC), Jason Tumlinson(STScI/JHU)", 
      author_email=" ",
      license="CC",
      keywords=["simulation", "astronomy", "astrophysics"],
      url="https://github.com/HWO-GOMAP-Working-Groups/Sci-Eng-Interface", 
      packages=["hwo_sci_eng", "hwo_sci_eng/obs_config", "hwo_sci_eng/json", "hwo_sci_eng/utils"], 
      package_data={'':['*.yaml', '*.json', 'json/*json', 'obs_config/*.yaml']}, 
      include_package_data=True,
      classifiers=[
          "Programming Language :: Python :: 3.6",
      ],
      install_requires=[
            "setuptools>=61.0", 
      ],
)
