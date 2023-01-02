import os
from dotenv import load_dotenv

# The load_dotenv function will read a file named .env in the current working directory.
# It will then load any environment variables that are defined in the file.
# These environment variables can then be accessed using the os module.
load_dotenv()

CURATATRONU9000_API_TOKEN: str = os.environ['CURATATRONU9000_API_TOKEN']
groupFacetiBaCuratenie: str = os.environ['GROUP_FACETIBACURATENIE_ID']
SUPABASE_URL: str = os.environ.get("SUPABASE_URL")
SUPABASE_KEY: str = os.environ.get("SUPABASE_KEY")