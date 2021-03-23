import PyPDF2
import sys

message = '\nPlease type: python3 watermark_pdf.py path/file_to_watermark.pdf path/watermark_file.pdf \n' \
          'You can use absolute or relative path.\n'
try:
    pdf_file = sys.argv[1]

    watermark_file = sys.argv[2]
except IndexError:
    print(f'\nIncorrect number of arguments. {message} ')
    quit()


def watermark_pdf(file, watermark):
    template = PyPDF2.PdfFileReader(open(file, 'rb'))
    watermark = PyPDF2.PdfFileReader(open(watermark, 'rb'))
    watermarked_file = PyPDF2.PdfFileWriter()

    for i in range(template.numPages):
        page = template.getPage(i)
        page.mergePage(watermark.getPage(0))
        watermarked_file.addPage(page)

    split_ext = file.rsplit('.', 1)[0]

    with open(f'{split_ext}_marked.pdf', 'wb') as watermarked:
        watermarked_file.write(watermarked)


if __name__ == '__main__':
    try:
        watermark_pdf(pdf_file, watermark_file)
    except FileNotFoundError as err:
        print(err, message)
    except PyPDF2.utils.PdfReadError:
        print(f'File is not a PDF.{message}')
