def print_pdf(pdf):
    for pageNum in range(pdf.page_count): 
        print()
        print("Page Number:", pageNum + 1)
        print(pdf.load_page(pageNum).get_text())
        print("-------------------------------------------------")