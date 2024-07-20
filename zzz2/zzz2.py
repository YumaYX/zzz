import openpyxl


def sheet_to_text(book, sheet, max_rows=1000, max_cols=1000):
    """
    Convert an Excel sheet to a text string.

    :param book: The path to the Excel workbook.
    :type book: str
    :param sheet: The name of the sheet to convert.
    :type sheet: str
    :param max_rows: The maximum number of rows to read (default is 1000).
    :type max_rows: int, optional
    :param max_cols: The maximum number of columns to read (default is 1000).
    :type max_cols: int, optional
    :return: The contents of the sheet as a single string with cell values separated by newlines.
    :rtype: str
    """
    wb = openpyxl.load_workbook(book, data_only=True)
    ws = wb[sheet]

    contents = [
        str(cell.value)
        for row in ws.iter_rows(
            min_row=1, min_col=1, max_row=max_rows, max_col=max_cols
        )
        for cell in row
        if cell.value is not None
    ]

    return "\n".join(contents)
