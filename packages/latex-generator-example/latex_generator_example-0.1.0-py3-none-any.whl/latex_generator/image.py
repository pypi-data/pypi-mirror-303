def generate_latex_image(image_path, caption="Пример картинки", width="0.5\\textwidth"):

    latex_image = (
        "\\begin{figure}[ht]\n"
        "\\centering\n"
        f"\\includegraphics[width={width}]{{{image_path}}}\n"
        f"\\caption{{{caption}}}\n"
        "\\end{figure}\n"
    )
    return latex_image
