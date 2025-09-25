"""
    Python script to optimize PDF
    and reduce the pages size in the
    PDF
"""
from pypdf import PdfWriter


# optimize pdf size
def optimize_pdf(input_path: str, output_path: str) -> None:
    print(f"optimizing PDF : {input_path}...")
    writer = PdfWriter(clone_from=input_path)
    for page in writer.pages:
        for img in page.images:
            img.replace(img.image, quality=70)  # Set desired quality

    with open(output_path, "wb") as f:
        writer.write(f)


# init
def main():
    input_pdf_path = input("Enter source pdf location: ")
    output_path = input("Enter destination file: ")
    print("Optimizing...!")
    optimize_pdf(
        input_path=input_pdf_path,
        output_path=output_path
    )

if __name__ == "__main__":
    main()
