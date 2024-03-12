# llama-parse is async-first, running the sync code in a notebook requires the use of nest_asyncio
import nest_asyncio

nest_asyncio.apply()

import os
from llama_parse import LlamaParse

# Set the LLAMA_CLOUD_API_KEY environment variable
os.environ["LLAMA_CLOUD_API_KEY"] = "llx-WVxYwGsnAzY0buikzirrbABpIsfdJDPZGSg69zblmGItPLFc"

# Load the PDF and parse it, specifying the result_type as "text"
documents = LlamaParse(result_type="text").load_data("./attention.pdf")
print(documents[0].text[6000:7000])

# Parse the same PDF again, but this time specify the result_type as "markdown"
documents = LlamaParse(result_type="markdown").load_data("./attention.pdf")
print(documents[0].text[20000:21000] + "...")
