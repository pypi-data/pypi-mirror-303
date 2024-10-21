def generate_latex_document(data: str) -> str:

    return f"""
    \\documentclass{{article}}
    \\usepackage{{graphicx}}
    \\begin{{document}}

    {data}

    \\end{{document}}
    """
