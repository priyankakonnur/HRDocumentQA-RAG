from pypdf import PdfReader
#read data from pdf
def load_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)
    text= " "

    for page_number, page in enumerate(reader.pages):   #trying to loop through each page
        extracted = page.extract_text()         #extracting text from each page
        if extracted:
            text += f"\n--- Page {page_number + 1} ---\n"
            text += extracted
    return text


# file_path = r"E:\Microdegree AIML\coding\GenAI_Projects\Generative-AI\Rag\hr_policy_detailed_5_pages.pdf"

# data = load_pdf(file_path)
# print(data[:1000])  # print first 1000 chars only