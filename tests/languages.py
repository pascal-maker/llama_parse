import nest_asyncio
import os

# Apply nest_asyncio to run sync code in a notebook
nest_asyncio.apply()

# Set LLAMA_CLOUD_API_KEY environment variable if necessary
os.environ["LLAMA_CLOUD_API_KEY"] = "llx-WVxYwGsnAzY0buikzirrbABpIsfdJDPZGSg69zblmGItPLFc"

# Load in the French PDF

from llama_parse import LlamaParse

# Initialize LlamaParse with result_type and language parameters
parser = LlamaParse(
    result_type="text",
    language="fr"
)

# Load data from the PDF file
documents = parser.load_data("./treasury_report.pdf")

# Print a portion of the content of the first document
print(documents[0].get_content()[1000:10000])
