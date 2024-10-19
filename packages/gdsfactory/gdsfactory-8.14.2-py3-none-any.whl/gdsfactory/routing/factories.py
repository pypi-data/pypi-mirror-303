from __future__ import annotations

from gdsfactory.routing.route_bundle import (
    route_bundle,
    route_bundle_electrical,
)
from gdsfactory.routing.route_bundle_all_angle import route_bundle_all_angle

routing_strategy = dict(
    route_bundle=route_bundle,
    route_bundle_electrical=route_bundle_electrical,
    route_bundle_all_angle=route_bundle_all_angle,
)
