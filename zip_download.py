from io import BytesIO
import zipfile


def generate_zip(files):
    mem_zip = BytesIO()

    with zipfile.ZipFile(mem_zip, mode="w",compression=zipfile.ZIP_DEFLATED) as zf:
        for f in files:
            zf.writestr(f[0], f[1])

    return mem_zip.getvalue()
 
def generate_pdf():
	from reportlab.pdfgen.canvas import Canvas
	from reportlab.lib.pagesizes import A4
	buffer = BytesIO()
	canvas = Canvas(buffer, pagesize=A4)
	textobject = canvas.beginText(1.5 , -2.5 )
	textobject.textLine("Hello, world!")
	canvas.saveState()
	canvas.save()
	pdf = buffer.getvalue()
	buffer.close()
	return pdf
	
def main():
	file_names = ["test1.pdf", "test2.pdf"]
	files = []

	for f in file_names:
		pdf = generate_pdf() # your file generation method goes here
		files.append((f, pdf))

	full_zip_in_memory = generate_zip(files)


if __name__ == "__main__":
	main()
