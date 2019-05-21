
# from weasyprint import HTML,CSS
import pdfkit
import os   
options = {
    'quiet': '',
    'page-size': 'A4',
    'margin-top': '0in',
    'margin-right': '0in',
    'margin-bottom': '0in',
    'margin-left': '0in',
    'encoding': "UTF-8",
    'no-outline': None,
    'disable-smart-shrinking': ''
}
pdfkit.from_file("sourcehtmlfile.html","test2.pdf", options=options)
os.startfile("test2.pdf","print")
