from pathlib import Path 
import pymupdf as pdf

import _modules.pdf_engine as pe

filePath = Path("test_environment/files/Story_1.pdf")
file = pdf.open(filePath)


pe.print_pdf(file)