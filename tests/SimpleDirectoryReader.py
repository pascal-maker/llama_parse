import nest_asyncio
from llama_parse import LlamaParse

# Apply nest_asyncio to run sync code in a notebook
nest_asyncio.apply()

# Initialize LlamaParse with necessary parameters
parser = LlamaParse(
    api_key="llx-WVxYwGsnAzY0buikzirrbABpIsfdJDPZGSg69zblmGItPLFc",  # Set your LLAMA_CLOUD_API_KEY here
    result_type="markdown",  # Specify the result type
    verbose=True
)

try:
    # Load data directly from the specific PDF file
    documents = parser.load_data("./Masterproef_ArthurSemay.pdf")
    
    # Process the parsed documents (replace with your logic)
    print(documents)
    
except FileNotFoundError as e:
    print("Error: File not found", e)
except Exception as e:  # Catch other potential exceptions
    print("Error:", e)

