import multiprocessing

from dotenv import load_dotenv

__version__ = "0.1.1"

multiprocessing.set_start_method("spawn", force=True)

load_dotenv()
