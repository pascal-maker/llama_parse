import asyncio
import nest_asyncio
from llama_parse import LlamaParse
import os


async def extract_text(pdf_path, result_type="text"):
    """Extracts text or markdown content from a PDF file asynchronously.

    Args:
        pdf_path (str): Path to the PDF file.
        result_type (str, optional): Desired output format, "text" or "markdown". Defaults to "text".

    Returns:
        str: Extracted text content from the PDF file.
    """

    os.environ["LLAMA_CLOUD_API_KEY"] = "llx-WVxYwGsnAzY0buikzirrbABpIsfdJDPZGSg69zblmGItPLFc"  # Replace with your API key
    parser = LlamaParse(result_type=result_type)

    # Asynchronous parsing
    documents = await parser.aload_data(pdf_path)

    # Access extracted text from the first document
    return documents[0].text


async def main():
    """Main function to demonstrate asynchronous text extraction."""

    pdf_path = "./Masterproef_ArthurSemay.pdf"  # Path to your PDF file
    result_type = "text"  # Choose "text" or "markdown"

    extracted_text = await extract_text(pdf_path, result_type)
    print(extracted_text)  # Print the entire extracted text


if __name__ == "__main__":
    nest_asyncio.apply()
    asyncio.run(main())  # Run the main function asynchronously
