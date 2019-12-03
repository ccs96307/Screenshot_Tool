# -*- coding: utf-8 -*-
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM


def convert(input, output):
    drawing = svg2rlg(input)
    renderPM.drawToFile(drawing, output, fmt='PNG')