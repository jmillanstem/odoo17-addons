/** @odoo-module **/
import { getColor } from "@web/core/colors/colors";

// Paleta de colores en tonos azules
var blue_theme_color = ["#003f5c", "#2f4b7c", "#665191", "#a05195", "#d45087",
        "#f95d6a", "#ff7c43", "#ffa600", "#003f5c", "#2f4b7c", "#665191",
        "#a05195", "#d45087", "#f95d6a", "#ff7c43", "#ffa600", "#003f5c",
        "#2f4b7c", "#665191", "#a05195"];

// Sustituir los colores predeterminados por los colores personalizados.
for (let i = 0; i < blue_theme_color.length; i++) {
    getColor[i] = blue_theme_color[i];
}
