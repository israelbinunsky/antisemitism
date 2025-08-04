from loader import Loader
from researcher import Researcher

loader = Loader()
researcher = Researcher(loader.df)
researcher.write_results_to_json()