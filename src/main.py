from loader import Loader
from researcher import Researcher

loader = Loader()
researcher = Researcher(loader.df)
researcher.length_calculation()