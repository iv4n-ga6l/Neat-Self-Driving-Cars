from render.engine import Engine
from pycache_handler.handler import py_cache_handler

NEAT_CONFIG_PATH = "neat_config.ini"
RAY_CAST = True
MAX_SIMULATIONS = 1000

@py_cache_handler
def main() -> None:
    window = Engine(NEAT_CONFIG_PATH, RAY_CAST, MAX_SIMULATIONS)
    window.run()

if __name__ == "__main__":
    main()
