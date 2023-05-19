from os import path

import matplotlib.pyplot as plt
from io import BytesIO

def path_sand():
    p =  "D:\\semester8\\Diploma\\app\\static/data/uploads\\data\\time_value_3.txt"
    abs_path = path.abspath(p)
    base_name = path.basename(p)
    dirname = path.dirname(p)
    splited_path = path.split(p)
    print(f"p: {p}")
    print(f"abs_path: {abs_path}")
    print(f"basename: {base_name}")
    print(f"dirname: {dirname}")
    print(f"splited_path:\n{splited_path}")




def tex2svg(formula, fontsize=2, dpi=300):
        """Render TeX formula to SVG.

        Args:
            formula (str): TeX formula.
            fontsize (int, optional): Font size.
            dpi (int, optional): DPI.

        Returns:
            str: SVG render.
        """
        fig = plt.figure(figsize=(100, 100))
        fig.text(0, 0, r'{}'.format(formula), fontsize=fontsize)
        output = BytesIO()
        fig.savefig(output, dpi=dpi, transparent=True, format='svg', bbox_inches='tight', pad_inches=0.0)
        plt.close(fig)
        output.seek(0)
        data_str = output.read().decode("utf-8")
        return data_str

svg_data = tex2svg(formula=r'$x = \frac{-10.58 z^4 - 21.15 z^3 - 31.72 z^2 - 2.3 z + 0.5}{67.5 z^5 - 105.8 z^4 + 63.75 z^3 - 9.625 z^2 - 5.75 z + 1}\quad dt = 0.06$', fontsize=50)
with open("app/templates/svg_test.svg", "w") as f:
    f.write(svg_data)


