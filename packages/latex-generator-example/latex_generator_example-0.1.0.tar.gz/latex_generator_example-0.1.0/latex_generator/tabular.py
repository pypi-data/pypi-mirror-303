def generate_latex_table(data: list, table_name: str) -> str:

    if not data or not all(isinstance(row, list) for row in data):
        raise ValueError
    
    num_columns = len(data[0])
    
    latex_table = "\\begin{table}[ht]\n\\centering\n\\begin{tabular}{" + "|".join(['c'] * num_columns) + "}\n\\hline\n"
    
    for row in data:
        latex_table += " & ".join(str(cell) for cell in row) + " \\\\\n\\hline\n"
    
    latex_table += f"\\end{{tabular}}\n\\caption{{{table_name}}}\n\\end{{table}}"

    
    return latex_table
