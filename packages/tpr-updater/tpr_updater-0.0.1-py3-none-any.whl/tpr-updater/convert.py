import win32com.client as win32
from tkinter import filedialog, Tk
import os

def convert_xls_to_xlsx(xls_file):
    if not os.path.exists(xls_file):
        print(f"File not found: {xls_file}")
        return

    print(f"Converting {xls_file} to {os.path.basename(xls_file).replace('.xls', '.xlsx')}")
    
    excel = win32.Dispatch('Excel.Application')
    excel.Visible = False
    excel.DisplayAlerts = False

    try:
        wb = excel.Workbooks.Open(xls_file)

        # Prompt user to save the file
        print("Please select the location to save the converted file")

        xlsx_file = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])

        if xlsx_file:
            # Normalize the path to use Windows-style separators
            xlsx_file = os.path.normpath(xlsx_file)

            # Ensure the directory exists
            os.makedirs(os.path.dirname(xlsx_file), exist_ok=True)

            # Close any open workbook with the same name
            for open_wb in excel.Workbooks:
                if open_wb.FullName.lower() == xlsx_file.lower():
                    open_wb.Close(SaveChanges=False)

            # Save as .xlsx
            print(f"Saving as {xlsx_file}")
            try:
                wb.SaveAs(xlsx_file, FileFormat=51)
                print(f"Conversion complete. File saved as {xlsx_file}")
            except Exception as save_error:
                print(f"Error saving file: {str(save_error)}")
                # Try an alternative save method
                try:
                    temp_path = os.path.join(os.path.dirname(xlsx_file), "temp_" + os.path.basename(xlsx_file))
                    wb.SaveAs(temp_path, FileFormat=51)
                    os.replace(temp_path, xlsx_file)
                    print(f"Conversion complete using alternative method. File saved as {xlsx_file}")
                except Exception as alt_save_error:
                    print(f"Alternative save method also failed: {str(alt_save_error)}")
        else:
            print("Save operation cancelled.")

        wb.Close()

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        import traceback
        print(traceback.format_exc())

    finally:
        excel.Quit()

    return xlsx_file