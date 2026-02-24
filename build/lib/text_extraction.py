import pypdfium2 as pdfium

def load_pdf(pdf_path): 
    """
    Takes a pdf_path and return the pdf object and the number of pages.
    """
    pdf = pdfium.PdfDocument(pdf_path)
    return pdf

def load_page_number(pdf_obj): 
    """
    Takes a pdf_path and return the number of pages.
    """
    n_pages = len(pdf_obj) 
    return n_pages

def get_page_text(pdf_obj, page_number):
    """
    Get the text from each page.
    """
    for page in pdf_obj: 
        textpage = page.get_textpage()
        text_all = textpage.get_text_bounded()
    print(text_all)


pdf_obj=load_pdf("input_data.pdf")
page_number=load_page_number(pdf_obj)
get_page_text(pdf_obj,page_number)