"""
    Python script to create
    a PDF based on the list of images.
    The pages are ordered according
    to the list index
"""
from PIL import Image


# concatenate pages into a single pdf
def create_pdf_using_pil(image_paths: list[str], output_path: str):
    image_list = [Image.open(img).convert('RGB') for img in image_paths]
    # Save into one PDF file, compress by setting quality and optimize
    if image_list:
        first_image = image_list[0]
        remaining_images = image_list[1:]
        first_image.save(output_path, save_all=True, append_images=remaining_images, quality=85, optimize=True)
    else:
        print("No JPEG images found in directory.")


# init
def main():
    image_paths_input = input("Enter comma-separated paths to JPEG images: ")
    image_paths = [path.strip() for path in image_paths_input.split(',')]
    output_path = input("Enter destination PDF file path: ")
    print("Creating PDF...!")
    create_pdf_using_pil(
        image_paths=image_paths,
        output_path=output_path
    )


if __name__ == "__main__":
    main()
