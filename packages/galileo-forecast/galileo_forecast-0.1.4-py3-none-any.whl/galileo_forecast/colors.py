from dataclasses import dataclass


@dataclass
class PlotColors:
    """
    container for colors to use
    """

    primary_color: str = "220, 71, 52"
    secondary_color: str = "218, 150, 130"
    tertiary_color: str = "242, 205, 105"
    grey_tint_color: str = "170, 170, 171"

    def __post_init__(self):
        self.colors = {
            "primary_color": self.primary_color,
            "secondary_color": self.secondary_color,
            "tertiary_color": self.tertiary_color,
            "grey_tint_color": self.grey_tint_color,
        }

    def get_rgba(self, color: str = "primary_color", opacity: float = 1):
        if color not in self.colors.keys():
            raise ValueError(
                f"{color} is not one of the colors, choose from: {list(self.colors.keys())}"
            )

        return "rgba(" + self.colors[color] + f", {opacity})"

    def get_grey_rgba(self, opacity: float = 1):
        return "rgba(" + self.colors["grey_tint_color"] + f", {opacity})"


POS_COLORS = PlotColors(
    primary_color="220, 71, 52",
    secondary_color="218, 150, 130",
    tertiary_color="242, 205, 105",
    grey_tint_color="170, 170, 171",
)

BCG_COLORS = PlotColors(
    primary_color="40, 186, 116",
    secondary_color="41, 94, 126",
    tertiary_color="153, 204, 235",
    grey_tint_color="110, 111, 115",
)

def main():
    print(POS_COLORS.get_rgba("primary_color"))

if __name__ == "__main__":
    main()