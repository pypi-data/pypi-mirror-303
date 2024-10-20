import sgqlc.types


utils_api_schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
class AccessLevelSorting(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('id', 'name', 'order')


class AccountSorting(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('creator', 'id', 'key', 'lastUpdater', 'name', 'platformKey', 'systemRegistrationDate', 'systemUpdateDate', 'url')


Boolean = sgqlc.types.Boolean

class ChildVisibility(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('all', 'childrenOnly')


class ComponentView(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('keyValue', 'value')


class CompositePropertyValueTemplateSorting(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('id', 'name', 'registrationDate')


class ConceptLinkDirection(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('from', 'to')


class ConceptLinkTypeSorting(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('conceptType', 'id', 'name')


class ConceptPropertyTypeSorting(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('name', 'registrationDate')


class ConceptPropertyValueTypeSorting(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('id', 'name')


class ConceptSorting(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('id', 'name', 'score', 'systemRegistrationDate', 'systemUpdateDate')


class ConceptTypeLinkMetadata(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('creator', 'endDate', 'lastUpdater', 'linkType', 'registrationDate', 'startDate', 'updateDate')


class ConceptTypeMetadata(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('concept', 'conceptType', 'creator', 'endDate', 'image', 'lastUpdater', 'markers', 'name', 'notes', 'startDate', 'systemRegistrationDate', 'systemUpdateDate')


class ConceptTypePresentationWidgetTypeSorting(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('id', 'name', 'order')


class ConceptTypeSorting(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('dictionary', 'id', 'name', 'regexp')


class ConceptUpdate(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('link', 'linkProperty', 'metadata', 'property')


class ConceptVariant(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('event', 'obj')


class DocumentContentType(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('image', 'text')


class DocumentGrouping(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('none', 'story')


class DocumentGroupingCategory(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('account', 'accountCountry', 'concept', 'conceptLinkType', 'conceptPropertyType', 'conceptPropertyValue', 'conceptType', 'documentLanguage', 'marker', 'platform', 'platformCountry', 'platformLanguage', 'platformType', 'publicationAuthor')


class DocumentSorting(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('countLinks', 'countNamedEntities', 'id', 'publicationDate', 'registrationDate', 'relevance', 'score', 'title', 'updateDate')


class DocumentSourceType(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('external', 'internal')


class DocumentTypeSorting(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('dictionary', 'id', 'name', 'regexp')


class DocumentUpdate(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('content', 'markup', 'metadata')


class DomainName(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('compositeConceptPropertyType', 'compositeLinkPropertyType', 'conceptPropertyType', 'conceptType', 'conceptTypePresentation', 'conceptTypePresentationWidgetType', 'linkPropertyType', 'linkType', 'valueType')


class FactStatus(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('approved', 'auto', 'autoApproved', 'declined', 'hidden', 'new')


Float = sgqlc.types.Float

ID = sgqlc.types.ID

Int = sgqlc.types.Int

class IssuePriority(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('High', 'Low', 'Medium')


class IssueSorting(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('creator', 'executor', 'id', 'lastUpdater', 'priority', 'registrationDate', 'status', 'topic', 'updateDate')


class IssueStatus(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('canceled', 'closed', 'dataRequested', 'development', 'improvementRequested', 'open', 'reviewRequested')


class JSON(sgqlc.types.Scalar):
    __schema__ = utils_api_schema


class KbFactStatus(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('approved', 'notApproved')


class KbFactStatusFilter(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('all', 'approved', 'notApproved')


class LinkDirection(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('in', 'out', 'undirected')


class Locale(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('eng', 'other', 'ru')


class Long(sgqlc.types.Scalar):
    __schema__ = utils_api_schema


class MapEdgeType(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('conceptCandidateFactMention', 'conceptFactLink', 'conceptImplicitLink', 'conceptLink', 'conceptLinkCandidateFact', 'conceptMention', 'conceptTypeLink', 'documentLink')


class MapNodeType(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('concept', 'conceptCandidateFact', 'conceptType', 'document', 'documentType')


class MentionLinkType(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('equivalent', 'reference', 'translation')


class Name(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('approvedPropsRelevance', 'conceptApprovedPropsRelevance', 'conceptFactRelevance', 'conceptMeaningPropsRelevance', 'conceptNercRelevance', 'conceptNercSearchRelevance', 'conceptPropsRelevance', 'conceptSubstituteRelevance', 'factRelevance', 'mapApprovedPropsRelevance', 'mapFactRelevance', 'mapMeaningPropsRelevance', 'mapNercRelevance', 'mapNercSearchRelevance', 'mapPropsRelevance', 'meaningPropsRelevance', 'nercRelevance', 'nercSearchRelevance', 'propsRelevance', 'queryScore', 'significantTextRelevance', 'totalRelevance')


class NodeType(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('base64', 'cell', 'file', 'header', 'image', 'json', 'key', 'list', 'other', 'row', 'table', 'text')


class PlatformSorting(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('creator', 'id', 'key', 'lastUpdater', 'name', 'platformType', 'systemRegistrationDate', 'systemUpdateDate', 'url')


class PlatformType(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('blog', 'database', 'fileStorage', 'forum', 'government', 'media', 'messenger', 'newsAggregator', 'procurement', 'review', 'socialNetwork')


class PropLinkOrConcept(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('concept', 'link')


class ResearchMapSorting(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('accessLevel', 'conceptAndDocumentLink', 'conceptLink', 'creator', 'documentLink', 'id', 'lastUpdater', 'name', 'systemRegistrationDate', 'systemUpdateDate')


class SortDirection(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('ascending', 'descending')


String = sgqlc.types.String

class TrustLevel(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('high', 'low', 'medium')


class UnixTime(sgqlc.types.Scalar):
    __schema__ = utils_api_schema


class ValueType(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('Date', 'Double', 'Geo', 'Int', 'Link', 'String', 'StringLocale', 'Timestamp')


class WidgetTypeTableType(sgqlc.types.Enum):
    __schema__ = utils_api_schema
    __choices__ = ('horizontal', 'vertical')



########################################################################
# Input Objects
########################################################################
class AccountFilterSettings(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('search_string', 'ids', 'keys', 'platform_ids', 'country', 'markers', 'creator', 'last_updater', 'registration_date', 'update_date')
    search_string = sgqlc.types.Field(String, graphql_name='searchString')
    ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids')
    keys = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='keys')
    platform_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='platformIds')
    country = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='country')
    markers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='markers')
    creator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='creator')
    last_updater = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='lastUpdater')
    registration_date = sgqlc.types.Field('TimestampInterval', graphql_name='registrationDate')
    update_date = sgqlc.types.Field('TimestampInterval', graphql_name='updateDate')


class AccountGetOrCreateInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('key', 'platform_key', 'name', 'url')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    platform_key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='platformKey')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')


class AliasCreateInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('concept_id', 'value')
    concept_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptId')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class AnnotationInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('start', 'end', 'node_id')
    start = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='start')
    end = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='end')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='nodeId')


class BatchUpdateFactInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('access_level_id', 'concept_fact', 'concept_property_fact', 'concept_link_fact', 'concept_link_property_fact', 'property_value_fact', 'composite_property_value_component_fact', 'composite_property_value_fact', 'property_value_mention_fact', 'mention')
    access_level_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='accessLevelId')
    concept_fact = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ConceptFactInput')), graphql_name='conceptFact')
    concept_property_fact = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ConceptPropertyFactInput')), graphql_name='conceptPropertyFact')
    concept_link_fact = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ConceptLinkFactInput')), graphql_name='conceptLinkFact')
    concept_link_property_fact = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ConceptLinkPropertyFactInput')), graphql_name='conceptLinkPropertyFact')
    property_value_fact = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('PropertyValueFactInput')), graphql_name='propertyValueFact')
    composite_property_value_component_fact = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('CompositePropertyValueComponentFactInput')), graphql_name='compositePropertyValueComponentFact')
    composite_property_value_fact = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('CompositePropertyValueFactInput')), graphql_name='compositePropertyValueFact')
    property_value_mention_fact = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('PropertyValueMentionFactInput')), graphql_name='propertyValueMentionFact')
    mention = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('MentionInput')), graphql_name='mention')


class CompositePropertyValueComponentFactInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'component_value_type_id', 'composite_property_value_fact_id', 'value_fact_id', 'reject')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    component_value_type_id = sgqlc.types.Field(ID, graphql_name='componentValueTypeId')
    composite_property_value_fact_id = sgqlc.types.Field(ID, graphql_name='compositePropertyValueFactId')
    value_fact_id = sgqlc.types.Field(ID, graphql_name='valueFactId')
    reject = sgqlc.types.Field(Boolean, graphql_name='reject')


class CompositePropertyValueFactInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'composite_value_type_id', 'reject')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    composite_value_type_id = sgqlc.types.Field(ID, graphql_name='compositeValueTypeId')
    reject = sgqlc.types.Field(Boolean, graphql_name='reject')


class CompositePropertyValueTemplateFilterSettings(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('name', 'creator', 'last_updater', 'registration_date', 'update_date')
    name = sgqlc.types.Field(String, graphql_name='name')
    creator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='creator')
    last_updater = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='lastUpdater')
    registration_date = sgqlc.types.Field('TimestampInterval', graphql_name='registrationDate')
    update_date = sgqlc.types.Field('TimestampInterval', graphql_name='updateDate')


class ConceptExtraSettings(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('search_on_map', 'selected_content')
    search_on_map = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='searchOnMap')
    selected_content = sgqlc.types.Field('ResearchMapContentSelectInput', graphql_name='selectedContent')


class ConceptFactInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'concept_type_id', 'concept_id', 'reject', 'approved')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    concept_type_id = sgqlc.types.Field(ID, graphql_name='conceptTypeId')
    concept_id = sgqlc.types.Field(ID, graphql_name='conceptId')
    reject = sgqlc.types.Field(Boolean, graphql_name='reject')
    approved = sgqlc.types.Field(Boolean, graphql_name='approved')


class ConceptFactsCreationInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('document_id', 'access_level_id', 'concept_fact', 'concept_property_fact', 'property_value_fact', 'composite_property_value_component_fact', 'composite_property_value_fact', 'property_value_mention_fact', 'mention')
    document_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='documentId')
    access_level_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='accessLevelId')
    concept_fact = sgqlc.types.Field(sgqlc.types.non_null(ConceptFactInput), graphql_name='conceptFact')
    concept_property_fact = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptPropertyFactInput'))), graphql_name='conceptPropertyFact')
    property_value_fact = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PropertyValueFactInput'))), graphql_name='propertyValueFact')
    composite_property_value_component_fact = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CompositePropertyValueComponentFactInput)), graphql_name='compositePropertyValueComponentFact')
    composite_property_value_fact = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CompositePropertyValueFactInput)), graphql_name='compositePropertyValueFact')
    property_value_mention_fact = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('PropertyValueMentionFactInput')), graphql_name='propertyValueMentionFact')
    mention = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('MentionInput')), graphql_name='mention')


class ConceptFilterSettings(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('property_filter_settings', 'link_filter_settings', 'concept_type_ids', 'concept_variant', 'name', 'exact_name', 'substring', 'access_level_id', 'creator', 'last_updater', 'creation_date', 'update_date', 'markers', 'has_linked_issues', 'status')
    property_filter_settings = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('PropertyFilterSettings')), graphql_name='propertyFilterSettings')
    link_filter_settings = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('LinkFilterSettings')), graphql_name='linkFilterSettings')
    concept_type_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='conceptTypeIds')
    concept_variant = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ConceptVariant)), graphql_name='conceptVariant')
    name = sgqlc.types.Field(String, graphql_name='name')
    exact_name = sgqlc.types.Field(String, graphql_name='exactName')
    substring = sgqlc.types.Field(String, graphql_name='substring')
    access_level_id = sgqlc.types.Field(ID, graphql_name='accessLevelId')
    creator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='creator')
    last_updater = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='lastUpdater')
    creation_date = sgqlc.types.Field('TimestampInterval', graphql_name='creationDate')
    update_date = sgqlc.types.Field('TimestampInterval', graphql_name='updateDate')
    markers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='markers')
    has_linked_issues = sgqlc.types.Field(Boolean, graphql_name='hasLinkedIssues')
    status = sgqlc.types.Field(KbFactStatusFilter, graphql_name='status')


class ConceptLinkFactInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'link_type_id', 'concept_from_fact_id', 'concept_to_fact_id', 'reject', 'approved')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    link_type_id = sgqlc.types.Field(ID, graphql_name='linkTypeId')
    concept_from_fact_id = sgqlc.types.Field(ID, graphql_name='conceptFromFactId')
    concept_to_fact_id = sgqlc.types.Field(ID, graphql_name='conceptToFactId')
    reject = sgqlc.types.Field(Boolean, graphql_name='reject')
    approved = sgqlc.types.Field(Boolean, graphql_name='approved')


class ConceptLinkFilterSettings(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('is_event', 'concept_link_type', 'document_id', 'creation_date', 'update_date', 'other_concept_name', 'value_type', 'value', 'status')
    is_event = sgqlc.types.Field(Boolean, graphql_name='isEvent')
    concept_link_type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='conceptLinkType')
    document_id = sgqlc.types.Field(ID, graphql_name='documentId')
    creation_date = sgqlc.types.Field('TimestampInterval', graphql_name='creationDate')
    update_date = sgqlc.types.Field('TimestampInterval', graphql_name='updateDate')
    other_concept_name = sgqlc.types.Field(String, graphql_name='otherConceptName')
    value_type = sgqlc.types.Field(ValueType, graphql_name='valueType')
    value = sgqlc.types.Field('ValueFilter', graphql_name='value')
    status = sgqlc.types.Field(KbFactStatusFilter, graphql_name='status')


class ConceptLinkPropertyFactInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'link_property_type_id', 'concept_link_fact_id', 'value_fact_id', 'reject', 'approved')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    link_property_type_id = sgqlc.types.Field(ID, graphql_name='linkPropertyTypeId')
    concept_link_fact_id = sgqlc.types.Field(ID, graphql_name='conceptLinkFactId')
    value_fact_id = sgqlc.types.Field(ID, graphql_name='valueFactId')
    reject = sgqlc.types.Field(Boolean, graphql_name='reject')
    approved = sgqlc.types.Field(Boolean, graphql_name='approved')


class ConceptLinkTypeFilterSettings(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('name', 'concept_from_type_id', 'concept_to_type_id', 'concept_type_and_event_filter', 'is_directed', 'is_hierarchical', 'creator', 'last_updater', 'registration_date', 'update_date', 'has_rel_ext_models')
    name = sgqlc.types.Field(String, graphql_name='name')
    concept_from_type_id = sgqlc.types.Field(ID, graphql_name='conceptFromTypeId')
    concept_to_type_id = sgqlc.types.Field(ID, graphql_name='conceptToTypeId')
    concept_type_and_event_filter = sgqlc.types.Field('conceptTypeAndEventFilter', graphql_name='conceptTypeAndEventFilter')
    is_directed = sgqlc.types.Field(Boolean, graphql_name='isDirected')
    is_hierarchical = sgqlc.types.Field(Boolean, graphql_name='isHierarchical')
    creator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='creator')
    last_updater = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='lastUpdater')
    registration_date = sgqlc.types.Field('TimestampInterval', graphql_name='registrationDate')
    update_date = sgqlc.types.Field('TimestampInterval', graphql_name='updateDate')
    has_rel_ext_models = sgqlc.types.Field(Boolean, graphql_name='hasRelExtModels')


class ConceptMentionCountBatchInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('inputs', 'limit', 'extend_results')
    inputs = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptMentionCountInput'))), graphql_name='inputs')
    limit = sgqlc.types.Field(Int, graphql_name='limit')
    extend_results = sgqlc.types.Field(Boolean, graphql_name='extendResults')


class ConceptMentionCountInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('term', 'concept_types')
    term = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='term')
    concept_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='conceptTypes')


class ConceptMutationInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('name', 'concept_type_id', 'notes', 'fact_info', 'markers', 'access_level_id', 'start_date', 'end_date')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    concept_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptTypeId')
    notes = sgqlc.types.Field(String, graphql_name='notes')
    fact_info = sgqlc.types.Field('FactInput', graphql_name='factInfo')
    markers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='markers')
    access_level_id = sgqlc.types.Field(ID, graphql_name='accessLevelId')
    start_date = sgqlc.types.Field('DateTimeInput', graphql_name='startDate')
    end_date = sgqlc.types.Field('DateTimeInput', graphql_name='endDate')


class ConceptPropertyFactInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'property_type_id', 'concept_fact_id', 'value_fact_id', 'reject', 'approved')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    property_type_id = sgqlc.types.Field(ID, graphql_name='propertyTypeId')
    concept_fact_id = sgqlc.types.Field(ID, graphql_name='conceptFactId')
    value_fact_id = sgqlc.types.Field(ID, graphql_name='valueFactId')
    reject = sgqlc.types.Field(Boolean, graphql_name='reject')
    approved = sgqlc.types.Field(Boolean, graphql_name='approved')


class ConceptPropertyFilterSettings(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('only_main', 'document_id', 'property_type', 'value_type', 'value', 'status')
    only_main = sgqlc.types.Field(Boolean, graphql_name='onlyMain')
    document_id = sgqlc.types.Field(ID, graphql_name='documentId')
    property_type = sgqlc.types.Field(ID, graphql_name='propertyType')
    value_type = sgqlc.types.Field(ValueType, graphql_name='valueType')
    value = sgqlc.types.Field('ValueFilter', graphql_name='value')
    status = sgqlc.types.Field(KbFactStatusFilter, graphql_name='status')


class ConceptPropertyTypeFilterSettings(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('name', 'concept_type_id', 'concept_type_name', 'concept_link_type_id', 'concept_link_type_name', 'concept_value_type_id', 'value_type', 'concept_type_from_link_type_id')
    name = sgqlc.types.Field(String, graphql_name='name')
    concept_type_id = sgqlc.types.Field(ID, graphql_name='conceptTypeId')
    concept_type_name = sgqlc.types.Field(String, graphql_name='conceptTypeName')
    concept_link_type_id = sgqlc.types.Field(ID, graphql_name='conceptLinkTypeId')
    concept_link_type_name = sgqlc.types.Field(String, graphql_name='conceptLinkTypeName')
    concept_value_type_id = sgqlc.types.Field(ID, graphql_name='conceptValueTypeId')
    value_type = sgqlc.types.Field(ValueType, graphql_name='valueType')
    concept_type_from_link_type_id = sgqlc.types.Field(ID, graphql_name='conceptTypeFromLinkTypeId')


class ConceptPropertyValueTypeFilterSettings(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('name', 'value_type', 'creator', 'last_updater', 'registration_date', 'update_date', 'regexp_exists', 'dictionary_exists', 'pretrained_nercmodels')
    name = sgqlc.types.Field(String, graphql_name='name')
    value_type = sgqlc.types.Field(ValueType, graphql_name='valueType')
    creator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='creator')
    last_updater = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='lastUpdater')
    registration_date = sgqlc.types.Field('TimestampInterval', graphql_name='registrationDate')
    update_date = sgqlc.types.Field('TimestampInterval', graphql_name='updateDate')
    regexp_exists = sgqlc.types.Field(Boolean, graphql_name='regexpExists')
    dictionary_exists = sgqlc.types.Field(Boolean, graphql_name='dictionaryExists')
    pretrained_nercmodels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pretrainedNERCModels')


class ConceptTypeFilterSettings(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('name', 'is_event', 'creator', 'last_updater', 'registration_date', 'update_date', 'regexp_exists', 'dictionary_exists', 'pretrained_nercmodels')
    name = sgqlc.types.Field(String, graphql_name='name')
    is_event = sgqlc.types.Field(Boolean, graphql_name='isEvent')
    creator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='creator')
    last_updater = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='lastUpdater')
    registration_date = sgqlc.types.Field('TimestampInterval', graphql_name='registrationDate')
    update_date = sgqlc.types.Field('TimestampInterval', graphql_name='updateDate')
    regexp_exists = sgqlc.types.Field(Boolean, graphql_name='regexpExists')
    dictionary_exists = sgqlc.types.Field(Boolean, graphql_name='dictionaryExists')
    pretrained_nercmodels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pretrainedNERCModels')


class CoordinatesInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('latitude', 'longitude')
    latitude = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='latitude')
    longitude = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='longitude')


class DateInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('year', 'month', 'day')
    year = sgqlc.types.Field(Int, graphql_name='year')
    month = sgqlc.types.Field(Int, graphql_name='month')
    day = sgqlc.types.Field(Int, graphql_name='day')


class DateTimeInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('date', 'time')
    date = sgqlc.types.Field(sgqlc.types.non_null(DateInput), graphql_name='date')
    time = sgqlc.types.Field('TimeInput', graphql_name='time')


class DateTimeIntervalInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('start', 'end')
    start = sgqlc.types.Field(DateTimeInput, graphql_name='start')
    end = sgqlc.types.Field(DateTimeInput, graphql_name='end')


class DocumentDoubleCreationInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('uuid', 'double_uuid', 'parent_uuid', 'concept_id', 'job_id', 'periodic_job_id', 'task_id', 'periodic_task_id')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='uuid')
    double_uuid = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='doubleUuid')
    parent_uuid = sgqlc.types.Field(ID, graphql_name='parentUuid')
    concept_id = sgqlc.types.Field(ID, graphql_name='conceptId')
    job_id = sgqlc.types.Field(String, graphql_name='jobId')
    periodic_job_id = sgqlc.types.Field(String, graphql_name='periodicJobId')
    task_id = sgqlc.types.Field(String, graphql_name='taskId')
    periodic_task_id = sgqlc.types.Field(String, graphql_name='periodicTaskId')


class DocumentFilterSettings(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('search_string', 'substring', 'named_entities', 'concepts', 'meaning_concept_candidates', 'platforms', 'accounts', 'nerc_num', 'concepts_num', 'child_docs_num', 'publication_date', 'registration_date', 'last_update', 'creator', 'publication_author', 'last_updater', 'access_level_id', 'links', 'external_url', 'markers', 'document_content_type', 'source_type', 'trust_level', 'has_linked_issues', 'nested_ids', 'fact_types', 'story', 'show_read', 'job_ids', 'periodic_job_ids', 'task_ids', 'periodic_task_ids', 'document_is_media', 'document_is_processed', 'child_visibility')
    search_string = sgqlc.types.Field(String, graphql_name='searchString')
    substring = sgqlc.types.Field(String, graphql_name='substring')
    named_entities = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='namedEntities')
    concepts = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='concepts')
    meaning_concept_candidates = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='meaningConceptCandidates')
    platforms = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='platforms')
    accounts = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='accounts')
    nerc_num = sgqlc.types.Field('IntervalInt', graphql_name='nercNum')
    concepts_num = sgqlc.types.Field('IntervalInt', graphql_name='conceptsNum')
    child_docs_num = sgqlc.types.Field('IntervalInt', graphql_name='childDocsNum')
    publication_date = sgqlc.types.Field('TimestampInterval', graphql_name='publicationDate')
    registration_date = sgqlc.types.Field('TimestampInterval', graphql_name='registrationDate')
    last_update = sgqlc.types.Field('TimestampInterval', graphql_name='lastUpdate')
    creator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='creator')
    publication_author = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='publicationAuthor')
    last_updater = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='lastUpdater')
    access_level_id = sgqlc.types.Field(ID, graphql_name='accessLevelId')
    links = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='links')
    external_url = sgqlc.types.Field(String, graphql_name='externalUrl')
    markers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='markers')
    document_content_type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DocumentContentType)), graphql_name='documentContentType')
    source_type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DocumentSourceType)), graphql_name='sourceType')
    trust_level = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TrustLevel)), graphql_name='trustLevel')
    has_linked_issues = sgqlc.types.Field(Boolean, graphql_name='hasLinkedIssues')
    nested_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='nestedIds')
    fact_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='factTypes')
    story = sgqlc.types.Field(String, graphql_name='story')
    show_read = sgqlc.types.Field(Boolean, graphql_name='showRead')
    job_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='jobIds')
    periodic_job_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='periodicJobIds')
    task_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='taskIds')
    periodic_task_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='periodicTaskIds')
    document_is_media = sgqlc.types.Field(Boolean, graphql_name='documentIsMedia')
    document_is_processed = sgqlc.types.Field(Boolean, graphql_name='documentIsProcessed')
    child_visibility = sgqlc.types.Field(ChildVisibility, graphql_name='childVisibility')


class DocumentRelevanceMetricsInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('nerc_relevance', 'fact_relevance', 'props_relevance', 'approved_props_relevance', 'meaning_props_relevance', 'concept_substitute_relevance', 'nerc_search_relevance', 'significant_text_relevance', 'concept_nerc_relevance', 'concept_fact_relevance', 'concept_props_relevance', 'concept_approved_props_relevance', 'concept_meaning_props_relevance', 'concept_nerc_search_relevance', 'map_nerc_relevance', 'map_fact_relevance', 'map_props_relevance', 'map_approved_props_relevance', 'map_meaning_props_relevance', 'map_nerc_search_relevance')
    nerc_relevance = sgqlc.types.Field(Int, graphql_name='nercRelevance')
    fact_relevance = sgqlc.types.Field(Int, graphql_name='factRelevance')
    props_relevance = sgqlc.types.Field(Int, graphql_name='propsRelevance')
    approved_props_relevance = sgqlc.types.Field(Int, graphql_name='approvedPropsRelevance')
    meaning_props_relevance = sgqlc.types.Field(Int, graphql_name='meaningPropsRelevance')
    concept_substitute_relevance = sgqlc.types.Field(Int, graphql_name='conceptSubstituteRelevance')
    nerc_search_relevance = sgqlc.types.Field(Int, graphql_name='nercSearchRelevance')
    significant_text_relevance = sgqlc.types.Field(Int, graphql_name='significantTextRelevance')
    concept_nerc_relevance = sgqlc.types.Field(Int, graphql_name='conceptNercRelevance')
    concept_fact_relevance = sgqlc.types.Field(Int, graphql_name='conceptFactRelevance')
    concept_props_relevance = sgqlc.types.Field(Int, graphql_name='conceptPropsRelevance')
    concept_approved_props_relevance = sgqlc.types.Field(Int, graphql_name='conceptApprovedPropsRelevance')
    concept_meaning_props_relevance = sgqlc.types.Field(Int, graphql_name='conceptMeaningPropsRelevance')
    concept_nerc_search_relevance = sgqlc.types.Field(Int, graphql_name='conceptNercSearchRelevance')
    map_nerc_relevance = sgqlc.types.Field(Int, graphql_name='mapNercRelevance')
    map_fact_relevance = sgqlc.types.Field(Int, graphql_name='mapFactRelevance')
    map_props_relevance = sgqlc.types.Field(Int, graphql_name='mapPropsRelevance')
    map_approved_props_relevance = sgqlc.types.Field(Int, graphql_name='mapApprovedPropsRelevance')
    map_meaning_props_relevance = sgqlc.types.Field(Int, graphql_name='mapMeaningPropsRelevance')
    map_nerc_search_relevance = sgqlc.types.Field(Int, graphql_name='mapNercSearchRelevance')


class DocumentTypeFilterSettings(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('name', 'creator', 'last_updater', 'registration_date', 'update_date', 'regexp_exists', 'dictionary_exists', 'pretrained_nercmodels')
    name = sgqlc.types.Field(String, graphql_name='name')
    creator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='creator')
    last_updater = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='lastUpdater')
    registration_date = sgqlc.types.Field('TimestampInterval', graphql_name='registrationDate')
    update_date = sgqlc.types.Field('TimestampInterval', graphql_name='updateDate')
    regexp_exists = sgqlc.types.Field(Boolean, graphql_name='regexpExists')
    dictionary_exists = sgqlc.types.Field(Boolean, graphql_name='dictionaryExists')
    pretrained_nercmodels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pretrainedNERCModels')


class DocumentsTextWithMarkerByDateInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('marker', 'start_date', 'end_date')
    marker = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='marker')
    start_date = sgqlc.types.Field(UnixTime, graphql_name='startDate')
    end_date = sgqlc.types.Field(UnixTime, graphql_name='endDate')


class DocumentsWithConceptByDateInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('concept_type_id', 'start_date', 'end_date')
    concept_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptTypeId')
    start_date = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='startDate')
    end_date = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='endDate')


class DoubleValueInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('double',)
    double = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='double')


class ExtraSettings(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('search_on_map', 'ranking_script', 'selected_content')
    search_on_map = sgqlc.types.Field(Boolean, graphql_name='searchOnMap')
    ranking_script = sgqlc.types.Field(String, graphql_name='rankingScript')
    selected_content = sgqlc.types.Field('ResearchMapContentSelectInput', graphql_name='selectedContent')


class FactInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('document_id', 'annotations', 'fact_id', 'add_as_name')
    document_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='documentId')
    annotations = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TextBoundingInput')), graphql_name='annotations')
    fact_id = sgqlc.types.Field(ID, graphql_name='factId')
    add_as_name = sgqlc.types.Field(Boolean, graphql_name='addAsName')


class GeoPointFormInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('latitude', 'longitude')
    latitude = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='latitude')
    longitude = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='longitude')


class GeoPointInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('point', 'name')
    point = sgqlc.types.Field(CoordinatesInput, graphql_name='point')
    name = sgqlc.types.Field(String, graphql_name='name')


class GeoPointWithNameFormInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('point', 'name', 'radius', 'area')
    point = sgqlc.types.Field(GeoPointFormInput, graphql_name='point')
    name = sgqlc.types.Field(String, graphql_name='name')
    radius = sgqlc.types.Field(Float, graphql_name='radius')
    area = sgqlc.types.Field('GeoRectangularAreaFormInput', graphql_name='area')


class GeoRectangularAreaFormInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('latitude_min', 'longitude_min', 'latitude_max', 'longitude_max')
    latitude_min = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='latitudeMin')
    longitude_min = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='longitudeMin')
    latitude_max = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='latitudeMax')
    longitude_max = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='longitudeMax')


class IntValueInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('int',)
    int = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='int')


class IntervalDouble(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('start', 'end')
    start = sgqlc.types.Field(Float, graphql_name='start')
    end = sgqlc.types.Field(Float, graphql_name='end')


class IntervalInt(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('start', 'end')
    start = sgqlc.types.Field(Int, graphql_name='start')
    end = sgqlc.types.Field(Int, graphql_name='end')


class IssueFilterSettings(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('executor', 'creator', 'last_updater', 'status', 'priority', 'registration_date', 'update_date', 'issue_for_document', 'issue_for_concept', 'only_my', 'issue', 'concept', 'document', 'name', 'description', 'execution_time_limit', 'markers')
    executor = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='executor')
    creator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='creator')
    last_updater = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='lastUpdater')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IssueStatus)), graphql_name='status')
    priority = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IssuePriority)), graphql_name='priority')
    registration_date = sgqlc.types.Field('TimestampInterval', graphql_name='registrationDate')
    update_date = sgqlc.types.Field('TimestampInterval', graphql_name='updateDate')
    issue_for_document = sgqlc.types.Field(Boolean, graphql_name='issueForDocument')
    issue_for_concept = sgqlc.types.Field(Boolean, graphql_name='issueForConcept')
    only_my = sgqlc.types.Field(Boolean, graphql_name='onlyMy')
    issue = sgqlc.types.Field(ID, graphql_name='issue')
    concept = sgqlc.types.Field(ID, graphql_name='concept')
    document = sgqlc.types.Field(ID, graphql_name='document')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    execution_time_limit = sgqlc.types.Field('TimestampInterval', graphql_name='executionTimeLimit')
    markers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='markers')


class LinkFilterSettings(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('link_type_id', 'link_direction', 'other_concept_id', 'status')
    link_type_id = sgqlc.types.Field(ID, graphql_name='linkTypeId')
    link_direction = sgqlc.types.Field(LinkDirection, graphql_name='linkDirection')
    other_concept_id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='otherConceptId')
    status = sgqlc.types.Field(KbFactStatusFilter, graphql_name='status')


class LinkValueInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('link',)
    link = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='link')


class LinkedDocumentFilterSettings(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('document_content_type',)
    document_content_type = sgqlc.types.Field(DocumentContentType, graphql_name='documentContentType')


class MapEdgeFilterSettings(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('edge_type',)
    edge_type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MapEdgeType)), graphql_name='edgeType')


class MapNodeFilterSettings(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('node_type',)
    node_type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MapNodeType)), graphql_name='nodeType')


class MentionInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'annotation')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    annotation = sgqlc.types.Field(AnnotationInput, graphql_name='annotation')


class PlatformFilterSettings(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('ids', 'keys', 'search_string', 'platform_type', 'markers', 'country', 'language', 'creator', 'last_updater', 'registration_date', 'update_date')
    ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids')
    keys = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='keys')
    search_string = sgqlc.types.Field(String, graphql_name='searchString')
    platform_type = sgqlc.types.Field(PlatformType, graphql_name='platformType')
    markers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='markers')
    country = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='country')
    language = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='language')
    creator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='creator')
    last_updater = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='lastUpdater')
    registration_date = sgqlc.types.Field('TimestampInterval', graphql_name='registrationDate')
    update_date = sgqlc.types.Field('TimestampInterval', graphql_name='updateDate')


class PlatformGetOrCreateInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('key', 'name', 'platform_type', 'url')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    platform_type = sgqlc.types.Field(sgqlc.types.non_null(PlatformType), graphql_name='platformType')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')


class PropertyFilterSettings(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('property_type_id', 'component_id', 'property_type', 'string_filter', 'int_filter', 'double_filter', 'date_time_filter', 'geo_filter', 'status')
    property_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='propertyTypeId')
    component_id = sgqlc.types.Field(ID, graphql_name='componentId')
    property_type = sgqlc.types.Field(sgqlc.types.non_null(PropLinkOrConcept), graphql_name='propertyType')
    string_filter = sgqlc.types.Field('StringFilter', graphql_name='stringFilter')
    int_filter = sgqlc.types.Field(IntervalInt, graphql_name='intFilter')
    double_filter = sgqlc.types.Field(IntervalDouble, graphql_name='doubleFilter')
    date_time_filter = sgqlc.types.Field(DateTimeIntervalInput, graphql_name='dateTimeFilter')
    geo_filter = sgqlc.types.Field(GeoPointWithNameFormInput, graphql_name='geoFilter')
    status = sgqlc.types.Field(KbFactStatusFilter, graphql_name='status')


class PropertyValueFactInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'value', 'reject')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    value = sgqlc.types.Field('ValueInput', graphql_name='value')
    reject = sgqlc.types.Field(Boolean, graphql_name='reject')


class PropertyValueMentionFactInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'value_fact_id', 'mention_id', 'reject')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    value_fact_id = sgqlc.types.Field(ID, graphql_name='valueFactId')
    mention_id = sgqlc.types.Field(ID, graphql_name='mentionId')
    reject = sgqlc.types.Field(Boolean, graphql_name='reject')


class ResearchMapContentSelectInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('nodes',)
    nodes = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='nodes')


class ResearchMapContentUpdateInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('nodes',)
    nodes = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='nodes')


class ResearchMapFilterSettings(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('name', 'description', 'access_level_id', 'creator', 'last_updater', 'markers', 'creation_date', 'update_date', 'concept_id')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    access_level_id = sgqlc.types.Field(ID, graphql_name='accessLevelId')
    creator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='creator')
    last_updater = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='lastUpdater')
    markers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='markers')
    creation_date = sgqlc.types.Field('TimestampInterval', graphql_name='creationDate')
    update_date = sgqlc.types.Field('TimestampInterval', graphql_name='updateDate')
    concept_id = sgqlc.types.Field(ID, graphql_name='conceptId')


class S3FileInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('bucket_name', 'object_name')
    bucket_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bucketName')
    object_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='objectName')


class StringFilter(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('str', 'exact')
    str = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='str')
    exact = sgqlc.types.Field(Boolean, graphql_name='exact')


class StringLocaleValueInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('str', 'locale')
    str = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='str')
    locale = sgqlc.types.Field(sgqlc.types.non_null(Locale), graphql_name='locale')


class StringValueInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('str',)
    str = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='str')


class TextBoundingInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('component_id', 'start', 'end', 'node_id')
    component_id = sgqlc.types.Field(ID, graphql_name='componentId')
    start = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='start')
    end = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='end')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='nodeId')


class TimeInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('hour', 'minute', 'second')
    hour = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='hour')
    minute = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='minute')
    second = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='second')


class TimestampInterval(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('start', 'end')
    start = sgqlc.types.Field(UnixTime, graphql_name='start')
    end = sgqlc.types.Field(UnixTime, graphql_name='end')


class TimestampValueInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('value',)
    value = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='value')


class ValueFilter(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('string_filter', 'int_filter', 'double_filter', 'date_time_filter', 'geo_filter')
    string_filter = sgqlc.types.Field(StringFilter, graphql_name='stringFilter')
    int_filter = sgqlc.types.Field(IntervalInt, graphql_name='intFilter')
    double_filter = sgqlc.types.Field(IntervalDouble, graphql_name='doubleFilter')
    date_time_filter = sgqlc.types.Field(DateTimeIntervalInput, graphql_name='dateTimeFilter')
    geo_filter = sgqlc.types.Field(GeoPointWithNameFormInput, graphql_name='geoFilter')


class ValueInput(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('string_value_input', 'string_locale_value_input', 'int_value_input', 'double_value_input', 'geo_point_value_input', 'date_time_value_input', 'link_value_input', 'timestamp_value_input')
    string_value_input = sgqlc.types.Field(StringValueInput, graphql_name='stringValueInput')
    string_locale_value_input = sgqlc.types.Field(StringLocaleValueInput, graphql_name='stringLocaleValueInput')
    int_value_input = sgqlc.types.Field(IntValueInput, graphql_name='intValueInput')
    double_value_input = sgqlc.types.Field(DoubleValueInput, graphql_name='doubleValueInput')
    geo_point_value_input = sgqlc.types.Field(GeoPointInput, graphql_name='geoPointValueInput')
    date_time_value_input = sgqlc.types.Field(DateTimeInput, graphql_name='dateTimeValueInput')
    link_value_input = sgqlc.types.Field(LinkValueInput, graphql_name='linkValueInput')
    timestamp_value_input = sgqlc.types.Field(TimestampValueInput, graphql_name='timestampValueInput')


class conceptTypeAndEventFilter(sgqlc.types.Input):
    __schema__ = utils_api_schema
    __field_names__ = ('full_type', 'is_event')
    full_type = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='fullType')
    is_event = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isEvent')



########################################################################
# Output Objects and Interfaces
########################################################################
class DocumentGroupFacet(sgqlc.types.Interface):
    __schema__ = utils_api_schema
    __field_names__ = ('group', 'count')
    group = sgqlc.types.Field(sgqlc.types.non_null(DocumentGroupingCategory), graphql_name='group')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count')


class EntityTypePresentation(sgqlc.types.Interface):
    __schema__ = utils_api_schema
    __field_names__ = ('metric', 'list_concept_link_type', 'show_in_menu')
    metric = sgqlc.types.Field(sgqlc.types.non_null('EntityTypePresentationStatistics'), graphql_name='metric')
    list_concept_link_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptLinkType'))), graphql_name='listConceptLinkType')
    show_in_menu = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='showInMenu')


class FactInterface(sgqlc.types.Interface):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'system_registration_date', 'system_update_date', 'document')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    system_registration_date = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='systemRegistrationDate')
    system_update_date = sgqlc.types.Field(UnixTime, graphql_name='systemUpdateDate')
    document = sgqlc.types.Field(sgqlc.types.non_null('Document'), graphql_name='document')


class HasTypeSearchElements(sgqlc.types.Interface):
    __schema__ = utils_api_schema
    __field_names__ = ('pretrained_nercmodels', 'list_white_dictionary', 'list_white_regexp', 'list_black_dictionary', 'list_black_regexp', 'list_type_search_element', 'list_type_black_search_element')
    pretrained_nercmodels = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='pretrainedNERCModels')
    list_white_dictionary = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='listWhiteDictionary')
    list_white_regexp = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('NERCRegexp'))), graphql_name='listWhiteRegexp')
    list_black_dictionary = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='listBlackDictionary')
    list_black_regexp = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('NERCRegexp'))), graphql_name='listBlackRegexp')
    list_type_search_element = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TypeSearchElement'))), graphql_name='listTypeSearchElement')
    list_type_black_search_element = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TypeSearchElement'))), graphql_name='listTypeBlackSearchElement')


class LinkTarget(sgqlc.types.Interface):
    __schema__ = utils_api_schema
    __field_names__ = ('pagination_link',)
    pagination_link = sgqlc.types.Field(sgqlc.types.non_null('ConceptLinkPagination'), graphql_name='paginationLink', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptLinkFilterSettings), graphql_name='filterSettings', default=None)),
))
    )


class LinkTypeTarget(sgqlc.types.Interface):
    __schema__ = utils_api_schema
    __field_names__ = ('list_link_type', 'pagination_link_type')
    list_link_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptLinkType'))), graphql_name='listLinkType')
    pagination_link_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptLinkTypePagination'), graphql_name='paginationLinkType', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptLinkTypeFilterSettings), graphql_name='filterSettings', default=None)),
        ('sort_direction', sgqlc.types.Arg(SortDirection, graphql_name='sortDirection', default='descending')),
        ('sorting', sgqlc.types.Arg(ConceptLinkTypeSorting, graphql_name='sorting', default='id')),
))
    )


class MentionInterface(sgqlc.types.Interface):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'system_registration_date', 'system_update_date', 'document', 'mention_fact')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    system_registration_date = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='systemRegistrationDate')
    system_update_date = sgqlc.types.Field(UnixTime, graphql_name='systemUpdateDate')
    document = sgqlc.types.Field(sgqlc.types.non_null('Document'), graphql_name='document')
    mention_fact = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FactInterface))), graphql_name='mentionFact')


class PropertyTarget(sgqlc.types.Interface):
    __schema__ = utils_api_schema
    __field_names__ = ('pagination_property',)
    pagination_property = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyPagination'), graphql_name='paginationProperty', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptPropertyFilterSettings), graphql_name='filterSettings', default=None)),
))
    )


class PropertyTypeTarget(sgqlc.types.Interface):
    __schema__ = utils_api_schema
    __field_names__ = ('list_property_type', 'pagination_property_type')
    list_property_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptPropertyType'))), graphql_name='listPropertyType')
    pagination_property_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyTypePagination'), graphql_name='paginationPropertyType', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptPropertyTypeFilterSettings), graphql_name='filterSettings', default=None)),
        ('sort_direction', sgqlc.types.Arg(SortDirection, graphql_name='sortDirection', default='descending')),
        ('sorting', sgqlc.types.Arg(ConceptPropertyTypeSorting, graphql_name='sorting', default='name')),
))
    )


class RecordInterface(sgqlc.types.Interface):
    __schema__ = utils_api_schema
    __field_names__ = ('system_registration_date', 'system_update_date', 'creator', 'last_updater')
    system_registration_date = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='systemRegistrationDate')
    system_update_date = sgqlc.types.Field(UnixTime, graphql_name='systemUpdateDate')
    creator = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='creator')
    last_updater = sgqlc.types.Field('User', graphql_name='lastUpdater')


class EntityType(sgqlc.types.Interface):
    __schema__ = utils_api_schema
    __field_names__ = ('pretrained_nercmodels', 'list_white_dictionary', 'list_white_regexp', 'list_black_dictionary', 'id', 'name', 'x_coordinate', 'y_coordinate', 'list_black_regexp', 'metric', 'pagination_concept_property_type', 'pagination_concept_link_type', 'list_concept_property_type', 'list_concept_link_type', 'list_concept_header_property_type', 'image', 'image_new', 'full_dictionary', 'non_configurable_dictionary', 'list_names_dictionary', 'list_property_type', 'pagination_property_type', 'list_link_type', 'pagination_link_type', 'list_type_search_element', 'list_type_black_search_element')
    pretrained_nercmodels = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='pretrainedNERCModels')
    list_white_dictionary = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='listWhiteDictionary')
    list_white_regexp = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('NERCRegexp'))), graphql_name='listWhiteRegexp')
    list_black_dictionary = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='listBlackDictionary')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    x_coordinate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='xCoordinate')
    y_coordinate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yCoordinate')
    list_black_regexp = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('NERCRegexp'))), graphql_name='listBlackRegexp')
    metric = sgqlc.types.Field(sgqlc.types.non_null('EntityTypeStatistics'), graphql_name='metric')
    pagination_concept_property_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyTypePagination'), graphql_name='paginationConceptPropertyType', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptPropertyTypeFilterSettings), graphql_name='filterSettings', default=None)),
        ('sort_direction', sgqlc.types.Arg(SortDirection, graphql_name='sortDirection', default='descending')),
        ('sorting', sgqlc.types.Arg(ConceptPropertyTypeSorting, graphql_name='sorting', default='name')),
))
    )
    pagination_concept_link_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptLinkTypePagination'), graphql_name='paginationConceptLinkType', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptLinkTypeFilterSettings), graphql_name='filterSettings', default=None)),
        ('sort_direction', sgqlc.types.Arg(SortDirection, graphql_name='sortDirection', default='descending')),
        ('sorting', sgqlc.types.Arg(ConceptLinkTypeSorting, graphql_name='sorting', default='id')),
))
    )
    list_concept_property_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptPropertyType'))), graphql_name='listConceptPropertyType')
    list_concept_link_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptLinkType'))), graphql_name='listConceptLinkType')
    list_concept_header_property_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptPropertyType'))), graphql_name='listConceptHeaderPropertyType')
    image = sgqlc.types.Field('Image', graphql_name='image')
    image_new = sgqlc.types.Field('Image', graphql_name='imageNew')
    full_dictionary = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='fullDictionary')
    non_configurable_dictionary = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='nonConfigurableDictionary')
    list_names_dictionary = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='listNamesDictionary')
    list_property_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptPropertyType'))), graphql_name='listPropertyType')
    pagination_property_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyTypePagination'), graphql_name='paginationPropertyType', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptPropertyTypeFilterSettings), graphql_name='filterSettings', default=None)),
        ('sort_direction', sgqlc.types.Arg(SortDirection, graphql_name='sortDirection', default='descending')),
        ('sorting', sgqlc.types.Arg(ConceptPropertyTypeSorting, graphql_name='sorting', default='name')),
))
    )
    list_link_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptLinkType'))), graphql_name='listLinkType')
    pagination_link_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptLinkTypePagination'), graphql_name='paginationLinkType', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptLinkTypeFilterSettings), graphql_name='filterSettings', default=None)),
        ('sort_direction', sgqlc.types.Arg(SortDirection, graphql_name='sortDirection', default='descending')),
        ('sorting', sgqlc.types.Arg(ConceptLinkTypeSorting, graphql_name='sorting', default='id')),
))
    )
    list_type_search_element = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TypeSearchElement'))), graphql_name='listTypeSearchElement')
    list_type_black_search_element = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TypeSearchElement'))), graphql_name='listTypeBlackSearchElement')


class KBEntity(sgqlc.types.Interface):
    __schema__ = utils_api_schema
    __field_names__ = ('pagination_property', 'pagination_link', 'id')
    pagination_property = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyPagination'), graphql_name='paginationProperty', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptPropertyFilterSettings), graphql_name='filterSettings', default=None)),
))
    )
    pagination_link = sgqlc.types.Field(sgqlc.types.non_null('ConceptLinkPagination'), graphql_name='paginationLink', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptLinkFilterSettings), graphql_name='filterSettings', default=None)),
))
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class AccessLevel(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'name', 'order')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    order = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='order')


class AccessLevelPagination(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('list_access_level', 'total')
    list_access_level = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AccessLevel))), graphql_name='listAccessLevel')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class AccountFacet(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('value', 'count')
    value = sgqlc.types.Field(sgqlc.types.non_null('Account'), graphql_name='value')
    count = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='count')


class AccountPagination(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('list_account', 'total', 'total_platforms')
    list_account = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Account'))), graphql_name='listAccount')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')
    total_platforms = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalPlatforms')


class AccountStatistics(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('count_doc',)
    count_doc = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countDoc')


class Annotation(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('start', 'end', 'value')
    start = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='start')
    end = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='end')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class CompositePropertyValueTemplatePagination(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('list_composite_property_value_template', 'total')
    list_composite_property_value_template = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CompositePropertyValueTemplate'))), graphql_name='listCompositePropertyValueTemplate')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class CompositePropertyValueType(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'name', 'value_type', 'is_required', 'view')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyValueType'), graphql_name='valueType')
    is_required = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRequired')
    view = sgqlc.types.Field(sgqlc.types.non_null(ComponentView), graphql_name='view')


class CompositeValue(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('list_value',)
    list_value = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('NamedValue'))), graphql_name='listValue')


class ConceptCandidateFactMention(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('concept', 'mention')
    concept = sgqlc.types.Field(sgqlc.types.non_null('ConceptCandidateFact'), graphql_name='concept')
    mention = sgqlc.types.Field(sgqlc.types.non_null('Mention'), graphql_name='mention')


class ConceptFacet(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('count', 'value')
    count = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='count')
    value = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='value')


class ConceptFactLink(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('concept_id', 'concept_fact_id', 'status', 'is_implicit', 'concept', 'concept_fact')
    concept_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptId')
    concept_fact_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptFactId')
    status = sgqlc.types.Field(FactStatus, graphql_name='status')
    is_implicit = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isImplicit')
    concept = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='concept')
    concept_fact = sgqlc.types.Field(sgqlc.types.non_null('ConceptCandidateFact'), graphql_name='conceptFact')


class ConceptFactPagination(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('total', 'list_concept_fact')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')
    list_concept_fact = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptFact'))), graphql_name='listConceptFact')


class ConceptImplicitLink(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('concept_from_id', 'concept_to_id', 'concept_from', 'concept_to', 'concept_link_type')
    concept_from_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptFromId')
    concept_to_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptToId')
    concept_from = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='conceptFrom')
    concept_to = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='conceptTo')
    concept_link_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptLinkType'), graphql_name='conceptLinkType')


class ConceptLinkFactPagination(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('total', 'list_concept_link_fact')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')
    list_concept_link_fact = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptLinkFact'))), graphql_name='listConceptLinkFact')


class ConceptLinkPagination(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('total', 'list_concept_link')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')
    list_concept_link = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptLink'))), graphql_name='listConceptLink')


class ConceptLinkTypePagination(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('list_concept_link_type', 'total')
    list_concept_link_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptLinkType'))), graphql_name='listConceptLinkType')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class ConceptLinkTypePath(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('link_type', 'fixed')
    link_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptLinkType'), graphql_name='linkType')
    fixed = sgqlc.types.Field(ConceptLinkDirection, graphql_name='fixed')


class ConceptLinkTypeStatistics(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('count_property_type',)
    count_property_type = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countPropertyType')


class ConceptMention(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('concept', 'mention')
    concept = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='concept')
    mention = sgqlc.types.Field(sgqlc.types.non_null('Mention'), graphql_name='mention')


class ConceptMentionCount(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('concept', 'count')
    concept = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='concept')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count')


class ConceptPagination(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('total', 'show_total', 'list_concept', 'precise_total')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')
    show_total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='showTotal')
    list_concept = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Concept'))), graphql_name='listConcept')
    precise_total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='preciseTotal')


class ConceptPaginationResult(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('total', 'show_total', 'list_concept')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')
    show_total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='showTotal')
    list_concept = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Concept'))), graphql_name='listConcept')


class ConceptPropertyPagination(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('total', 'list_concept_property')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')
    list_concept_property = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptProperty'))), graphql_name='listConceptProperty')


class ConceptPropertyTypePagination(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('list_concept_property_type', 'total')
    list_concept_property_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptPropertyType'))), graphql_name='listConceptPropertyType')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class ConceptPropertyValueStatistics(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('count_concept_type', 'count_link_type', 'count_dictionary', 'count_regexp')
    count_concept_type = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countConceptType')
    count_link_type = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countLinkType')
    count_dictionary = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countDictionary')
    count_regexp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countRegexp')


class ConceptPropertyValueTypePagination(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('list_concept_property_value_type', 'total')
    list_concept_property_value_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptPropertyValueType'))), graphql_name='listConceptPropertyValueType')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class ConceptStatistics(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('count_properties', 'count_objects', 'count_events', 'count_document_facts', 'count_potential_documents', 'count_research_maps', 'count_tasks', 'count_concepts', 'count_document_mentions', 'count_concepts_and_documents')
    count_properties = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countProperties')
    count_objects = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countObjects')
    count_events = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countEvents')
    count_document_facts = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countDocumentFacts')
    count_potential_documents = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countPotentialDocuments')
    count_research_maps = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countResearchMaps')
    count_tasks = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countTasks')
    count_concepts = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countConcepts')
    count_document_mentions = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countDocumentMentions')
    count_concepts_and_documents = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countConceptsAndDocuments')


class ConceptSubscriptions(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('subscriptions', 'list_user', 'count_users')
    subscriptions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptUpdate))), graphql_name='subscriptions')
    list_user = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='listUser')
    count_users = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countUsers')


class ConceptTypePagination(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('list_concept_type', 'total')
    list_concept_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptType'))), graphql_name='listConceptType')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class ConceptTypePresentationWidgetTypeColumn(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'name', 'is_main_properties', 'list_values', 'sort_by_column', 'sort_direction', 'concept_link_types_path', 'property_type', 'metadata', 'link_property_type', 'link_metadata', 'sortable')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    is_main_properties = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isMainProperties')
    list_values = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='listValues')
    sort_by_column = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='sortByColumn')
    sort_direction = sgqlc.types.Field(SortDirection, graphql_name='sortDirection')
    concept_link_types_path = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptLinkTypePath))), graphql_name='conceptLinkTypesPath')
    property_type = sgqlc.types.Field('ConceptPropertyType', graphql_name='propertyType')
    metadata = sgqlc.types.Field(ConceptTypeMetadata, graphql_name='metadata')
    link_property_type = sgqlc.types.Field('ConceptPropertyType', graphql_name='linkPropertyType')
    link_metadata = sgqlc.types.Field(ConceptTypeLinkMetadata, graphql_name='linkMetadata')
    sortable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='sortable')


class ConceptTypePresentationWidgetTypePagination(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('list_concept_type_presentation_widget', 'total')
    list_concept_type_presentation_widget = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptTypePresentationWidgetType'))), graphql_name='listConceptTypePresentationWidget')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class ConceptTypeViewPagination(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('list_concept_type_view', 'total')
    list_concept_type_view = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptTypeView'))), graphql_name='listConceptTypeView')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class ConceptView(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('concept', 'rows')
    concept = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='concept')
    rows = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptViewValue'))))), graphql_name='rows')


class ConceptViewPagination(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('total', 'list_concept_view')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')
    list_concept_view = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptView))), graphql_name='listConceptView')


class ConceptWithConfidence(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('concept', 'confidence')
    concept = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='concept')
    confidence = sgqlc.types.Field(Float, graphql_name='confidence')


class Coordinates(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('latitude', 'longitude')
    latitude = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='latitude')
    longitude = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='longitude')


class Date(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('year', 'month', 'day')
    year = sgqlc.types.Field(Int, graphql_name='year')
    month = sgqlc.types.Field(Int, graphql_name='month')
    day = sgqlc.types.Field(Int, graphql_name='day')


class DateTimeInterval(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('start', 'end')
    start = sgqlc.types.Field('DateTimeValue', graphql_name='start')
    end = sgqlc.types.Field('DateTimeValue', graphql_name='end')


class DateTimeValue(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('date', 'time')
    date = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='date')
    time = sgqlc.types.Field('Time', graphql_name='time')


class DictValue(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('value',)
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class DocSpecificMetadata(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('category', 'last_printed_date', 'last_modified_by', 'created_date', 'comments', 'author', 'document_subject', 'keywords', 'modified_data', 'doc_name')
    category = sgqlc.types.Field(String, graphql_name='category')
    last_printed_date = sgqlc.types.Field(UnixTime, graphql_name='lastPrintedDate')
    last_modified_by = sgqlc.types.Field(String, graphql_name='lastModifiedBy')
    created_date = sgqlc.types.Field(UnixTime, graphql_name='createdDate')
    comments = sgqlc.types.Field(String, graphql_name='comments')
    author = sgqlc.types.Field(String, graphql_name='author')
    document_subject = sgqlc.types.Field(String, graphql_name='documentSubject')
    keywords = sgqlc.types.Field(String, graphql_name='keywords')
    modified_data = sgqlc.types.Field(UnixTime, graphql_name='modifiedData')
    doc_name = sgqlc.types.Field(String, graphql_name='docName')


class DocumentFacets(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('document_metadata_facets', 'approved_entities_facets', 'not_approved_entities_facets', 'calculated_at', 'id')
    document_metadata_facets = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DocumentGroupFacet)), graphql_name='documentMetadataFacets')
    approved_entities_facets = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DocumentGroupFacet)), graphql_name='approvedEntitiesFacets')
    not_approved_entities_facets = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DocumentGroupFacet)), graphql_name='notApprovedEntitiesFacets')
    calculated_at = sgqlc.types.Field(UnixTime, graphql_name='calculatedAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class DocumentLink(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('parent_id', 'child_id')
    parent_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='parentId')
    child_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='childId')


class DocumentMetadata(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('file_name', 'size', 'file_type', 'modified_time', 'created_time', 'access_time', 'doc_specific_metadata', 'pdf_specific_metadata', 'image_specific_metadata', 'source', 'language', 'job_id', 'periodic_job_id', 'task_id', 'periodic_task_id', 'platform', 'account')
    file_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fileName')
    size = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='size')
    file_type = sgqlc.types.Field(String, graphql_name='fileType')
    modified_time = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='modifiedTime')
    created_time = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='createdTime')
    access_time = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='accessTime')
    doc_specific_metadata = sgqlc.types.Field(DocSpecificMetadata, graphql_name='docSpecificMetadata')
    pdf_specific_metadata = sgqlc.types.Field('PdfSpecificMetadataGQL', graphql_name='pdfSpecificMetadata')
    image_specific_metadata = sgqlc.types.Field('ImageSpecificMetadataGQL', graphql_name='imageSpecificMetadata')
    source = sgqlc.types.Field(String, graphql_name='source')
    language = sgqlc.types.Field('Language', graphql_name='language')
    job_id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='jobId')
    periodic_job_id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='periodicJobId')
    task_id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='taskId')
    periodic_task_id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='periodicTaskId')
    platform = sgqlc.types.Field('Platform', graphql_name='platform')
    account = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Account'))), graphql_name='account')


class DocumentPagination(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('list_document', 'total')
    list_document = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Document'))), graphql_name='listDocument')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class DocumentSubscriptions(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('subscriptions', 'list_user', 'count_users')
    subscriptions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DocumentUpdate))), graphql_name='subscriptions')
    list_user = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='listUser')
    count_users = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countUsers')


class DocumentTypePagination(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('list_document_type', 'total')
    list_document_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DocumentType'))), graphql_name='listDocumentType')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class DomainUpdateInfo(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('name', 'update_date')
    name = sgqlc.types.Field(sgqlc.types.non_null(DomainName), graphql_name='name')
    update_date = sgqlc.types.Field(UnixTime, graphql_name='updateDate')


class DoubleValue(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('value',)
    value = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='value')


class EntityTypePresentationStatistics(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('count_concept_types', 'count_document_types', 'count_entity_types')
    count_concept_types = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countConceptTypes')
    count_document_types = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countDocumentTypes')
    count_entity_types = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countEntityTypes')


class EntityTypeStatistics(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('count_property_type', 'count_link_type', 'count_dictionary', 'count_regexp')
    count_property_type = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countPropertyType')
    count_link_type = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countLinkType')
    count_dictionary = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countDictionary')
    count_regexp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countRegexp')


class Facet(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('value', 'count')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')
    count = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='count')


class FlatDocumentStructure(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('text', 'annotations', 'metadata', 'document_id', 'is_main', 'node_id', 'hierarchy_level', 'translated_text', 'id', 'language', 'translation_mention')
    text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='text')
    annotations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Annotation))), graphql_name='annotations')
    metadata = sgqlc.types.Field(sgqlc.types.non_null('ParagraphMetadata'), graphql_name='metadata')
    document_id = sgqlc.types.Field(ID, graphql_name='documentId')
    is_main = sgqlc.types.Field(Boolean, graphql_name='isMain')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    hierarchy_level = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='hierarchyLevel')
    translated_text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='translatedText')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    language = sgqlc.types.Field('Language', graphql_name='language')
    translation_mention = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MentionUnion'))), graphql_name='translationMention')


class GeoConceptProperty(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('concept', 'concept_property')
    concept = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='concept')
    concept_property = sgqlc.types.Field(sgqlc.types.non_null('ConceptProperty'), graphql_name='conceptProperty')


class GeoPointValue(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('point', 'name')
    point = sgqlc.types.Field(Coordinates, graphql_name='point')
    name = sgqlc.types.Field(String, graphql_name='name')


class Group(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'name', 'x_coordinate', 'y_coordinate', 'collapsed', 'layout', 'annotation')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    x_coordinate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='xCoordinate')
    y_coordinate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yCoordinate')
    collapsed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='collapsed')
    layout = sgqlc.types.Field(String, graphql_name='layout')
    annotation = sgqlc.types.Field(String, graphql_name='annotation')


class HLAnnotation(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('start', 'end')
    start = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='start')
    end = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='end')


class Highlighting(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('highlighting', 'annotations')
    highlighting = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='highlighting')
    annotations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(HLAnnotation))), graphql_name='annotations')


class Image(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('url',)
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')


class ImageSpecificMetadataGQL(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('height', 'width', 'orientation')
    height = sgqlc.types.Field(Long, graphql_name='height')
    width = sgqlc.types.Field(Long, graphql_name='width')
    orientation = sgqlc.types.Field(Int, graphql_name='orientation')


class IntValue(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('value',)
    value = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='value')


class IssueChangePagination(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('total', 'list_issue_change')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')
    list_issue_change = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IssueChange'))), graphql_name='listIssueChange')


class IssueInfo(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('topic', 'description', 'status', 'priority', 'execution_time_limit', 'markers', 'executor', 'list_concept', 'list_document', 'list_issue')
    topic = sgqlc.types.Field(String, graphql_name='topic')
    description = sgqlc.types.Field(String, graphql_name='description')
    status = sgqlc.types.Field(IssueStatus, graphql_name='status')
    priority = sgqlc.types.Field(IssuePriority, graphql_name='priority')
    execution_time_limit = sgqlc.types.Field(UnixTime, graphql_name='executionTimeLimit')
    markers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='markers')
    executor = sgqlc.types.Field('User', graphql_name='executor')
    list_concept = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Concept')), graphql_name='listConcept')
    list_document = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Document')), graphql_name='listDocument')
    list_issue = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Issue')), graphql_name='listIssue')


class IssuePagination(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('list_issue', 'total')
    list_issue = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Issue'))), graphql_name='listIssue')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class IssueStatistics(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('count_concept', 'count_doc', 'count_issue')
    count_concept = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countConcept')
    count_doc = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countDoc')
    count_issue = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countIssue')


class Language(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class LinkValue(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('link',)
    link = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='link')


class ListsTextsFromDocumentWithMarkerResponse(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('marker_text', 'not_marker_text')
    marker_text = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='markerText')
    not_marker_text = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='notMarkerText')


class MapDrawing(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'x_coordinate', 'y_coordinate', 'geo', 'stroke_color', 'stroke_width', 'annotation')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    x_coordinate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='xCoordinate')
    y_coordinate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yCoordinate')
    geo = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='geo')
    stroke_color = sgqlc.types.Field(String, graphql_name='strokeColor')
    stroke_width = sgqlc.types.Field(String, graphql_name='strokeWidth')
    annotation = sgqlc.types.Field(String, graphql_name='annotation')


class MapEdge(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('from_id', 'to_id', 'link_type', 'id', 'annotation', 'link')
    from_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='fromID')
    to_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='toID')
    link_type = sgqlc.types.Field(sgqlc.types.non_null(MapEdgeType), graphql_name='linkType')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    annotation = sgqlc.types.Field(String, graphql_name='annotation')
    link = sgqlc.types.Field(sgqlc.types.non_null('EntityLink'), graphql_name='link')


class MapNode(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'group_id', 'x_coordinate', 'y_coordinate', 'node_type', 'annotation', 'entity')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    group_id = sgqlc.types.Field(ID, graphql_name='groupId')
    x_coordinate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='xCoordinate')
    y_coordinate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yCoordinate')
    node_type = sgqlc.types.Field(sgqlc.types.non_null(MapNodeType), graphql_name='nodeType')
    annotation = sgqlc.types.Field(String, graphql_name='annotation')
    entity = sgqlc.types.Field(sgqlc.types.non_null('Entity'), graphql_name='entity')


class Mention(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'document_id', 'text_bounding', 'verifier', 'system_registration_date', 'system_update_date', 'access_level')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    document_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='documentId')
    text_bounding = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TextBounding'))), graphql_name='textBounding')
    verifier = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='verifier')
    system_registration_date = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='systemRegistrationDate')
    system_update_date = sgqlc.types.Field(UnixTime, graphql_name='systemUpdateDate')
    access_level = sgqlc.types.Field(sgqlc.types.non_null(AccessLevel), graphql_name='accessLevel')


class MentionLink(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'mention_link_type', 'source', 'target')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    mention_link_type = sgqlc.types.Field(sgqlc.types.non_null(MentionLinkType), graphql_name='mentionLinkType')
    source = sgqlc.types.Field(sgqlc.types.non_null('MentionUnion'), graphql_name='source')
    target = sgqlc.types.Field(sgqlc.types.non_null('MentionUnion'), graphql_name='target')


class MergedConcept(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('concept', 'merge_author', 'merge_date')
    concept = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='concept')
    merge_author = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='mergeAuthor')
    merge_date = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='mergeDate')


class MergedConceptPagination(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('total', 'list_merged_concept')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')
    list_merged_concept = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MergedConcept))), graphql_name='listMergedConcept')


class Metrics(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('count_concepts', 'count_objects', 'count_events', 'count_named_entities', 'count_disambiguated_entities', 'count_property_candidates', 'count_links', 'count_research_maps', 'count_child_docs', 'count_tasks', 'count_story_docs', 'count_entities')
    count_concepts = sgqlc.types.Field(Int, graphql_name='countConcepts')
    count_objects = sgqlc.types.Field(Int, graphql_name='countObjects')
    count_events = sgqlc.types.Field(Int, graphql_name='countEvents')
    count_named_entities = sgqlc.types.Field(Int, graphql_name='countNamedEntities')
    count_disambiguated_entities = sgqlc.types.Field(Int, graphql_name='countDisambiguatedEntities')
    count_property_candidates = sgqlc.types.Field(Int, graphql_name='countPropertyCandidates')
    count_links = sgqlc.types.Field(Int, graphql_name='countLinks')
    count_research_maps = sgqlc.types.Field(Int, graphql_name='countResearchMaps')
    count_child_docs = sgqlc.types.Field(Int, graphql_name='countChildDocs')
    count_tasks = sgqlc.types.Field(Int, graphql_name='countTasks')
    count_story_docs = sgqlc.types.Field(Int, graphql_name='countStoryDocs')
    count_entities = sgqlc.types.Field(Int, graphql_name='countEntities')


class Mutation(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('add_alias_to_concept_internal', 'add_document_double_internal', 'get_or_add_account_internal', 'get_or_add_platform_internal', 'get_or_add_concept_internal', 'get_or_add_concept_new_internal', 'update_document_facts_internal', 'reserve_concept_uuidv7')
    add_alias_to_concept_internal = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='addAliasToConceptInternal', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(AliasCreateInput), graphql_name='form', default=None)),
))
    )
    add_document_double_internal = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='addDocumentDoubleInternal', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(DocumentDoubleCreationInput), graphql_name='form', default=None)),
))
    )
    get_or_add_account_internal = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='getOrAddAccountInternal', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(AccountGetOrCreateInput), graphql_name='form', default=None)),
))
    )
    get_or_add_platform_internal = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='getOrAddPlatformInternal', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(PlatformGetOrCreateInput), graphql_name='form', default=None)),
))
    )
    get_or_add_concept_internal = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='getOrAddConceptInternal', args=sgqlc.types.ArgDict((
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptFilterSettings), graphql_name='filterSettings', default=None)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptMutationInput), graphql_name='form', default=None)),
        ('file', sgqlc.types.Arg(S3FileInput, graphql_name='file', default=None)),
        ('take_first_result', sgqlc.types.Arg(Boolean, graphql_name='takeFirstResult', default=False)),
))
    )
    get_or_add_concept_new_internal = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='getOrAddConceptNewInternal', args=sgqlc.types.ArgDict((
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptFilterSettings), graphql_name='filterSettings', default=None)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptFactsCreationInput), graphql_name='form', default=None)),
        ('take_first_result', sgqlc.types.Arg(Boolean, graphql_name='takeFirstResult', default=False)),
))
    )
    update_document_facts_internal = sgqlc.types.Field(sgqlc.types.non_null('StateWithErrors'), graphql_name='updateDocumentFactsInternal', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(BatchUpdateFactInput), graphql_name='form', default=None)),
))
    )
    reserve_concept_uuidv7 = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='reserveConceptUUIDv7', args=sgqlc.types.ArgDict((
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptFilterSettings), graphql_name='filterSettings', default=None)),
))
    )


class NERCRegexp(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('regexp', 'context_regexp', 'auto_create')
    regexp = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='regexp')
    context_regexp = sgqlc.types.Field(String, graphql_name='contextRegexp')
    auto_create = sgqlc.types.Field(Boolean, graphql_name='autoCreate')


class NamedValue(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'property_value_type', 'value')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    property_value_type = sgqlc.types.Field(sgqlc.types.non_null(CompositePropertyValueType), graphql_name='propertyValueType')
    value = sgqlc.types.Field(sgqlc.types.non_null('Value'), graphql_name='value')


class ParagraphMetadata(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('page_id', 'line_id', 'original_text', 'hidden', 'content_type', 'bullet', 'header', 'width', 'height', 'language', 'rowspan', 'colspan', 'name', 'size', 'md5', 'paragraph_type')
    page_id = sgqlc.types.Field(Int, graphql_name='pageId')
    line_id = sgqlc.types.Field(Int, graphql_name='lineId')
    original_text = sgqlc.types.Field(String, graphql_name='originalText')
    hidden = sgqlc.types.Field(Boolean, graphql_name='hidden')
    content_type = sgqlc.types.Field(String, graphql_name='contentType')
    bullet = sgqlc.types.Field(String, graphql_name='bullet')
    header = sgqlc.types.Field(Boolean, graphql_name='header')
    width = sgqlc.types.Field(Int, graphql_name='width')
    height = sgqlc.types.Field(Int, graphql_name='height')
    language = sgqlc.types.Field(String, graphql_name='language')
    rowspan = sgqlc.types.Field(Int, graphql_name='rowspan')
    colspan = sgqlc.types.Field(Int, graphql_name='colspan')
    name = sgqlc.types.Field(String, graphql_name='name')
    size = sgqlc.types.Field(Int, graphql_name='size')
    md5 = sgqlc.types.Field(String, graphql_name='md5')
    paragraph_type = sgqlc.types.Field(sgqlc.types.non_null(NodeType), graphql_name='paragraphType')


class Parameter(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('key', 'value')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class PdfSpecificMetadataGQL(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('author', 'creation_date')
    author = sgqlc.types.Field(String, graphql_name='author')
    creation_date = sgqlc.types.Field(UnixTime, graphql_name='creationDate')


class PlatformFacet(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('value', 'count')
    value = sgqlc.types.Field(sgqlc.types.non_null('Platform'), graphql_name='value')
    count = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='count')


class PlatformPagination(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('list_platform', 'total')
    list_platform = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Platform'))), graphql_name='listPlatform')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class PlatformStatistics(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('count_account', 'count_doc')
    count_account = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countAccount')
    count_doc = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countDoc')


class Query(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('mention_search_internal', 'batch_mention_search_internal', 'list_document_for_time_period_internal', 'list_text_from_document_with_marker_internal', 'pagination_concept_without_elastic_internal', 'tdm_internal', 'tdm_new_internal', 'document_uuid_internal', 'domain_update_info_internal', 'child_ids_internal', 'concept_ids_internal', 'pagination_concept_internal', 'pagination_concept_property_type_internal', 'pagination_concept_type_internal', 'pagination_document_type_internal', 'pagination_concept_property_value_type_internal', 'pagination_composite_property_value_template_internal', 'pagination_concept_link_type_internal', 'pagination_concept_link_property_type_internal', 'pagination_concept_property_internal', 'pagination_platform_internal', 'pagination_account_internal', 'pagination_access_level_internal')
    mention_search_internal = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptMentionCount))), graphql_name='mentionSearchInternal', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptMentionCountInput), graphql_name='form', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=5)),
        ('extend_results', sgqlc.types.Arg(Boolean, graphql_name='extendResults', default=False)),
))
    )
    batch_mention_search_internal = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptMentionCount))))), graphql_name='batchMentionSearchInternal', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptMentionCountBatchInput), graphql_name='form', default=None)),
))
    )
    list_document_for_time_period_internal = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Document'))), graphql_name='listDocumentForTimePeriodInternal', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(DocumentsWithConceptByDateInput), graphql_name='form', default=None)),
))
    )
    list_text_from_document_with_marker_internal = sgqlc.types.Field(sgqlc.types.non_null(ListsTextsFromDocumentWithMarkerResponse), graphql_name='listTextFromDocumentWithMarkerInternal', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(DocumentsTextWithMarkerByDateInput), graphql_name='form', default=None)),
))
    )
    pagination_concept_without_elastic_internal = sgqlc.types.Field(sgqlc.types.non_null(ConceptPaginationResult), graphql_name='paginationConceptWithoutElasticInternal', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(ConceptSorting, graphql_name='sortField', default='score')),
))
    )
    tdm_internal = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='tdmInternal', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('hide_new', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='hideNew', default=False)),
))
    )
    tdm_new_internal = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='tdmNewInternal', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    document_uuid_internal = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='documentUuidInternal', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    domain_update_info_internal = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DomainUpdateInfo))), graphql_name='domainUpdateInfoInternal')
    child_ids_internal = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='childIdsInternal', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    concept_ids_internal = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='conceptIdsInternal', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    pagination_concept_internal = sgqlc.types.Field(ConceptPagination, graphql_name='paginationConceptInternal', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(ConceptFilterSettings, graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(ConceptSorting, graphql_name='sortField', default='score')),
))
    )
    pagination_concept_property_type_internal = sgqlc.types.Field(sgqlc.types.non_null(ConceptPropertyTypePagination), graphql_name='paginationConceptPropertyTypeInternal', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptPropertyTypeFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(ConceptPropertyTypeSorting, graphql_name='sortField', default='name')),
))
    )
    pagination_concept_type_internal = sgqlc.types.Field(sgqlc.types.non_null(ConceptTypePagination), graphql_name='paginationConceptTypeInternal', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptTypeFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(ConceptTypeSorting, graphql_name='sortField', default='id')),
))
    )
    pagination_document_type_internal = sgqlc.types.Field(sgqlc.types.non_null(DocumentTypePagination), graphql_name='paginationDocumentTypeInternal', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(DocumentTypeFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(DocumentTypeSorting, graphql_name='sortField', default='id')),
))
    )
    pagination_concept_property_value_type_internal = sgqlc.types.Field(sgqlc.types.non_null(ConceptPropertyValueTypePagination), graphql_name='paginationConceptPropertyValueTypeInternal', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptPropertyValueTypeFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(ConceptPropertyValueTypeSorting, graphql_name='sortField', default='id')),
))
    )
    pagination_composite_property_value_template_internal = sgqlc.types.Field(sgqlc.types.non_null(CompositePropertyValueTemplatePagination), graphql_name='paginationCompositePropertyValueTemplateInternal', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(CompositePropertyValueTemplateFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(CompositePropertyValueTemplateSorting, graphql_name='sortField', default='id')),
))
    )
    pagination_concept_link_type_internal = sgqlc.types.Field(sgqlc.types.non_null(ConceptLinkTypePagination), graphql_name='paginationConceptLinkTypeInternal', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptLinkTypeFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(ConceptLinkTypeSorting, graphql_name='sortField', default='id')),
))
    )
    pagination_concept_link_property_type_internal = sgqlc.types.Field(sgqlc.types.non_null(ConceptPropertyTypePagination), graphql_name='paginationConceptLinkPropertyTypeInternal', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptPropertyTypeFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(ConceptPropertyTypeSorting, graphql_name='sortField', default='name')),
))
    )
    pagination_concept_property_internal = sgqlc.types.Field(sgqlc.types.non_null(ConceptPropertyPagination), graphql_name='paginationConceptPropertyInternal', args=sgqlc.types.ArgDict((
        ('concept_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='conceptId', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptPropertyFilterSettings), graphql_name='filterSettings', default=None)),
))
    )
    pagination_platform_internal = sgqlc.types.Field(sgqlc.types.non_null(PlatformPagination), graphql_name='paginationPlatformInternal', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(PlatformFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(PlatformSorting, graphql_name='sortField', default='id')),
))
    )
    pagination_account_internal = sgqlc.types.Field(sgqlc.types.non_null(AccountPagination), graphql_name='paginationAccountInternal', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(AccountFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(AccountSorting, graphql_name='sortField', default='id')),
))
    )
    pagination_access_level_internal = sgqlc.types.Field(sgqlc.types.non_null(AccessLevelPagination), graphql_name='paginationAccessLevelInternal', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(AccessLevelSorting, graphql_name='sortField', default='id')),
))
    )


class RedmineIssue(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'subject', 'tracker', 'status', 'priority', 'author', 'assignee', 'creation_date')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    subject = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='subject')
    tracker = sgqlc.types.Field(sgqlc.types.non_null('RedmineTracker'), graphql_name='tracker')
    status = sgqlc.types.Field(sgqlc.types.non_null('RedmineStatus'), graphql_name='status')
    priority = sgqlc.types.Field(sgqlc.types.non_null('RedminePriority'), graphql_name='priority')
    author = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='author')
    assignee = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='assignee')
    creation_date = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='creationDate')


class RedmineIssuePagination(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('list_redmine_issue', 'total')
    list_redmine_issue = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(RedmineIssue))), graphql_name='listRedmineIssue')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class RedminePriority(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class RedmineStatus(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class RedmineTracker(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class RelExtModel(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('source_annotation_type', 'target_annotation_type', 'relation_type', 'invert_direction')
    source_annotation_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sourceAnnotationType')
    target_annotation_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='targetAnnotationType')
    relation_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='relationType')
    invert_direction = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='invertDirection')


class ResearchMapPagination(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('total', 'list_research_map')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')
    list_research_map = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ResearchMap'))), graphql_name='listResearchMap')


class ResearchMapStatistics(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('object_num', 'event_num', 'document_num', 'concept_num', 'concept_and_document_num')
    object_num = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='objectNum')
    event_num = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='eventNum')
    document_num = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='documentNum')
    concept_num = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='conceptNum')
    concept_and_document_num = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='conceptAndDocumentNum')


class Score(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('name', 'score')
    name = sgqlc.types.Field(sgqlc.types.non_null(Name), graphql_name='name')
    score = sgqlc.types.Field(Float, graphql_name='score')


class State(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('is_success',)
    is_success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSuccess')


class StateWithErrors(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('state', 'info')
    state = sgqlc.types.Field(sgqlc.types.non_null(State), graphql_name='state')
    info = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(State)), graphql_name='info')


class Story(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'title', 'system_registration_date', 'system_update_date', 'main', 'list_document', 'highlighting', 'count_doc', 'preview', 'access_level')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(String, graphql_name='title')
    system_registration_date = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='systemRegistrationDate')
    system_update_date = sgqlc.types.Field(UnixTime, graphql_name='systemUpdateDate')
    main = sgqlc.types.Field(sgqlc.types.non_null('Document'), graphql_name='main')
    list_document = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Document'))), graphql_name='listDocument')
    highlighting = sgqlc.types.Field(Highlighting, graphql_name='highlighting')
    count_doc = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countDoc')
    preview = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='preview')
    access_level = sgqlc.types.Field(sgqlc.types.non_null(AccessLevel), graphql_name='accessLevel')


class StoryPagination(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('list_story', 'document_facets', 'total', 'show_total', 'list_named_entity_count_facet', 'list_concept_count_facet', 'list_account_count_facet', 'list_platform_count_facet', 'list_markers', 'sources', 'new_documents_today', 'precise_total')
    list_story = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Story))), graphql_name='listStory')
    document_facets = sgqlc.types.Field(sgqlc.types.non_null(DocumentFacets), graphql_name='documentFacets')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')
    show_total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='showTotal')
    list_named_entity_count_facet = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Facet))), graphql_name='listNamedEntityCountFacet')
    list_concept_count_facet = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptFacet))), graphql_name='listConceptCountFacet')
    list_account_count_facet = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AccountFacet))), graphql_name='listAccountCountFacet')
    list_platform_count_facet = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PlatformFacet))), graphql_name='listPlatformCountFacet')
    list_markers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Facet))), graphql_name='listMarkers')
    sources = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='sources')
    new_documents_today = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='newDocumentsToday')
    precise_total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='preciseTotal')


class StringLocaleValue(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('locale', 'value')
    locale = sgqlc.types.Field(sgqlc.types.non_null(Locale), graphql_name='locale')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class StringValue(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('value',)
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class Table(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('cells', 'metadata')
    cells = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))))), graphql_name='cells')
    metadata = sgqlc.types.Field(sgqlc.types.non_null('TableMetadata'), graphql_name='metadata')


class TableMetadata(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('page_id',)
    page_id = sgqlc.types.Field(Int, graphql_name='pageId')


class TextBounding(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('component_id', 'start', 'end', 'node_id')
    component_id = sgqlc.types.Field(ID, graphql_name='componentId')
    start = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='start')
    end = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='end')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='nodeId')


class Time(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('hour', 'minute', 'second')
    hour = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='hour')
    minute = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='minute')
    second = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='second')


class TimestampValue(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('value',)
    value = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='value')


class Translation(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('text', 'language')
    text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='text')
    language = sgqlc.types.Field(sgqlc.types.non_null(Language), graphql_name='language')


class User(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class ValueWithConfidence(sgqlc.types.Type):
    __schema__ = utils_api_schema
    __field_names__ = ('confidence', 'value')
    confidence = sgqlc.types.Field(Float, graphql_name='confidence')
    value = sgqlc.types.Field(sgqlc.types.non_null('Value'), graphql_name='value')


class Account(sgqlc.types.Type, RecordInterface):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'key', 'name', 'url', 'country', 'markers', 'params', 'platform', 'image', 'image_new', 'metric', 'period')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    country = sgqlc.types.Field(String, graphql_name='country')
    markers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='markers')
    params = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Parameter))), graphql_name='params')
    platform = sgqlc.types.Field(sgqlc.types.non_null('Platform'), graphql_name='platform')
    image = sgqlc.types.Field(Image, graphql_name='image')
    image_new = sgqlc.types.Field(Image, graphql_name='imageNew')
    metric = sgqlc.types.Field(AccountStatistics, graphql_name='metric')
    period = sgqlc.types.Field(DateTimeInterval, graphql_name='period')


class CompositePropertyValueCandidateFact(sgqlc.types.Type, FactInterface):
    __schema__ = utils_api_schema
    __field_names__ = ('property_value_type', 'value_slot_fact', 'fact_from')
    property_value_type = sgqlc.types.Field(sgqlc.types.non_null('CompositePropertyValueTemplate'), graphql_name='propertyValueType')
    value_slot_fact = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CompositePropertyValueComponentCandidateFact'))), graphql_name='valueSlotFact')
    fact_from = sgqlc.types.Field('AnyCompositePropertyFact', graphql_name='factFrom')


class CompositePropertyValueComponentCandidateFact(sgqlc.types.Type, FactInterface):
    __schema__ = utils_api_schema
    __field_names__ = ('fact_from', 'fact_to', 'component_value_type')
    fact_from = sgqlc.types.Field(sgqlc.types.non_null(CompositePropertyValueCandidateFact), graphql_name='factFrom')
    fact_to = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyValueCandidateFact'), graphql_name='factTo')
    component_value_type = sgqlc.types.Field(sgqlc.types.non_null(CompositePropertyValueType), graphql_name='componentValueType')


class CompositePropertyValueTemplate(sgqlc.types.Type, RecordInterface):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'name', 'component_value_types')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    component_value_types = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CompositePropertyValueType))), graphql_name='componentValueTypes')


class Concept(sgqlc.types.Type, KBEntity, PropertyTarget, LinkTarget, RecordInterface):
    __schema__ = utils_api_schema
    __field_names__ = ('is_actual', 'name', 'notes', 'markers', 'start_date', 'end_date', 'status', 'concept_type', 'pagination_concept_property', 'pagination_concept_link', 'pagination_concept_fact', 'pagination_concept_property_documents', 'pagination_concept_link_documents', 'list_concept_fact', 'list_concept_candidate_fact', 'image', 'image_new', 'metric', 'list_alias', 'pagination_alias', 'pagination_merged_concept', 'list_header_concept_property', 'pagination_redmine_issues', 'pagination_issue', 'access_level', 'list_subscription', 'pagination_research_map', 'avatar_document')
    is_actual = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActual')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    notes = sgqlc.types.Field(String, graphql_name='notes')
    markers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='markers')
    start_date = sgqlc.types.Field(DateTimeValue, graphql_name='startDate')
    end_date = sgqlc.types.Field(DateTimeValue, graphql_name='endDate')
    status = sgqlc.types.Field(sgqlc.types.non_null(KbFactStatus), graphql_name='status')
    concept_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptType'), graphql_name='conceptType')
    pagination_concept_property = sgqlc.types.Field(sgqlc.types.non_null(ConceptPropertyPagination), graphql_name='paginationConceptProperty', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptPropertyFilterSettings), graphql_name='filterSettings', default=None)),
))
    )
    pagination_concept_link = sgqlc.types.Field(sgqlc.types.non_null(ConceptLinkPagination), graphql_name='paginationConceptLink', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptLinkFilterSettings), graphql_name='filterSettings', default=None)),
))
    )
    pagination_concept_fact = sgqlc.types.Field(sgqlc.types.non_null(ConceptFactPagination), graphql_name='paginationConceptFact', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(LinkedDocumentFilterSettings), graphql_name='filterSettings', default=None)),
))
    )
    pagination_concept_property_documents = sgqlc.types.Field(sgqlc.types.non_null(DocumentPagination), graphql_name='paginationConceptPropertyDocuments', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptPropertyFilterSettings), graphql_name='filterSettings', default=None)),
))
    )
    pagination_concept_link_documents = sgqlc.types.Field(sgqlc.types.non_null(DocumentPagination), graphql_name='paginationConceptLinkDocuments', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptLinkFilterSettings), graphql_name='filterSettings', default=None)),
))
    )
    list_concept_fact = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptFact'))), graphql_name='listConceptFact')
    list_concept_candidate_fact = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptCandidateFact'))), graphql_name='listConceptCandidateFact')
    image = sgqlc.types.Field(Image, graphql_name='image')
    image_new = sgqlc.types.Field(Image, graphql_name='imageNew')
    metric = sgqlc.types.Field(sgqlc.types.non_null(ConceptStatistics), graphql_name='metric')
    list_alias = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptProperty'))), graphql_name='listAlias')
    pagination_alias = sgqlc.types.Field(sgqlc.types.non_null(ConceptPropertyPagination), graphql_name='paginationAlias', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
))
    )
    pagination_merged_concept = sgqlc.types.Field(sgqlc.types.non_null(MergedConceptPagination), graphql_name='paginationMergedConcept', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
))
    )
    list_header_concept_property = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptProperty'))), graphql_name='listHeaderConceptProperty')
    pagination_redmine_issues = sgqlc.types.Field(sgqlc.types.non_null(RedmineIssuePagination), graphql_name='paginationRedmineIssues', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('sort_direction', sgqlc.types.Arg(SortDirection, graphql_name='sortDirection', default='ascending')),
))
    )
    pagination_issue = sgqlc.types.Field(sgqlc.types.non_null(IssuePagination), graphql_name='paginationIssue', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(IssueFilterSettings), graphql_name='filterSettings', default=None)),
        ('sort_direction', sgqlc.types.Arg(sgqlc.types.non_null(SortDirection), graphql_name='sortDirection', default=None)),
        ('sorting', sgqlc.types.Arg(sgqlc.types.non_null(IssueSorting), graphql_name='sorting', default=None)),
))
    )
    access_level = sgqlc.types.Field(sgqlc.types.non_null(AccessLevel), graphql_name='accessLevel')
    list_subscription = sgqlc.types.Field(sgqlc.types.non_null(ConceptSubscriptions), graphql_name='listSubscription')
    pagination_research_map = sgqlc.types.Field(sgqlc.types.non_null(ResearchMapPagination), graphql_name='paginationResearchMap', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ResearchMapFilterSettings), graphql_name='filterSettings', default=None)),
        ('sort_direction', sgqlc.types.Arg(sgqlc.types.non_null(SortDirection), graphql_name='sortDirection', default=None)),
        ('sorting', sgqlc.types.Arg(sgqlc.types.non_null(ResearchMapSorting), graphql_name='sorting', default=None)),
))
    )
    avatar_document = sgqlc.types.Field('Document', graphql_name='avatarDocument')


class ConceptCandidateFact(sgqlc.types.Type, FactInterface):
    __schema__ = utils_api_schema
    __field_names__ = ('name', 'concept_type', 'list_concept')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    concept_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptType'), graphql_name='conceptType')
    list_concept = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptWithConfidence))), graphql_name='listConcept')


class ConceptCompositePropertyCandidateFact(sgqlc.types.Type, FactInterface):
    __schema__ = utils_api_schema
    __field_names__ = ('concept_property_type', 'fact_to', 'fact_from')
    concept_property_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyType'), graphql_name='conceptPropertyType')
    fact_to = sgqlc.types.Field(sgqlc.types.non_null(CompositePropertyValueCandidateFact), graphql_name='factTo')
    fact_from = sgqlc.types.Field('ConceptLikeFact', graphql_name='factFrom')


class ConceptFact(sgqlc.types.Type, FactInterface, RecordInterface):
    __schema__ = utils_api_schema
    __field_names__ = ('access_level', 'concept')
    access_level = sgqlc.types.Field(sgqlc.types.non_null(AccessLevel), graphql_name='accessLevel')
    concept = sgqlc.types.Field(sgqlc.types.non_null(Concept), graphql_name='concept')


class ConceptGroupFacet(sgqlc.types.Type, DocumentGroupFacet):
    __schema__ = utils_api_schema
    __field_names__ = ('concept',)
    concept = sgqlc.types.Field(sgqlc.types.non_null(Concept), graphql_name='concept')


class ConceptLink(sgqlc.types.Type, RecordInterface):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'concept_from_id', 'concept_to_id', 'notes', 'start_date', 'end_date', 'status', 'from_', 'to', 'concept_from', 'concept_to', 'concept_link_type', 'pagination_concept_link_property', 'pagination_concept_link_property_documents', 'pagination_document', 'list_concept_link_fact', 'access_level')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    concept_from_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptFromId')
    concept_to_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptToId')
    notes = sgqlc.types.Field(String, graphql_name='notes')
    start_date = sgqlc.types.Field(DateTimeValue, graphql_name='startDate')
    end_date = sgqlc.types.Field(DateTimeValue, graphql_name='endDate')
    status = sgqlc.types.Field(sgqlc.types.non_null(KbFactStatus), graphql_name='status')
    from_ = sgqlc.types.Field(sgqlc.types.non_null(LinkTarget), graphql_name='from')
    to = sgqlc.types.Field(sgqlc.types.non_null(LinkTarget), graphql_name='to')
    concept_from = sgqlc.types.Field(sgqlc.types.non_null(Concept), graphql_name='conceptFrom')
    concept_to = sgqlc.types.Field(sgqlc.types.non_null(Concept), graphql_name='conceptTo')
    concept_link_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptLinkType'), graphql_name='conceptLinkType')
    pagination_concept_link_property = sgqlc.types.Field(sgqlc.types.non_null(ConceptPropertyPagination), graphql_name='paginationConceptLinkProperty', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptPropertyFilterSettings), graphql_name='filterSettings', default=None)),
))
    )
    pagination_concept_link_property_documents = sgqlc.types.Field(sgqlc.types.non_null(DocumentPagination), graphql_name='paginationConceptLinkPropertyDocuments', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptPropertyFilterSettings), graphql_name='filterSettings', default=None)),
))
    )
    pagination_document = sgqlc.types.Field(sgqlc.types.non_null(DocumentPagination), graphql_name='paginationDocument', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
))
    )
    list_concept_link_fact = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptLinkFact'))), graphql_name='listConceptLinkFact')
    access_level = sgqlc.types.Field(sgqlc.types.non_null(AccessLevel), graphql_name='accessLevel')


class ConceptLinkCandidateFact(sgqlc.types.Type, FactInterface):
    __schema__ = utils_api_schema
    __field_names__ = ('concept_link_type', 'fact_from', 'fact_to')
    concept_link_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptLinkType'), graphql_name='conceptLinkType')
    fact_from = sgqlc.types.Field('ConceptLikeFact', graphql_name='factFrom')
    fact_to = sgqlc.types.Field('ConceptLikeFact', graphql_name='factTo')


class ConceptLinkCompositePropertyCandidateFact(sgqlc.types.Type, FactInterface):
    __schema__ = utils_api_schema
    __field_names__ = ('concept_link_property_type', 'fact_to', 'fact_from')
    concept_link_property_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyType'), graphql_name='conceptLinkPropertyType')
    fact_to = sgqlc.types.Field(sgqlc.types.non_null(CompositePropertyValueCandidateFact), graphql_name='factTo')
    fact_from = sgqlc.types.Field('ConceptLinkLikeFact', graphql_name='factFrom')


class ConceptLinkFact(sgqlc.types.Type, FactInterface, RecordInterface):
    __schema__ = utils_api_schema
    __field_names__ = ('access_level', 'concept_link')
    access_level = sgqlc.types.Field(sgqlc.types.non_null(AccessLevel), graphql_name='accessLevel')
    concept_link = sgqlc.types.Field(sgqlc.types.non_null(ConceptLink), graphql_name='conceptLink')


class ConceptLinkPropertyCandidateFact(sgqlc.types.Type, FactInterface):
    __schema__ = utils_api_schema
    __field_names__ = ('fact_to', 'concept_link_property_type', 'fact_from')
    fact_to = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyValueCandidateFact'), graphql_name='factTo')
    concept_link_property_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyType'), graphql_name='conceptLinkPropertyType')
    fact_from = sgqlc.types.Field('ConceptLinkLikeFact', graphql_name='factFrom')


class ConceptLinkPropertyFact(sgqlc.types.Type, FactInterface, RecordInterface):
    __schema__ = utils_api_schema
    __field_names__ = ('access_level', 'concept_link_property', 'parent_concept_link', 'mention', 'fact_from')
    access_level = sgqlc.types.Field(sgqlc.types.non_null(AccessLevel), graphql_name='accessLevel')
    concept_link_property = sgqlc.types.Field(sgqlc.types.non_null('ConceptProperty'), graphql_name='conceptLinkProperty')
    parent_concept_link = sgqlc.types.Field(sgqlc.types.non_null(ConceptLink), graphql_name='parentConceptLink')
    mention = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MentionUnion'))), graphql_name='mention')
    fact_from = sgqlc.types.Field('ConceptLinkLikeFact', graphql_name='factFrom')


class ConceptLinkType(sgqlc.types.Type, PropertyTypeTarget, RecordInterface):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'name', 'is_directed', 'is_hierarchical', 'pretrained_rel_ext_models', 'notify_on_update', 'from_type', 'to_type', 'concept_from_type', 'concept_to_type', 'pagination_concept_link_property_type', 'list_concept_link_property_type', 'metric')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    is_directed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDirected')
    is_hierarchical = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isHierarchical')
    pretrained_rel_ext_models = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(RelExtModel))), graphql_name='pretrainedRelExtModels')
    notify_on_update = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='notifyOnUpdate')
    from_type = sgqlc.types.Field(sgqlc.types.non_null(LinkTypeTarget), graphql_name='fromType')
    to_type = sgqlc.types.Field(sgqlc.types.non_null(LinkTypeTarget), graphql_name='toType')
    concept_from_type = sgqlc.types.Field(sgqlc.types.non_null(EntityType), graphql_name='conceptFromType')
    concept_to_type = sgqlc.types.Field(sgqlc.types.non_null(EntityType), graphql_name='conceptToType')
    pagination_concept_link_property_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptPropertyTypePagination), graphql_name='paginationConceptLinkPropertyType', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptPropertyTypeFilterSettings), graphql_name='filterSettings', default=None)),
        ('sort_direction', sgqlc.types.Arg(sgqlc.types.non_null(SortDirection), graphql_name='sortDirection', default=None)),
        ('sorting', sgqlc.types.Arg(sgqlc.types.non_null(ConceptTypeSorting), graphql_name='sorting', default=None)),
))
    )
    list_concept_link_property_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptPropertyType'))), graphql_name='listConceptLinkPropertyType')
    metric = sgqlc.types.Field(sgqlc.types.non_null(ConceptLinkTypeStatistics), graphql_name='metric')


class ConceptLinkTypeGroupFacet(sgqlc.types.Type, DocumentGroupFacet):
    __schema__ = utils_api_schema
    __field_names__ = ('concept_link_type',)
    concept_link_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptLinkType), graphql_name='conceptLinkType')


class ConceptProperty(sgqlc.types.Type, RecordInterface):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'is_main', 'property_type', 'notes', 'start_date', 'end_date', 'status', 'pagination_document', 'access_level', 'value', 'list_concept_property_fact')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_main = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isMain')
    property_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyType'), graphql_name='propertyType')
    notes = sgqlc.types.Field(String, graphql_name='notes')
    start_date = sgqlc.types.Field(DateTimeValue, graphql_name='startDate')
    end_date = sgqlc.types.Field(DateTimeValue, graphql_name='endDate')
    status = sgqlc.types.Field(sgqlc.types.non_null(KbFactStatus), graphql_name='status')
    pagination_document = sgqlc.types.Field(sgqlc.types.non_null(DocumentPagination), graphql_name='paginationDocument', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
))
    )
    access_level = sgqlc.types.Field(sgqlc.types.non_null(AccessLevel), graphql_name='accessLevel')
    value = sgqlc.types.Field(sgqlc.types.non_null('AnyValue'), graphql_name='value')
    list_concept_property_fact = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptPropertyLikeFact'))), graphql_name='listConceptPropertyFact')


class ConceptPropertyCandidateFact(sgqlc.types.Type, FactInterface):
    __schema__ = utils_api_schema
    __field_names__ = ('fact_to', 'concept_property_type', 'fact_from')
    fact_to = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyValueCandidateFact'), graphql_name='factTo')
    concept_property_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyType'), graphql_name='conceptPropertyType')
    fact_from = sgqlc.types.Field('ConceptLikeFact', graphql_name='factFrom')


class ConceptPropertyFact(sgqlc.types.Type, FactInterface, RecordInterface):
    __schema__ = utils_api_schema
    __field_names__ = ('access_level', 'concept_property', 'parent_concept', 'mention', 'fact_from')
    access_level = sgqlc.types.Field(sgqlc.types.non_null(AccessLevel), graphql_name='accessLevel')
    concept_property = sgqlc.types.Field(sgqlc.types.non_null(ConceptProperty), graphql_name='conceptProperty')
    parent_concept = sgqlc.types.Field(sgqlc.types.non_null(Concept), graphql_name='parentConcept')
    mention = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MentionUnion'))), graphql_name='mention')
    fact_from = sgqlc.types.Field('ConceptLikeFact', graphql_name='factFrom')


class ConceptPropertyType(sgqlc.types.Type, RecordInterface):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'name', 'pretrained_rel_ext_models', 'notify_on_update', 'computable_formula', 'deprecated', 'parent_type', 'parent_concept_type', 'parent_concept_link_type', 'is_identifying', 'value_type')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    pretrained_rel_ext_models = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(RelExtModel))), graphql_name='pretrainedRelExtModels')
    notify_on_update = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='notifyOnUpdate')
    computable_formula = sgqlc.types.Field(String, graphql_name='computableFormula')
    deprecated = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deprecated')
    parent_type = sgqlc.types.Field(sgqlc.types.non_null(PropertyTypeTarget), graphql_name='parentType')
    parent_concept_type = sgqlc.types.Field(EntityType, graphql_name='parentConceptType')
    parent_concept_link_type = sgqlc.types.Field(ConceptLinkType, graphql_name='parentConceptLinkType')
    is_identifying = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isIdentifying')
    value_type = sgqlc.types.Field(sgqlc.types.non_null('AnyValueType'), graphql_name='valueType')


class ConceptPropertyTypeGroupFacet(sgqlc.types.Type, DocumentGroupFacet):
    __schema__ = utils_api_schema
    __field_names__ = ('concept_property_type',)
    concept_property_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptPropertyType), graphql_name='conceptPropertyType')


class ConceptPropertyValueCandidateFact(sgqlc.types.Type, FactInterface):
    __schema__ = utils_api_schema
    __field_names__ = ('concept_property_value_type', 'meanings', 'fact_from')
    concept_property_value_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyValueType'), graphql_name='conceptPropertyValueType')
    meanings = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ValueWithConfidence))), graphql_name='meanings')
    fact_from = sgqlc.types.Field('AnyPropertyOrValueComponentFact', graphql_name='factFrom')


class ConceptPropertyValueGroupFacet(sgqlc.types.Type, DocumentGroupFacet):
    __schema__ = utils_api_schema
    __field_names__ = ('concept_property_type', 'concept_property_value')
    concept_property_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptPropertyType), graphql_name='conceptPropertyType')
    concept_property_value = sgqlc.types.Field(sgqlc.types.non_null('AnyValue'), graphql_name='conceptPropertyValue')


class ConceptPropertyValueType(sgqlc.types.Type, HasTypeSearchElements, RecordInterface):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'name', 'value_type', 'value_restriction', 'metric', 'list_concept_type', 'pagination_concept_type', 'list_concept_link_type', 'pagination_concept_link_type')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value_type = sgqlc.types.Field(sgqlc.types.non_null(ValueType), graphql_name='valueType')
    value_restriction = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='valueRestriction')
    metric = sgqlc.types.Field(sgqlc.types.non_null(ConceptPropertyValueStatistics), graphql_name='metric')
    list_concept_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptType'))), graphql_name='listConceptType')
    pagination_concept_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptTypePagination), graphql_name='paginationConceptType', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
))
    )
    list_concept_link_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptLinkType))), graphql_name='listConceptLinkType')
    pagination_concept_link_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptLinkTypePagination), graphql_name='paginationConceptLinkType', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
))
    )


class ConceptType(sgqlc.types.Type, RecordInterface, EntityType, PropertyTypeTarget, LinkTypeTarget, HasTypeSearchElements):
    __schema__ = utils_api_schema
    __field_names__ = ('is_event', 'show_in_menu', 'pagination_concept_type_view', 'list_concept_type_presentation')
    is_event = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isEvent')
    show_in_menu = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='showInMenu')
    pagination_concept_type_view = sgqlc.types.Field(sgqlc.types.non_null(ConceptTypeViewPagination), graphql_name='paginationConceptTypeView', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
))
    )
    list_concept_type_presentation = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptTypePresentation'))), graphql_name='listConceptTypePresentation')


class ConceptTypeGroupFacet(sgqlc.types.Type, DocumentGroupFacet):
    __schema__ = utils_api_schema
    __field_names__ = ('concept_type',)
    concept_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptType), graphql_name='conceptType')


class ConceptTypePresentation(sgqlc.types.Type, RecordInterface, EntityTypePresentation):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'name', 'root_concept_type', 'is_default', 'layout', 'has_supporting_documents', 'has_header_information', 'hide_empty_rows', 'pagination_widget_type', 'list_widget_type', 'internal_url', 'internal_url_new')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    root_concept_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptType), graphql_name='rootConceptType')
    is_default = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDefault')
    layout = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='layout')
    has_supporting_documents = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasSupportingDocuments')
    has_header_information = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasHeaderInformation')
    hide_empty_rows = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hideEmptyRows')
    pagination_widget_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptTypePresentationWidgetTypePagination), graphql_name='paginationWidgetType', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('sort_direction', sgqlc.types.Arg(SortDirection, graphql_name='sortDirection', default='ascending')),
        ('sorting', sgqlc.types.Arg(ConceptTypePresentationWidgetTypeSorting, graphql_name='sorting', default='order')),
))
    )
    list_widget_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptTypePresentationWidgetType'))), graphql_name='listWidgetType')
    internal_url = sgqlc.types.Field(String, graphql_name='internalUrl')
    internal_url_new = sgqlc.types.Field(String, graphql_name='internalUrlNew')


class ConceptTypePresentationWidgetType(sgqlc.types.Type, RecordInterface):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'name', 'table_type', 'concept_type_presentation', 'hierarchy', 'columns_info')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    table_type = sgqlc.types.Field(sgqlc.types.non_null(WidgetTypeTableType), graphql_name='tableType')
    concept_type_presentation = sgqlc.types.Field(sgqlc.types.non_null(ConceptTypePresentation), graphql_name='conceptTypePresentation')
    hierarchy = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptLinkTypePath))))), graphql_name='hierarchy')
    columns_info = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptTypePresentationWidgetTypeColumn))), graphql_name='columnsInfo')


class ConceptTypeView(sgqlc.types.Type, RecordInterface):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'name', 'show_in_menu', 'concept_type', 'columns', 'pagination_concept')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    show_in_menu = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='showInMenu')
    concept_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptType), graphql_name='conceptType')
    columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptTypePresentationWidgetTypeColumn))), graphql_name='columns')
    pagination_concept = sgqlc.types.Field(sgqlc.types.non_null(ConceptViewPagination), graphql_name='paginationConcept', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('sort_column', sgqlc.types.Arg(ID, graphql_name='sortColumn', default=None)),
        ('sort_direction', sgqlc.types.Arg(SortDirection, graphql_name='sortDirection', default='descending')),
        ('filter_settings', sgqlc.types.Arg(ConceptFilterSettings, graphql_name='filterSettings', default=None)),
))
    )


class Document(sgqlc.types.Type, KBEntity, PropertyTarget, LinkTarget, RecordInterface):
    __schema__ = utils_api_schema
    __field_names__ = ('title', 'external_url', 'publication_date', 'publication_author', 'notes', 'document_content_type', 'highlightings', 'markers', 'tables', 'metadata', 'uuid', 'trust_level', 'story', 'score', 'has_text', 'parent', 'list_child', 'pagination_child', 'internal_url', 'internal_url_new', 'avatar', 'avatar_new', 'metric', 'pagination_concept_fact', 'list_concept_fact', 'pagination_concept_link_fact', 'list_concept_link_document_fact', 'preview', 'list_fact_with_mention', 'pagination_redmine_issues', 'pagination_issue', 'access_level', 'text', 'additional_text', 'list_subscription', 'pagination_similar_documents', 'is_read', 'list_mention_link', 'node', 'document_type', 'text_translations', 'metadata_concept', 'list_fact', 'extra_metadata', 'list_mention', 'fact')
    title = sgqlc.types.Field(String, graphql_name='title')
    external_url = sgqlc.types.Field(String, graphql_name='externalUrl')
    publication_date = sgqlc.types.Field(UnixTime, graphql_name='publicationDate')
    publication_author = sgqlc.types.Field(String, graphql_name='publicationAuthor')
    notes = sgqlc.types.Field(String, graphql_name='notes')
    document_content_type = sgqlc.types.Field(sgqlc.types.non_null(DocumentContentType), graphql_name='documentContentType')
    highlightings = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Highlighting))), graphql_name='highlightings')
    markers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='markers')
    tables = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Table))), graphql_name='tables')
    metadata = sgqlc.types.Field(DocumentMetadata, graphql_name='metadata')
    uuid = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='uuid')
    trust_level = sgqlc.types.Field(TrustLevel, graphql_name='trustLevel')
    story = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='story')
    score = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Score))), graphql_name='score')
    has_text = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasText')
    parent = sgqlc.types.Field('Document', graphql_name='parent')
    list_child = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Document'))), graphql_name='listChild')
    pagination_child = sgqlc.types.Field(sgqlc.types.non_null(DocumentPagination), graphql_name='paginationChild', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(LinkedDocumentFilterSettings), graphql_name='filterSettings', default=None)),
))
    )
    internal_url = sgqlc.types.Field(String, graphql_name='internalUrl')
    internal_url_new = sgqlc.types.Field(String, graphql_name='internalUrlNew')
    avatar = sgqlc.types.Field(Image, graphql_name='avatar')
    avatar_new = sgqlc.types.Field(Image, graphql_name='avatarNew')
    metric = sgqlc.types.Field(sgqlc.types.non_null(Metrics), graphql_name='metric')
    pagination_concept_fact = sgqlc.types.Field(sgqlc.types.non_null(ConceptFactPagination), graphql_name='paginationConceptFact', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
))
    )
    list_concept_fact = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptFact))), graphql_name='listConceptFact')
    pagination_concept_link_fact = sgqlc.types.Field(sgqlc.types.non_null(ConceptLinkFactPagination), graphql_name='paginationConceptLinkFact', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
))
    )
    list_concept_link_document_fact = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptLinkFact))), graphql_name='listConceptLinkDocumentFact')
    preview = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='preview')
    list_fact_with_mention = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FactInterface))), graphql_name='listFactWithMention', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(String, graphql_name='nodeId', default=None)),
))
    )
    pagination_redmine_issues = sgqlc.types.Field(sgqlc.types.non_null(RedmineIssuePagination), graphql_name='paginationRedmineIssues', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('sort_direction', sgqlc.types.Arg(SortDirection, graphql_name='sortDirection', default='ascending')),
))
    )
    pagination_issue = sgqlc.types.Field(sgqlc.types.non_null(IssuePagination), graphql_name='paginationIssue', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(IssueFilterSettings), graphql_name='filterSettings', default=None)),
        ('sort_direction', sgqlc.types.Arg(sgqlc.types.non_null(SortDirection), graphql_name='sortDirection', default=None)),
        ('sorting', sgqlc.types.Arg(sgqlc.types.non_null(IssueSorting), graphql_name='sorting', default=None)),
))
    )
    access_level = sgqlc.types.Field(sgqlc.types.non_null(AccessLevel), graphql_name='accessLevel')
    text = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FlatDocumentStructure))), graphql_name='text', args=sgqlc.types.ArgDict((
        ('show_hidden', sgqlc.types.Arg(Boolean, graphql_name='showHidden', default=False)),
))
    )
    additional_text = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FlatDocumentStructure))))), graphql_name='additionalText', args=sgqlc.types.ArgDict((
        ('show_hidden', sgqlc.types.Arg(Boolean, graphql_name='showHidden', default=False)),
))
    )
    list_subscription = sgqlc.types.Field(sgqlc.types.non_null(DocumentSubscriptions), graphql_name='listSubscription')
    pagination_similar_documents = sgqlc.types.Field(sgqlc.types.non_null(DocumentPagination), graphql_name='paginationSimilarDocuments', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
))
    )
    is_read = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRead')
    list_mention_link = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MentionLink))), graphql_name='listMentionLink', args=sgqlc.types.ArgDict((
        ('mention_link_type', sgqlc.types.Arg(MentionLinkType, graphql_name='mentionLinkType', default=None)),
))
    )
    node = sgqlc.types.Field(FlatDocumentStructure, graphql_name='node', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    document_type = sgqlc.types.Field(sgqlc.types.non_null('DocumentType'), graphql_name='documentType')
    text_translations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Translation))), graphql_name='textTranslations', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    metadata_concept = sgqlc.types.Field(Concept, graphql_name='metadataConcept')
    list_fact = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Fact'))), graphql_name='listFact')
    extra_metadata = sgqlc.types.Field(JSON, graphql_name='extraMetadata')
    list_mention = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MentionUnion'))), graphql_name='listMention')
    fact = sgqlc.types.Field('Fact', graphql_name='fact', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )


class DocumentAccountGroupFacet(sgqlc.types.Type, DocumentGroupFacet):
    __schema__ = utils_api_schema
    __field_names__ = ('account',)
    account = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name='account')


class DocumentPlatformGroupFacet(sgqlc.types.Type, DocumentGroupFacet):
    __schema__ = utils_api_schema
    __field_names__ = ('platform',)
    platform = sgqlc.types.Field(sgqlc.types.non_null('Platform'), graphql_name='platform')


class DocumentPlatformTypeGroupFacet(sgqlc.types.Type, DocumentGroupFacet):
    __schema__ = utils_api_schema
    __field_names__ = ('platform_type',)
    platform_type = sgqlc.types.Field(sgqlc.types.non_null(PlatformType), graphql_name='platformType')


class DocumentPropertyGroupFacet(sgqlc.types.Type, DocumentGroupFacet):
    __schema__ = utils_api_schema
    __field_names__ = ('value',)
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class DocumentType(sgqlc.types.Type, RecordInterface, EntityType, PropertyTypeTarget, LinkTypeTarget, HasTypeSearchElements):
    __schema__ = utils_api_schema
    __field_names__ = ('list_document_type_presentation',)
    list_document_type_presentation = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DocumentTypePresentation'))), graphql_name='listDocumentTypePresentation')


class DocumentTypePresentation(sgqlc.types.Type, RecordInterface, EntityTypePresentation):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'name', 'root_document_type', 'is_default', 'hierarchy', 'columns_info')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    root_document_type = sgqlc.types.Field(sgqlc.types.non_null(DocumentType), graphql_name='rootDocumentType')
    is_default = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDefault')
    hierarchy = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptLinkTypePath))))), graphql_name='hierarchy')
    columns_info = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptTypePresentationWidgetTypeColumn))), graphql_name='columnsInfo')


class ImageNodeMention(sgqlc.types.Type, MentionInterface, RecordInterface):
    __schema__ = utils_api_schema
    __field_names__ = ('node_id', 'top', 'bottom', 'left', 'right')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='nodeId')
    top = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='top')
    bottom = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='bottom')
    left = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='left')
    right = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='right')


class Issue(sgqlc.types.Type, RecordInterface):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'topic', 'description', 'status', 'priority', 'execution_time_limit', 'markers', 'executor', 'pagination_document', 'pagination_concept', 'pagination_issue', 'metric', 'pagination_issue_change')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    topic = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='topic')
    description = sgqlc.types.Field(String, graphql_name='description')
    status = sgqlc.types.Field(sgqlc.types.non_null(IssueStatus), graphql_name='status')
    priority = sgqlc.types.Field(sgqlc.types.non_null(IssuePriority), graphql_name='priority')
    execution_time_limit = sgqlc.types.Field(UnixTime, graphql_name='executionTimeLimit')
    markers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='markers')
    executor = sgqlc.types.Field(sgqlc.types.non_null(User), graphql_name='executor')
    pagination_document = sgqlc.types.Field(sgqlc.types.non_null(DocumentPagination), graphql_name='paginationDocument', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
))
    )
    pagination_concept = sgqlc.types.Field(sgqlc.types.non_null(ConceptPaginationResult), graphql_name='paginationConcept', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
))
    )
    pagination_issue = sgqlc.types.Field(sgqlc.types.non_null(IssuePagination), graphql_name='paginationIssue', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(IssueFilterSettings), graphql_name='filterSettings', default=None)),
        ('sort_direction', sgqlc.types.Arg(sgqlc.types.non_null(SortDirection), graphql_name='sortDirection', default=None)),
        ('sorting', sgqlc.types.Arg(sgqlc.types.non_null(IssueSorting), graphql_name='sorting', default=None)),
))
    )
    metric = sgqlc.types.Field(sgqlc.types.non_null(IssueStatistics), graphql_name='metric')
    pagination_issue_change = sgqlc.types.Field(sgqlc.types.non_null(IssueChangePagination), graphql_name='paginationIssueChange', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
))
    )


class IssueChange(sgqlc.types.Type, RecordInterface):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'from_', 'to', 'comment')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    from_ = sgqlc.types.Field(sgqlc.types.non_null(IssueInfo), graphql_name='from')
    to = sgqlc.types.Field(sgqlc.types.non_null(IssueInfo), graphql_name='to')
    comment = sgqlc.types.Field(String, graphql_name='comment')


class NodeMention(sgqlc.types.Type, MentionInterface, RecordInterface):
    __schema__ = utils_api_schema
    __field_names__ = ('node_id',)
    node_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='nodeId')


class Platform(sgqlc.types.Type, RecordInterface):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'key', 'name', 'platform_type', 'url', 'country', 'language', 'markers', 'params', 'image', 'image_new', 'metric', 'period', 'accounts')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    platform_type = sgqlc.types.Field(sgqlc.types.non_null(PlatformType), graphql_name='platformType')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    country = sgqlc.types.Field(String, graphql_name='country')
    language = sgqlc.types.Field(String, graphql_name='language')
    markers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='markers')
    params = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Parameter))), graphql_name='params')
    image = sgqlc.types.Field(Image, graphql_name='image')
    image_new = sgqlc.types.Field(Image, graphql_name='imageNew')
    metric = sgqlc.types.Field(PlatformStatistics, graphql_name='metric')
    period = sgqlc.types.Field(DateTimeInterval, graphql_name='period')
    accounts = sgqlc.types.Field(sgqlc.types.non_null(AccountPagination), graphql_name='accounts', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(AccountFilterSettings), graphql_name='filterSettings', default=None)),
        ('sort_direction', sgqlc.types.Arg(SortDirection, graphql_name='sortDirection', default='descending')),
        ('sorting', sgqlc.types.Arg(AccountSorting, graphql_name='sorting', default='id')),
))
    )


class PropertyValueMentionCandidateFact(sgqlc.types.Type, FactInterface):
    __schema__ = utils_api_schema
    __field_names__ = ('value_fact', 'mention')
    value_fact = sgqlc.types.Field(sgqlc.types.non_null(ConceptPropertyValueCandidateFact), graphql_name='valueFact')
    mention = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MentionUnion'))), graphql_name='mention')


class ResearchMap(sgqlc.types.Type, RecordInterface):
    __schema__ = utils_api_schema
    __field_names__ = ('id', 'name', 'description', 'is_temporary', 'markers', 'list_node', 'list_edge', 'research_map_statistics', 'list_group', 'list_drawing', 'is_active', 'access_level', 'pagination_concept', 'pagination_story', 'pagination_research_map', 'list_geo_concept_properties')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    is_temporary = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isTemporary')
    markers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='markers')
    list_node = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MapNode))), graphql_name='listNode', args=sgqlc.types.ArgDict((
        ('filter_settings', sgqlc.types.Arg(MapNodeFilterSettings, graphql_name='filterSettings', default=None)),
        ('default_view', sgqlc.types.Arg(Boolean, graphql_name='defaultView', default=True)),
))
    )
    list_edge = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MapEdge))), graphql_name='listEdge', args=sgqlc.types.ArgDict((
        ('filter_settings', sgqlc.types.Arg(MapEdgeFilterSettings, graphql_name='filterSettings', default=None)),
        ('default_view', sgqlc.types.Arg(Boolean, graphql_name='defaultView', default=True)),
))
    )
    research_map_statistics = sgqlc.types.Field(sgqlc.types.non_null(ResearchMapStatistics), graphql_name='researchMapStatistics')
    list_group = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Group))), graphql_name='listGroup')
    list_drawing = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MapDrawing))), graphql_name='listDrawing')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    access_level = sgqlc.types.Field(sgqlc.types.non_null(AccessLevel), graphql_name='accessLevel')
    pagination_concept = sgqlc.types.Field(sgqlc.types.non_null(ConceptPagination), graphql_name='paginationConcept', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=1000)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(ConceptFilterSettings, graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(ConceptSorting, graphql_name='sortField', default=None)),
        ('extra_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptExtraSettings), graphql_name='extraSettings', default=None)),
))
    )
    pagination_story = sgqlc.types.Field(sgqlc.types.non_null(StoryPagination), graphql_name='paginationStory', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=1000)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('grouping', sgqlc.types.Arg(DocumentGrouping, graphql_name='grouping', default='none')),
        ('filter_settings', sgqlc.types.Arg(DocumentFilterSettings, graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(DocumentSorting, graphql_name='sortField', default=None)),
        ('extra_settings', sgqlc.types.Arg(sgqlc.types.non_null(ExtraSettings), graphql_name='extraSettings', default=None)),
        ('relevance', sgqlc.types.Arg(DocumentRelevanceMetricsInput, graphql_name='relevance', default=None)),
))
    )
    pagination_research_map = sgqlc.types.Field(sgqlc.types.non_null(ResearchMapPagination), graphql_name='paginationResearchMap', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ResearchMapFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(ResearchMapSorting, graphql_name='sortField', default='conceptAndDocumentLink')),
        ('research_map_content_select_input', sgqlc.types.Arg(ResearchMapContentUpdateInput, graphql_name='ResearchMapContentSelectInput', default=None)),
))
    )
    list_geo_concept_properties = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GeoConceptProperty))), graphql_name='listGeoConceptProperties')


class TextNodeMention(sgqlc.types.Type, MentionInterface, RecordInterface):
    __schema__ = utils_api_schema
    __field_names__ = ('node_id', 'start', 'end')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='nodeId')
    start = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='start')
    end = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='end')



########################################################################
# Unions
########################################################################
class AnyCompositePropertyFact(sgqlc.types.Union):
    __schema__ = utils_api_schema
    __types__ = (ConceptCompositePropertyCandidateFact, ConceptLinkCompositePropertyCandidateFact)


class AnyPropertyOrValueComponentFact(sgqlc.types.Union):
    __schema__ = utils_api_schema
    __types__ = (ConceptPropertyFact, ConceptLinkPropertyFact, ConceptPropertyCandidateFact, ConceptLinkPropertyCandidateFact, CompositePropertyValueComponentCandidateFact)


class AnyValue(sgqlc.types.Union):
    __schema__ = utils_api_schema
    __types__ = (CompositeValue, DateTimeValue, GeoPointValue, IntValue, DoubleValue, StringLocaleValue, StringValue, LinkValue, TimestampValue)


class AnyValueType(sgqlc.types.Union):
    __schema__ = utils_api_schema
    __types__ = (ConceptPropertyValueType, CompositePropertyValueTemplate)


class ConceptLikeFact(sgqlc.types.Union):
    __schema__ = utils_api_schema
    __types__ = (ConceptCandidateFact, ConceptFact)


class ConceptLinkLikeFact(sgqlc.types.Union):
    __schema__ = utils_api_schema
    __types__ = (ConceptLinkCandidateFact, ConceptLinkFact)


class ConceptPropertyLikeFact(sgqlc.types.Union):
    __schema__ = utils_api_schema
    __types__ = (ConceptPropertyFact, ConceptLinkPropertyFact)


class ConceptViewValue(sgqlc.types.Union):
    __schema__ = utils_api_schema
    __types__ = (DateTimeValue, GeoPointValue, IntValue, DoubleValue, StringLocaleValue, StringValue, LinkValue, CompositeValue, Concept, ConceptType, ConceptLinkType, User, Image, TimestampValue)


class Entity(sgqlc.types.Union):
    __schema__ = utils_api_schema
    __types__ = (Concept, Document, ConceptCandidateFact, ConceptType, DocumentType)


class EntityLink(sgqlc.types.Union):
    __schema__ = utils_api_schema
    __types__ = (ConceptLink, ConceptFactLink, ConceptImplicitLink, ConceptCandidateFactMention, ConceptMention, DocumentLink, ConceptLinkCandidateFact, ConceptLinkType)


class Fact(sgqlc.types.Union):
    __schema__ = utils_api_schema
    __types__ = (ConceptCandidateFact, ConceptFact, ConceptLinkCandidateFact, ConceptLinkFact, ConceptPropertyCandidateFact, ConceptPropertyFact, ConceptPropertyValueCandidateFact, ConceptLinkPropertyFact, ConceptLinkPropertyCandidateFact, CompositePropertyValueCandidateFact, CompositePropertyValueComponentCandidateFact, ConceptCompositePropertyCandidateFact, ConceptLinkCompositePropertyCandidateFact, PropertyValueMentionCandidateFact)


class MentionUnion(sgqlc.types.Union):
    __schema__ = utils_api_schema
    __types__ = (TextNodeMention, ImageNodeMention, NodeMention)


class TypeSearchElement(sgqlc.types.Union):
    __schema__ = utils_api_schema
    __types__ = (DictValue, NERCRegexp)


class Value(sgqlc.types.Union):
    __schema__ = utils_api_schema
    __types__ = (DateTimeValue, GeoPointValue, IntValue, DoubleValue, StringLocaleValue, StringValue, LinkValue, TimestampValue)



########################################################################
# Schema Entry Points
########################################################################
utils_api_schema.query_type = Query
utils_api_schema.mutation_type = Mutation
utils_api_schema.subscription_type = None

