from io import BytesIO
from matplotlib import pyplot as plt


def tex2svg(formula, fontsize=25, dpi=300):
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