import nest_asyncio
nest_asyncio.apply()

from llama_parse import LlamaParse

# Replace 'llx-WVxYwGsnAzY0buikzirrbABpIsfdJDPZGSg69zblmGItPLFc' with your actual API key
parser = LlamaParse(api_key="llx-WVxYwGsnAzY0buikzirrbABpIsfdJDPZGSg69zblmGItPLFc", result_type="markdown", verbose=True, language="en")

# Load data synchronously from one PDF
document = parser.load_data("./Masterproef_ArthurSemay.pdf")
# Further processing of the document, such as printing the parsed content
print(document)