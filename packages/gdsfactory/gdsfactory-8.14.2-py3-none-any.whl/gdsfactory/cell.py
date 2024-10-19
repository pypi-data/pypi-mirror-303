from collections.abc import Callable, Iterable
from typing import Any, ParamSpec, Protocol, overload

from cachetools import Cache
from kfactory.conf import CHECK_INSTANCES
from kfactory.kcell import KCell, MetaData
from kfactory.kcell import cell as _cell

from gdsfactory.component import Component

ComponentParams = ParamSpec("ComponentParams")


class ComponentFunc(Protocol[ComponentParams]):
    def __call__(
        self, *args: ComponentParams.args, **kwargs: ComponentParams.kwargs
    ) -> Component: ...


@overload
def cell(
    _func: ComponentFunc[ComponentParams],
    /,
) -> ComponentFunc[ComponentParams]: ...


@overload
def cell(
    *,
    set_settings: bool = True,
    set_name: bool = True,
    check_ports: bool = True,
    check_instances: CHECK_INSTANCES | None = None,
    snap_ports: bool = True,
    basename: str | None = None,
    drop_params: tuple[str, ...] = ("self", "cls"),
    register_factory: bool = True,
    overwrite_existing: bool | None = None,
    layout_cache: bool | None = None,
    info: dict[str, MetaData] | None = None,
    post_process: Iterable[Callable[[KCell], None]] | None = None,
) -> Callable[[ComponentFunc[ComponentParams]], ComponentFunc[ComponentParams]]: ...


def cell(
    _func: ComponentFunc[ComponentParams] | None = None,
    /,
    *,
    set_settings: bool = True,
    set_name: bool = True,
    check_ports: bool = True,
    check_instances: CHECK_INSTANCES | None = None,
    snap_ports: bool = True,
    add_port_layers: bool = True,
    cache: Cache[int, Any] | dict[int, Any] | None = None,
    basename: str | None = None,
    drop_params: tuple[str, ...] = ("self", "cls"),
    register_factory: bool = True,
    overwrite_existing: bool | None = None,
    layout_cache: bool | None = None,
    info: dict[str, MetaData] | None = None,
    post_process: Iterable[Callable[[KCell], None]] | None = None,
) -> (
    ComponentFunc[ComponentParams]
    | Callable[[ComponentFunc[ComponentParams]], ComponentFunc[ComponentParams]]
):
    """Decorator to convert a function into a Component."""
    if post_process is None:
        post_process = []
    return _cell(  # type: ignore
        _func,
        set_settings=set_settings,
        set_name=set_name,
        check_ports=check_ports,
        check_instances=check_instances,
        snap_ports=snap_ports,
        add_port_layers=add_port_layers,
        cache=cache,
        basename=basename,
        drop_params=list(drop_params),
        register_factory=register_factory,
        overwrite_existing=overwrite_existing,
        layout_cache=layout_cache,
        info=info,
        post_process=post_process,
    )
