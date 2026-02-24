import pypdfium2 as pdfium
import yaml 

def load_pdf(pdf_path): 
    """
    Takes a pdf_path and return the pdf object and the number of pages.
    """
    pdf = pdfium.PdfDocument(pdf_path)
    return pdf

def get_page_text(pdf_obj):
    """
    Get the text from each page and writes a dict {page_number: text}.
    """
    for page in pdf_obj: 
        n_pages = len(pdf_obj)
        
        textpage = page.get_textpage()
        text_all = textpage.get_text_bounded()
        text_dict={n_pages:text_all}
    return text_dict

def put_text_in_file(text_dict, output_file):
    """
    Given text in a file it writes an output yaml file with that text and page number.
    """
    with open(output_file, "w") as file: 
        yaml.dump(text_dict)
    

pdf_obj=load_pdf("core/input/input_data.pdf")
text_dict=get_page_text(pdf_obj)
print(text_dict)
put_text_in_file(text_dict, "/Users/jacquiline/Desktop/2_Code/Personal/FlashCardsSystem/FlashCard_system/core/output/pdf_text.yaml")