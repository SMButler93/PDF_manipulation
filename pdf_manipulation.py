"""A script for manipulating PDF files. Through this script, PDF files
can be merged together and/or stamped."""

import os
import PyPDF2


def pdf_stamper():
    """Stamps pdf's with specified stamp."""

    # Aquire file paths for files:
    while True:
        doc_in = input(
            "\nEnter the relative file path for the PDF to be stamped: ")
        if os.path.exists(doc_in):
            break
        print("File path does not exist.")

    while True:
        stamp_in = input("\nEnter the relative file path for your stamp PDF: ")
        if os.path.exists(stamp_in):
            break
        print("File path does not exist.")

    stamped_pdf_name = input("\nEnter the name for your new stamped PDF: ")

    # create reader and writer objects:
    doc = PyPDF2.PdfFileReader(open(f"./{doc_in}", "rb"))
    stamp = PyPDF2.PdfFileReader(open(f"./{stamp_in}", "rb"))
    completion = PyPDF2.PdfFileWriter()

    # Create a loop that will stamp PDF's of various lengths:
    for i in range(doc.getNumPages()):
        page = doc.getPage(i)
        page.mergePage(stamp.getPage(0))
        completion.addPage(page)
    # Once all pages have been stamped, write the PDF file:
    with open(stamped_pdf_name, "wb") as file:
        completion.write(file)

    print("\nPDF stamping completed.")


def pdf_merger():
    """merges seperate PDF files together."""
    # Hold file paths for all files in a list:
    file_paths = []
    file_count = 1

    print("\nEnter 'Q' to cancel the adding of a new file")
    while True:
        # Append file paths to list until user has entered all file paths:
        doc = input(
            f"Please enter the relative file path for file number {file_count}: ")
        # check for a valid file path:
        if os.path.exists(doc):
            file_paths.append(doc)
            file_count += 1
        # Allow a user to cancell the adding of another document.
        elif doc.upper() == 'Q':
            print("New file cancelled.")
            break
        else:
            print("That file path does not exist.\n")
            continue

        # nested while loop to ensure response is appropriate:
        while True:
            add_file = input(
                "\nWould you like to add more files to be merged (Y/N): ")

            # If input is valid break out of loop.
            if (n := add_file.upper()) == 'Y' or n == 'N':
                break

            print("Your input was not valid, please tray again.")

        # If 'Y' is entered, repeat the loop to add a new file.
        if add_file.upper() == 'Y':
            continue

        break

    # Allow user to provide name for new merged PDF file name:
    merged_pdf_name = input(
        "Please provide a name for your newly merged PDF file: ")

    # Merge files given from above:
    merger = PyPDF2.PdfFileMerger()
    for pdf_file in file_paths:
        merger.append(pdf_file)
    merger.write(f"./{merged_pdf_name}")

    print("Your file has been merged and saved successfully")


# Main program:
if __name__ == '__main__':

    # PDF merging:
    while True:
        # Give the choice to use merger:
        merger_choice = input("\nWould you like to merge PDF files(Y/N): ")
        # check response:
        if merger_choice.upper() == 'Y':
            pdf_merger()
            break
        elif merger_choice.upper() == 'N':
            break
        else:
            # If input does not match 'Y' or 'N' user informed, and loop repeated:
            print("Your respsonse is not valid. Please enter 'Y' or 'N'.")

    # PDF stamping
    while True:
        # Same structure used as the PDF merging while loop:
        stamper_choice = input("\nWould you like to stamp a PDF file (Y/N): ")

        if stamper_choice.upper() == 'Y':
            pdf_stamper()
            break
        elif stamper_choice.upper() == 'N':
            break
        else:
            # If input does not match 'Y' or 'N' user informed, and loop repeated:
            print("Your respsonse is not valid. Please enter 'Y' or 'N'. ")
