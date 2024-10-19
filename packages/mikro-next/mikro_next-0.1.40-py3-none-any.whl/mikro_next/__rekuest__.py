from mikro_next.api.schema import (
    EntityRelation,
    SearchEntityRelationsQuery,
    aget_entity_relation,
)


def register_structures(structure_reg):
    from rekuest_next.structures.default import (
        PortScope,
        id_shrink,
    )
    from rekuest_next.widgets import SearchWidget
    from mikro_next.api.schema import (
        Image,
        aget_image,
        SearchImagesQuery,
        Dataset,
        Stage,
        aget_stage,
        File,
        aget_file,
        SearchStagesQuery,
        SearchFilesQuery,
        ProtocolStep,
        aget_protocol_step,
        SearchProtocolStepsQuery,
        aget_rgb_context,
        RGBContext,
        aget_dataset,
    )
    from mikro_next.api.schema import (
        Snapshot,
        aget_snapshot,
        SearchSnapshotsQuery,
        Ontology,
        aget_ontology,
        Entity,
        ROI,
        Reagent,
        aget_reagent,
        SearchReagentsQuery,
        aget_roi,
        aget_entity,
        SearchOntologiesQuery,
        SearchEntitiesQuery,
        aget_rendered_plot,
        RenderedPlot,
        Protocol,
        aget_protocol,
        SearchRoisQuery,
        SearchProtocolsQuery,
        SearchRenderedPlotsQuery,
        LinkedExpression,
        aget_linked_expression,
        SearchLinkedExpressionsQuery,
    )

    structure_reg.register_as_structure(
        Image,
        identifier="@mikro/image",
        aexpand=aget_image,
        ashrink=id_shrink,
        scope=PortScope.GLOBAL,
        default_widget=SearchWidget(
            query=SearchImagesQuery.Meta.document, ward="mikro"
        ),
    )
    structure_reg.register_as_structure(
        Snapshot,
        identifier="@mikro/snapshot",
        aexpand=aget_snapshot,
        ashrink=id_shrink,
        scope=PortScope.GLOBAL,
        default_widget=SearchWidget(
            query=SearchSnapshotsQuery.Meta.document, ward="mikro"
        ),
    )

    structure_reg.register_as_structure(
        ROI,
        identifier="@mikro/roi",
        aexpand=aget_roi,
        ashrink=id_shrink,
        scope=PortScope.GLOBAL,
        default_widget=SearchWidget(query=SearchRoisQuery.Meta.document, ward="mikro"),
    )
    structure_reg.register_as_structure(
        Stage,
        identifier="@mikro/stage",
        aexpand=aget_stage,
        ashrink=id_shrink,
        scope=PortScope.GLOBAL,
        default_widget=SearchWidget(
            query=SearchStagesQuery.Meta.document, ward="mikro"
        ),
    )
    structure_reg.register_as_structure(
        Dataset,
        identifier="@mikro/dataset",
        aexpand=aget_dataset,
        ashrink=id_shrink,
        scope=PortScope.GLOBAL,
        default_widget=SearchWidget(
            query=SearchImagesQuery.Meta.document, ward="mikro"
        ),
    )
    structure_reg.register_as_structure(
        File,
        identifier="@mikro/file",
        aexpand=aget_file,
        ashrink=id_shrink,
        scope=PortScope.GLOBAL,
        default_widget=SearchWidget(query=SearchFilesQuery.Meta.document, ward="mikro"),
    )
    structure_reg.register_as_structure(
        RGBContext,
        identifier="@mikro/rbgcontext",
        aexpand=aget_rgb_context,
        ashrink=id_shrink,
        scope=PortScope.GLOBAL,
    )

    structure_reg.register_as_structure(
        LinkedExpression,
        identifier="@mikro/linked_expression",
        aexpand=aget_linked_expression,
        ashrink=id_shrink,
        scope=PortScope.GLOBAL,
        default_widget=SearchWidget(
            query=SearchLinkedExpressionsQuery.Meta.document, ward="mikro"
        ),
    )

    structure_reg.register_as_structure(
        Ontology,
        identifier="@mikro/ontology",
        aexpand=aget_ontology,
        ashrink=id_shrink,
        scope=PortScope.GLOBAL,
        default_widget=SearchWidget(
            query=SearchOntologiesQuery.Meta.document, ward="mikro"
        ),
    )

    structure_reg.register_as_structure(
        RenderedPlot,
        identifier="@mikro/renderedplot",
        aexpand=aget_rendered_plot,
        ashrink=id_shrink,
        scope=PortScope.GLOBAL,
        default_widget=SearchWidget(
            query=SearchRenderedPlotsQuery.Meta.document, ward="mikro"
        ),
    )

    structure_reg.register_as_structure(
        Entity,
        identifier="@mikro/entity",
        aexpand=aget_entity,
        ashrink=id_shrink,
        scope=PortScope.GLOBAL,
        default_widget=SearchWidget(
            query=SearchEntitiesQuery.Meta.document, ward="mikro"
        ),
    )
    structure_reg.register_as_structure(
        Reagent,
        identifier="@mikro/reagent",
        aexpand=aget_reagent,
        ashrink=id_shrink,
        scope=PortScope.GLOBAL,
        default_widget=SearchWidget(
            query=SearchReagentsQuery.Meta.document, ward="mikro"
        ),
    )

    structure_reg.register_as_structure(
        EntityRelation,
        identifier="@mikro/entity_relation",
        aexpand=aget_entity_relation,
        ashrink=id_shrink,
        scope=PortScope.GLOBAL,
        default_widget=SearchWidget(
            query=SearchEntityRelationsQuery.Meta.document, ward="mikro"
        ),
    )

    structure_reg.register_as_structure(
        Protocol,
        identifier="@mikro/protocol",
        aexpand=aget_protocol,
        ashrink=id_shrink,
        scope=PortScope.GLOBAL,
        default_widget=SearchWidget(
            query=SearchProtocolsQuery.Meta.document, ward="mikro"
        ),
    )

    structure_reg.register_as_structure(
        ProtocolStep,
        identifier="@mikro/protocolstep",
        aexpand=aget_protocol_step,
        ashrink=id_shrink,
        scope=PortScope.GLOBAL,
        default_widget=SearchWidget(
            query=SearchProtocolStepsQuery.Meta.document, ward="mikro"
        ),
    )
