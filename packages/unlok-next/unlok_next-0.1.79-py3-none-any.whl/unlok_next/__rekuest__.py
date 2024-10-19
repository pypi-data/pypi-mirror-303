def register_structures(structure_reg):
    from rekuest_next.structures.default import (
        PortScope,
        id_shrink,
    )
    from rekuest_next.widgets import SearchWidget
    from unlok_next.api.schema import (
        Room,
        aget_room,
        Stream,
        aget_stream,
    )

    structure_reg.register_as_structure(
        Room,
        identifier="@lok/room",
        aexpand=aget_room,
        ashrink=id_shrink,
        scope=PortScope.GLOBAL,
    )
    structure_reg.register_as_structure(
        Stream,
        identifier="@lok/stream",
        aexpand=aget_stream,
        ashrink=id_shrink,
        scope=PortScope.GLOBAL,
    )
