from pathlib import Path 
import pymupdf as pdf

import _modules.pdf_engine as pe

filePath = Path("test_environment/files/Story_1.pdf")
file = pdf.open(filePath)
file2 = pdf.open()
file2.insert_pdf(file, to_page=2)
file2.save("test_environment/files/Story_Z.pdf")


# pe.print_pdf(file)
print(file.metadata)


file2.close()


filePic = file.load_page(1)
filePic = filePic.get_pixmap()
filePic.save("test_environment/files/Story_1_0_img.png")
# Returns the raw image data as PNG bytes
# image_bytes = filePic.tobytes("png")
file.close()