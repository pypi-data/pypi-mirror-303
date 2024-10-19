from __future__ import annotations

import gdsfactory as gf
from gdsfactory.component import Component
from gdsfactory.typings import Float2, Layer

layer = (1, 0)
nm = 1e-3


@gf.cell
def width_min(size: Float2 = (0.1, 0.1)) -> Component:
    return gf.components.rectangle(size=size, layer=layer)


@gf.cell
def area_min() -> Component:
    size = (0.2, 0.2)
    return gf.components.rectangle(size=size, layer=layer)


@gf.cell
def gap_min(gap: float = 0.1) -> Component:
    c = gf.Component()
    r1 = c << gf.components.rectangle(size=(1, 1), layer=layer)
    r2 = c << gf.components.rectangle(size=(1, 1), layer=layer)
    r1.dxmax = 0
    r2.dxmin = gap
    return c


@gf.cell
def separation(
    gap: float = 0.1, layer1: Layer = (47, 0), layer2: Layer = (41, 0)
) -> Component:
    c = gf.Component()
    r1 = c << gf.components.rectangle(size=(1, 1), layer=layer1)
    r2 = c << gf.components.rectangle(size=(1, 1), layer=layer2)
    r1.dxmax = 0
    r2.dxmin = gap
    return c


@gf.cell
def enclosing(
    enclosing: float = 0.1, layer1: Layer = (40, 0), layer2: Layer = (41, 0)
) -> Component:
    """Layer1 must be enclosed by layer2 by value.

    checks if layer1 encloses (is bigger than) layer2 by value
    """
    w1 = 1
    w2 = w1 + enclosing
    c = gf.Component()
    c << gf.components.rectangle(size=(w1, w1), layer=layer1, centered=True)
    r2 = c << gf.components.rectangle(size=(w2, w2), layer=layer2, centered=True)
    r2.dmovex(0.5)
    return c


@gf.cell
def snapping_error(gap: float = 1e-3) -> Component:
    c = gf.Component()
    r1 = c << gf.components.rectangle(size=(1, 1), layer=layer)
    r2 = c << gf.components.rectangle(size=(1, 1), layer=layer)
    r1.dxmax = 0
    r2.dxmin = gap
    return c


@gf.cell
def not_inside(layer: Layer = (40, 0), not_inside: Layer = (24, 0)) -> Component:
    """Layer must be inside by layer."""
    enclosing = 0.1
    w1 = 1
    w2 = w1 + enclosing
    c = gf.Component()
    c << gf.components.rectangle(size=(w1, w1), layer=layer, centered=True)
    r2 = c << gf.components.rectangle(size=(w2, w2), layer=not_inside, centered=True)
    r2.dmovex(0.5)
    return c


@gf.cell
def errors() -> Component:
    components = (
        [width_min(), gap_min(), separation(), enclosing(), not_inside()]
        # + [width_min(size=(i * nm, i * nm)) for i in range(1, 199)]
        # + [gap_min(i * nm) for i in range(199)]
    )
    c = gf.pack(components, spacing=1.5)
    return c[0]


if __name__ == "__main__":
    # c = width_min()
    # c.write_gds("wmin.gds")
    # c = gap_min()
    # c.write_gds("gmin.gds")
    # c = snapping_error()
    # c.write_gds("snap.gds")

    c = errors()
    c = gf.add_padding_container(c, layers=((64, 0),), default=5)
    c.write_gds("errors.gds")
    c.show()
