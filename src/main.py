import pypdf
from PyPDF2 import PdfReader, PdfWriter
import os
from tkinter import Tk, filedialog
from pdf2image import convert_from_path
import matplotlib.pyplot as plt


def select_pdf_file():
    root = Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(initialdir="/mnt/c", filetypes=[("PDF files", "*.pdf")])
    root.destroy()  # Close the root window
    return file_path


def preview_pdf(file_path):
    images = convert_from_path(file_path)
    current_page = [0]  # Use a list to allow modification within nested function

    def show_page(page_num):
        plt.axis("off")
        plt.imshow(images[page_num])
        plt.title(f"Page {page_num + 1} - Press arrow key to see another page")
        plt.draw()

    def on_key(event):
        if event.key == "right":
            current_page[0] = (current_page[0] + 1) % len(images)
        elif event.key == "left":
            current_page[0] = (current_page[0] - 1) % len(images)
        plt.clf()
        show_page(current_page[0])

    fig, ax = plt.subplots()
    fig.canvas.mpl_connect("key_press_event", on_key)
    show_page(current_page[0])
    plt.show()
    print("PDF previewed.")


def get_page_range():
    try:
        page_range = input("Enter the range of pages you want to keep (e.g., 1-3,5): ")
        pages_to_keep = []
        for part in page_range.split(","):
            if "-" in part:
                start, end = map(int, part.split("-"))
                pages_to_keep.extend(range(start, end + 1))
            else:
                pages_to_keep.append(int(part))
        return pages_to_keep
    except ValueError:
        print("Refused")
        quit()


def create_new_pdf(file_path, pages_to_keep):
    reader = PdfReader(file_path)
    writer = PdfWriter()
    for page_num in pages_to_keep:
        writer.add_page(reader.pages[page_num - 1])
    new_file_path = os.path.splitext(file_path)[0] + "_edited.pdf"
    with open(new_file_path, "wb") as f:
        writer.write(f)
    print(f"New PDF created: {new_file_path}")


def main():
    file_path = select_pdf_file()
    if not file_path:
        print("No file selected.")
        return
    preview_pdf(file_path)
    pages_to_keep = get_page_range()
    create_new_pdf(file_path, pages_to_keep)


if __name__ == "__main__":
    main()
