import sgqlc.types


api_schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
class AccessLevelSorting(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('id', 'name', 'order')


class AccountSorting(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('creator', 'id', 'key', 'lastUpdater', 'name', 'platformKey', 'systemRegistrationDate', 'systemUpdateDate', 'url')


class AggregationFunction(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('daily', 'monthly', 'weekly')


class AutocompleteConceptDestination(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('markers',)


class AutocompleteDocumentDestination(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('links', 'markers')


Boolean = sgqlc.types.Boolean

class BulkType(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('account', 'concept', 'document', 'issue', 'map', 'platform')


class ChartTarget(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('document',)


class ChartType(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('line',)


class ChildVisibility(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('all', 'childrenOnly')


class ComponentView(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('keyValue', 'value')


class CompositePropertyTypeSorting(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('id', 'name', 'registrationDate')


class CompositePropertyValueTemplateSorting(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('id', 'name', 'registrationDate')


class ConceptLinkDirection(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('from', 'to')


class ConceptLinkTypeSorting(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('conceptType', 'id', 'name')


class ConceptPropertyTypeSorting(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('name', 'registrationDate')


class ConceptPropertyValueTypeSorting(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('id', 'name')


class ConceptSorting(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('id', 'name', 'score', 'systemRegistrationDate', 'systemUpdateDate')


class ConceptTypeLinkMetadata(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('creator', 'endDate', 'lastUpdater', 'linkType', 'registrationDate', 'startDate', 'updateDate')


class ConceptTypeMetadata(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('concept', 'conceptType', 'creator', 'endDate', 'image', 'lastUpdater', 'markers', 'name', 'notes', 'startDate', 'systemRegistrationDate', 'systemUpdateDate')


class ConceptTypePresentationSorting(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('id', 'name')


class ConceptTypePresentationWidgetTypeSorting(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('id', 'name', 'order')


class ConceptTypeSorting(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('dictionary', 'id', 'name', 'regexp')


class ConceptUpdate(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('link', 'linkProperty', 'metadata', 'property')


class ConceptVariant(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('event', 'obj')


class ConceptViewColumnType(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('accessLevel', 'conceptType', 'creator', 'id', 'image', 'lastUpdater', 'metrics', 'name', 'systemRegistrationDate', 'systemUpdateDate')


class ConceptViewMetricType(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('countConcepts', 'countConceptsAndDocuments', 'countDocumentFacts', 'countDocumentMentions', 'countEvents', 'countObjects', 'countPotentialDocuments', 'countProperties', 'countResearchMaps', 'countTasks')


class CountryTarget(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('account', 'platform')


class DocumentContentType(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('image', 'text')


class DocumentDuplicateComparisonField(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('accessLevel', 'account', 'externalUrl', 'fileName', 'fileType', 'language', 'markers', 'platform', 'publicationAuthor', 'publicationDate', 'size', 'story', 'text', 'title', 'trustLevel')


class DocumentDuplicateReportStatus(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('Error', 'InProgress', 'Pending', 'Success')


class DocumentDuplicateTaskStatus(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('Declined', 'Deleted', 'Error', 'InProgress', 'New', 'Pending')


class DocumentFeedMode(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('all', 'deleted', 'favorites')


class DocumentFeedSorting(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('creator', 'id', 'lastUpdater', 'name', 'systemRegistrationDate', 'systemUpdateDate')


class DocumentGrouping(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('none', 'story')


class DocumentGroupingCategory(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('account', 'accountCountry', 'concept', 'conceptLinkType', 'conceptPropertyType', 'conceptPropertyValue', 'conceptType', 'documentLanguage', 'marker', 'platform', 'platformCountry', 'platformLanguage', 'platformType', 'publicationAuthor')


class DocumentSorting(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('countLinks', 'countNamedEntities', 'id', 'publicationDate', 'registrationDate', 'relevance', 'score', 'title', 'updateDate')


class DocumentSourceType(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('external', 'internal')


class DocumentTypePresentationSorting(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('id', 'name')


class DocumentTypeSorting(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('dictionary', 'id', 'name', 'regexp')


class DocumentUpdate(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('content', 'markup', 'metadata')


class DocumentViewColumnType(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('accessLevel', 'account', 'creator', 'externalUrl', 'lastUpdater', 'platform', 'publicationAuthor', 'publicationDate', 'systemRegistrationDate', 'systemUpdateDate', 'trustLevel')


class DocumentViewMetricType(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('countChildDocs', 'countConcepts', 'countDisambiguatedEntities', 'countEntities', 'countEvents', 'countLinks', 'countNamedEntities', 'countObjects', 'countPropertyCandidates', 'countResearchMaps', 'countStoryDocs', 'countTasks')


class ElementType(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('blackList', 'whiteList')


class FactStatus(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('approved', 'auto', 'autoApproved', 'declined', 'hidden', 'new')


Float = sgqlc.types.Float

ID = sgqlc.types.ID

Int = sgqlc.types.Int

class IssuePriority(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('High', 'Low', 'Medium')


class IssueSorting(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('creator', 'executor', 'id', 'lastUpdater', 'priority', 'registrationDate', 'status', 'topic', 'updateDate')


class IssueStatus(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('canceled', 'closed', 'dataRequested', 'development', 'improvementRequested', 'open', 'reviewRequested')


class JSON(sgqlc.types.Scalar):
    __schema__ = api_schema


class KbFactStatus(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('approved', 'notApproved')


class KbFactStatusFilter(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('all', 'approved', 'notApproved')


class LinkDirection(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('in', 'out', 'undirected')


class Locale(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('eng', 'other', 'ru')


class Long(sgqlc.types.Scalar):
    __schema__ = api_schema


class MapEdgeType(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('conceptCandidateFactMention', 'conceptFactLink', 'conceptImplicitLink', 'conceptLink', 'conceptLinkCandidateFact', 'conceptMention', 'conceptTypeLink', 'documentLink')


class MapNodeType(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('concept', 'conceptCandidateFact', 'conceptType', 'document', 'documentType')


class MentionLinkType(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('equivalent', 'reference', 'translation')


class Name(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('approvedPropsRelevance', 'conceptApprovedPropsRelevance', 'conceptFactRelevance', 'conceptMeaningPropsRelevance', 'conceptNercRelevance', 'conceptNercSearchRelevance', 'conceptPropsRelevance', 'conceptSubstituteRelevance', 'factRelevance', 'mapApprovedPropsRelevance', 'mapFactRelevance', 'mapMeaningPropsRelevance', 'mapNercRelevance', 'mapNercSearchRelevance', 'mapPropsRelevance', 'meaningPropsRelevance', 'nercRelevance', 'nercSearchRelevance', 'propsRelevance', 'queryScore', 'significantTextRelevance', 'totalRelevance')


class NodeType(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('base64', 'cell', 'file', 'header', 'image', 'json', 'key', 'list', 'other', 'row', 'table', 'text')


class PlatformSorting(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('creator', 'id', 'key', 'lastUpdater', 'name', 'platformType', 'systemRegistrationDate', 'systemUpdateDate', 'url')


class PlatformType(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('blog', 'database', 'fileStorage', 'forum', 'government', 'media', 'messenger', 'newsAggregator', 'procurement', 'review', 'socialNetwork')


class PropLinkOrConcept(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('concept', 'link')


class RedmineIssueType(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('concept', 'document')


class RelatedDocumentSorting(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('publicationDate', 'registrationDate', 'updateDate')


class ResearchMapSorting(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('accessLevel', 'conceptAndDocumentLink', 'conceptLink', 'creator', 'documentLink', 'id', 'lastUpdater', 'name', 'systemRegistrationDate', 'systemUpdateDate')


class SortDirection(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('ascending', 'descending')


String = sgqlc.types.String

class SyncMode(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('manual', 'ok', 'zk')


class TrustLevel(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('high', 'low', 'medium')


class UnixTime(sgqlc.types.Scalar):
    __schema__ = api_schema


class ValueType(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('Date', 'Double', 'Geo', 'Int', 'Link', 'String', 'StringLocale', 'Timestamp')


class WidgetTypeTableType(sgqlc.types.Enum):
    __schema__ = api_schema
    __choices__ = ('horizontal', 'vertical')



########################################################################
# Input Objects
########################################################################
class AccessLevelCreationInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('name', 'order')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    order = sgqlc.types.Field(Long, graphql_name='order')


class AccessLevelUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('name',)
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class AccountCreationInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('platform_id', 'name', 'key', 'url', 'country', 'markers', 'params')
    platform_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='platformId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    country = sgqlc.types.Field(String, graphql_name='country')
    markers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='markers')
    params = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ParameterInput')), graphql_name='params')


class AccountFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema
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


class AccountUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('id', 'key', 'platform_id', 'name', 'url', 'country', 'markers', 'params')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    platform_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='platformId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    country = sgqlc.types.Field(String, graphql_name='country')
    markers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='markers')
    params = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ParameterInput'))), graphql_name='params')


class AnnotationInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('start', 'end', 'node_id')
    start = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='start')
    end = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='end')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='nodeId')


class BatchUpdateFactInput(sgqlc.types.Input):
    __schema__ = api_schema
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


class BulkDocumentUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('publication_author', 'clear_publication_author', 'publication_date', 'clear_publication_date', 'platform', 'clear_platform', 'account', 'clear_account', 'notes', 'clear_notes', 'external_url', 'clear_external_url', 'access_level_id', 'clear_access_level_id', 'trust_level', 'clear_trust_level')
    publication_author = sgqlc.types.Field(String, graphql_name='publicationAuthor')
    clear_publication_author = sgqlc.types.Field(Boolean, graphql_name='clearPublicationAuthor')
    publication_date = sgqlc.types.Field(UnixTime, graphql_name='publicationDate')
    clear_publication_date = sgqlc.types.Field(Boolean, graphql_name='clearPublicationDate')
    platform = sgqlc.types.Field(ID, graphql_name='platform')
    clear_platform = sgqlc.types.Field(Boolean, graphql_name='clearPlatform')
    account = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='account')
    clear_account = sgqlc.types.Field(Boolean, graphql_name='clearAccount')
    notes = sgqlc.types.Field(String, graphql_name='notes')
    clear_notes = sgqlc.types.Field(Boolean, graphql_name='clearNotes')
    external_url = sgqlc.types.Field(String, graphql_name='externalUrl')
    clear_external_url = sgqlc.types.Field(Boolean, graphql_name='clearExternalUrl')
    access_level_id = sgqlc.types.Field(ID, graphql_name='accessLevelId')
    clear_access_level_id = sgqlc.types.Field(Boolean, graphql_name='clearAccessLevelId')
    trust_level = sgqlc.types.Field(TrustLevel, graphql_name='trustLevel')
    clear_trust_level = sgqlc.types.Field(Boolean, graphql_name='clearTrustLevel')


class BulkMarkersInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('ids', 'bulk_type')
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')
    bulk_type = sgqlc.types.Field(sgqlc.types.non_null(BulkType), graphql_name='bulkType')


class BulkMarkersUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('ids', 'bulk_type', 'markers_to_delete', 'markers_to_add')
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')
    bulk_type = sgqlc.types.Field(sgqlc.types.non_null(BulkType), graphql_name='bulkType')
    markers_to_delete = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='markersToDelete')
    markers_to_add = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='markersToAdd')


class ChartDescriptionInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('chart_type', 'target', 'query', 'aggregation_field', 'aggregation_function', 'output_limiter')
    chart_type = sgqlc.types.Field(sgqlc.types.non_null(ChartType), graphql_name='chartType')
    target = sgqlc.types.Field(sgqlc.types.non_null(ChartTarget), graphql_name='target')
    query = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='query')
    aggregation_field = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='aggregationField')
    aggregation_function = sgqlc.types.Field(AggregationFunction, graphql_name='aggregationFunction')
    output_limiter = sgqlc.types.Field(sgqlc.types.non_null('OutputLimiterInput'), graphql_name='outputLimiter')


class Comment2IssueInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('id_issue', 'comment')
    id_issue = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='idIssue')
    comment = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='comment')


class ComponentValueInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('id', 'value')
    id = sgqlc.types.Field(ID, graphql_name='id')
    value = sgqlc.types.Field(sgqlc.types.non_null('ValueInput'), graphql_name='value')


class CompositePropertyTypeFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('name', 'concept_type_id', 'link_type_id')
    name = sgqlc.types.Field(String, graphql_name='name')
    concept_type_id = sgqlc.types.Field(ID, graphql_name='conceptTypeId')
    link_type_id = sgqlc.types.Field(ID, graphql_name='linkTypeId')


class CompositePropertyValueComponentFactInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('id', 'component_value_type_id', 'composite_property_value_fact_id', 'value_fact_id', 'reject')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    component_value_type_id = sgqlc.types.Field(ID, graphql_name='componentValueTypeId')
    composite_property_value_fact_id = sgqlc.types.Field(ID, graphql_name='compositePropertyValueFactId')
    value_fact_id = sgqlc.types.Field(ID, graphql_name='valueFactId')
    reject = sgqlc.types.Field(Boolean, graphql_name='reject')


class CompositePropertyValueFactInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('id', 'composite_value_type_id', 'reject')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    composite_value_type_id = sgqlc.types.Field(ID, graphql_name='compositeValueTypeId')
    reject = sgqlc.types.Field(Boolean, graphql_name='reject')


class CompositePropertyValueTemplateCreateInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('id', 'name', 'component_value_types')
    id = sgqlc.types.Field(ID, graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    component_value_types = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('NamedValueType'))), graphql_name='componentValueTypes')


class CompositePropertyValueTemplateFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('name', 'creator', 'last_updater', 'registration_date', 'update_date')
    name = sgqlc.types.Field(String, graphql_name='name')
    creator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='creator')
    last_updater = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='lastUpdater')
    registration_date = sgqlc.types.Field('TimestampInterval', graphql_name='registrationDate')
    update_date = sgqlc.types.Field('TimestampInterval', graphql_name='updateDate')


class Concept2IssueInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('id_issue', 'concept_ids', 'comment')
    id_issue = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='idIssue')
    concept_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='conceptIds')
    comment = sgqlc.types.Field(String, graphql_name='comment')


class ConceptAddImplicitLinkInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('first_node_id', 'second_node_id')
    first_node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='firstNodeId')
    second_node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='secondNodeId')


class ConceptAddInputInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('concept_id', 'x_coordinate', 'y_coordinate', 'group_id', 'annotation')
    concept_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptId')
    x_coordinate = sgqlc.types.Field(Float, graphql_name='xCoordinate')
    y_coordinate = sgqlc.types.Field(Float, graphql_name='yCoordinate')
    group_id = sgqlc.types.Field(ID, graphql_name='groupId')
    annotation = sgqlc.types.Field(String, graphql_name='annotation')


class ConceptCandidateAddInputInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('document_id', 'group_id')
    document_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='documentId')
    group_id = sgqlc.types.Field(ID, graphql_name='groupId')


class ConceptExtraSettings(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('search_on_map', 'selected_content')
    search_on_map = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='searchOnMap')
    selected_content = sgqlc.types.Field('ResearchMapContentSelectInput', graphql_name='selectedContent')


class ConceptFactInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('id', 'concept_type_id', 'concept_id', 'reject', 'approved')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    concept_type_id = sgqlc.types.Field(ID, graphql_name='conceptTypeId')
    concept_id = sgqlc.types.Field(ID, graphql_name='conceptId')
    reject = sgqlc.types.Field(Boolean, graphql_name='reject')
    approved = sgqlc.types.Field(Boolean, graphql_name='approved')


class ConceptFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema
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


class ConceptLinkCreationMutationInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('concept_from_id', 'concept_to_id', 'link_type_id', 'notes', 'fact_info', 'start_date', 'end_date', 'access_level_id')
    concept_from_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptFromId')
    concept_to_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptToId')
    link_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='linkTypeId')
    notes = sgqlc.types.Field(String, graphql_name='notes')
    fact_info = sgqlc.types.Field('FactInput', graphql_name='factInfo')
    start_date = sgqlc.types.Field('DateTimeInput', graphql_name='startDate')
    end_date = sgqlc.types.Field('DateTimeInput', graphql_name='endDate')
    access_level_id = sgqlc.types.Field(ID, graphql_name='accessLevelId')


class ConceptLinkFactInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('id', 'link_type_id', 'concept_from_fact_id', 'concept_to_fact_id', 'reject', 'approved')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    link_type_id = sgqlc.types.Field(ID, graphql_name='linkTypeId')
    concept_from_fact_id = sgqlc.types.Field(ID, graphql_name='conceptFromFactId')
    concept_to_fact_id = sgqlc.types.Field(ID, graphql_name='conceptToFactId')
    reject = sgqlc.types.Field(Boolean, graphql_name='reject')
    approved = sgqlc.types.Field(Boolean, graphql_name='approved')


class ConceptLinkFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema
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
    __schema__ = api_schema
    __field_names__ = ('id', 'link_property_type_id', 'concept_link_fact_id', 'value_fact_id', 'reject', 'approved')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    link_property_type_id = sgqlc.types.Field(ID, graphql_name='linkPropertyTypeId')
    concept_link_fact_id = sgqlc.types.Field(ID, graphql_name='conceptLinkFactId')
    value_fact_id = sgqlc.types.Field(ID, graphql_name='valueFactId')
    reject = sgqlc.types.Field(Boolean, graphql_name='reject')
    approved = sgqlc.types.Field(Boolean, graphql_name='approved')


class ConceptLinkPropertyInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('property_type_id', 'fact_info', 'notes', 'value_input', 'computable_value', 'link_id', 'is_main', 'start_date', 'end_date', 'access_level_id')
    property_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='propertyTypeId')
    fact_info = sgqlc.types.Field('FactInput', graphql_name='factInfo')
    notes = sgqlc.types.Field(String, graphql_name='notes')
    value_input = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ComponentValueInput))), graphql_name='valueInput')
    computable_value = sgqlc.types.Field(String, graphql_name='computableValue')
    link_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='linkId')
    is_main = sgqlc.types.Field(Boolean, graphql_name='isMain')
    start_date = sgqlc.types.Field('DateTimeInput', graphql_name='startDate')
    end_date = sgqlc.types.Field('DateTimeInput', graphql_name='endDate')
    access_level_id = sgqlc.types.Field(ID, graphql_name='accessLevelId')


class ConceptLinkPropertyTypeCreationInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('link_type_id', 'name', 'value_type_id', 'computable_formula', 'pretrained_rel_ext_models', 'notify_on_update')
    link_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='linkTypeId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='valueTypeId')
    computable_formula = sgqlc.types.Field(String, graphql_name='computableFormula')
    pretrained_rel_ext_models = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('RelExtModelInput')), graphql_name='pretrainedRelExtModels')
    notify_on_update = sgqlc.types.Field(Boolean, graphql_name='notifyOnUpdate')


class ConceptLinkPropertyTypeUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('id', 'name', 'value_type_id', 'computable_formula', 'pretrained_rel_ext_models', 'notify_on_update', 'deprecated')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='valueTypeId')
    computable_formula = sgqlc.types.Field(String, graphql_name='computableFormula')
    pretrained_rel_ext_models = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('RelExtModelInput')), graphql_name='pretrainedRelExtModels')
    notify_on_update = sgqlc.types.Field(Boolean, graphql_name='notifyOnUpdate')
    deprecated = sgqlc.types.Field(Boolean, graphql_name='deprecated')


class ConceptLinkTypeCreationInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('name', 'is_directed', 'is_hierarchical', 'concept_from_type_id', 'concept_to_type_id', 'pretrained_rel_ext_models', 'notify_on_update')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    is_directed = sgqlc.types.Field(Boolean, graphql_name='isDirected')
    is_hierarchical = sgqlc.types.Field(Boolean, graphql_name='isHierarchical')
    concept_from_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptFromTypeId')
    concept_to_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptToTypeId')
    pretrained_rel_ext_models = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('RelExtModelInput')), graphql_name='pretrainedRelExtModels')
    notify_on_update = sgqlc.types.Field(Boolean, graphql_name='notifyOnUpdate')


class ConceptLinkTypeFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema
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


class ConceptLinkTypePathInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('link_type_id', 'fixed')
    link_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='linkTypeId')
    fixed = sgqlc.types.Field(ConceptLinkDirection, graphql_name='fixed')


class ConceptLinkTypeUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('id', 'name', 'concept_from_type_id', 'concept_to_type_id', 'pretrained_rel_ext_models', 'is_directed', 'is_hierarchical', 'notify_on_update')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    concept_from_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptFromTypeId')
    concept_to_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptToTypeId')
    pretrained_rel_ext_models = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('RelExtModelInput')), graphql_name='pretrainedRelExtModels')
    is_directed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDirected')
    is_hierarchical = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isHierarchical')
    notify_on_update = sgqlc.types.Field(Boolean, graphql_name='notifyOnUpdate')


class ConceptLinkUpdateMutationInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('id', 'notes', 'start_date', 'end_date', 'access_level_id', 'approved')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    notes = sgqlc.types.Field(String, graphql_name='notes')
    start_date = sgqlc.types.Field('DateTimeInput', graphql_name='startDate')
    end_date = sgqlc.types.Field('DateTimeInput', graphql_name='endDate')
    access_level_id = sgqlc.types.Field(ID, graphql_name='accessLevelId')
    approved = sgqlc.types.Field(Boolean, graphql_name='approved')


class ConceptMergeInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('main_concept_id', 'merged_concept_id')
    main_concept_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='mainConceptId')
    merged_concept_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='mergedConceptId')


class ConceptMutationInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('name', 'concept_type_id', 'notes', 'fact_info', 'markers', 'access_level_id', 'start_date', 'end_date')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    concept_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptTypeId')
    notes = sgqlc.types.Field(String, graphql_name='notes')
    fact_info = sgqlc.types.Field('FactInput', graphql_name='factInfo')
    markers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='markers')
    access_level_id = sgqlc.types.Field(ID, graphql_name='accessLevelId')
    start_date = sgqlc.types.Field('DateTimeInput', graphql_name='startDate')
    end_date = sgqlc.types.Field('DateTimeInput', graphql_name='endDate')


class ConceptPresentationFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('property_filter_settings', 'link_filter_settings', 'concept_variant', 'name', 'exact_name', 'substring', 'access_level_id', 'creator', 'last_updater', 'creation_date', 'update_date', 'markers', 'has_linked_issues', 'status', 'concept_type_presentation_ids')
    property_filter_settings = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('PropertyFilterSettings')), graphql_name='propertyFilterSettings')
    link_filter_settings = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('LinkFilterSettings')), graphql_name='linkFilterSettings')
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
    concept_type_presentation_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='conceptTypePresentationIds')


class ConceptPropertyCreateInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('property_type_id', 'concept_id', 'value_input', 'computable_value', 'fact_info', 'notes', 'is_main', 'start_date', 'end_date', 'access_level_id')
    property_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='propertyTypeId')
    concept_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptId')
    value_input = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ComponentValueInput))), graphql_name='valueInput')
    computable_value = sgqlc.types.Field(String, graphql_name='computableValue')
    fact_info = sgqlc.types.Field('FactInput', graphql_name='factInfo')
    notes = sgqlc.types.Field(String, graphql_name='notes')
    is_main = sgqlc.types.Field(Boolean, graphql_name='isMain')
    start_date = sgqlc.types.Field('DateTimeInput', graphql_name='startDate')
    end_date = sgqlc.types.Field('DateTimeInput', graphql_name='endDate')
    access_level_id = sgqlc.types.Field(ID, graphql_name='accessLevelId')


class ConceptPropertyFactInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('id', 'property_type_id', 'concept_fact_id', 'value_fact_id', 'reject', 'approved')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    property_type_id = sgqlc.types.Field(ID, graphql_name='propertyTypeId')
    concept_fact_id = sgqlc.types.Field(ID, graphql_name='conceptFactId')
    value_fact_id = sgqlc.types.Field(ID, graphql_name='valueFactId')
    reject = sgqlc.types.Field(Boolean, graphql_name='reject')
    approved = sgqlc.types.Field(Boolean, graphql_name='approved')


class ConceptPropertyFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('only_main', 'document_id', 'property_type', 'value_type', 'value', 'status')
    only_main = sgqlc.types.Field(Boolean, graphql_name='onlyMain')
    document_id = sgqlc.types.Field(ID, graphql_name='documentId')
    property_type = sgqlc.types.Field(ID, graphql_name='propertyType')
    value_type = sgqlc.types.Field(ValueType, graphql_name='valueType')
    value = sgqlc.types.Field('ValueFilter', graphql_name='value')
    status = sgqlc.types.Field(KbFactStatusFilter, graphql_name='status')


class ConceptPropertyTypeCreationInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('concept_type_id', 'name', 'value_type_id', 'computable_formula', 'pretrained_rel_ext_models', 'notify_on_update')
    concept_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptTypeId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='valueTypeId')
    computable_formula = sgqlc.types.Field(String, graphql_name='computableFormula')
    pretrained_rel_ext_models = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('RelExtModelInput')), graphql_name='pretrainedRelExtModels')
    notify_on_update = sgqlc.types.Field(Boolean, graphql_name='notifyOnUpdate')


class ConceptPropertyTypeFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('name', 'concept_type_id', 'concept_type_name', 'concept_link_type_id', 'concept_link_type_name', 'concept_value_type_id', 'value_type', 'concept_type_from_link_type_id')
    name = sgqlc.types.Field(String, graphql_name='name')
    concept_type_id = sgqlc.types.Field(ID, graphql_name='conceptTypeId')
    concept_type_name = sgqlc.types.Field(String, graphql_name='conceptTypeName')
    concept_link_type_id = sgqlc.types.Field(ID, graphql_name='conceptLinkTypeId')
    concept_link_type_name = sgqlc.types.Field(String, graphql_name='conceptLinkTypeName')
    concept_value_type_id = sgqlc.types.Field(ID, graphql_name='conceptValueTypeId')
    value_type = sgqlc.types.Field(ValueType, graphql_name='valueType')
    concept_type_from_link_type_id = sgqlc.types.Field(ID, graphql_name='conceptTypeFromLinkTypeId')


class ConceptPropertyTypeUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('id', 'name', 'value_type_id', 'computable_formula', 'pretrained_rel_ext_models', 'notify_on_update', 'deprecated')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='valueTypeId')
    computable_formula = sgqlc.types.Field(String, graphql_name='computableFormula')
    pretrained_rel_ext_models = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('RelExtModelInput')), graphql_name='pretrainedRelExtModels')
    notify_on_update = sgqlc.types.Field(Boolean, graphql_name='notifyOnUpdate')
    deprecated = sgqlc.types.Field(Boolean, graphql_name='deprecated')


class ConceptPropertyUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('property_id', 'is_main', 'notes', 'computable_value', 'start_date', 'end_date', 'value_input', 'access_level_id', 'approved')
    property_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='propertyId')
    is_main = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isMain')
    notes = sgqlc.types.Field(String, graphql_name='notes')
    computable_value = sgqlc.types.Field(String, graphql_name='computableValue')
    start_date = sgqlc.types.Field('DateTimeInput', graphql_name='startDate')
    end_date = sgqlc.types.Field('DateTimeInput', graphql_name='endDate')
    value_input = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ComponentValueInput))), graphql_name='valueInput')
    access_level_id = sgqlc.types.Field(ID, graphql_name='accessLevelId')
    approved = sgqlc.types.Field(Boolean, graphql_name='approved')


class ConceptPropertyValueTypeCreationInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('name', 'value_type', 'pretrained_nercmodels', 'value_restriction')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value_type = sgqlc.types.Field(sgqlc.types.non_null(ValueType), graphql_name='valueType')
    pretrained_nercmodels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pretrainedNERCModels')
    value_restriction = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='valueRestriction')


class ConceptPropertyValueTypeFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema
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


class ConceptPropertyValueTypeUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('id', 'name', 'value_type', 'pretrained_nercmodels', 'value_restriction')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value_type = sgqlc.types.Field(sgqlc.types.non_null(ValueType), graphql_name='valueType')
    pretrained_nercmodels = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='pretrainedNERCModels')
    value_restriction = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='valueRestriction')


class ConceptRegistryViewInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('columns', 'metrics', 'sorting')
    columns = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ConceptViewColumnType)), graphql_name='columns')
    metrics = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ConceptViewMetricType)), graphql_name='metrics')
    sorting = sgqlc.types.Field('ConceptRegistryViewSortingInput', graphql_name='sorting')


class ConceptRegistryViewSortingInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('sorting_type', 'sort_direction')
    sorting_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptSorting), graphql_name='sortingType')
    sort_direction = sgqlc.types.Field(sgqlc.types.non_null(SortDirection), graphql_name='sortDirection')


class ConceptTypeAddInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('name', 'x_coordinate', 'y_coordinate', 'pretrained_nercmodels', 'is_event', 'show_in_menu')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    x_coordinate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='xCoordinate')
    y_coordinate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yCoordinate')
    pretrained_nercmodels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pretrainedNERCModels')
    is_event = sgqlc.types.Field(Boolean, graphql_name='isEvent')
    show_in_menu = sgqlc.types.Field(Boolean, graphql_name='showInMenu')


class ConceptTypeFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema
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


class ConceptTypePresentationAddInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('name', 'root_concept_type_id', 'is_default', 'layout', 'has_supporting_documents', 'has_header_information', 'show_in_menu', 'hide_empty_rows')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    root_concept_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='rootConceptTypeId')
    is_default = sgqlc.types.Field(Boolean, graphql_name='isDefault')
    layout = sgqlc.types.Field(String, graphql_name='layout')
    has_supporting_documents = sgqlc.types.Field(Boolean, graphql_name='hasSupportingDocuments')
    has_header_information = sgqlc.types.Field(Boolean, graphql_name='hasHeaderInformation')
    show_in_menu = sgqlc.types.Field(Boolean, graphql_name='showInMenu')
    hide_empty_rows = sgqlc.types.Field(Boolean, graphql_name='hideEmptyRows')


class ConceptTypePresentationFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('name', 'creator', 'last_updater', 'registration_date', 'update_date')
    name = sgqlc.types.Field(String, graphql_name='name')
    creator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='creator')
    last_updater = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='lastUpdater')
    registration_date = sgqlc.types.Field('TimestampInterval', graphql_name='registrationDate')
    update_date = sgqlc.types.Field('TimestampInterval', graphql_name='updateDate')


class ConceptTypePresentationUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('id', 'name', 'is_default', 'layout', 'has_supporting_documents', 'has_header_information', 'show_in_menu', 'hide_empty_rows')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    is_default = sgqlc.types.Field(Boolean, graphql_name='isDefault')
    layout = sgqlc.types.Field(String, graphql_name='layout')
    has_supporting_documents = sgqlc.types.Field(Boolean, graphql_name='hasSupportingDocuments')
    has_header_information = sgqlc.types.Field(Boolean, graphql_name='hasHeaderInformation')
    show_in_menu = sgqlc.types.Field(Boolean, graphql_name='showInMenu')
    hide_empty_rows = sgqlc.types.Field(Boolean, graphql_name='hideEmptyRows')


class ConceptTypePresentationUpdateTemplateFilenameInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('id', 'filename', 'bucket')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    filename = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='filename')
    bucket = sgqlc.types.Field(String, graphql_name='bucket')


class ConceptTypePresentationViewInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('concept_type_id', 'concept_type_presentation_id')
    concept_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptTypeId')
    concept_type_presentation_id = sgqlc.types.Field(ID, graphql_name='conceptTypePresentationId')


class ConceptTypePresentationWidgetTypeAddInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('name', 'table_type', 'concept_type_presentation_id', 'columns')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    table_type = sgqlc.types.Field(sgqlc.types.non_null(WidgetTypeTableType), graphql_name='tableType')
    concept_type_presentation_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptTypePresentationId')
    columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptTypePresentationWidgetTypeColumnInput'))), graphql_name='columns')


class ConceptTypePresentationWidgetTypeColumnInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('name', 'is_main_properties', 'list_values', 'concept_link_type_ids_path', 'sort_by_column', 'sort_direction', 'value_info')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    is_main_properties = sgqlc.types.Field(Boolean, graphql_name='isMainProperties')
    list_values = sgqlc.types.Field(Boolean, graphql_name='listValues')
    concept_link_type_ids_path = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ConceptLinkTypePathInput)), graphql_name='conceptLinkTypeIdsPath')
    sort_by_column = sgqlc.types.Field(Boolean, graphql_name='sortByColumn')
    sort_direction = sgqlc.types.Field(SortDirection, graphql_name='sortDirection')
    value_info = sgqlc.types.Field(sgqlc.types.non_null('ConceptTypePresentationWidgetTypeColumnValueInfoInput'), graphql_name='valueInfo')


class ConceptTypePresentationWidgetTypeColumnValueInfoInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('property_type_id', 'metadata', 'link_property_type_id', 'link_metadata')
    property_type_id = sgqlc.types.Field(ID, graphql_name='propertyTypeId')
    metadata = sgqlc.types.Field(ConceptTypeMetadata, graphql_name='metadata')
    link_property_type_id = sgqlc.types.Field(ID, graphql_name='linkPropertyTypeId')
    link_metadata = sgqlc.types.Field(ConceptTypeLinkMetadata, graphql_name='linkMetadata')


class ConceptTypePresentationWidgetTypeUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('id', 'name', 'table_type', 'columns')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    table_type = sgqlc.types.Field(sgqlc.types.non_null(WidgetTypeTableType), graphql_name='tableType')
    columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptTypePresentationWidgetTypeColumnInput))), graphql_name='columns')


class ConceptTypePresentationWidgetTypeUpdateOrderInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('concept_type_presentation_id', 'ids')
    concept_type_presentation_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptTypePresentationId')
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')


class ConceptTypeUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('id', 'x_coordinate', 'y_coordinate', 'name', 'pretrained_nercmodels', 'is_event', 'show_in_menu')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    x_coordinate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='xCoordinate')
    y_coordinate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yCoordinate')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    pretrained_nercmodels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pretrainedNERCModels')
    is_event = sgqlc.types.Field(Boolean, graphql_name='isEvent')
    show_in_menu = sgqlc.types.Field(Boolean, graphql_name='showInMenu')


class ConceptTypeViewCreationInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('concept_type_id', 'name', 'show_in_menu', 'columns')
    concept_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptTypeId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    show_in_menu = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='showInMenu')
    columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptTypePresentationWidgetTypeColumnInput))), graphql_name='columns')


class ConceptTypeViewUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('id', 'name', 'show_in_menu', 'columns')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    show_in_menu = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='showInMenu')
    columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptTypePresentationWidgetTypeColumnInput))), graphql_name='columns')


class ConceptUnmergeInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('main_concept_id', 'merged_concept_id')
    main_concept_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='mainConceptId')
    merged_concept_id = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='mergedConceptId')


class ConceptUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('concept_id', 'name', 'concept_type_id', 'notes', 'document_input', 'markers', 'access_level_id', 'start_date', 'end_date', 'approved')
    concept_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    concept_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptTypeId')
    notes = sgqlc.types.Field(String, graphql_name='notes')
    document_input = sgqlc.types.Field('FactInput', graphql_name='documentInput')
    markers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='markers')
    access_level_id = sgqlc.types.Field(ID, graphql_name='accessLevelId')
    start_date = sgqlc.types.Field('DateTimeInput', graphql_name='startDate')
    end_date = sgqlc.types.Field('DateTimeInput', graphql_name='endDate')
    approved = sgqlc.types.Field(Boolean, graphql_name='approved')


class Coordinate(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('x', 'y')
    x = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='x')
    y = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='y')


class CoordinatesInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('latitude', 'longitude')
    latitude = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='latitude')
    longitude = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='longitude')


class CountryFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('search_string', 'target')
    search_string = sgqlc.types.Field(String, graphql_name='searchString')
    target = sgqlc.types.Field(CountryTarget, graphql_name='target')


class DateInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('year', 'month', 'day')
    year = sgqlc.types.Field(Int, graphql_name='year')
    month = sgqlc.types.Field(Int, graphql_name='month')
    day = sgqlc.types.Field(Int, graphql_name='day')


class DateTimeInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('date', 'time')
    date = sgqlc.types.Field(sgqlc.types.non_null(DateInput), graphql_name='date')
    time = sgqlc.types.Field('TimeInput', graphql_name='time')


class DateTimeIntervalInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('start', 'end')
    start = sgqlc.types.Field(DateTimeInput, graphql_name='start')
    end = sgqlc.types.Field(DateTimeInput, graphql_name='end')


class Document2IssueInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('id_issue', 'document_ids', 'comment')
    id_issue = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='idIssue')
    document_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='documentIds')
    comment = sgqlc.types.Field(String, graphql_name='comment')


class DocumentAddInputInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('document_id', 'x_coordinate', 'y_coordinate', 'group_id', 'annotation')
    document_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='documentId')
    x_coordinate = sgqlc.types.Field(Float, graphql_name='xCoordinate')
    y_coordinate = sgqlc.types.Field(Float, graphql_name='yCoordinate')
    group_id = sgqlc.types.Field(ID, graphql_name='groupId')
    annotation = sgqlc.types.Field(String, graphql_name='annotation')


class DocumentAllKBFactsRemoveInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('document_id', 'kb_entity_id')
    document_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='documentId')
    kb_entity_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='kbEntityId')


class DocumentAvatarUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('id', 'children_document_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    children_document_id = sgqlc.types.Field(ID, graphql_name='childrenDocumentId')


class DocumentCardViewInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('columns', 'metrics')
    columns = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DocumentViewColumnType)), graphql_name='columns')
    metrics = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DocumentViewMetricType)), graphql_name='metrics')


class DocumentDeleteCandidateFactInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('document_id', 'fact_id')
    document_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='documentId')
    fact_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='factId')


class DocumentDuplicateReportFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('input_value', 'status', 'creators', 'created_at')
    input_value = sgqlc.types.Field(String, graphql_name='inputValue')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DocumentDuplicateReportStatus)), graphql_name='status')
    creators = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='creators')
    created_at = sgqlc.types.Field('TimestampInterval', graphql_name='createdAt')


class DocumentDuplicateReportInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('filter_setting', 'comparison_fields', 'ignore_markup', 'auto_delete')
    filter_setting = sgqlc.types.Field(sgqlc.types.non_null('DocumentFilterSettings'), graphql_name='filterSetting')
    comparison_fields = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DocumentDuplicateComparisonField))), graphql_name='comparisonFields')
    ignore_markup = sgqlc.types.Field(Boolean, graphql_name='ignoreMarkup')
    auto_delete = sgqlc.types.Field(Boolean, graphql_name='autoDelete')


class DocumentDuplicateTaskFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('report_id', 'query', 'status')
    report_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='reportId')
    query = sgqlc.types.Field(String, graphql_name='query')
    status = sgqlc.types.Field(DocumentDuplicateTaskStatus, graphql_name='status')


class DocumentFeedCreationInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('name', 'query', 'filter_settings')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    query = sgqlc.types.Field(String, graphql_name='query')
    filter_settings = sgqlc.types.Field('DocumentFilterSettings', graphql_name='filterSettings')


class DocumentFeedFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('id', 'search_string', 'creator', 'last_updater', 'registration_date', 'update_date')
    id = sgqlc.types.Field(ID, graphql_name='id')
    search_string = sgqlc.types.Field(String, graphql_name='searchString')
    creator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='creator')
    last_updater = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='lastUpdater')
    registration_date = sgqlc.types.Field('TimestampInterval', graphql_name='registrationDate')
    update_date = sgqlc.types.Field('TimestampInterval', graphql_name='updateDate')


class DocumentFeedUpdateDocumentsInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('document_ids',)
    document_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='documentIds')


class DocumentFeedUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('name', 'query', 'filter_settings')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    query = sgqlc.types.Field(String, graphql_name='query')
    filter_settings = sgqlc.types.Field('DocumentFilterSettings', graphql_name='filterSettings')


class DocumentFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema
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


class DocumentNodeUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('id', 'node_id', 'language', 'translation')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    language = sgqlc.types.Field('LanguageUpdateInput', graphql_name='language')
    translation = sgqlc.types.Field('TranslationInput', graphql_name='translation')


class DocumentRegistryViewInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('columns', 'metrics', 'sorting', 'relevance_metrics')
    columns = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DocumentViewColumnType)), graphql_name='columns')
    metrics = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DocumentViewMetricType)), graphql_name='metrics')
    sorting = sgqlc.types.Field('DocumentRegistryViewSortingInput', graphql_name='sorting')
    relevance_metrics = sgqlc.types.Field('DocumentRelevanceMetricsInput', graphql_name='relevanceMetrics')


class DocumentRegistryViewSortingInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('sorting_type', 'sort_direction')
    sorting_type = sgqlc.types.Field(sgqlc.types.non_null(DocumentSorting), graphql_name='sortingType')
    sort_direction = sgqlc.types.Field(sgqlc.types.non_null(SortDirection), graphql_name='sortDirection')


class DocumentRelevanceMetricsInput(sgqlc.types.Input):
    __schema__ = api_schema
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


class DocumentTypeAddInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('name', 'x_coordinate', 'y_coordinate', 'pretrained_nercmodels')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    x_coordinate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='xCoordinate')
    y_coordinate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yCoordinate')
    pretrained_nercmodels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pretrainedNERCModels')


class DocumentTypeFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('name', 'creator', 'last_updater', 'registration_date', 'update_date', 'regexp_exists', 'dictionary_exists', 'pretrained_nercmodels')
    name = sgqlc.types.Field(String, graphql_name='name')
    creator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='creator')
    last_updater = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='lastUpdater')
    registration_date = sgqlc.types.Field('TimestampInterval', graphql_name='registrationDate')
    update_date = sgqlc.types.Field('TimestampInterval', graphql_name='updateDate')
    regexp_exists = sgqlc.types.Field(Boolean, graphql_name='regexpExists')
    dictionary_exists = sgqlc.types.Field(Boolean, graphql_name='dictionaryExists')
    pretrained_nercmodels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pretrainedNERCModels')


class DocumentTypePresentationAddInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('name', 'document_type_id', 'is_default', 'show_in_menu', 'columns')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    document_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='documentTypeId')
    is_default = sgqlc.types.Field(Boolean, graphql_name='isDefault')
    show_in_menu = sgqlc.types.Field(Boolean, graphql_name='showInMenu')
    columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptTypePresentationWidgetTypeColumnInput))), graphql_name='columns')


class DocumentTypePresentationFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('name', 'creator', 'last_updater', 'registration_date', 'update_date')
    name = sgqlc.types.Field(String, graphql_name='name')
    creator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='creator')
    last_updater = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='lastUpdater')
    registration_date = sgqlc.types.Field('TimestampInterval', graphql_name='registrationDate')
    update_date = sgqlc.types.Field('TimestampInterval', graphql_name='updateDate')


class DocumentTypePresentationUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('id', 'name', 'is_default', 'show_in_menu', 'columns')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    is_default = sgqlc.types.Field(Boolean, graphql_name='isDefault')
    show_in_menu = sgqlc.types.Field(Boolean, graphql_name='showInMenu')
    columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptTypePresentationWidgetTypeColumnInput))), graphql_name='columns')


class DocumentTypePresentationViewInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('document_type_id', 'document_type_presentation_id')
    document_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='documentTypeId')
    document_type_presentation_id = sgqlc.types.Field(ID, graphql_name='documentTypePresentationId')


class DocumentTypeUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('id', 'x_coordinate', 'y_coordinate', 'name', 'pretrained_nercmodels')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    x_coordinate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='xCoordinate')
    y_coordinate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yCoordinate')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    pretrained_nercmodels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pretrainedNERCModels')


class DocumentUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('id', 'notes', 'title', 'preview_text', 'external_url', 'publication_date', 'publication_author', 'markers', 'trust_level', 'platform', 'account', 'language', 'access_level_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    notes = sgqlc.types.Field(String, graphql_name='notes')
    title = sgqlc.types.Field(String, graphql_name='title')
    preview_text = sgqlc.types.Field(String, graphql_name='previewText')
    external_url = sgqlc.types.Field(String, graphql_name='externalUrl')
    publication_date = sgqlc.types.Field(Long, graphql_name='publicationDate')
    publication_author = sgqlc.types.Field(String, graphql_name='publicationAuthor')
    markers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='markers')
    trust_level = sgqlc.types.Field(TrustLevel, graphql_name='trustLevel')
    platform = sgqlc.types.Field(ID, graphql_name='platform')
    account = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='account')
    language = sgqlc.types.Field(String, graphql_name='language')
    access_level_id = sgqlc.types.Field(ID, graphql_name='accessLevelId')


class DoubleValueInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('double',)
    double = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='double')


class ExtraSettings(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('search_on_map', 'ranking_script', 'selected_content')
    search_on_map = sgqlc.types.Field(Boolean, graphql_name='searchOnMap')
    ranking_script = sgqlc.types.Field(String, graphql_name='rankingScript')
    selected_content = sgqlc.types.Field('ResearchMapContentSelectInput', graphql_name='selectedContent')


class FactInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('document_id', 'annotations', 'fact_id', 'add_as_name')
    document_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='documentId')
    annotations = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TextBoundingInput')), graphql_name='annotations')
    fact_id = sgqlc.types.Field(ID, graphql_name='factId')
    add_as_name = sgqlc.types.Field(Boolean, graphql_name='addAsName')


class GeoPointFormInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('latitude', 'longitude')
    latitude = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='latitude')
    longitude = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='longitude')


class GeoPointInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('point', 'name')
    point = sgqlc.types.Field(CoordinatesInput, graphql_name='point')
    name = sgqlc.types.Field(String, graphql_name='name')


class GeoPointWithNameFormInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('point', 'name', 'radius', 'area')
    point = sgqlc.types.Field(GeoPointFormInput, graphql_name='point')
    name = sgqlc.types.Field(String, graphql_name='name')
    radius = sgqlc.types.Field(Float, graphql_name='radius')
    area = sgqlc.types.Field('GeoRectangularAreaFormInput', graphql_name='area')


class GeoRectangularAreaFormInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('latitude_min', 'longitude_min', 'latitude_max', 'longitude_max')
    latitude_min = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='latitudeMin')
    longitude_min = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='longitudeMin')
    latitude_max = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='latitudeMax')
    longitude_max = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='longitudeMax')


class GroupCreationInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('research_map_id', 'name', 'x_coordinate', 'y_coordinate', 'collapsed', 'layout', 'annotation')
    research_map_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='researchMapId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    x_coordinate = sgqlc.types.Field(Float, graphql_name='xCoordinate')
    y_coordinate = sgqlc.types.Field(Float, graphql_name='yCoordinate')
    collapsed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='collapsed')
    layout = sgqlc.types.Field(String, graphql_name='layout')
    annotation = sgqlc.types.Field(String, graphql_name='annotation')


class GroupUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('name', 'x_coordinate', 'y_coordinate', 'collapsed', 'layout', 'annotation')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    x_coordinate = sgqlc.types.Field(Float, graphql_name='xCoordinate')
    y_coordinate = sgqlc.types.Field(Float, graphql_name='yCoordinate')
    collapsed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='collapsed')
    layout = sgqlc.types.Field(String, graphql_name='layout')
    annotation = sgqlc.types.Field(String, graphql_name='annotation')


class IntValueInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('int',)
    int = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='int')


class InterestObjectMainPropertiesOrderUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('concept_type_id', 'ordered_main_property_type_ids')
    concept_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptTypeId')
    ordered_main_property_type_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='orderedMainPropertyTypeIds')


class IntervalDouble(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('start', 'end')
    start = sgqlc.types.Field(Float, graphql_name='start')
    end = sgqlc.types.Field(Float, graphql_name='end')


class IntervalInt(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('start', 'end')
    start = sgqlc.types.Field(Int, graphql_name='start')
    end = sgqlc.types.Field(Int, graphql_name='end')


class Issue2TaskInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('id_issue', 'task_ids', 'comment')
    id_issue = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='idIssue')
    task_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='taskIds')
    comment = sgqlc.types.Field(String, graphql_name='comment')


class IssueCreationInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('topic', 'description', 'status', 'priority', 'executor_id', 'execution_time_limit', 'documents', 'concepts', 'issues', 'markers')
    topic = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='topic')
    description = sgqlc.types.Field(String, graphql_name='description')
    status = sgqlc.types.Field(sgqlc.types.non_null(IssueStatus), graphql_name='status')
    priority = sgqlc.types.Field(sgqlc.types.non_null(IssuePriority), graphql_name='priority')
    executor_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='executorId')
    execution_time_limit = sgqlc.types.Field(UnixTime, graphql_name='executionTimeLimit')
    documents = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='documents')
    concepts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='concepts')
    issues = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='issues')
    markers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='markers')


class IssueEditFieldsInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('id', 'topic', 'description', 'status', 'priority', 'executor_id', 'execution_time_limit', 'markers', 'comment')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    topic = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='topic')
    description = sgqlc.types.Field(String, graphql_name='description')
    status = sgqlc.types.Field(sgqlc.types.non_null(IssueStatus), graphql_name='status')
    priority = sgqlc.types.Field(sgqlc.types.non_null(IssuePriority), graphql_name='priority')
    executor_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='executorId')
    execution_time_limit = sgqlc.types.Field(UnixTime, graphql_name='executionTimeLimit')
    markers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='markers')
    comment = sgqlc.types.Field(String, graphql_name='comment')


class IssueFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema
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


class LanguageFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('search_string',)
    search_string = sgqlc.types.Field(String, graphql_name='searchString')


class LanguageInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class LanguageUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(ID, graphql_name='id')


class LinkFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('link_type_id', 'link_direction', 'other_concept_id', 'status')
    link_type_id = sgqlc.types.Field(ID, graphql_name='linkTypeId')
    link_direction = sgqlc.types.Field(LinkDirection, graphql_name='linkDirection')
    other_concept_id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='otherConceptId')
    status = sgqlc.types.Field(KbFactStatusFilter, graphql_name='status')


class LinkValueInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('link',)
    link = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='link')


class LinkedDocumentFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('document_content_type',)
    document_content_type = sgqlc.types.Field(DocumentContentType, graphql_name='documentContentType')


class MapDrawingAddInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('research_map_id', 'x_coordinate', 'y_coordinate', 'geo', 'stroke_color', 'stroke_width', 'annotation')
    research_map_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='researchMapId')
    x_coordinate = sgqlc.types.Field(Float, graphql_name='xCoordinate')
    y_coordinate = sgqlc.types.Field(Float, graphql_name='yCoordinate')
    geo = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='geo')
    stroke_color = sgqlc.types.Field(String, graphql_name='strokeColor')
    stroke_width = sgqlc.types.Field(String, graphql_name='strokeWidth')
    annotation = sgqlc.types.Field(String, graphql_name='annotation')


class MapDrawingUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('x_coordinate', 'y_coordinate', 'geo', 'stroke_color', 'stroke_width', 'annotation')
    x_coordinate = sgqlc.types.Field(Float, graphql_name='xCoordinate')
    y_coordinate = sgqlc.types.Field(Float, graphql_name='yCoordinate')
    geo = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='geo')
    stroke_color = sgqlc.types.Field(String, graphql_name='strokeColor')
    stroke_width = sgqlc.types.Field(String, graphql_name='strokeWidth')
    annotation = sgqlc.types.Field(String, graphql_name='annotation')


class MapEdgeFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('edge_type',)
    edge_type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MapEdgeType)), graphql_name='edgeType')


class MapNodeFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('node_type',)
    node_type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MapNodeType)), graphql_name='nodeType')


class MassUpdateIssueInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('ids', 'status', 'priority', 'executor', 'execution_time_limit', 'comment')
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')
    status = sgqlc.types.Field(IssueStatus, graphql_name='status')
    priority = sgqlc.types.Field(IssuePriority, graphql_name='priority')
    executor = sgqlc.types.Field(ID, graphql_name='executor')
    execution_time_limit = sgqlc.types.Field(UnixTime, graphql_name='executionTimeLimit')
    comment = sgqlc.types.Field(String, graphql_name='comment')


class MentionInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('id', 'annotation')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    annotation = sgqlc.types.Field(AnnotationInput, graphql_name='annotation')


class NERCRegexpInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('regexp', 'context_regexp', 'auto_create')
    regexp = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='regexp')
    context_regexp = sgqlc.types.Field(String, graphql_name='contextRegexp')
    auto_create = sgqlc.types.Field(Boolean, graphql_name='autoCreate')


class NamedValueType(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('name', 'value_type_id', 'view', 'is_required')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='valueTypeId')
    view = sgqlc.types.Field(ComponentView, graphql_name='view')
    is_required = sgqlc.types.Field(Boolean, graphql_name='isRequired')


class NodeMoveInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('id', 'x_coordinate', 'y_coordinate')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    x_coordinate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='xCoordinate')
    y_coordinate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yCoordinate')


class NormalizationInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('type_id', 'value')
    type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='typeId')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class OutputLimiterInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('maximum_points', 'minimum_number')
    maximum_points = sgqlc.types.Field(Long, graphql_name='maximumPoints')
    minimum_number = sgqlc.types.Field(Long, graphql_name='minimumNumber')


class ParameterInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('key', 'value')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class PerformSynchronously(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('perform_synchronously',)
    perform_synchronously = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='performSynchronously')


class PlatformCreationInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('key', 'name', 'platform_type', 'url', 'country', 'language', 'markers', 'params')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    platform_type = sgqlc.types.Field(sgqlc.types.non_null(PlatformType), graphql_name='platformType')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    country = sgqlc.types.Field(String, graphql_name='country')
    language = sgqlc.types.Field(String, graphql_name='language')
    markers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='markers')
    params = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ParameterInput)), graphql_name='params')


class PlatformFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema
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


class PlatformUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('id', 'name', 'key', 'platform_type', 'url', 'country', 'language', 'markers', 'params')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    platform_type = sgqlc.types.Field(sgqlc.types.non_null(PlatformType), graphql_name='platformType')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    country = sgqlc.types.Field(String, graphql_name='country')
    language = sgqlc.types.Field(String, graphql_name='language')
    markers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='markers')
    params = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ParameterInput))), graphql_name='params')


class PropertyAddInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('target_id', 'property_type_id', 'value_input', 'fact_info', 'notes', 'computable_value', 'is_main', 'start_date', 'end_date', 'access_level_id')
    target_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='targetId')
    property_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='propertyTypeId')
    value_input = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ComponentValueInput))), graphql_name='valueInput')
    fact_info = sgqlc.types.Field(FactInput, graphql_name='factInfo')
    notes = sgqlc.types.Field(String, graphql_name='notes')
    computable_value = sgqlc.types.Field(String, graphql_name='computableValue')
    is_main = sgqlc.types.Field(Boolean, graphql_name='isMain')
    start_date = sgqlc.types.Field(DateTimeInput, graphql_name='startDate')
    end_date = sgqlc.types.Field(DateTimeInput, graphql_name='endDate')
    access_level_id = sgqlc.types.Field(ID, graphql_name='accessLevelId')


class PropertyFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema
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


class PropertyUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('property_id', 'is_main', 'notes', 'computable_value', 'start_date', 'end_date', 'value_input', 'access_level_id', 'approved')
    property_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='propertyId')
    is_main = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isMain')
    notes = sgqlc.types.Field(String, graphql_name='notes')
    computable_value = sgqlc.types.Field(String, graphql_name='computableValue')
    start_date = sgqlc.types.Field(DateTimeInput, graphql_name='startDate')
    end_date = sgqlc.types.Field(DateTimeInput, graphql_name='endDate')
    value_input = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ComponentValueInput))), graphql_name='valueInput')
    access_level_id = sgqlc.types.Field(ID, graphql_name='accessLevelId')
    approved = sgqlc.types.Field(Boolean, graphql_name='approved')


class PropertyValueFactInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('id', 'value', 'reject')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    value = sgqlc.types.Field('ValueInput', graphql_name='value')
    reject = sgqlc.types.Field(Boolean, graphql_name='reject')


class PropertyValueMentionFactInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('id', 'value_fact_id', 'mention_id', 'reject')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    value_fact_id = sgqlc.types.Field(ID, graphql_name='valueFactId')
    mention_id = sgqlc.types.Field(ID, graphql_name='mentionId')
    reject = sgqlc.types.Field(Boolean, graphql_name='reject')


class RedmineIssueCreationInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('obj_ids', 'issue_type', 'subject', 'assignee_id', 'tracker_id', 'status_id', 'priority_id', 'due_to', 'description', 'related_issues')
    obj_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='objIds')
    issue_type = sgqlc.types.Field(sgqlc.types.non_null(RedmineIssueType), graphql_name='issueType')
    subject = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='subject')
    assignee_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='assigneeId')
    tracker_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='trackerId')
    status_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='statusId')
    priority_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='priorityId')
    due_to = sgqlc.types.Field(Long, graphql_name='dueTo')
    description = sgqlc.types.Field(String, graphql_name='description')
    related_issues = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='relatedIssues')


class RedmineIssueDefaultParametersInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('obj_ids', 'issue_type')
    obj_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='objIds')
    issue_type = sgqlc.types.Field(sgqlc.types.non_null(RedmineIssueType), graphql_name='issueType')


class RedmineIssueUnlinkInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('object_id', 'issue_type', 'issue_ids')
    object_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='objectId')
    issue_type = sgqlc.types.Field(sgqlc.types.non_null(RedmineIssueType), graphql_name='issueType')
    issue_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='issueIds')


class RedmineIssueUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('obj_ids', 'issue_type', 'issue_ids', 'description')
    obj_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='objIds')
    issue_type = sgqlc.types.Field(sgqlc.types.non_null(RedmineIssueType), graphql_name='issueType')
    issue_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='issueIds')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')


class RegexpToUpdate(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('regexp_to_replace', 'regexp_to_insert')
    regexp_to_replace = sgqlc.types.Field(NERCRegexpInput, graphql_name='regexpToReplace')
    regexp_to_insert = sgqlc.types.Field(NERCRegexpInput, graphql_name='regexpToInsert')


class RelExtModelInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('source_annotation_type', 'target_annotation_type', 'relation_type', 'invert_direction')
    source_annotation_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sourceAnnotationType')
    target_annotation_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='targetAnnotationType')
    relation_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='relationType')
    invert_direction = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='invertDirection')


class RelatedDocumentFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('document_content_type', 'publication_date', 'registration_date', 'update_date')
    document_content_type = sgqlc.types.Field(DocumentContentType, graphql_name='documentContentType')
    publication_date = sgqlc.types.Field('TimestampInterval', graphql_name='publicationDate')
    registration_date = sgqlc.types.Field('TimestampInterval', graphql_name='registrationDate')
    update_date = sgqlc.types.Field('TimestampInterval', graphql_name='updateDate')


class ResearchMapBatchMoveInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('node_move_input',)
    node_move_input = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(NodeMoveInput))), graphql_name='nodeMoveInput')


class ResearchMapBatchUpdateGroupInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('node_ids', 'group_id')
    node_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='nodeIds')
    group_id = sgqlc.types.Field(ID, graphql_name='groupId')


class ResearchMapContentAddInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('documents', 'concepts', 'concept_candidates')
    documents = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DocumentAddInputInput)), graphql_name='documents')
    concepts = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ConceptAddInputInput)), graphql_name='concepts')
    concept_candidates = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ConceptCandidateAddInputInput)), graphql_name='conceptCandidates')


class ResearchMapContentSelectInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('nodes',)
    nodes = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='nodes')


class ResearchMapContentUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('nodes',)
    nodes = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='nodes')


class ResearchMapCreationInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('name', 'concepts', 'documents', 'description', 'access_level_id', 'markers')
    name = sgqlc.types.Field(String, graphql_name='name')
    concepts = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='concepts')
    documents = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='documents')
    description = sgqlc.types.Field(String, graphql_name='description')
    access_level_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='accessLevelId')
    markers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='markers')


class ResearchMapFilterSettings(sgqlc.types.Input):
    __schema__ = api_schema
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


class ResearchMapUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('name', 'description', 'access_level_id', 'markers')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    access_level_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='accessLevelId')
    markers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='markers')


class S3FileInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('bucket_name', 'object_name')
    bucket_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bucketName')
    object_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='objectName')


class SearchElementToUpdate(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('dict', 'regexp')
    dict = sgqlc.types.Field('WordsToUpdate', graphql_name='dict')
    regexp = sgqlc.types.Field(RegexpToUpdate, graphql_name='regexp')


class StringFilter(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('str', 'exact')
    str = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='str')
    exact = sgqlc.types.Field(Boolean, graphql_name='exact')


class StringLocaleValueInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('str', 'locale')
    str = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='str')
    locale = sgqlc.types.Field(sgqlc.types.non_null(Locale), graphql_name='locale')


class StringValueInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('str',)
    str = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='str')


class TextBoundingInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('component_id', 'start', 'end', 'node_id')
    component_id = sgqlc.types.Field(ID, graphql_name='componentId')
    start = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='start')
    end = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='end')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='nodeId')


class TimeInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('hour', 'minute', 'second')
    hour = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='hour')
    minute = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='minute')
    second = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='second')


class TimestampInterval(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('start', 'end')
    start = sgqlc.types.Field(UnixTime, graphql_name='start')
    end = sgqlc.types.Field(UnixTime, graphql_name='end')


class TimestampValueInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('value',)
    value = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='value')


class TranslationInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('language', 'text')
    language = sgqlc.types.Field(sgqlc.types.non_null(LanguageInput), graphql_name='language')
    text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='text')


class TypeSearchElementUpdateInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('id', 'elements_type', 'search_element_to_update')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    elements_type = sgqlc.types.Field(sgqlc.types.non_null(ElementType), graphql_name='elementsType')
    search_element_to_update = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SearchElementToUpdate))), graphql_name='searchElementToUpdate')


class UpdateCommentInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('task_change_id', 'comment')
    task_change_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='taskChangeId')
    comment = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='comment')


class UpdateEdgeAnnotationInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('edge_id', 'annotation')
    edge_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='edgeId')
    annotation = sgqlc.types.Field(String, graphql_name='annotation')


class UpdateNodeAnnotationInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('node_id', 'annotation')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    annotation = sgqlc.types.Field(String, graphql_name='annotation')


class ValueFilter(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('string_filter', 'int_filter', 'double_filter', 'date_time_filter', 'geo_filter')
    string_filter = sgqlc.types.Field(StringFilter, graphql_name='stringFilter')
    int_filter = sgqlc.types.Field(IntervalInt, graphql_name='intFilter')
    double_filter = sgqlc.types.Field(IntervalDouble, graphql_name='doubleFilter')
    date_time_filter = sgqlc.types.Field(DateTimeIntervalInput, graphql_name='dateTimeFilter')
    geo_filter = sgqlc.types.Field(GeoPointWithNameFormInput, graphql_name='geoFilter')


class ValueInput(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('string_value_input', 'string_locale_value_input', 'int_value_input', 'double_value_input', 'geo_point_value_input', 'date_time_value_input', 'link_value_input', 'timestamp_value_input')
    string_value_input = sgqlc.types.Field(StringValueInput, graphql_name='stringValueInput')
    string_locale_value_input = sgqlc.types.Field(StringLocaleValueInput, graphql_name='stringLocaleValueInput')
    int_value_input = sgqlc.types.Field(IntValueInput, graphql_name='intValueInput')
    double_value_input = sgqlc.types.Field(DoubleValueInput, graphql_name='doubleValueInput')
    geo_point_value_input = sgqlc.types.Field(GeoPointInput, graphql_name='geoPointValueInput')
    date_time_value_input = sgqlc.types.Field(DateTimeInput, graphql_name='dateTimeValueInput')
    link_value_input = sgqlc.types.Field(LinkValueInput, graphql_name='linkValueInput')
    timestamp_value_input = sgqlc.types.Field(TimestampValueInput, graphql_name='timestampValueInput')


class WordsToUpdate(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('word_to_replace', 'word_to_insert')
    word_to_replace = sgqlc.types.Field(String, graphql_name='wordToReplace')
    word_to_insert = sgqlc.types.Field(String, graphql_name='wordToInsert')


class conceptTypeAndEventFilter(sgqlc.types.Input):
    __schema__ = api_schema
    __field_names__ = ('full_type', 'is_event')
    full_type = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='fullType')
    is_event = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isEvent')



########################################################################
# Output Objects and Interfaces
########################################################################
class DocumentGroupFacet(sgqlc.types.Interface):
    __schema__ = api_schema
    __field_names__ = ('group', 'count')
    group = sgqlc.types.Field(sgqlc.types.non_null(DocumentGroupingCategory), graphql_name='group')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count')


class EntityTypePresentation(sgqlc.types.Interface):
    __schema__ = api_schema
    __field_names__ = ('metric', 'list_concept_link_type', 'show_in_menu')
    metric = sgqlc.types.Field(sgqlc.types.non_null('EntityTypePresentationStatistics'), graphql_name='metric')
    list_concept_link_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptLinkType'))), graphql_name='listConceptLinkType')
    show_in_menu = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='showInMenu')


class FactInterface(sgqlc.types.Interface):
    __schema__ = api_schema
    __field_names__ = ('id', 'system_registration_date', 'system_update_date', 'document')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    system_registration_date = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='systemRegistrationDate')
    system_update_date = sgqlc.types.Field(UnixTime, graphql_name='systemUpdateDate')
    document = sgqlc.types.Field(sgqlc.types.non_null('Document'), graphql_name='document')


class HasTypeSearchElements(sgqlc.types.Interface):
    __schema__ = api_schema
    __field_names__ = ('pretrained_nercmodels', 'list_white_dictionary', 'list_white_regexp', 'list_black_dictionary', 'list_black_regexp', 'list_type_search_element', 'list_type_black_search_element')
    pretrained_nercmodels = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='pretrainedNERCModels')
    list_white_dictionary = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='listWhiteDictionary')
    list_white_regexp = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('NERCRegexp'))), graphql_name='listWhiteRegexp')
    list_black_dictionary = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='listBlackDictionary')
    list_black_regexp = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('NERCRegexp'))), graphql_name='listBlackRegexp')
    list_type_search_element = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TypeSearchElement'))), graphql_name='listTypeSearchElement')
    list_type_black_search_element = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TypeSearchElement'))), graphql_name='listTypeBlackSearchElement')


class LinkTarget(sgqlc.types.Interface):
    __schema__ = api_schema
    __field_names__ = ('pagination_link',)
    pagination_link = sgqlc.types.Field(sgqlc.types.non_null('ConceptLinkPagination'), graphql_name='paginationLink', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptLinkFilterSettings), graphql_name='filterSettings', default=None)),
))
    )


class LinkTypeTarget(sgqlc.types.Interface):
    __schema__ = api_schema
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
    __schema__ = api_schema
    __field_names__ = ('id', 'system_registration_date', 'system_update_date', 'document', 'mention_fact')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    system_registration_date = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='systemRegistrationDate')
    system_update_date = sgqlc.types.Field(UnixTime, graphql_name='systemUpdateDate')
    document = sgqlc.types.Field(sgqlc.types.non_null('Document'), graphql_name='document')
    mention_fact = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FactInterface))), graphql_name='mentionFact')


class PropertyTarget(sgqlc.types.Interface):
    __schema__ = api_schema
    __field_names__ = ('pagination_property',)
    pagination_property = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyPagination'), graphql_name='paginationProperty', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptPropertyFilterSettings), graphql_name='filterSettings', default=None)),
))
    )


class PropertyTypeTarget(sgqlc.types.Interface):
    __schema__ = api_schema
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
    __schema__ = api_schema
    __field_names__ = ('system_registration_date', 'system_update_date', 'creator', 'last_updater')
    system_registration_date = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='systemRegistrationDate')
    system_update_date = sgqlc.types.Field(UnixTime, graphql_name='systemUpdateDate')
    creator = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='creator')
    last_updater = sgqlc.types.Field('User', graphql_name='lastUpdater')


class EntityType(sgqlc.types.Interface):
    __schema__ = api_schema
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
    __schema__ = api_schema
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
    __schema__ = api_schema
    __field_names__ = ('id', 'name', 'order')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    order = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='order')


class AccessLevelPagination(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('list_access_level', 'total')
    list_access_level = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AccessLevel))), graphql_name='listAccessLevel')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class AccountFacet(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('value', 'count')
    value = sgqlc.types.Field(sgqlc.types.non_null('Account'), graphql_name='value')
    count = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='count')


class AccountPagination(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('list_account', 'total', 'total_platforms')
    list_account = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Account'))), graphql_name='listAccount')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')
    total_platforms = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalPlatforms')


class AccountStatistics(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('count_doc',)
    count_doc = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countDoc')


class Annotation(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('start', 'end', 'value')
    start = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='start')
    end = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='end')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class Autocomplete(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('autocomplete',)
    autocomplete = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='autocomplete')


class Chart(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('id', 'description', 'data')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    description = sgqlc.types.Field(sgqlc.types.non_null('ChartDescription'), graphql_name='description')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ChartData'))), graphql_name='data')


class ChartData(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('x', 'y')
    x = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='x')
    y = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='y')


class ChartDescription(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('chart_type', 'target', 'query', 'aggregation_field', 'aggregation_function', 'output_limiter')
    chart_type = sgqlc.types.Field(sgqlc.types.non_null(ChartType), graphql_name='chartType')
    target = sgqlc.types.Field(sgqlc.types.non_null(ChartTarget), graphql_name='target')
    query = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='query')
    aggregation_field = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='aggregationField')
    aggregation_function = sgqlc.types.Field(AggregationFunction, graphql_name='aggregationFunction')
    output_limiter = sgqlc.types.Field(sgqlc.types.non_null('OutputLimiter'), graphql_name='outputLimiter')


class CommonStringPagination(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('total', 'list_string')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')
    list_string = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='listString')


class CompositePropertyValueTemplatePagination(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('list_composite_property_value_template', 'total')
    list_composite_property_value_template = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CompositePropertyValueTemplate'))), graphql_name='listCompositePropertyValueTemplate')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class CompositePropertyValueType(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('id', 'name', 'value_type', 'is_required', 'view')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyValueType'), graphql_name='valueType')
    is_required = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRequired')
    view = sgqlc.types.Field(sgqlc.types.non_null(ComponentView), graphql_name='view')


class CompositeValue(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('list_value',)
    list_value = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('NamedValue'))), graphql_name='listValue')


class ConceptCandidateFactMention(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('concept', 'mention')
    concept = sgqlc.types.Field(sgqlc.types.non_null('ConceptCandidateFact'), graphql_name='concept')
    mention = sgqlc.types.Field(sgqlc.types.non_null('Mention'), graphql_name='mention')


class ConceptFacet(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('count', 'value')
    count = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='count')
    value = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='value')


class ConceptFactLink(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('concept_id', 'concept_fact_id', 'status', 'is_implicit', 'concept', 'concept_fact')
    concept_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptId')
    concept_fact_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptFactId')
    status = sgqlc.types.Field(FactStatus, graphql_name='status')
    is_implicit = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isImplicit')
    concept = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='concept')
    concept_fact = sgqlc.types.Field(sgqlc.types.non_null('ConceptCandidateFact'), graphql_name='conceptFact')


class ConceptFactPagination(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('total', 'list_concept_fact')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')
    list_concept_fact = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptFact'))), graphql_name='listConceptFact')


class ConceptImplicitLink(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('concept_from_id', 'concept_to_id', 'concept_from', 'concept_to', 'concept_link_type')
    concept_from_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptFromId')
    concept_to_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='conceptToId')
    concept_from = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='conceptFrom')
    concept_to = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='conceptTo')
    concept_link_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptLinkType'), graphql_name='conceptLinkType')


class ConceptLinkFactPagination(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('total', 'list_concept_link_fact')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')
    list_concept_link_fact = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptLinkFact'))), graphql_name='listConceptLinkFact')


class ConceptLinkPagination(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('total', 'list_concept_link')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')
    list_concept_link = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptLink'))), graphql_name='listConceptLink')


class ConceptLinkTypePagination(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('list_concept_link_type', 'total')
    list_concept_link_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptLinkType'))), graphql_name='listConceptLinkType')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class ConceptLinkTypePath(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('link_type', 'fixed')
    link_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptLinkType'), graphql_name='linkType')
    fixed = sgqlc.types.Field(ConceptLinkDirection, graphql_name='fixed')


class ConceptLinkTypeStatistics(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('count_property_type',)
    count_property_type = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countPropertyType')


class ConceptMention(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('concept', 'mention')
    concept = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='concept')
    mention = sgqlc.types.Field(sgqlc.types.non_null('Mention'), graphql_name='mention')


class ConceptPagination(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('total', 'show_total', 'list_concept', 'precise_total')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')
    show_total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='showTotal')
    list_concept = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Concept'))), graphql_name='listConcept')
    precise_total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='preciseTotal')


class ConceptPaginationResult(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('total', 'show_total', 'list_concept')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')
    show_total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='showTotal')
    list_concept = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Concept'))), graphql_name='listConcept')


class ConceptPresentation(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('root_concept', 'concept_type_presentation', 'id', 'list_concepts', 'paginate_single_widget', 'pagination_concept_mention', 'list_concept_mention')
    root_concept = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='rootConcept')
    concept_type_presentation = sgqlc.types.Field(sgqlc.types.non_null('ConceptTypePresentation'), graphql_name='conceptTypePresentation')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    list_concepts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Concept'))), graphql_name='listConcepts')
    paginate_single_widget = sgqlc.types.Field(sgqlc.types.non_null('ConceptPresentationWidgetRowPagination'), graphql_name='paginateSingleWidget', args=sgqlc.types.ArgDict((
        ('widget_type_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='widgetTypeId', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
))
    )
    pagination_concept_mention = sgqlc.types.Field(ConceptFactPagination, graphql_name='paginationConceptMention', args=sgqlc.types.ArgDict((
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(LinkedDocumentFilterSettings), graphql_name='filterSettings', default=None)),
))
    )
    list_concept_mention = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ConceptFact')), graphql_name='listConceptMention')


class ConceptPresentationPagination(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('list_concept_presentation', 'total')
    list_concept_presentation = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptPresentation))), graphql_name='listConceptPresentation')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')


class ConceptPresentationWidgetRowPagination(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('widget_type', 'total', 'rows')
    widget_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptTypePresentationWidgetType'), graphql_name='widgetType')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')
    rows = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptViewValue'))))))), graphql_name='rows')


class ConceptPropertyPagination(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('total', 'list_concept_property')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')
    list_concept_property = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptProperty'))), graphql_name='listConceptProperty')


class ConceptPropertyTypePagination(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('list_concept_property_type', 'total')
    list_concept_property_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptPropertyType'))), graphql_name='listConceptPropertyType')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class ConceptPropertyValueStatistics(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('count_concept_type', 'count_link_type', 'count_dictionary', 'count_regexp')
    count_concept_type = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countConceptType')
    count_link_type = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countLinkType')
    count_dictionary = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countDictionary')
    count_regexp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countRegexp')


class ConceptPropertyValueTypePagination(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('list_concept_property_value_type', 'total')
    list_concept_property_value_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptPropertyValueType'))), graphql_name='listConceptPropertyValueType')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class ConceptRegistryView(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('columns', 'metrics', 'sorting')
    columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptRegistryViewColumn'))), graphql_name='columns')
    metrics = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptRegistryViewMetric'))), graphql_name='metrics')
    sorting = sgqlc.types.Field('ConceptRegistryViewSorting', graphql_name='sorting')


class ConceptRegistryViewColumn(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('column_type',)
    column_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptViewColumnType), graphql_name='columnType')


class ConceptRegistryViewMetric(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('metric_type',)
    metric_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptViewMetricType), graphql_name='metricType')


class ConceptRegistryViewSorting(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('sorting_type', 'sort_direction')
    sorting_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptSorting), graphql_name='sortingType')
    sort_direction = sgqlc.types.Field(sgqlc.types.non_null(SortDirection), graphql_name='sortDirection')


class ConceptStatistics(sgqlc.types.Type):
    __schema__ = api_schema
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
    __schema__ = api_schema
    __field_names__ = ('subscriptions', 'list_user', 'count_users')
    subscriptions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptUpdate))), graphql_name='subscriptions')
    list_user = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='listUser')
    count_users = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countUsers')


class ConceptTypePagination(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('list_concept_type', 'total')
    list_concept_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptType'))), graphql_name='listConceptType')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class ConceptTypePresentationPagination(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('list_concept_type_presentation', 'total')
    list_concept_type_presentation = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptTypePresentation'))), graphql_name='listConceptTypePresentation')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class ConceptTypePresentationWidgetTypeColumn(sgqlc.types.Type):
    __schema__ = api_schema
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
    __schema__ = api_schema
    __field_names__ = ('list_concept_type_presentation_widget', 'total')
    list_concept_type_presentation_widget = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptTypePresentationWidgetType'))), graphql_name='listConceptTypePresentationWidget')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class ConceptTypeViewPagination(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('list_concept_type_view', 'total')
    list_concept_type_view = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptTypeView'))), graphql_name='listConceptTypeView')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class ConceptView(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('concept', 'rows')
    concept = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='concept')
    rows = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptViewValue'))))), graphql_name='rows')


class ConceptViewPagination(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('total', 'list_concept_view')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')
    list_concept_view = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptView))), graphql_name='listConceptView')


class ConceptWithConfidence(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('concept', 'confidence')
    concept = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='concept')
    confidence = sgqlc.types.Field(Float, graphql_name='confidence')


class ConceptWithNeighbors(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('concept', 'num_of_neighbors')
    concept = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='concept')
    num_of_neighbors = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='numOfNeighbors')


class Coordinates(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('latitude', 'longitude')
    latitude = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='latitude')
    longitude = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='longitude')


class CountryPagination(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('list_country', 'total')
    list_country = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='listCountry')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class Date(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('year', 'month', 'day')
    year = sgqlc.types.Field(Int, graphql_name='year')
    month = sgqlc.types.Field(Int, graphql_name='month')
    day = sgqlc.types.Field(Int, graphql_name='day')


class DateTimeInterval(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('start', 'end')
    start = sgqlc.types.Field('DateTimeValue', graphql_name='start')
    end = sgqlc.types.Field('DateTimeValue', graphql_name='end')


class DateTimeValue(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('date', 'time')
    date = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='date')
    time = sgqlc.types.Field('Time', graphql_name='time')


class DeleteDrawing(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class DeleteEdge(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class DeleteGroup(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class DeleteNode(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class DictValue(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('value',)
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class DocSpecificMetadata(sgqlc.types.Type):
    __schema__ = api_schema
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


class DocumentCardView(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('columns', 'metrics')
    columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DocumentCardViewColumn'))), graphql_name='columns')
    metrics = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DocumentViewMetric'))), graphql_name='metrics')


class DocumentCardViewColumn(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('column_type',)
    column_type = sgqlc.types.Field(sgqlc.types.non_null(DocumentViewColumnType), graphql_name='columnType')


class DocumentDuplicateReportMetrics(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('documents_count', 'duplicates_count', 'deleted_count')
    documents_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='documentsCount')
    duplicates_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='duplicatesCount')
    deleted_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='deletedCount')


class DocumentDuplicateReportPagination(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('list_document_duplicate_report', 'total')
    list_document_duplicate_report = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DocumentDuplicateReport'))), graphql_name='listDocumentDuplicateReport')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class DocumentDuplicateTask(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('id', 'report_id', 'duplicate_document_id', 'original_document_id', 'status')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    report_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='reportId')
    duplicate_document_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='duplicateDocumentId')
    original_document_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='originalDocumentId')
    status = sgqlc.types.Field(sgqlc.types.non_null(DocumentDuplicateTaskStatus), graphql_name='status')


class DocumentDuplicateTaskPagination(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('list_document_duplicate_task', 'total')
    list_document_duplicate_task = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DocumentDuplicateTask))), graphql_name='listDocumentDuplicateTask')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class DocumentFacets(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('document_metadata_facets', 'approved_entities_facets', 'not_approved_entities_facets', 'calculated_at', 'id')
    document_metadata_facets = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DocumentGroupFacet)), graphql_name='documentMetadataFacets')
    approved_entities_facets = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DocumentGroupFacet)), graphql_name='approvedEntitiesFacets')
    not_approved_entities_facets = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DocumentGroupFacet)), graphql_name='notApprovedEntitiesFacets')
    calculated_at = sgqlc.types.Field(UnixTime, graphql_name='calculatedAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class DocumentFeedPagination(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('list_document_feed', 'total')
    list_document_feed = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DocumentFeed'))), graphql_name='listDocumentFeed')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class DocumentFromDocumentFeed(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('document', 'is_from_favorites', 'is_from_deleted')
    document = sgqlc.types.Field(sgqlc.types.non_null('Document'), graphql_name='document')
    is_from_favorites = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isFromFavorites')
    is_from_deleted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isFromDeleted')


class DocumentFromDocumentFeedPagination(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('list_document', 'list_named_entity_count_facet', 'list_concept_count_facet', 'document_facets', 'total', 'show_total')
    list_document = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DocumentFromDocumentFeed))), graphql_name='listDocument')
    list_named_entity_count_facet = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Facet'))), graphql_name='listNamedEntityCountFacet')
    list_concept_count_facet = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptFacet))), graphql_name='listConceptCountFacet')
    document_facets = sgqlc.types.Field(sgqlc.types.non_null(DocumentFacets), graphql_name='documentFacets')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')
    show_total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='showTotal')


class DocumentLink(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('parent_id', 'child_id')
    parent_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='parentId')
    child_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='childId')


class DocumentMetadata(sgqlc.types.Type):
    __schema__ = api_schema
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
    __schema__ = api_schema
    __field_names__ = ('list_document', 'total')
    list_document = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Document'))), graphql_name='listDocument')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class DocumentRegistryView(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('columns', 'metrics', 'sorting', 'relevance')
    columns = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DocumentRegistryViewColumn'))), graphql_name='columns')
    metrics = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DocumentViewMetric'))), graphql_name='metrics')
    sorting = sgqlc.types.Field('DocumentRegistryViewSorting', graphql_name='sorting')
    relevance = sgqlc.types.Field('DocumentRelevanceMetrics', graphql_name='relevance')


class DocumentRegistryViewColumn(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('column_type',)
    column_type = sgqlc.types.Field(sgqlc.types.non_null(DocumentViewColumnType), graphql_name='columnType')


class DocumentRegistryViewSorting(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('sorting_type', 'sort_direction')
    sorting_type = sgqlc.types.Field(sgqlc.types.non_null(DocumentSorting), graphql_name='sortingType')
    sort_direction = sgqlc.types.Field(sgqlc.types.non_null(SortDirection), graphql_name='sortDirection')


class DocumentRelevanceMetrics(sgqlc.types.Type):
    __schema__ = api_schema
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


class DocumentSubscriptions(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('subscriptions', 'list_user', 'count_users')
    subscriptions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DocumentUpdate))), graphql_name='subscriptions')
    list_user = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='listUser')
    count_users = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countUsers')


class DocumentTypePagination(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('list_document_type', 'total')
    list_document_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DocumentType'))), graphql_name='listDocumentType')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class DocumentTypePresentationPagination(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('list_document_type_presentation', 'total')
    list_document_type_presentation = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DocumentTypePresentation'))), graphql_name='listDocumentTypePresentation')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class DocumentViewMetric(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('metric_type',)
    metric_type = sgqlc.types.Field(sgqlc.types.non_null(DocumentViewMetricType), graphql_name='metricType')


class DomainMap(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('list_node', 'list_edge')
    list_node = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MapNode'))), graphql_name='listNode')
    list_edge = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MapEdge'))), graphql_name='listEdge')


class DoubleValue(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('value',)
    value = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='value')


class EntityTypePresentationStatistics(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('count_concept_types', 'count_document_types', 'count_entity_types')
    count_concept_types = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countConceptTypes')
    count_document_types = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countDocumentTypes')
    count_entity_types = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countEntityTypes')


class EntityTypeStatistics(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('count_property_type', 'count_link_type', 'count_dictionary', 'count_regexp')
    count_property_type = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countPropertyType')
    count_link_type = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countLinkType')
    count_dictionary = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countDictionary')
    count_regexp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countRegexp')


class Facet(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('value', 'count')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')
    count = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='count')


class FlatDocumentStructure(sgqlc.types.Type):
    __schema__ = api_schema
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
    __schema__ = api_schema
    __field_names__ = ('concept', 'concept_property')
    concept = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='concept')
    concept_property = sgqlc.types.Field(sgqlc.types.non_null('ConceptProperty'), graphql_name='conceptProperty')


class GeoPointValue(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('point', 'name')
    point = sgqlc.types.Field(Coordinates, graphql_name='point')
    name = sgqlc.types.Field(String, graphql_name='name')


class Group(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('id', 'name', 'x_coordinate', 'y_coordinate', 'collapsed', 'layout', 'annotation')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    x_coordinate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='xCoordinate')
    y_coordinate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yCoordinate')
    collapsed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='collapsed')
    layout = sgqlc.types.Field(String, graphql_name='layout')
    annotation = sgqlc.types.Field(String, graphql_name='annotation')


class HLAnnotation(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('start', 'end')
    start = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='start')
    end = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='end')


class Highlighting(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('highlighting', 'annotations')
    highlighting = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='highlighting')
    annotations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(HLAnnotation))), graphql_name='annotations')


class Image(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('url',)
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')


class ImageSpecificMetadataGQL(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('height', 'width', 'orientation')
    height = sgqlc.types.Field(Long, graphql_name='height')
    width = sgqlc.types.Field(Long, graphql_name='width')
    orientation = sgqlc.types.Field(Int, graphql_name='orientation')


class IntValue(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('value',)
    value = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='value')


class IssueChangePagination(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('total', 'list_issue_change')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')
    list_issue_change = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IssueChange'))), graphql_name='listIssueChange')


class IssueInfo(sgqlc.types.Type):
    __schema__ = api_schema
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
    __schema__ = api_schema
    __field_names__ = ('list_issue', 'total')
    list_issue = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Issue'))), graphql_name='listIssue')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class IssueStatistics(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('count_concept', 'count_doc', 'count_issue')
    count_concept = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countConcept')
    count_doc = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countDoc')
    count_issue = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countIssue')


class Language(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class LanguagePagination(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('list_language', 'total')
    list_language = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='listLanguage')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class LinkValue(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('link',)
    link = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='link')


class MapDrawing(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('id', 'x_coordinate', 'y_coordinate', 'geo', 'stroke_color', 'stroke_width', 'annotation')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    x_coordinate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='xCoordinate')
    y_coordinate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yCoordinate')
    geo = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='geo')
    stroke_color = sgqlc.types.Field(String, graphql_name='strokeColor')
    stroke_width = sgqlc.types.Field(String, graphql_name='strokeWidth')
    annotation = sgqlc.types.Field(String, graphql_name='annotation')


class MapEdge(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('from_id', 'to_id', 'link_type', 'id', 'annotation', 'link')
    from_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='fromID')
    to_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='toID')
    link_type = sgqlc.types.Field(sgqlc.types.non_null(MapEdgeType), graphql_name='linkType')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    annotation = sgqlc.types.Field(String, graphql_name='annotation')
    link = sgqlc.types.Field(sgqlc.types.non_null('EntityLink'), graphql_name='link')


class MapEvents(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('event_list',)
    event_list = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MapEvent'))), graphql_name='eventList')


class MapNode(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('id', 'group_id', 'x_coordinate', 'y_coordinate', 'node_type', 'annotation', 'entity')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    group_id = sgqlc.types.Field(ID, graphql_name='groupId')
    x_coordinate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='xCoordinate')
    y_coordinate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yCoordinate')
    node_type = sgqlc.types.Field(sgqlc.types.non_null(MapNodeType), graphql_name='nodeType')
    annotation = sgqlc.types.Field(String, graphql_name='annotation')
    entity = sgqlc.types.Field(sgqlc.types.non_null('Entity'), graphql_name='entity')


class Markers(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('markers',)
    markers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='markers')


class Mention(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('id', 'document_id', 'text_bounding', 'verifier', 'system_registration_date', 'system_update_date', 'access_level')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    document_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='documentId')
    text_bounding = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TextBounding'))), graphql_name='textBounding')
    verifier = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='verifier')
    system_registration_date = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='systemRegistrationDate')
    system_update_date = sgqlc.types.Field(UnixTime, graphql_name='systemUpdateDate')
    access_level = sgqlc.types.Field(sgqlc.types.non_null(AccessLevel), graphql_name='accessLevel')


class MentionLink(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('id', 'mention_link_type', 'source', 'target')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    mention_link_type = sgqlc.types.Field(sgqlc.types.non_null(MentionLinkType), graphql_name='mentionLinkType')
    source = sgqlc.types.Field(sgqlc.types.non_null('MentionUnion'), graphql_name='source')
    target = sgqlc.types.Field(sgqlc.types.non_null('MentionUnion'), graphql_name='target')


class MergedConcept(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('concept', 'merge_author', 'merge_date')
    concept = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='concept')
    merge_author = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='mergeAuthor')
    merge_date = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='mergeDate')


class MergedConceptPagination(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('total', 'list_merged_concept')
    total = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='total')
    list_merged_concept = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MergedConcept))), graphql_name='listMergedConcept')


class Metrics(sgqlc.types.Type):
    __schema__ = api_schema
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
    __schema__ = api_schema
    __field_names__ = ('add_concept', 'add_concept_link', 'reverse_concept_link', 'update_concept_link', 'add_concept_property', 'add_concept_link_property', 'add_concept_fact', 'delete_concept_fact', 'add_concept_link_property_fact', 'delete_concept_link_property_fact', 'add_concept_property_fact', 'delete_concept_property_fact', 'add_concept_link_fact', 'delete_concept_link_fact', 'update_concept', 'update_concept_avatar', 'update_concept_property', 'approve_kb_fact', 'delete_concept_property', 'delete_concept_link', 'delete_concept', 'delete_concept_link_property', 'merge_concepts', 'unmerge_concepts', 'delete_fact', 'normalize_value', 'update_concept_subscriptions', 'add_property', 'update_property', 'delete_property', 'add_concept_type', 'add_document_type', 'add_concept_type_presentation', 'add_concept_type_presentation_template', 'add_concept_type_presentation_widget_type', 'add_document_type_presentation', 'set_concept_type_default_view', 'set_document_type_default_view', 'add_concept_property_type', 'add_concept_link_property_type', 'add_concept_link_type', 'add_concept_property_value_type', 'add_concept_type_view', 'update_concept_type', 'update_document_type', 'update_concept_type_presentation', 'update_concept_type_presentation_template_filename', 'update_concept_type_presentation_widget_type', 'update_concept_type_presentation_widget_types_order', 'update_document_type_presentation', 'update_concept_property_type', 'update_concept_main_property_type_order', 'update_concept_link_property_type', 'update_concept_link_type', 'update_concept_property_value_type', 'update_concept_type_view', 'update_concept_type_view_show_in_menu', 'delete_concept_type_avatar', 'delete_concept_type', 'delete_document_type', 'delete_concept_type_presentation', 'delete_concept_type_presentation_widget_type', 'delete_document_type_presentation', 'delete_concept_property_type', 'delete_concept_link_property_type', 'delete_concept_link_type', 'delete_concept_property_value_type', 'delete_concept_type_view', 'delete_bulk', 'move_bulk', 'update_type_search_element', 'add_composite_property_value_template', 'update_composite_property_value_template', 'delete_composite_property_value_template', 'add_issue', 'delete_issue', 'add_concept_to_issue', 'add_document_to_issue', 'add_issue_to_issue', 'delete_document_from_issue', 'delete_concept_from_issue', 'delete_issue_from_issue', 'update_issue', 'update_issue_massive', 'add_comment_to_issue', 'update_issue_comment', 'delete_issue_comment', 'update_document', 'update_document_avatar', 'remove_candidate_fact_from_document', 'remove_all_candidate_facts_from_document', 'update_document_facts', 'remove_all_kbfacts_from_document', 'delete_documents', 'update_document_node', 'update_document_subscriptions', 'mark_document_as_read', 'mark_document_as_unread', 'add_document_duplicate_report', 'delete_document_duplicate_report', 'decline_document_duplicate_task', 'delete_document_duplicate_task', 'delete_all_document_duplicate_task', 'delete_research_map', 'bulk_delete_research_map', 'add_research_map', 'add_research_map_from_files', 'update_research_map', 'add_content_on_research_map', 'delete_content_from_research_map', 'batch_move_nodes_on_map', 'batch_update_group_on_map', 'update_node_annotation', 'update_edge_annotation', 'add_top_neighbors_on_map', 'add_concept_fact_neighbors_on_map', 'add_not_approved_neighbors_on_map', 'set_research_map_active', 'find_shortest_path_on_map', 'find_shortest_implicit_path_on_map', 'add_group', 'update_group', 'delete_group', 'add_drawing', 'update_drawing', 'delete_drawing', 'create_redmine_issue', 'update_redmine_issue', 'unlink_issues', 'add_access_level', 'update_access_level', 'delete_access_level', 'add_template_docx', 'update_markers_bulk', 'update_document_bulk', 'add_platform', 'update_platform', 'delete_platform', 'add_account', 'update_account', 'delete_account', 'add_document_feed', 'update_document_feed', 'add_document_to_document_feed_favorites', 'delete_document_from_document_feed_favorites', 'delete_document_from_document_feed', 'restore_document_to_document_feed', 'delete_document_feed', 'update_document_facets', 'update_concept_registry_view', 'update_document_registry_view', 'update_document_card_view', 'add_chart', 'update_chart', 'delete_chart', 'translate_tql', 'create_ok_sync_package')
    add_concept = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='addConcept', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptMutationInput), graphql_name='form', default=None)),
        ('performance_control', sgqlc.types.Arg(PerformSynchronously, graphql_name='performanceControl', default={'performSynchronously': True})),
        ('file', sgqlc.types.Arg(S3FileInput, graphql_name='file', default=None)),
))
    )
    add_concept_link = sgqlc.types.Field(sgqlc.types.non_null('ConceptLink'), graphql_name='addConceptLink', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptLinkCreationMutationInput), graphql_name='form', default=None)),
        ('performance_control', sgqlc.types.Arg(PerformSynchronously, graphql_name='performanceControl', default={'performSynchronously': True})),
))
    )
    reverse_concept_link = sgqlc.types.Field(sgqlc.types.non_null('ConceptLink'), graphql_name='reverseConceptLink', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    update_concept_link = sgqlc.types.Field(sgqlc.types.non_null('ConceptLink'), graphql_name='updateConceptLink', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptLinkUpdateMutationInput), graphql_name='form', default=None)),
))
    )
    add_concept_property = sgqlc.types.Field(sgqlc.types.non_null('ConceptProperty'), graphql_name='addConceptProperty', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptPropertyCreateInput), graphql_name='form', default=None)),
        ('performance_control', sgqlc.types.Arg(PerformSynchronously, graphql_name='performanceControl', default={'performSynchronously': True})),
))
    )
    add_concept_link_property = sgqlc.types.Field(sgqlc.types.non_null('ConceptProperty'), graphql_name='addConceptLinkProperty', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptLinkPropertyInput), graphql_name='form', default=None)),
        ('performance_control', sgqlc.types.Arg(PerformSynchronously, graphql_name='performanceControl', default={'performSynchronously': True})),
))
    )
    add_concept_fact = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='addConceptFact', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('fact', sgqlc.types.Arg(sgqlc.types.non_null(FactInput), graphql_name='fact', default=None)),
        ('performance_control', sgqlc.types.Arg(PerformSynchronously, graphql_name='performanceControl', default={'performSynchronously': True})),
))
    )
    delete_concept_fact = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteConceptFact', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    add_concept_link_property_fact = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='addConceptLinkPropertyFact', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('fact', sgqlc.types.Arg(sgqlc.types.non_null(FactInput), graphql_name='fact', default=None)),
        ('performance_control', sgqlc.types.Arg(PerformSynchronously, graphql_name='performanceControl', default={'performSynchronously': True})),
))
    )
    delete_concept_link_property_fact = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteConceptLinkPropertyFact', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    add_concept_property_fact = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='addConceptPropertyFact', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('fact', sgqlc.types.Arg(sgqlc.types.non_null(FactInput), graphql_name='fact', default=None)),
        ('performance_control', sgqlc.types.Arg(PerformSynchronously, graphql_name='performanceControl', default={'performSynchronously': True})),
))
    )
    delete_concept_property_fact = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteConceptPropertyFact', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    add_concept_link_fact = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='addConceptLinkFact', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('fact', sgqlc.types.Arg(sgqlc.types.non_null(FactInput), graphql_name='fact', default=None)),
        ('performance_control', sgqlc.types.Arg(PerformSynchronously, graphql_name='performanceControl', default={'performSynchronously': True})),
))
    )
    delete_concept_link_fact = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteConceptLinkFact', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    update_concept = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='updateConcept', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptUpdateInput), graphql_name='form', default=None)),
        ('performance_control', sgqlc.types.Arg(PerformSynchronously, graphql_name='performanceControl', default={'performSynchronously': True})),
))
    )
    update_concept_avatar = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='updateConceptAvatar', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('document_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='documentId', default=None)),
))
    )
    update_concept_property = sgqlc.types.Field(sgqlc.types.non_null('ConceptProperty'), graphql_name='updateConceptProperty', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptPropertyUpdateInput), graphql_name='form', default=None)),
))
    )
    approve_kb_fact = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='approveKbFact', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    delete_concept_property = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteConceptProperty', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_concept_link = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteConceptLink', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_concept = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteConcept', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
        ('performance_control', sgqlc.types.Arg(PerformSynchronously, graphql_name='performanceControl', default={'performSynchronously': False})),
))
    )
    delete_concept_link_property = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteConceptLinkProperty', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    merge_concepts = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='mergeConcepts', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptMergeInput), graphql_name='form', default=None)),
))
    )
    unmerge_concepts = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='unmergeConcepts', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptUnmergeInput), graphql_name='form', default=None)),
))
    )
    delete_fact = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteFact', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    normalize_value = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AnyValue'))), graphql_name='normalizeValue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(NormalizationInput), graphql_name='input', default=None)),
))
    )
    update_concept_subscriptions = sgqlc.types.Field(sgqlc.types.non_null('Concept'), graphql_name='updateConceptSubscriptions', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('events', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptUpdate))), graphql_name='events', default=None)),
))
    )
    add_property = sgqlc.types.Field(sgqlc.types.non_null('ConceptProperty'), graphql_name='addProperty', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(PropertyAddInput), graphql_name='form', default=None)),
        ('performance_control', sgqlc.types.Arg(PerformSynchronously, graphql_name='performanceControl', default={'performSynchronously': True})),
))
    )
    update_property = sgqlc.types.Field(sgqlc.types.non_null('ConceptProperty'), graphql_name='updateProperty', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(PropertyUpdateInput), graphql_name='form', default=None)),
))
    )
    delete_property = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteProperty', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    add_concept_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptType'), graphql_name='addConceptType', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptTypeAddInput), graphql_name='form', default=None)),
        ('file', sgqlc.types.Arg(S3FileInput, graphql_name='file', default=None)),
))
    )
    add_document_type = sgqlc.types.Field(sgqlc.types.non_null('DocumentType'), graphql_name='addDocumentType', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(DocumentTypeAddInput), graphql_name='form', default=None)),
        ('file', sgqlc.types.Arg(S3FileInput, graphql_name='file', default=None)),
))
    )
    add_concept_type_presentation = sgqlc.types.Field(sgqlc.types.non_null('ConceptTypePresentation'), graphql_name='addConceptTypePresentation', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptTypePresentationAddInput), graphql_name='form', default=None)),
))
    )
    add_concept_type_presentation_template = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='addConceptTypePresentationTemplate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('s3_file_input', sgqlc.types.Arg(sgqlc.types.non_null(S3FileInput), graphql_name='s3FileInput', default=None)),
))
    )
    add_concept_type_presentation_widget_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptTypePresentationWidgetType'), graphql_name='addConceptTypePresentationWidgetType', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptTypePresentationWidgetTypeAddInput), graphql_name='form', default=None)),
))
    )
    add_document_type_presentation = sgqlc.types.Field(sgqlc.types.non_null('DocumentTypePresentation'), graphql_name='addDocumentTypePresentation', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(DocumentTypePresentationAddInput), graphql_name='form', default=None)),
))
    )
    set_concept_type_default_view = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='setConceptTypeDefaultView', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptTypePresentationViewInput), graphql_name='form', default=None)),
))
    )
    set_document_type_default_view = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='setDocumentTypeDefaultView', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(DocumentTypePresentationViewInput), graphql_name='form', default=None)),
))
    )
    add_concept_property_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyType'), graphql_name='addConceptPropertyType', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptPropertyTypeCreationInput), graphql_name='form', default=None)),
))
    )
    add_concept_link_property_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyType'), graphql_name='addConceptLinkPropertyType', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptLinkPropertyTypeCreationInput), graphql_name='form', default=None)),
))
    )
    add_concept_link_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptLinkType'), graphql_name='addConceptLinkType', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptLinkTypeCreationInput), graphql_name='form', default=None)),
))
    )
    add_concept_property_value_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyValueType'), graphql_name='addConceptPropertyValueType', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptPropertyValueTypeCreationInput), graphql_name='form', default=None)),
))
    )
    add_concept_type_view = sgqlc.types.Field(sgqlc.types.non_null('ConceptTypeView'), graphql_name='addConceptTypeView', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptTypeViewCreationInput), graphql_name='form', default=None)),
))
    )
    update_concept_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptType'), graphql_name='updateConceptType', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptTypeUpdateInput), graphql_name='form', default=None)),
        ('file', sgqlc.types.Arg(S3FileInput, graphql_name='file', default=None)),
        ('delete_image', sgqlc.types.Arg(Boolean, graphql_name='deleteImage', default=False)),
))
    )
    update_document_type = sgqlc.types.Field(sgqlc.types.non_null('DocumentType'), graphql_name='updateDocumentType', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(DocumentTypeUpdateInput), graphql_name='form', default=None)),
        ('file', sgqlc.types.Arg(S3FileInput, graphql_name='file', default=None)),
        ('delete_image', sgqlc.types.Arg(Boolean, graphql_name='deleteImage', default=False)),
))
    )
    update_concept_type_presentation = sgqlc.types.Field(sgqlc.types.non_null('ConceptTypePresentation'), graphql_name='updateConceptTypePresentation', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptTypePresentationUpdateInput), graphql_name='form', default=None)),
))
    )
    update_concept_type_presentation_template_filename = sgqlc.types.Field(sgqlc.types.non_null('ConceptTypePresentation'), graphql_name='updateConceptTypePresentationTemplateFilename', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptTypePresentationUpdateTemplateFilenameInput), graphql_name='form', default=None)),
))
    )
    update_concept_type_presentation_widget_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptTypePresentationWidgetType'), graphql_name='updateConceptTypePresentationWidgetType', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptTypePresentationWidgetTypeUpdateInput), graphql_name='form', default=None)),
))
    )
    update_concept_type_presentation_widget_types_order = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='updateConceptTypePresentationWidgetTypesOrder', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptTypePresentationWidgetTypeUpdateOrderInput), graphql_name='form', default=None)),
))
    )
    update_document_type_presentation = sgqlc.types.Field(sgqlc.types.non_null('DocumentTypePresentation'), graphql_name='updateDocumentTypePresentation', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(DocumentTypePresentationUpdateInput), graphql_name='form', default=None)),
))
    )
    update_concept_property_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyType'), graphql_name='updateConceptPropertyType', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptPropertyTypeUpdateInput), graphql_name='form', default=None)),
))
    )
    update_concept_main_property_type_order = sgqlc.types.Field(sgqlc.types.non_null('ConceptType'), graphql_name='updateConceptMainPropertyTypeOrder', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(InterestObjectMainPropertiesOrderUpdateInput), graphql_name='form', default=None)),
))
    )
    update_concept_link_property_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyType'), graphql_name='updateConceptLinkPropertyType', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptLinkPropertyTypeUpdateInput), graphql_name='form', default=None)),
))
    )
    update_concept_link_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptLinkType'), graphql_name='updateConceptLinkType', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptLinkTypeUpdateInput), graphql_name='form', default=None)),
))
    )
    update_concept_property_value_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyValueType'), graphql_name='updateConceptPropertyValueType', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptPropertyValueTypeUpdateInput), graphql_name='form', default=None)),
))
    )
    update_concept_type_view = sgqlc.types.Field(sgqlc.types.non_null('ConceptTypeView'), graphql_name='updateConceptTypeView', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptTypeViewUpdateInput), graphql_name='form', default=None)),
))
    )
    update_concept_type_view_show_in_menu = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='updateConceptTypeViewShowInMenu', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    delete_concept_type_avatar = sgqlc.types.Field(sgqlc.types.non_null('ConceptType'), graphql_name='deleteConceptTypeAvatar', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_concept_type = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteConceptType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_document_type = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteDocumentType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_concept_type_presentation = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteConceptTypePresentation', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_concept_type_presentation_widget_type = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteConceptTypePresentationWidgetType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_document_type_presentation = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteDocumentTypePresentation', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_concept_property_type = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteConceptPropertyType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_concept_link_property_type = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteConceptLinkPropertyType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_concept_link_type = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteConceptLinkType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_concept_property_value_type = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteConceptPropertyValueType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_concept_type_view = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteConceptTypeView', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_bulk = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('State')), graphql_name='deleteBulk', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    move_bulk = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptType'))), graphql_name='moveBulk', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Coordinate))), graphql_name='form', default=None)),
))
    )
    update_type_search_element = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='updateTypeSearchElement', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(TypeSearchElementUpdateInput), graphql_name='form', default=None)),
))
    )
    add_composite_property_value_template = sgqlc.types.Field(sgqlc.types.non_null('CompositePropertyValueTemplate'), graphql_name='addCompositePropertyValueTemplate', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(CompositePropertyValueTemplateCreateInput), graphql_name='form', default=None)),
))
    )
    update_composite_property_value_template = sgqlc.types.Field(sgqlc.types.non_null('CompositePropertyValueTemplate'), graphql_name='updateCompositePropertyValueTemplate', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(CompositePropertyValueTemplateCreateInput), graphql_name='form', default=None)),
))
    )
    delete_composite_property_value_template = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteCompositePropertyValueTemplate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    add_issue = sgqlc.types.Field(sgqlc.types.non_null('Issue'), graphql_name='addIssue', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(IssueCreationInput), graphql_name='form', default=None)),
))
    )
    delete_issue = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteIssue', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    add_concept_to_issue = sgqlc.types.Field(sgqlc.types.non_null('Issue'), graphql_name='addConceptToIssue', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(Concept2IssueInput), graphql_name='form', default=None)),
))
    )
    add_document_to_issue = sgqlc.types.Field(sgqlc.types.non_null('Issue'), graphql_name='addDocumentToIssue', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(Document2IssueInput), graphql_name='form', default=None)),
))
    )
    add_issue_to_issue = sgqlc.types.Field(sgqlc.types.non_null('Issue'), graphql_name='addIssueToIssue', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(Issue2TaskInput), graphql_name='form', default=None)),
))
    )
    delete_document_from_issue = sgqlc.types.Field(sgqlc.types.non_null('Issue'), graphql_name='deleteDocumentFromIssue', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(Document2IssueInput), graphql_name='form', default=None)),
))
    )
    delete_concept_from_issue = sgqlc.types.Field(sgqlc.types.non_null('Issue'), graphql_name='deleteConceptFromIssue', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(Concept2IssueInput), graphql_name='form', default=None)),
))
    )
    delete_issue_from_issue = sgqlc.types.Field(sgqlc.types.non_null('Issue'), graphql_name='deleteIssueFromIssue', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(Issue2TaskInput), graphql_name='form', default=None)),
))
    )
    update_issue = sgqlc.types.Field(sgqlc.types.non_null('Issue'), graphql_name='updateIssue', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(IssueEditFieldsInput), graphql_name='form', default=None)),
))
    )
    update_issue_massive = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='updateIssueMassive', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(MassUpdateIssueInput), graphql_name='form', default=None)),
))
    )
    add_comment_to_issue = sgqlc.types.Field(sgqlc.types.non_null('IssueChange'), graphql_name='addCommentToIssue', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(Comment2IssueInput), graphql_name='form', default=None)),
))
    )
    update_issue_comment = sgqlc.types.Field(sgqlc.types.non_null('IssueChange'), graphql_name='updateIssueComment', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(UpdateCommentInput), graphql_name='form', default=None)),
))
    )
    delete_issue_comment = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteIssueComment', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    update_document = sgqlc.types.Field(sgqlc.types.non_null('Document'), graphql_name='updateDocument', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(DocumentUpdateInput), graphql_name='form', default=None)),
))
    )
    update_document_avatar = sgqlc.types.Field(sgqlc.types.non_null('Document'), graphql_name='updateDocumentAvatar', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(DocumentAvatarUpdateInput), graphql_name='form', default=None)),
))
    )
    remove_candidate_fact_from_document = sgqlc.types.Field(sgqlc.types.non_null('Document'), graphql_name='removeCandidateFactFromDocument', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(DocumentDeleteCandidateFactInput), graphql_name='form', default=None)),
))
    )
    remove_all_candidate_facts_from_document = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='removeAllCandidateFactsFromDocument', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    update_document_facts = sgqlc.types.Field(sgqlc.types.non_null('StateWithErrors'), graphql_name='updateDocumentFacts', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(BatchUpdateFactInput), graphql_name='form', default=None)),
))
    )
    remove_all_kbfacts_from_document = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='removeAllKBFactsFromDocument', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(DocumentAllKBFactsRemoveInput), graphql_name='form', default=None)),
))
    )
    delete_documents = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteDocuments', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
        ('performance_control', sgqlc.types.Arg(PerformSynchronously, graphql_name='performanceControl', default={'performSynchronously': False})),
))
    )
    update_document_node = sgqlc.types.Field(sgqlc.types.non_null('Document'), graphql_name='updateDocumentNode', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(DocumentNodeUpdateInput), graphql_name='form', default=None)),
))
    )
    update_document_subscriptions = sgqlc.types.Field(sgqlc.types.non_null('Document'), graphql_name='updateDocumentSubscriptions', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('events', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DocumentUpdate))), graphql_name='events', default=None)),
))
    )
    mark_document_as_read = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='markDocumentAsRead', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    mark_document_as_unread = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='markDocumentAsUnread', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    add_document_duplicate_report = sgqlc.types.Field(sgqlc.types.non_null('DocumentDuplicateReport'), graphql_name='addDocumentDuplicateReport', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DocumentDuplicateReportInput), graphql_name='input', default=None)),
))
    )
    delete_document_duplicate_report = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteDocumentDuplicateReport', args=sgqlc.types.ArgDict((
        ('report_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='reportId', default=None)),
))
    )
    decline_document_duplicate_task = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='declineDocumentDuplicateTask', args=sgqlc.types.ArgDict((
        ('report_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='reportId', default=None)),
        ('task_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='taskIds', default=None)),
))
    )
    delete_document_duplicate_task = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteDocumentDuplicateTask', args=sgqlc.types.ArgDict((
        ('report_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='reportId', default=None)),
        ('task_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='taskIds', default=None)),
))
    )
    delete_all_document_duplicate_task = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteAllDocumentDuplicateTask', args=sgqlc.types.ArgDict((
        ('report_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='reportId', default=None)),
))
    )
    delete_research_map = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteResearchMap', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    bulk_delete_research_map = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='bulkDeleteResearchMap', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    add_research_map = sgqlc.types.Field(sgqlc.types.non_null('ResearchMap'), graphql_name='addResearchMap', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ResearchMapCreationInput), graphql_name='form', default=None)),
))
    )
    add_research_map_from_files = sgqlc.types.Field(sgqlc.types.non_null('ResearchMapFromFilesType'), graphql_name='addResearchMapFromFiles', args=sgqlc.types.ArgDict((
        ('files', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(S3FileInput)), graphql_name='files', default=None)),
))
    )
    update_research_map = sgqlc.types.Field(sgqlc.types.non_null('ResearchMap'), graphql_name='updateResearchMap', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ResearchMapUpdateInput), graphql_name='form', default=None)),
))
    )
    add_content_on_research_map = sgqlc.types.Field(sgqlc.types.non_null('ResearchMap'), graphql_name='addContentOnResearchMap', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ResearchMapContentAddInput), graphql_name='form', default=None)),
))
    )
    delete_content_from_research_map = sgqlc.types.Field(sgqlc.types.non_null('ResearchMap'), graphql_name='deleteContentFromResearchMap', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ResearchMapContentUpdateInput), graphql_name='form', default=None)),
))
    )
    batch_move_nodes_on_map = sgqlc.types.Field(sgqlc.types.non_null('ResearchMap'), graphql_name='batchMoveNodesOnMap', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ResearchMapBatchMoveInput), graphql_name='form', default=None)),
))
    )
    batch_update_group_on_map = sgqlc.types.Field(sgqlc.types.non_null('ResearchMap'), graphql_name='batchUpdateGroupOnMap', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ResearchMapBatchUpdateGroupInput), graphql_name='form', default=None)),
))
    )
    update_node_annotation = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='updateNodeAnnotation', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(UpdateNodeAnnotationInput), graphql_name='form', default=None)),
))
    )
    update_edge_annotation = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='updateEdgeAnnotation', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEdgeAnnotationInput), graphql_name='form', default=None)),
))
    )
    add_top_neighbors_on_map = sgqlc.types.Field(sgqlc.types.non_null('ResearchMap'), graphql_name='addTopNeighborsOnMap', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('quantity', sgqlc.types.Arg(Int, graphql_name='quantity', default=10)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ResearchMapContentSelectInput), graphql_name='form', default=None)),
))
    )
    add_concept_fact_neighbors_on_map = sgqlc.types.Field(sgqlc.types.non_null('ResearchMap'), graphql_name='addConceptFactNeighborsOnMap', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('concept_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='conceptId', default=None)),
))
    )
    add_not_approved_neighbors_on_map = sgqlc.types.Field(sgqlc.types.non_null('StateWithCount'), graphql_name='addNotApprovedNeighborsOnMap', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('concept_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='conceptIds', default=None)),
))
    )
    set_research_map_active = sgqlc.types.Field(sgqlc.types.non_null('ResearchMap'), graphql_name='setResearchMapActive', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    find_shortest_path_on_map = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='findShortestPathOnMap', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('concept_node_ids', sgqlc.types.Arg(sgqlc.types.non_null(ConceptAddImplicitLinkInput), graphql_name='conceptNodeIds', default=None)),
))
    )
    find_shortest_implicit_path_on_map = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='findShortestImplicitPathOnMap', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('concept_node_ids', sgqlc.types.Arg(sgqlc.types.non_null(ConceptAddImplicitLinkInput), graphql_name='conceptNodeIds', default=None)),
))
    )
    add_group = sgqlc.types.Field(sgqlc.types.non_null(Group), graphql_name='addGroup', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(GroupCreationInput), graphql_name='form', default=None)),
))
    )
    update_group = sgqlc.types.Field(sgqlc.types.non_null(Group), graphql_name='updateGroup', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(GroupUpdateInput), graphql_name='form', default=None)),
))
    )
    delete_group = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteGroup', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    add_drawing = sgqlc.types.Field(sgqlc.types.non_null(MapDrawing), graphql_name='addDrawing', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(MapDrawingAddInput), graphql_name='form', default=None)),
))
    )
    update_drawing = sgqlc.types.Field(sgqlc.types.non_null(MapDrawing), graphql_name='updateDrawing', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(MapDrawingUpdateInput), graphql_name='form', default=None)),
))
    )
    delete_drawing = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteDrawing', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    create_redmine_issue = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='createRedmineIssue', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(RedmineIssueCreationInput), graphql_name='form', default=None)),
))
    )
    update_redmine_issue = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='updateRedmineIssue', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(RedmineIssueUpdateInput), graphql_name='form', default=None)),
))
    )
    unlink_issues = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='unlinkIssues', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(RedmineIssueUnlinkInput), graphql_name='form', default=None)),
))
    )
    add_access_level = sgqlc.types.Field(sgqlc.types.non_null(AccessLevel), graphql_name='addAccessLevel', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(AccessLevelCreationInput), graphql_name='form', default=None)),
))
    )
    update_access_level = sgqlc.types.Field(sgqlc.types.non_null(AccessLevel), graphql_name='updateAccessLevel', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(AccessLevelUpdateInput), graphql_name='form', default=None)),
))
    )
    delete_access_level = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteAccessLevel', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    add_template_docx = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='addTemplateDocx', args=sgqlc.types.ArgDict((
        ('file', sgqlc.types.Arg(S3FileInput, graphql_name='file', default=None)),
))
    )
    update_markers_bulk = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='updateMarkersBulk', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(BulkMarkersUpdateInput), graphql_name='form', default=None)),
))
    )
    update_document_bulk = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='updateDocumentBulk', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(BulkDocumentUpdateInput), graphql_name='form', default=None)),
))
    )
    add_platform = sgqlc.types.Field(sgqlc.types.non_null('Platform'), graphql_name='addPlatform', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(PlatformCreationInput), graphql_name='form', default=None)),
        ('file', sgqlc.types.Arg(S3FileInput, graphql_name='file', default=None)),
))
    )
    update_platform = sgqlc.types.Field(sgqlc.types.non_null('Platform'), graphql_name='updatePlatform', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(PlatformUpdateInput), graphql_name='form', default=None)),
        ('file', sgqlc.types.Arg(S3FileInput, graphql_name='file', default=None)),
        ('delete_image', sgqlc.types.Arg(Boolean, graphql_name='deleteImage', default=False)),
))
    )
    delete_platform = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deletePlatform', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    add_account = sgqlc.types.Field(sgqlc.types.non_null('Account'), graphql_name='addAccount', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(AccountCreationInput), graphql_name='form', default=None)),
        ('file', sgqlc.types.Arg(S3FileInput, graphql_name='file', default=None)),
))
    )
    update_account = sgqlc.types.Field(sgqlc.types.non_null('Account'), graphql_name='updateAccount', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(AccountUpdateInput), graphql_name='form', default=None)),
        ('file', sgqlc.types.Arg(S3FileInput, graphql_name='file', default=None)),
        ('delete_image', sgqlc.types.Arg(Boolean, graphql_name='deleteImage', default=False)),
))
    )
    delete_account = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteAccount', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    add_document_feed = sgqlc.types.Field(sgqlc.types.non_null('DocumentFeed'), graphql_name='addDocumentFeed', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(DocumentFeedCreationInput), graphql_name='form', default=None)),
))
    )
    update_document_feed = sgqlc.types.Field(sgqlc.types.non_null('DocumentFeed'), graphql_name='updateDocumentFeed', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(DocumentFeedUpdateInput), graphql_name='form', default=None)),
))
    )
    add_document_to_document_feed_favorites = sgqlc.types.Field(sgqlc.types.non_null('DocumentFeed'), graphql_name='addDocumentToDocumentFeedFavorites', args=sgqlc.types.ArgDict((
        ('document_feed_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='documentFeedId', default=None)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(DocumentFeedUpdateDocumentsInput), graphql_name='form', default=None)),
))
    )
    delete_document_from_document_feed_favorites = sgqlc.types.Field(sgqlc.types.non_null('DocumentFeed'), graphql_name='deleteDocumentFromDocumentFeedFavorites', args=sgqlc.types.ArgDict((
        ('document_feed_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='documentFeedId', default=None)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(DocumentFeedUpdateDocumentsInput), graphql_name='form', default=None)),
))
    )
    delete_document_from_document_feed = sgqlc.types.Field(sgqlc.types.non_null('DocumentFeed'), graphql_name='deleteDocumentFromDocumentFeed', args=sgqlc.types.ArgDict((
        ('document_feed_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='documentFeedId', default=None)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(DocumentFeedUpdateDocumentsInput), graphql_name='form', default=None)),
))
    )
    restore_document_to_document_feed = sgqlc.types.Field(sgqlc.types.non_null('DocumentFeed'), graphql_name='restoreDocumentToDocumentFeed', args=sgqlc.types.ArgDict((
        ('document_feed_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='documentFeedId', default=None)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(DocumentFeedUpdateDocumentsInput), graphql_name='form', default=None)),
))
    )
    delete_document_feed = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteDocumentFeed', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    update_document_facets = sgqlc.types.Field(sgqlc.types.non_null(DocumentFacets), graphql_name='updateDocumentFacets', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    update_concept_registry_view = sgqlc.types.Field(sgqlc.types.non_null(ConceptRegistryView), graphql_name='updateConceptRegistryView', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ConceptRegistryViewInput), graphql_name='form', default=None)),
))
    )
    update_document_registry_view = sgqlc.types.Field(sgqlc.types.non_null(DocumentRegistryView), graphql_name='updateDocumentRegistryView', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(DocumentRegistryViewInput), graphql_name='form', default=None)),
))
    )
    update_document_card_view = sgqlc.types.Field(sgqlc.types.non_null(DocumentCardView), graphql_name='updateDocumentCardView', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(DocumentCardViewInput), graphql_name='form', default=None)),
))
    )
    add_chart = sgqlc.types.Field(sgqlc.types.non_null(Chart), graphql_name='addChart', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ChartDescriptionInput), graphql_name='form', default=None)),
))
    )
    update_chart = sgqlc.types.Field(sgqlc.types.non_null(Chart), graphql_name='updateChart', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ChartDescriptionInput), graphql_name='form', default=None)),
))
    )
    delete_chart = sgqlc.types.Field(sgqlc.types.non_null('State'), graphql_name='deleteChart', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    translate_tql = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='translateTQL', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='query', default=None)),
        ('source_language', sgqlc.types.Arg(String, graphql_name='sourceLanguage', default=None)),
        ('target_language', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='targetLanguage', default=None)),
))
    )
    create_ok_sync_package = sgqlc.types.Field('OkZkSync', graphql_name='createOkSyncPackage', args=sgqlc.types.ArgDict((
        ('timestamp_interval', sgqlc.types.Arg(sgqlc.types.non_null(TimestampInterval), graphql_name='timestampInterval', default=None)),
))
    )


class NERCRegexp(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('regexp', 'context_regexp', 'auto_create')
    regexp = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='regexp')
    context_regexp = sgqlc.types.Field(String, graphql_name='contextRegexp')
    auto_create = sgqlc.types.Field(Boolean, graphql_name='autoCreate')


class NamedValue(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('id', 'property_value_type', 'value')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    property_value_type = sgqlc.types.Field(sgqlc.types.non_null(CompositePropertyValueType), graphql_name='propertyValueType')
    value = sgqlc.types.Field(sgqlc.types.non_null('Value'), graphql_name='value')


class OkZkSync(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('id', 's3_file', 's3_file_id', 'sync_mode', 'sync_date')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    s3_file = sgqlc.types.Field(sgqlc.types.non_null('S3File'), graphql_name='s3File')
    s3_file_id = sgqlc.types.Field(ID, graphql_name='s3FileId')
    sync_mode = sgqlc.types.Field(sgqlc.types.non_null(SyncMode), graphql_name='syncMode')
    sync_date = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='syncDate')


class OutputLimiter(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('maximum_points', 'minimum_number')
    maximum_points = sgqlc.types.Field(Long, graphql_name='maximumPoints')
    minimum_number = sgqlc.types.Field(Long, graphql_name='minimumNumber')


class ParagraphMetadata(sgqlc.types.Type):
    __schema__ = api_schema
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
    __schema__ = api_schema
    __field_names__ = ('key', 'value')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class PdfSpecificMetadataGQL(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('author', 'creation_date')
    author = sgqlc.types.Field(String, graphql_name='author')
    creation_date = sgqlc.types.Field(UnixTime, graphql_name='creationDate')


class PlatformFacet(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('value', 'count')
    value = sgqlc.types.Field(sgqlc.types.non_null('Platform'), graphql_name='value')
    count = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='count')


class PlatformPagination(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('list_platform', 'total')
    list_platform = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Platform'))), graphql_name='listPlatform')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class PlatformStatistics(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('count_account', 'count_doc')
    count_account = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countAccount')
    count_doc = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countDoc')


class PotentialDocumentFactUpdates(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('concept_facts_to_update_count', 'concept_property_facts_to_update_count', 'concept_link_facts_to_update_count', 'link_property_facts_to_update_count', 'concept_facts_to_reject_count', 'concept_property_facts_to_reject_count', 'concept_link_facts_to_reject_count', 'link_property_facts_to_reject_count')
    concept_facts_to_update_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='conceptFactsToUpdateCount')
    concept_property_facts_to_update_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='conceptPropertyFactsToUpdateCount')
    concept_link_facts_to_update_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='conceptLinkFactsToUpdateCount')
    link_property_facts_to_update_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkPropertyFactsToUpdateCount')
    concept_facts_to_reject_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='conceptFactsToRejectCount')
    concept_property_facts_to_reject_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='conceptPropertyFactsToRejectCount')
    concept_link_facts_to_reject_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='conceptLinkFactsToRejectCount')
    link_property_facts_to_reject_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='linkPropertyFactsToRejectCount')


class Query(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('document', 'story', 'pagination_story', 'pagination_document_markers', 'pagination_kbrelated_document', 'check_potential_document_fact_updates', 'document_duplicate_report', 'pagination_document_duplicate_report', 'document_duplicate_task', 'pagination_document_duplicate_task', 'concept_type', 'document_type', 'entity_type', 'concept_type_presentation', 'pagination_concept_type_presentation', 'document_type_presentation', 'pagination_document_type_presentation', 'concept_property_type', 'concept_link_type', 'concept_property_value_type', 'list_concept_type', 'list_document_type', 'list_user_menu_type', 'list_concept_property_type', 'list_concept_property_type_by_id', 'list_concept_link_type', 'list_concept_property_value_type', 'pagination_concept_type', 'pagination_document_type', 'pagination_concept_property_type', 'pagination_concept_link_property_type', 'pagination_concept_link_type', 'pagination_concept_property_value_type', 'composite_concept_property_type', 'composite_link_property_type', 'list_composite_concept_property_type', 'list_composite_link_property_type', 'pagination_composite_concept_property_type', 'pagination_composite_link_property_type', 'composite_property_value_template', 'list_composite_property_value_template', 'pagination_composite_property_value_template', 'concept_type_view', 'domain_map', 'concept', 'list_concept_by_id', 'pagination_concept', 'concept_presentation', 'pagination_concept_presentation', 'list_concept_link_between_fixed_concepts', 'concept_property', 'concept_link', 'pagination_concept_link', 'issue', 'pagination_issue', 'pagination_issue_change', 'research_map', 'pagination_research_map', 'active_research_map', 'list_top_neighbors_on_map', 'list_last_research_map', 'document_autocomplete', 'concept_autocomplete', 'get_osm_place_name', 'get_osm_coordinates', 'get_redmine_issue_creation_default_parameters', 'get_redmine_issue_update_default_description', 'search_similar_redmine_issues', 'access_level', 'pagination_access_level', 'story_fs2_query', 'concept_fs2_query', 'markers_bulk', 'platform', 'list_platform_by_id', 'pagination_platform', 'account', 'list_account_by_id', 'pagination_account', 'pagination_country', 'pagination_language', 'document_feed', 'pagination_document_feed', 'document_facets', 'concept_registry_view', 'document_registry_view', 'document_card_view', 'chart', 'preview_chart', 'zklast_sync')
    document = sgqlc.types.Field('Document', graphql_name='document', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    story = sgqlc.types.Field('Story', graphql_name='story', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    pagination_story = sgqlc.types.Field(sgqlc.types.non_null('StoryPagination'), graphql_name='paginationStory', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('grouping', sgqlc.types.Arg(DocumentGrouping, graphql_name='grouping', default='none')),
        ('filter_settings', sgqlc.types.Arg(DocumentFilterSettings, graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(DocumentSorting, graphql_name='sortField', default='score')),
        ('extra_settings', sgqlc.types.Arg(sgqlc.types.non_null(ExtraSettings), graphql_name='extraSettings', default=None)),
        ('relevance', sgqlc.types.Arg(DocumentRelevanceMetricsInput, graphql_name='relevance', default=None)),
))
    )
    pagination_document_markers = sgqlc.types.Field(sgqlc.types.non_null(CommonStringPagination), graphql_name='paginationDocumentMarkers', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
))
    )
    pagination_kbrelated_document = sgqlc.types.Field(DocumentPagination, graphql_name='paginationKBRelatedDocument', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(RelatedDocumentFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(RelatedDocumentSorting, graphql_name='sortField', default='registrationDate')),
))
    )
    check_potential_document_fact_updates = sgqlc.types.Field(sgqlc.types.non_null(PotentialDocumentFactUpdates), graphql_name='checkPotentialDocumentFactUpdates', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(BatchUpdateFactInput), graphql_name='form', default=None)),
))
    )
    document_duplicate_report = sgqlc.types.Field(sgqlc.types.non_null('DocumentDuplicateReport'), graphql_name='documentDuplicateReport', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    pagination_document_duplicate_report = sgqlc.types.Field(sgqlc.types.non_null(DocumentDuplicateReportPagination), graphql_name='paginationDocumentDuplicateReport', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(DocumentDuplicateReportFilterSettings), graphql_name='filterSettings', default=None)),
))
    )
    document_duplicate_task = sgqlc.types.Field(sgqlc.types.non_null(DocumentDuplicateTask), graphql_name='documentDuplicateTask', args=sgqlc.types.ArgDict((
        ('report_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='reportId', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    pagination_document_duplicate_task = sgqlc.types.Field(sgqlc.types.non_null(DocumentDuplicateTaskPagination), graphql_name='paginationDocumentDuplicateTask', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(DocumentDuplicateTaskFilterSettings), graphql_name='filterSettings', default=None)),
))
    )
    concept_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptType'), graphql_name='conceptType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    document_type = sgqlc.types.Field(sgqlc.types.non_null('DocumentType'), graphql_name='documentType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    entity_type = sgqlc.types.Field(sgqlc.types.non_null(EntityType), graphql_name='entityType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    concept_type_presentation = sgqlc.types.Field(sgqlc.types.non_null('ConceptTypePresentation'), graphql_name='conceptTypePresentation', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    pagination_concept_type_presentation = sgqlc.types.Field(sgqlc.types.non_null(ConceptTypePresentationPagination), graphql_name='paginationConceptTypePresentation', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptTypePresentationFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(ConceptTypePresentationSorting, graphql_name='sortField', default='id')),
))
    )
    document_type_presentation = sgqlc.types.Field(sgqlc.types.non_null('DocumentTypePresentation'), graphql_name='documentTypePresentation', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    pagination_document_type_presentation = sgqlc.types.Field(sgqlc.types.non_null(DocumentTypePresentationPagination), graphql_name='paginationDocumentTypePresentation', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(DocumentTypePresentationFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(DocumentTypePresentationSorting, graphql_name='sortField', default='id')),
))
    )
    concept_property_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyType'), graphql_name='conceptPropertyType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    concept_link_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptLinkType'), graphql_name='conceptLinkType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    concept_property_value_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyValueType'), graphql_name='conceptPropertyValueType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    list_concept_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptType'))), graphql_name='listConceptType')
    list_document_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DocumentType'))), graphql_name='listDocumentType')
    list_user_menu_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserMenuType'))), graphql_name='listUserMenuType')
    list_concept_property_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptPropertyType'))), graphql_name='listConceptPropertyType')
    list_concept_property_type_by_id = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ConceptPropertyType')), graphql_name='listConceptPropertyTypeById', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    list_concept_link_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptLinkType'))), graphql_name='listConceptLinkType')
    list_concept_property_value_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptPropertyValueType'))), graphql_name='listConceptPropertyValueType')
    pagination_concept_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptTypePagination), graphql_name='paginationConceptType', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptTypeFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(ConceptTypeSorting, graphql_name='sortField', default='id')),
))
    )
    pagination_document_type = sgqlc.types.Field(sgqlc.types.non_null(DocumentTypePagination), graphql_name='paginationDocumentType', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(DocumentTypeFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(DocumentTypeSorting, graphql_name='sortField', default='id')),
))
    )
    pagination_concept_property_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptPropertyTypePagination), graphql_name='paginationConceptPropertyType', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptPropertyTypeFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(ConceptPropertyTypeSorting, graphql_name='sortField', default='name')),
))
    )
    pagination_concept_link_property_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptPropertyTypePagination), graphql_name='paginationConceptLinkPropertyType', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptPropertyTypeFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(ConceptPropertyTypeSorting, graphql_name='sortField', default='name')),
))
    )
    pagination_concept_link_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptLinkTypePagination), graphql_name='paginationConceptLinkType', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptLinkTypeFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(ConceptLinkTypeSorting, graphql_name='sortField', default='id')),
))
    )
    pagination_concept_property_value_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptPropertyValueTypePagination), graphql_name='paginationConceptPropertyValueType', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptPropertyValueTypeFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(ConceptPropertyValueTypeSorting, graphql_name='sortField', default='id')),
))
    )
    composite_concept_property_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyType'), graphql_name='compositeConceptPropertyType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    composite_link_property_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyType'), graphql_name='compositeLinkPropertyType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    list_composite_concept_property_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptPropertyType'))), graphql_name='listCompositeConceptPropertyType')
    list_composite_link_property_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptPropertyType'))), graphql_name='listCompositeLinkPropertyType')
    pagination_composite_concept_property_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptPropertyTypePagination), graphql_name='paginationCompositeConceptPropertyType', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(CompositePropertyTypeFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(CompositePropertyTypeSorting, graphql_name='sortField', default='name')),
))
    )
    pagination_composite_link_property_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptPropertyTypePagination), graphql_name='paginationCompositeLinkPropertyType', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(CompositePropertyTypeFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(CompositePropertyTypeSorting, graphql_name='sortField', default='name')),
))
    )
    composite_property_value_template = sgqlc.types.Field(sgqlc.types.non_null('CompositePropertyValueTemplate'), graphql_name='compositePropertyValueTemplate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    list_composite_property_value_template = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CompositePropertyValueTemplate'))), graphql_name='listCompositePropertyValueTemplate')
    pagination_composite_property_value_template = sgqlc.types.Field(sgqlc.types.non_null(CompositePropertyValueTemplatePagination), graphql_name='paginationCompositePropertyValueTemplate', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(CompositePropertyValueTemplateFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(CompositePropertyValueTemplateSorting, graphql_name='sortField', default='id')),
))
    )
    concept_type_view = sgqlc.types.Field(sgqlc.types.non_null('ConceptTypeView'), graphql_name='conceptTypeView', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    domain_map = sgqlc.types.Field(sgqlc.types.non_null(DomainMap), graphql_name='domainMap')
    concept = sgqlc.types.Field('Concept', graphql_name='concept', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    list_concept_by_id = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Concept')), graphql_name='listConceptById', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    pagination_concept = sgqlc.types.Field(ConceptPagination, graphql_name='paginationConcept', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(ConceptFilterSettings, graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(ConceptSorting, graphql_name='sortField', default='score')),
))
    )
    concept_presentation = sgqlc.types.Field(sgqlc.types.non_null(ConceptPresentation), graphql_name='conceptPresentation', args=sgqlc.types.ArgDict((
        ('concept_type_presentation_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='conceptTypePresentationId', default=None)),
        ('root_concept_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='rootConceptId', default=None)),
))
    )
    pagination_concept_presentation = sgqlc.types.Field(sgqlc.types.non_null(ConceptPresentationPagination), graphql_name='paginationConceptPresentation', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(ConceptPresentationFilterSettings, graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(ConceptSorting, graphql_name='sortField', default='score')),
))
    )
    list_concept_link_between_fixed_concepts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ConceptLink'))), graphql_name='listConceptLinkBetweenFixedConcepts', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptLinkFilterSettings), graphql_name='filterSettings', default=None)),
))
    )
    concept_property = sgqlc.types.Field('ConceptProperty', graphql_name='conceptProperty', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    concept_link = sgqlc.types.Field(sgqlc.types.non_null('ConceptLink'), graphql_name='conceptLink', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    pagination_concept_link = sgqlc.types.Field(sgqlc.types.non_null(ConceptLinkPagination), graphql_name='paginationConceptLink', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptLinkFilterSettings), graphql_name='filterSettings', default=None)),
))
    )
    issue = sgqlc.types.Field('Issue', graphql_name='issue', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    pagination_issue = sgqlc.types.Field(IssuePagination, graphql_name='paginationIssue', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(IssueFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(IssueSorting, graphql_name='sortField', default='id')),
))
    )
    pagination_issue_change = sgqlc.types.Field(sgqlc.types.non_null(IssueChangePagination), graphql_name='paginationIssueChange', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
))
    )
    research_map = sgqlc.types.Field(sgqlc.types.non_null('ResearchMap'), graphql_name='researchMap', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    pagination_research_map = sgqlc.types.Field(sgqlc.types.non_null('ResearchMapPagination'), graphql_name='paginationResearchMap', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ResearchMapFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(ResearchMapSorting, graphql_name='sortField', default='id')),
))
    )
    active_research_map = sgqlc.types.Field('ResearchMap', graphql_name='activeResearchMap')
    list_top_neighbors_on_map = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptWithNeighbors))), graphql_name='listTopNeighborsOnMap', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ResearchMapContentSelectInput), graphql_name='form', default=None)),
        ('quantity', sgqlc.types.Arg(Int, graphql_name='quantity', default=10)),
))
    )
    list_last_research_map = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ResearchMap'))), graphql_name='listLastResearchMap')
    document_autocomplete = sgqlc.types.Field(sgqlc.types.non_null(Autocomplete), graphql_name='documentAutocomplete', args=sgqlc.types.ArgDict((
        ('destination', sgqlc.types.Arg(sgqlc.types.non_null(AutocompleteDocumentDestination), graphql_name='destination', default=None)),
        ('query', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='query', default=None)),
))
    )
    concept_autocomplete = sgqlc.types.Field(sgqlc.types.non_null(Autocomplete), graphql_name='conceptAutocomplete', args=sgqlc.types.ArgDict((
        ('destination', sgqlc.types.Arg(sgqlc.types.non_null(AutocompleteConceptDestination), graphql_name='destination', default=None)),
        ('query', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='query', default=None)),
))
    )
    get_osm_place_name = sgqlc.types.Field(sgqlc.types.non_null(GeoPointValue), graphql_name='getOsmPlaceName', args=sgqlc.types.ArgDict((
        ('latitude', sgqlc.types.Arg(sgqlc.types.non_null(Float), graphql_name='latitude', default=None)),
        ('longitude', sgqlc.types.Arg(sgqlc.types.non_null(Float), graphql_name='longitude', default=None)),
))
    )
    get_osm_coordinates = sgqlc.types.Field(sgqlc.types.non_null(GeoPointValue), graphql_name='getOsmCoordinates', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    get_redmine_issue_creation_default_parameters = sgqlc.types.Field(sgqlc.types.non_null('RedmineIssueCreationDefaultParameters'), graphql_name='getRedmineIssueCreationDefaultParameters', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(RedmineIssueDefaultParametersInput), graphql_name='form', default=None)),
))
    )
    get_redmine_issue_update_default_description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='getRedmineIssueUpdateDefaultDescription', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(RedmineIssueDefaultParametersInput), graphql_name='form', default=None)),
))
    )
    search_similar_redmine_issues = sgqlc.types.Field(sgqlc.types.non_null('RedmineIssuePagination'), graphql_name='searchSimilarRedmineIssues', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    access_level = sgqlc.types.Field(sgqlc.types.non_null(AccessLevel), graphql_name='accessLevel', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    pagination_access_level = sgqlc.types.Field(sgqlc.types.non_null(AccessLevelPagination), graphql_name='paginationAccessLevel', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(AccessLevelSorting, graphql_name='sortField', default='id')),
))
    )
    story_fs2_query = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='storyFs2Query', args=sgqlc.types.ArgDict((
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(DocumentFilterSettings), graphql_name='filterSettings', default=None)),
))
    )
    concept_fs2_query = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='conceptFs2Query', args=sgqlc.types.ArgDict((
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(ConceptFilterSettings), graphql_name='filterSettings', default=None)),
))
    )
    markers_bulk = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(Markers)), graphql_name='markersBulk', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(BulkMarkersInput), graphql_name='form', default=None)),
))
    )
    platform = sgqlc.types.Field(sgqlc.types.non_null('Platform'), graphql_name='platform', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    list_platform_by_id = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Platform'))), graphql_name='listPlatformById', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    pagination_platform = sgqlc.types.Field(sgqlc.types.non_null(PlatformPagination), graphql_name='paginationPlatform', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(PlatformFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(PlatformSorting, graphql_name='sortField', default='id')),
))
    )
    account = sgqlc.types.Field(sgqlc.types.non_null('Account'), graphql_name='account', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    list_account_by_id = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Account'))), graphql_name='listAccountById', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    pagination_account = sgqlc.types.Field(sgqlc.types.non_null(AccountPagination), graphql_name='paginationAccount', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(AccountFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(AccountSorting, graphql_name='sortField', default='id')),
))
    )
    pagination_country = sgqlc.types.Field(sgqlc.types.non_null(CountryPagination), graphql_name='paginationCountry', args=sgqlc.types.ArgDict((
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(CountryFilterSettings), graphql_name='filterSettings', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
))
    )
    pagination_language = sgqlc.types.Field(sgqlc.types.non_null(LanguagePagination), graphql_name='paginationLanguage', args=sgqlc.types.ArgDict((
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(LanguageFilterSettings), graphql_name='filterSettings', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
))
    )
    document_feed = sgqlc.types.Field(sgqlc.types.non_null('DocumentFeed'), graphql_name='documentFeed', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    pagination_document_feed = sgqlc.types.Field(sgqlc.types.non_null(DocumentFeedPagination), graphql_name='paginationDocumentFeed', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(DocumentFeedFilterSettings), graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(DocumentFeedSorting, graphql_name='sortField', default='id')),
))
    )
    document_facets = sgqlc.types.Field(sgqlc.types.non_null(DocumentFacets), graphql_name='documentFacets', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    concept_registry_view = sgqlc.types.Field(sgqlc.types.non_null(ConceptRegistryView), graphql_name='conceptRegistryView')
    document_registry_view = sgqlc.types.Field(sgqlc.types.non_null(DocumentRegistryView), graphql_name='documentRegistryView')
    document_card_view = sgqlc.types.Field(sgqlc.types.non_null(DocumentCardView), graphql_name='documentCardView')
    chart = sgqlc.types.Field(sgqlc.types.non_null(Chart), graphql_name='chart', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    preview_chart = sgqlc.types.Field(sgqlc.types.non_null(Chart), graphql_name='previewChart', args=sgqlc.types.ArgDict((
        ('form', sgqlc.types.Arg(sgqlc.types.non_null(ChartDescriptionInput), graphql_name='form', default=None)),
))
    )
    zklast_sync = sgqlc.types.Field(OkZkSync, graphql_name='ZKLastSync')


class RedmineIssue(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('id', 'subject', 'tracker', 'status', 'priority', 'author', 'assignee', 'creation_date')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    subject = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='subject')
    tracker = sgqlc.types.Field(sgqlc.types.non_null('RedmineTracker'), graphql_name='tracker')
    status = sgqlc.types.Field(sgqlc.types.non_null('RedmineStatus'), graphql_name='status')
    priority = sgqlc.types.Field(sgqlc.types.non_null('RedminePriority'), graphql_name='priority')
    author = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='author')
    assignee = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='assignee')
    creation_date = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='creationDate')


class RedmineIssueCreationDefaultParameters(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('subject', 'description', 'users', 'trackers', 'statuses', 'priorities')
    subject = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='subject')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    users = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('RedmineUser'))), graphql_name='users')
    trackers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('RedmineTracker'))), graphql_name='trackers')
    statuses = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('RedmineStatus'))), graphql_name='statuses')
    priorities = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('RedminePriority'))), graphql_name='priorities')


class RedmineIssuePagination(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('list_redmine_issue', 'total')
    list_redmine_issue = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(RedmineIssue))), graphql_name='listRedmineIssue')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class RedminePriority(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class RedmineStatus(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class RedmineTracker(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class RedmineUser(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('id', 'full_name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    full_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fullName')


class RelExtModel(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('source_annotation_type', 'target_annotation_type', 'relation_type', 'invert_direction')
    source_annotation_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sourceAnnotationType')
    target_annotation_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='targetAnnotationType')
    relation_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='relationType')
    invert_direction = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='invertDirection')


class ResearchMapFromFilesType(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('research_maps', 'info')
    research_maps = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ResearchMap'))), graphql_name='researchMaps')
    info = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('State')), graphql_name='info')


class ResearchMapPagination(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('total', 'list_research_map')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')
    list_research_map = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ResearchMap'))), graphql_name='listResearchMap')


class ResearchMapStatistics(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('object_num', 'event_num', 'document_num', 'concept_num', 'concept_and_document_num')
    object_num = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='objectNum')
    event_num = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='eventNum')
    document_num = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='documentNum')
    concept_num = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='conceptNum')
    concept_and_document_num = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='conceptAndDocumentNum')


class S3File(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('bucket_name', 'object_name')
    bucket_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bucketName')
    object_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='objectName')


class Score(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('name', 'score')
    name = sgqlc.types.Field(sgqlc.types.non_null(Name), graphql_name='name')
    score = sgqlc.types.Field(Float, graphql_name='score')


class ShortestPath(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('path',)
    path = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ShortestPathEdge'))), graphql_name='path')


class ShortestPathEdge(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('node_id', 'link_id')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    link_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='linkId')


class State(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('is_success',)
    is_success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSuccess')


class StateWithCount(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('state', 'count')
    state = sgqlc.types.Field(sgqlc.types.non_null(State), graphql_name='state')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count')


class StateWithErrors(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('state', 'info')
    state = sgqlc.types.Field(sgqlc.types.non_null(State), graphql_name='state')
    info = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(State)), graphql_name='info')


class Story(sgqlc.types.Type):
    __schema__ = api_schema
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
    __schema__ = api_schema
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
    __schema__ = api_schema
    __field_names__ = ('locale', 'value')
    locale = sgqlc.types.Field(sgqlc.types.non_null(Locale), graphql_name='locale')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class StringValue(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('value',)
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class Subscription(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('research_map_changed', 'domain_map_changed')
    research_map_changed = sgqlc.types.Field(sgqlc.types.non_null(MapEvents), graphql_name='researchMapChanged', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    domain_map_changed = sgqlc.types.Field(sgqlc.types.non_null(MapEvents), graphql_name='domainMapChanged')


class Table(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('cells', 'metadata')
    cells = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))))), graphql_name='cells')
    metadata = sgqlc.types.Field(sgqlc.types.non_null('TableMetadata'), graphql_name='metadata')


class TableMetadata(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('page_id',)
    page_id = sgqlc.types.Field(Int, graphql_name='pageId')


class TextBounding(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('component_id', 'start', 'end', 'node_id')
    component_id = sgqlc.types.Field(ID, graphql_name='componentId')
    start = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='start')
    end = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='end')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='nodeId')


class Time(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('hour', 'minute', 'second')
    hour = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='hour')
    minute = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='minute')
    second = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='second')


class TimestampValue(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('value',)
    value = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='value')


class Translation(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('text', 'language')
    text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='text')
    language = sgqlc.types.Field(sgqlc.types.non_null(Language), graphql_name='language')


class UpsertDrawing(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('drawing',)
    drawing = sgqlc.types.Field(sgqlc.types.non_null(MapDrawing), graphql_name='drawing')


class UpsertEdge(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('edge',)
    edge = sgqlc.types.Field(sgqlc.types.non_null(MapEdge), graphql_name='edge')


class UpsertGroup(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('group',)
    group = sgqlc.types.Field(sgqlc.types.non_null(Group), graphql_name='group')


class UpsertNode(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('node',)
    node = sgqlc.types.Field(sgqlc.types.non_null(MapNode), graphql_name='node')


class User(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class ValueWithConfidence(sgqlc.types.Type):
    __schema__ = api_schema
    __field_names__ = ('confidence', 'value')
    confidence = sgqlc.types.Field(Float, graphql_name='confidence')
    value = sgqlc.types.Field(sgqlc.types.non_null('Value'), graphql_name='value')


class Account(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema
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
    __schema__ = api_schema
    __field_names__ = ('property_value_type', 'value_slot_fact', 'fact_from')
    property_value_type = sgqlc.types.Field(sgqlc.types.non_null('CompositePropertyValueTemplate'), graphql_name='propertyValueType')
    value_slot_fact = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CompositePropertyValueComponentCandidateFact'))), graphql_name='valueSlotFact')
    fact_from = sgqlc.types.Field('AnyCompositePropertyFact', graphql_name='factFrom')


class CompositePropertyValueComponentCandidateFact(sgqlc.types.Type, FactInterface):
    __schema__ = api_schema
    __field_names__ = ('fact_from', 'fact_to', 'component_value_type')
    fact_from = sgqlc.types.Field(sgqlc.types.non_null(CompositePropertyValueCandidateFact), graphql_name='factFrom')
    fact_to = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyValueCandidateFact'), graphql_name='factTo')
    component_value_type = sgqlc.types.Field(sgqlc.types.non_null(CompositePropertyValueType), graphql_name='componentValueType')


class CompositePropertyValueTemplate(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema
    __field_names__ = ('id', 'name', 'component_value_types')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    component_value_types = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CompositePropertyValueType))), graphql_name='componentValueTypes')


class Concept(sgqlc.types.Type, KBEntity, PropertyTarget, LinkTarget, RecordInterface):
    __schema__ = api_schema
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
    __schema__ = api_schema
    __field_names__ = ('name', 'concept_type', 'list_concept')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    concept_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptType'), graphql_name='conceptType')
    list_concept = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptWithConfidence))), graphql_name='listConcept')


class ConceptCompositePropertyCandidateFact(sgqlc.types.Type, FactInterface):
    __schema__ = api_schema
    __field_names__ = ('concept_property_type', 'fact_to', 'fact_from')
    concept_property_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyType'), graphql_name='conceptPropertyType')
    fact_to = sgqlc.types.Field(sgqlc.types.non_null(CompositePropertyValueCandidateFact), graphql_name='factTo')
    fact_from = sgqlc.types.Field('ConceptLikeFact', graphql_name='factFrom')


class ConceptFact(sgqlc.types.Type, FactInterface, RecordInterface):
    __schema__ = api_schema
    __field_names__ = ('access_level', 'concept')
    access_level = sgqlc.types.Field(sgqlc.types.non_null(AccessLevel), graphql_name='accessLevel')
    concept = sgqlc.types.Field(sgqlc.types.non_null(Concept), graphql_name='concept')


class ConceptGroupFacet(sgqlc.types.Type, DocumentGroupFacet):
    __schema__ = api_schema
    __field_names__ = ('concept',)
    concept = sgqlc.types.Field(sgqlc.types.non_null(Concept), graphql_name='concept')


class ConceptLink(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema
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
    __schema__ = api_schema
    __field_names__ = ('concept_link_type', 'fact_from', 'fact_to')
    concept_link_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptLinkType'), graphql_name='conceptLinkType')
    fact_from = sgqlc.types.Field('ConceptLikeFact', graphql_name='factFrom')
    fact_to = sgqlc.types.Field('ConceptLikeFact', graphql_name='factTo')


class ConceptLinkCompositePropertyCandidateFact(sgqlc.types.Type, FactInterface):
    __schema__ = api_schema
    __field_names__ = ('concept_link_property_type', 'fact_to', 'fact_from')
    concept_link_property_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyType'), graphql_name='conceptLinkPropertyType')
    fact_to = sgqlc.types.Field(sgqlc.types.non_null(CompositePropertyValueCandidateFact), graphql_name='factTo')
    fact_from = sgqlc.types.Field('ConceptLinkLikeFact', graphql_name='factFrom')


class ConceptLinkFact(sgqlc.types.Type, FactInterface, RecordInterface):
    __schema__ = api_schema
    __field_names__ = ('access_level', 'concept_link')
    access_level = sgqlc.types.Field(sgqlc.types.non_null(AccessLevel), graphql_name='accessLevel')
    concept_link = sgqlc.types.Field(sgqlc.types.non_null(ConceptLink), graphql_name='conceptLink')


class ConceptLinkPropertyCandidateFact(sgqlc.types.Type, FactInterface):
    __schema__ = api_schema
    __field_names__ = ('fact_to', 'concept_link_property_type', 'fact_from')
    fact_to = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyValueCandidateFact'), graphql_name='factTo')
    concept_link_property_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyType'), graphql_name='conceptLinkPropertyType')
    fact_from = sgqlc.types.Field('ConceptLinkLikeFact', graphql_name='factFrom')


class ConceptLinkPropertyFact(sgqlc.types.Type, FactInterface, RecordInterface):
    __schema__ = api_schema
    __field_names__ = ('access_level', 'concept_link_property', 'parent_concept_link', 'mention', 'fact_from')
    access_level = sgqlc.types.Field(sgqlc.types.non_null(AccessLevel), graphql_name='accessLevel')
    concept_link_property = sgqlc.types.Field(sgqlc.types.non_null('ConceptProperty'), graphql_name='conceptLinkProperty')
    parent_concept_link = sgqlc.types.Field(sgqlc.types.non_null(ConceptLink), graphql_name='parentConceptLink')
    mention = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MentionUnion'))), graphql_name='mention')
    fact_from = sgqlc.types.Field('ConceptLinkLikeFact', graphql_name='factFrom')


class ConceptLinkType(sgqlc.types.Type, PropertyTypeTarget, RecordInterface):
    __schema__ = api_schema
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
    __schema__ = api_schema
    __field_names__ = ('concept_link_type',)
    concept_link_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptLinkType), graphql_name='conceptLinkType')


class ConceptProperty(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema
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
    __schema__ = api_schema
    __field_names__ = ('fact_to', 'concept_property_type', 'fact_from')
    fact_to = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyValueCandidateFact'), graphql_name='factTo')
    concept_property_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyType'), graphql_name='conceptPropertyType')
    fact_from = sgqlc.types.Field('ConceptLikeFact', graphql_name='factFrom')


class ConceptPropertyFact(sgqlc.types.Type, FactInterface, RecordInterface):
    __schema__ = api_schema
    __field_names__ = ('access_level', 'concept_property', 'parent_concept', 'mention', 'fact_from')
    access_level = sgqlc.types.Field(sgqlc.types.non_null(AccessLevel), graphql_name='accessLevel')
    concept_property = sgqlc.types.Field(sgqlc.types.non_null(ConceptProperty), graphql_name='conceptProperty')
    parent_concept = sgqlc.types.Field(sgqlc.types.non_null(Concept), graphql_name='parentConcept')
    mention = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MentionUnion'))), graphql_name='mention')
    fact_from = sgqlc.types.Field('ConceptLikeFact', graphql_name='factFrom')


class ConceptPropertyType(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema
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
    __schema__ = api_schema
    __field_names__ = ('concept_property_type',)
    concept_property_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptPropertyType), graphql_name='conceptPropertyType')


class ConceptPropertyValueCandidateFact(sgqlc.types.Type, FactInterface):
    __schema__ = api_schema
    __field_names__ = ('concept_property_value_type', 'meanings', 'fact_from')
    concept_property_value_type = sgqlc.types.Field(sgqlc.types.non_null('ConceptPropertyValueType'), graphql_name='conceptPropertyValueType')
    meanings = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ValueWithConfidence))), graphql_name='meanings')
    fact_from = sgqlc.types.Field('AnyPropertyOrValueComponentFact', graphql_name='factFrom')


class ConceptPropertyValueGroupFacet(sgqlc.types.Type, DocumentGroupFacet):
    __schema__ = api_schema
    __field_names__ = ('concept_property_type', 'concept_property_value')
    concept_property_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptPropertyType), graphql_name='conceptPropertyType')
    concept_property_value = sgqlc.types.Field(sgqlc.types.non_null('AnyValue'), graphql_name='conceptPropertyValue')


class ConceptPropertyValueType(sgqlc.types.Type, HasTypeSearchElements, RecordInterface):
    __schema__ = api_schema
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
    __schema__ = api_schema
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
    __schema__ = api_schema
    __field_names__ = ('concept_type',)
    concept_type = sgqlc.types.Field(sgqlc.types.non_null(ConceptType), graphql_name='conceptType')


class ConceptTypePresentation(sgqlc.types.Type, RecordInterface, EntityTypePresentation):
    __schema__ = api_schema
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
    __schema__ = api_schema
    __field_names__ = ('id', 'name', 'table_type', 'concept_type_presentation', 'hierarchy', 'columns_info')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    table_type = sgqlc.types.Field(sgqlc.types.non_null(WidgetTypeTableType), graphql_name='tableType')
    concept_type_presentation = sgqlc.types.Field(sgqlc.types.non_null(ConceptTypePresentation), graphql_name='conceptTypePresentation')
    hierarchy = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptLinkTypePath))))), graphql_name='hierarchy')
    columns_info = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptTypePresentationWidgetTypeColumn))), graphql_name='columnsInfo')


class ConceptTypeView(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema
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
    __schema__ = api_schema
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
    __schema__ = api_schema
    __field_names__ = ('account',)
    account = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name='account')


class DocumentDuplicateReport(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema
    __field_names__ = ('id', 'search_query', 'ignore_markup', 'auto_delete', 'fields', 'status', 'error_message', 'metrics')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    search_query = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='searchQuery')
    ignore_markup = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='ignoreMarkup')
    auto_delete = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='autoDelete')
    fields = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DocumentDuplicateComparisonField))), graphql_name='fields')
    status = sgqlc.types.Field(sgqlc.types.non_null(DocumentDuplicateReportStatus), graphql_name='status')
    error_message = sgqlc.types.Field(String, graphql_name='errorMessage')
    metrics = sgqlc.types.Field(DocumentDuplicateReportMetrics, graphql_name='metrics')


class DocumentFeed(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema
    __field_names__ = ('id', 'name', 'search_string', 'pagination_document')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    search_string = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='searchString')
    pagination_document = sgqlc.types.Field(sgqlc.types.non_null(DocumentFromDocumentFeedPagination), graphql_name='paginationDocument', args=sgqlc.types.ArgDict((
        ('mode', sgqlc.types.Arg(DocumentFeedMode, graphql_name='mode', default='all')),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
        ('filter_settings', sgqlc.types.Arg(DocumentFilterSettings, graphql_name='filterSettings', default=None)),
        ('direction', sgqlc.types.Arg(SortDirection, graphql_name='direction', default='descending')),
        ('sort_field', sgqlc.types.Arg(DocumentSorting, graphql_name='sortField', default=None)),
        ('extra_settings', sgqlc.types.Arg(sgqlc.types.non_null(ExtraSettings), graphql_name='extraSettings', default=None)),
))
    )


class DocumentPlatformGroupFacet(sgqlc.types.Type, DocumentGroupFacet):
    __schema__ = api_schema
    __field_names__ = ('platform',)
    platform = sgqlc.types.Field(sgqlc.types.non_null('Platform'), graphql_name='platform')


class DocumentPlatformTypeGroupFacet(sgqlc.types.Type, DocumentGroupFacet):
    __schema__ = api_schema
    __field_names__ = ('platform_type',)
    platform_type = sgqlc.types.Field(sgqlc.types.non_null(PlatformType), graphql_name='platformType')


class DocumentPropertyGroupFacet(sgqlc.types.Type, DocumentGroupFacet):
    __schema__ = api_schema
    __field_names__ = ('value',)
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class DocumentType(sgqlc.types.Type, RecordInterface, EntityType, PropertyTypeTarget, LinkTypeTarget, HasTypeSearchElements):
    __schema__ = api_schema
    __field_names__ = ('list_document_type_presentation',)
    list_document_type_presentation = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DocumentTypePresentation'))), graphql_name='listDocumentTypePresentation')


class DocumentTypePresentation(sgqlc.types.Type, RecordInterface, EntityTypePresentation):
    __schema__ = api_schema
    __field_names__ = ('id', 'name', 'root_document_type', 'is_default', 'hierarchy', 'columns_info')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    root_document_type = sgqlc.types.Field(sgqlc.types.non_null(DocumentType), graphql_name='rootDocumentType')
    is_default = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDefault')
    hierarchy = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptLinkTypePath))))), graphql_name='hierarchy')
    columns_info = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ConceptTypePresentationWidgetTypeColumn))), graphql_name='columnsInfo')


class ImageNodeMention(sgqlc.types.Type, MentionInterface, RecordInterface):
    __schema__ = api_schema
    __field_names__ = ('node_id', 'top', 'bottom', 'left', 'right')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='nodeId')
    top = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='top')
    bottom = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='bottom')
    left = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='left')
    right = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='right')


class Issue(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema
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
    __schema__ = api_schema
    __field_names__ = ('id', 'from_', 'to', 'comment')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    from_ = sgqlc.types.Field(sgqlc.types.non_null(IssueInfo), graphql_name='from')
    to = sgqlc.types.Field(sgqlc.types.non_null(IssueInfo), graphql_name='to')
    comment = sgqlc.types.Field(String, graphql_name='comment')


class NodeMention(sgqlc.types.Type, MentionInterface, RecordInterface):
    __schema__ = api_schema
    __field_names__ = ('node_id',)
    node_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='nodeId')


class Platform(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema
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
    __schema__ = api_schema
    __field_names__ = ('value_fact', 'mention')
    value_fact = sgqlc.types.Field(sgqlc.types.non_null(ConceptPropertyValueCandidateFact), graphql_name='valueFact')
    mention = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MentionUnion'))), graphql_name='mention')


class ResearchMap(sgqlc.types.Type, RecordInterface):
    __schema__ = api_schema
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
    __schema__ = api_schema
    __field_names__ = ('node_id', 'start', 'end')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='nodeId')
    start = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='start')
    end = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='end')



########################################################################
# Unions
########################################################################
class AnyCompositePropertyFact(sgqlc.types.Union):
    __schema__ = api_schema
    __types__ = (ConceptCompositePropertyCandidateFact, ConceptLinkCompositePropertyCandidateFact)


class AnyPropertyOrValueComponentFact(sgqlc.types.Union):
    __schema__ = api_schema
    __types__ = (ConceptPropertyFact, ConceptLinkPropertyFact, ConceptPropertyCandidateFact, ConceptLinkPropertyCandidateFact, CompositePropertyValueComponentCandidateFact)


class AnyValue(sgqlc.types.Union):
    __schema__ = api_schema
    __types__ = (CompositeValue, DateTimeValue, GeoPointValue, IntValue, DoubleValue, StringLocaleValue, StringValue, LinkValue, TimestampValue)


class AnyValueType(sgqlc.types.Union):
    __schema__ = api_schema
    __types__ = (ConceptPropertyValueType, CompositePropertyValueTemplate)


class ConceptLikeFact(sgqlc.types.Union):
    __schema__ = api_schema
    __types__ = (ConceptCandidateFact, ConceptFact)


class ConceptLinkLikeFact(sgqlc.types.Union):
    __schema__ = api_schema
    __types__ = (ConceptLinkCandidateFact, ConceptLinkFact)


class ConceptPropertyLikeFact(sgqlc.types.Union):
    __schema__ = api_schema
    __types__ = (ConceptPropertyFact, ConceptLinkPropertyFact)


class ConceptViewValue(sgqlc.types.Union):
    __schema__ = api_schema
    __types__ = (DateTimeValue, GeoPointValue, IntValue, DoubleValue, StringLocaleValue, StringValue, LinkValue, CompositeValue, Concept, ConceptType, ConceptLinkType, User, Image, TimestampValue)


class Entity(sgqlc.types.Union):
    __schema__ = api_schema
    __types__ = (Concept, Document, ConceptCandidateFact, ConceptType, DocumentType)


class EntityLink(sgqlc.types.Union):
    __schema__ = api_schema
    __types__ = (ConceptLink, ConceptFactLink, ConceptImplicitLink, ConceptCandidateFactMention, ConceptMention, DocumentLink, ConceptLinkCandidateFact, ConceptLinkType)


class Fact(sgqlc.types.Union):
    __schema__ = api_schema
    __types__ = (ConceptCandidateFact, ConceptFact, ConceptLinkCandidateFact, ConceptLinkFact, ConceptPropertyCandidateFact, ConceptPropertyFact, ConceptPropertyValueCandidateFact, ConceptLinkPropertyFact, ConceptLinkPropertyCandidateFact, CompositePropertyValueCandidateFact, CompositePropertyValueComponentCandidateFact, ConceptCompositePropertyCandidateFact, ConceptLinkCompositePropertyCandidateFact, PropertyValueMentionCandidateFact)


class MapEvent(sgqlc.types.Union):
    __schema__ = api_schema
    __types__ = (UpsertNode, UpsertEdge, UpsertGroup, UpsertDrawing, DeleteNode, DeleteEdge, DeleteGroup, DeleteDrawing, ShortestPath)


class MentionUnion(sgqlc.types.Union):
    __schema__ = api_schema
    __types__ = (TextNodeMention, ImageNodeMention, NodeMention)


class TypeSearchElement(sgqlc.types.Union):
    __schema__ = api_schema
    __types__ = (DictValue, NERCRegexp)


class UserMenuType(sgqlc.types.Union):
    __schema__ = api_schema
    __types__ = (ConceptType, ConceptTypePresentation, ConceptTypeView, DocumentType, DocumentTypePresentation)


class Value(sgqlc.types.Union):
    __schema__ = api_schema
    __types__ = (DateTimeValue, GeoPointValue, IntValue, DoubleValue, StringLocaleValue, StringValue, LinkValue, TimestampValue)



########################################################################
# Schema Entry Points
########################################################################
api_schema.query_type = Query
api_schema.mutation_type = Mutation
api_schema.subscription_type = Subscription

