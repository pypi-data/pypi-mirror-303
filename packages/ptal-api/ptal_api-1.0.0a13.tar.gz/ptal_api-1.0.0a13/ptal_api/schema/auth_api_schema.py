import sgqlc.types


auth_api_schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
class AllowedFunctionsEnum(sgqlc.types.Enum):
    __schema__ = auth_api_schema
    __choices__ = ('Administration', 'Developer', 'EditCrawlers', 'EditDocumentFeeds', 'EditExport', 'EditExternalSearch', 'EditIssues', 'EditKBAndDocuments', 'EditReferenceInfo', 'EditResearchMaps', 'EditStream', 'EditTasks', 'EditTransformations', 'ExportKBAndDocuments', 'ReadCrawlers', 'ReadDocumentFeeds', 'ReadExport', 'ReadExternalSearch', 'ReadIssues', 'ReadKBAndDocuments', 'ReadReferenceInfo', 'ReadReportExport', 'ReadResearchMaps', 'ReadStream', 'ReadTasks', 'ReadTransformations', 'RunCrawlers', 'RunExternalSearch', 'RunTransformations')


class AttributeSource(sgqlc.types.Enum):
    __schema__ = auth_api_schema
    __choices__ = ('Group', 'Personal')


class AttributeType(sgqlc.types.Enum):
    __schema__ = auth_api_schema
    __choices__ = ('boolean', 'booleanList', 'double', 'doubleList', 'int', 'intList', 'string', 'stringList')


Boolean = sgqlc.types.Boolean

Float = sgqlc.types.Float

ID = sgqlc.types.ID

Int = sgqlc.types.Int

class JSON(sgqlc.types.Scalar):
    __schema__ = auth_api_schema


class Long(sgqlc.types.Scalar):
    __schema__ = auth_api_schema


class PolicyIndex(sgqlc.types.Enum):
    __schema__ = auth_api_schema
    __choices__ = ('concepts', 'documents')


class PolicyType(sgqlc.types.Enum):
    __schema__ = auth_api_schema
    __choices__ = ('es', 'local')


String = sgqlc.types.String

class UnixTime(sgqlc.types.Scalar):
    __schema__ = auth_api_schema



########################################################################
# Input Objects
########################################################################
class AddUserGroupMembersParams(sgqlc.types.Input):
    __schema__ = auth_api_schema
    __field_names__ = ('user_ids', 'group_ids')
    user_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='userIds')
    group_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='groupIds')


class AttributeFilterSettings(sgqlc.types.Input):
    __schema__ = auth_api_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(String, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')


class CreateUserGroupParams(sgqlc.types.Input):
    __schema__ = auth_api_schema
    __field_names__ = ('name', 'description')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')


class CreateUserParams(sgqlc.types.Input):
    __schema__ = auth_api_schema
    __field_names__ = ('login', 'first_name', 'last_name', 'fathers_name', 'email', 'access_level_id', 'is_admin', 'enabled', 'receive_notifications', 'receive_telegram_notifications', 'telegram_chat_id')
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')
    first_name = sgqlc.types.Field(String, graphql_name='firstName')
    last_name = sgqlc.types.Field(String, graphql_name='lastName')
    fathers_name = sgqlc.types.Field(String, graphql_name='fathersName')
    email = sgqlc.types.Field(String, graphql_name='email')
    access_level_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='accessLevelID')
    is_admin = sgqlc.types.Field(Boolean, graphql_name='isAdmin')
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')
    receive_notifications = sgqlc.types.Field(Boolean, graphql_name='receiveNotifications')
    receive_telegram_notifications = sgqlc.types.Field(Boolean, graphql_name='receiveTelegramNotifications')
    telegram_chat_id = sgqlc.types.Field(Long, graphql_name='telegramChatId')


class DeleteUserGroupMemberParams(sgqlc.types.Input):
    __schema__ = auth_api_schema
    __field_names__ = ('user_id', 'group_id')
    user_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='userId')
    group_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='groupId')


class PolicyParameterInputGQL(sgqlc.types.Input):
    __schema__ = auth_api_schema
    __field_names__ = ('param', 'parameter_type')
    param = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='param')
    parameter_type = sgqlc.types.Field(sgqlc.types.non_null(AttributeType), graphql_name='parameterType')


class SecurityPolicyArg(sgqlc.types.Input):
    __schema__ = auth_api_schema
    __field_names__ = ('id', 'name', 'target', 'policy_type', 'rule', 'params', 'index')
    id = sgqlc.types.Field(String, graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    target = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='target')
    policy_type = sgqlc.types.Field(sgqlc.types.non_null(PolicyType), graphql_name='policyType')
    rule = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='rule')
    params = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PolicyParameterInputGQL))), graphql_name='params')
    index = sgqlc.types.Field(PolicyIndex, graphql_name='index')


class TimestampInterval(sgqlc.types.Input):
    __schema__ = auth_api_schema
    __field_names__ = ('start', 'end')
    start = sgqlc.types.Field(UnixTime, graphql_name='start')
    end = sgqlc.types.Field(UnixTime, graphql_name='end')


class UpdateCurrentUserParams(sgqlc.types.Input):
    __schema__ = auth_api_schema
    __field_names__ = ('first_name', 'last_name', 'fathers_name', 'email', 'password', 'receive_notifications', 'receive_telegram_notifications', 'telegram_chat_id')
    first_name = sgqlc.types.Field(String, graphql_name='firstName')
    last_name = sgqlc.types.Field(String, graphql_name='lastName')
    fathers_name = sgqlc.types.Field(String, graphql_name='fathersName')
    email = sgqlc.types.Field(String, graphql_name='email')
    password = sgqlc.types.Field(String, graphql_name='password')
    receive_notifications = sgqlc.types.Field(Boolean, graphql_name='receiveNotifications')
    receive_telegram_notifications = sgqlc.types.Field(Boolean, graphql_name='receiveTelegramNotifications')
    telegram_chat_id = sgqlc.types.Field(Long, graphql_name='telegramChatId')


class UpdateUserGroupParams(sgqlc.types.Input):
    __schema__ = auth_api_schema
    __field_names__ = ('name', 'description')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')


class UpdateUserParams(sgqlc.types.Input):
    __schema__ = auth_api_schema
    __field_names__ = ('first_name', 'last_name', 'fathers_name', 'email', 'access_level_id', 'is_admin', 'enabled', 'receive_notifications', 'receive_telegram_notifications', 'telegram_chat_id')
    first_name = sgqlc.types.Field(String, graphql_name='firstName')
    last_name = sgqlc.types.Field(String, graphql_name='lastName')
    fathers_name = sgqlc.types.Field(String, graphql_name='fathersName')
    email = sgqlc.types.Field(String, graphql_name='email')
    access_level_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='accessLevelID')
    is_admin = sgqlc.types.Field(Boolean, graphql_name='isAdmin')
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')
    receive_notifications = sgqlc.types.Field(Boolean, graphql_name='receiveNotifications')
    receive_telegram_notifications = sgqlc.types.Field(Boolean, graphql_name='receiveTelegramNotifications')
    telegram_chat_id = sgqlc.types.Field(Long, graphql_name='telegramChatId')


class UserAttributeInput(sgqlc.types.Input):
    __schema__ = auth_api_schema
    __field_names__ = ('id', 'json_value')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    json_value = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='jsonValue')


class UserFilterSettings(sgqlc.types.Input):
    __schema__ = auth_api_schema
    __field_names__ = ('query', 'user_id', 'login', 'first_name', 'last_name', 'fathers_name', 'email', 'enabled', 'group_ids', 'creator', 'last_updater', 'creation_date', 'update_date', 'show_system_users')
    query = sgqlc.types.Field(String, graphql_name='query')
    user_id = sgqlc.types.Field(ID, graphql_name='userId')
    login = sgqlc.types.Field(String, graphql_name='login')
    first_name = sgqlc.types.Field(String, graphql_name='firstName')
    last_name = sgqlc.types.Field(String, graphql_name='lastName')
    fathers_name = sgqlc.types.Field(String, graphql_name='fathersName')
    email = sgqlc.types.Field(String, graphql_name='email')
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')
    group_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='groupIds')
    creator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='creator')
    last_updater = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='lastUpdater')
    creation_date = sgqlc.types.Field(TimestampInterval, graphql_name='creationDate')
    update_date = sgqlc.types.Field(TimestampInterval, graphql_name='updateDate')
    show_system_users = sgqlc.types.Field(Boolean, graphql_name='showSystemUsers')


class UserGroupFilterSettings(sgqlc.types.Input):
    __schema__ = auth_api_schema
    __field_names__ = ('query', 'name', 'description', 'user_ids', 'creator', 'last_updater', 'creation_date', 'update_date')
    query = sgqlc.types.Field(String, graphql_name='query')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    user_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='userIds')
    creator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='creator')
    last_updater = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='lastUpdater')
    creation_date = sgqlc.types.Field(TimestampInterval, graphql_name='creationDate')
    update_date = sgqlc.types.Field(TimestampInterval, graphql_name='updateDate')



########################################################################
# Output Objects and Interfaces
########################################################################
class RecordInterface(sgqlc.types.Interface):
    __schema__ = auth_api_schema
    __field_names__ = ('system_registration_date', 'system_update_date', 'creator', 'last_updater')
    system_registration_date = sgqlc.types.Field(sgqlc.types.non_null(UnixTime), graphql_name='systemRegistrationDate')
    system_update_date = sgqlc.types.Field(UnixTime, graphql_name='systemUpdateDate')
    creator = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='creator')
    last_updater = sgqlc.types.Field('User', graphql_name='lastUpdater')


class AccessLevel(sgqlc.types.Type):
    __schema__ = auth_api_schema
    __field_names__ = ('id', 'name', 'order')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    order = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='order')


class Attribute(sgqlc.types.Type):
    __schema__ = auth_api_schema
    __field_names__ = ('id', 'name', 'value_type', 'params_schema')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value_type = sgqlc.types.Field(sgqlc.types.non_null(AttributeType), graphql_name='valueType')
    params_schema = sgqlc.types.Field(sgqlc.types.non_null('ParamsSchema'), graphql_name='paramsSchema')


class AttributePagination(sgqlc.types.Type):
    __schema__ = auth_api_schema
    __field_names__ = ('list_attribute', 'total')
    list_attribute = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Attribute))), graphql_name='listAttribute')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class BooleanListValue(sgqlc.types.Type):
    __schema__ = auth_api_schema
    __field_names__ = ('value',)
    value = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Boolean))), graphql_name='value')


class BooleanValue(sgqlc.types.Type):
    __schema__ = auth_api_schema
    __field_names__ = ('value',)
    value = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='value')


class ConflictsState(sgqlc.types.Type):
    __schema__ = auth_api_schema
    __field_names__ = ('user_conflicts', 'group_conflicts')
    user_conflicts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(Boolean)), graphql_name='userConflicts')
    group_conflicts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(Boolean)), graphql_name='groupConflicts')


class DoubleListValue(sgqlc.types.Type):
    __schema__ = auth_api_schema
    __field_names__ = ('value',)
    value = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Float))), graphql_name='value')


class DoubleValue(sgqlc.types.Type):
    __schema__ = auth_api_schema
    __field_names__ = ('value',)
    value = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='value')


class IntListValue(sgqlc.types.Type):
    __schema__ = auth_api_schema
    __field_names__ = ('value',)
    value = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='value')


class IntValue(sgqlc.types.Type):
    __schema__ = auth_api_schema
    __field_names__ = ('value',)
    value = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='value')


class Mutation(sgqlc.types.Type):
    __schema__ = auth_api_schema
    __field_names__ = ('add_user', 'update_user_password', 'update_current_user_password', 'update_current_user', 'update_user', 'update_user_attributes', 'update_user_activity', 'delete_user', 'add_policy', 'delete_policy', 'set_kvstore_item', 'delete_kvstore_item', 'add_user_group', 'update_user_group', 'update_user_group_attributes', 'delete_user_group', 'add_user_group_members', 'delete_user_group_members')
    add_user = sgqlc.types.Field('User', graphql_name='addUser', args=sgqlc.types.ArgDict((
        ('create_user_params', sgqlc.types.Arg(sgqlc.types.non_null(CreateUserParams), graphql_name='createUserParams', default=None)),
))
    )
    update_user_password = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateUserPassword', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('password', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='password', default=None)),
))
    )
    update_current_user_password = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateCurrentUserPassword', args=sgqlc.types.ArgDict((
        ('old_password', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='oldPassword', default=None)),
        ('password', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='password', default=None)),
))
    )
    update_current_user = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateCurrentUser', args=sgqlc.types.ArgDict((
        ('update_current_user_params', sgqlc.types.Arg(sgqlc.types.non_null(UpdateCurrentUserParams), graphql_name='updateCurrentUserParams', default=None)),
))
    )
    update_user = sgqlc.types.Field('User', graphql_name='updateUser', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('update_user_params', sgqlc.types.Arg(sgqlc.types.non_null(UpdateUserParams), graphql_name='updateUserParams', default=None)),
))
    )
    update_user_attributes = sgqlc.types.Field(sgqlc.types.non_null('UserWithError'), graphql_name='updateUserAttributes', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('attributes', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(UserAttributeInput))), graphql_name='attributes', default=None)),
))
    )
    update_user_activity = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateUserActivity', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
        ('is_enabled', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='isEnabled', default=None)),
))
    )
    delete_user = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteUser', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    add_policy = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='addPolicy', args=sgqlc.types.ArgDict((
        ('policy_params', sgqlc.types.Arg(sgqlc.types.non_null(SecurityPolicyArg), graphql_name='policyParams', default=None)),
))
    )
    delete_policy = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deletePolicy', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    set_kvstore_item = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setKVStoreItem', args=sgqlc.types.ArgDict((
        ('key', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='key', default=None)),
        ('value', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='value', default=None)),
))
    )
    delete_kvstore_item = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteKVStoreItem', args=sgqlc.types.ArgDict((
        ('key', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='key', default=None)),
))
    )
    add_user_group = sgqlc.types.Field('UserGroup', graphql_name='addUserGroup', args=sgqlc.types.ArgDict((
        ('create_user_group_params', sgqlc.types.Arg(sgqlc.types.non_null(CreateUserGroupParams), graphql_name='createUserGroupParams', default=None)),
))
    )
    update_user_group = sgqlc.types.Field(sgqlc.types.non_null('UserGroup'), graphql_name='updateUserGroup', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('update_user_group_params', sgqlc.types.Arg(sgqlc.types.non_null(UpdateUserGroupParams), graphql_name='updateUserGroupParams', default=None)),
))
    )
    update_user_group_attributes = sgqlc.types.Field(sgqlc.types.non_null('UserGroupWithError'), graphql_name='updateUserGroupAttributes', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('attributes', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(UserAttributeInput))), graphql_name='attributes', default=None)),
))
    )
    delete_user_group = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteUserGroup', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    add_user_group_members = sgqlc.types.Field(sgqlc.types.non_null('StateWithError'), graphql_name='addUserGroupMembers', args=sgqlc.types.ArgDict((
        ('add_user_group_members_params', sgqlc.types.Arg(sgqlc.types.non_null(AddUserGroupMembersParams), graphql_name='addUserGroupMembersParams', default=None)),
))
    )
    delete_user_group_members = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteUserGroupMembers', args=sgqlc.types.ArgDict((
        ('delete_user_group_member_params', sgqlc.types.Arg(sgqlc.types.non_null(DeleteUserGroupMemberParams), graphql_name='deleteUserGroupMemberParams', default=None)),
))
    )


class ParamsSchema(sgqlc.types.Type):
    __schema__ = auth_api_schema
    __field_names__ = ('schema', 'ui_schema')
    schema = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='schema')
    ui_schema = sgqlc.types.Field(JSON, graphql_name='uiSchema')


class PolicyParameterGQL(sgqlc.types.Type):
    __schema__ = auth_api_schema
    __field_names__ = ('param', 'parameter_type')
    param = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='param')
    parameter_type = sgqlc.types.Field(sgqlc.types.non_null(AttributeType), graphql_name='parameterType')


class Query(sgqlc.types.Type):
    __schema__ = auth_api_schema
    __field_names__ = ('user', 'user_sys', 'user_idlist', 'user_idlist_sys', 'current_user', 'user_by_login', 'pagination_user', 'token_exchange', 'refresh_token', 'list_policy', 'get_kvstore_item', 'pagination_attribute', 'user_group', 'pagination_user_group')
    user = sgqlc.types.Field('User', graphql_name='user', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    user_sys = sgqlc.types.Field('User', graphql_name='userSys', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    user_idlist = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('User')), graphql_name='userIDList', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    user_idlist_sys = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('User')), graphql_name='userIDListSys', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    current_user = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='currentUser')
    user_by_login = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='userByLogin', args=sgqlc.types.ArgDict((
        ('username', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='username', default=None)),
        ('password', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='password', default=None)),
))
    )
    pagination_user = sgqlc.types.Field(sgqlc.types.non_null('UserPagination'), graphql_name='paginationUser', args=sgqlc.types.ArgDict((
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(UserFilterSettings), graphql_name='filterSettings', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
))
    )
    token_exchange = sgqlc.types.Field('Token', graphql_name='tokenExchange', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    refresh_token = sgqlc.types.Field('Token', graphql_name='refreshToken', args=sgqlc.types.ArgDict((
        ('refresh_token', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='refreshToken', default=None)),
))
    )
    list_policy = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SecurityPolicyGQL'))), graphql_name='listPolicy', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    get_kvstore_item = sgqlc.types.Field(String, graphql_name='getKVStoreItem', args=sgqlc.types.ArgDict((
        ('key', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='key', default=None)),
))
    )
    pagination_attribute = sgqlc.types.Field(sgqlc.types.non_null(AttributePagination), graphql_name='paginationAttribute', args=sgqlc.types.ArgDict((
        ('attribute_filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(AttributeFilterSettings), graphql_name='attributeFilterSettings', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
))
    )
    user_group = sgqlc.types.Field(sgqlc.types.non_null('UserGroup'), graphql_name='userGroup', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    pagination_user_group = sgqlc.types.Field(sgqlc.types.non_null('UserGroupPagination'), graphql_name='paginationUserGroup', args=sgqlc.types.ArgDict((
        ('filter_settings', sgqlc.types.Arg(sgqlc.types.non_null(UserGroupFilterSettings), graphql_name='filterSettings', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=20)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=0)),
))
    )


class SecurityPolicyGQL(sgqlc.types.Type):
    __schema__ = auth_api_schema
    __field_names__ = ('id', 'name', 'target', 'policy_type', 'rule', 'params', 'index')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    target = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='target')
    policy_type = sgqlc.types.Field(sgqlc.types.non_null(PolicyType), graphql_name='policyType')
    rule = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='rule')
    params = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PolicyParameterGQL))), graphql_name='params')
    index = sgqlc.types.Field(PolicyIndex, graphql_name='index')


class StateWithError(sgqlc.types.Type):
    __schema__ = auth_api_schema
    __field_names__ = ('state', 'info')
    state = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='state')
    info = sgqlc.types.Field(sgqlc.types.non_null(ConflictsState), graphql_name='info')


class StringListValue(sgqlc.types.Type):
    __schema__ = auth_api_schema
    __field_names__ = ('value',)
    value = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='value')


class StringValue(sgqlc.types.Type):
    __schema__ = auth_api_schema
    __field_names__ = ('value',)
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class Token(sgqlc.types.Type):
    __schema__ = auth_api_schema
    __field_names__ = ('access_token', 'refresh_token', 'access_token_expires_at', 'refresh_token_expires_at')
    access_token = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='accessToken')
    refresh_token = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='refreshToken')
    access_token_expires_at = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='accessTokenExpiresAt')
    refresh_token_expires_at = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='refreshTokenExpiresAt')


class UserAttribute(sgqlc.types.Type):
    __schema__ = auth_api_schema
    __field_names__ = ('id', 'name', 'attribute_source', 'value', 'json_value')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    attribute_source = sgqlc.types.Field(sgqlc.types.non_null(AttributeSource), graphql_name='attributeSource')
    value = sgqlc.types.Field(sgqlc.types.non_null('AttributeValue'), graphql_name='value')
    json_value = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='jsonValue')


class UserGroupMetrics(sgqlc.types.Type):
    __schema__ = auth_api_schema
    __field_names__ = ('count_user',)
    count_user = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countUser')


class UserGroupPagination(sgqlc.types.Type):
    __schema__ = auth_api_schema
    __field_names__ = ('list_user_group', 'total')
    list_user_group = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserGroup'))), graphql_name='listUserGroup')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class UserGroupWithError(sgqlc.types.Type):
    __schema__ = auth_api_schema
    __field_names__ = ('user_group', 'info')
    user_group = sgqlc.types.Field(sgqlc.types.non_null('UserGroup'), graphql_name='userGroup')
    info = sgqlc.types.Field(sgqlc.types.non_null(ConflictsState), graphql_name='info')


class UserMetrics(sgqlc.types.Type):
    __schema__ = auth_api_schema
    __field_names__ = ('count_group',)
    count_group = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='countGroup')


class UserPagination(sgqlc.types.Type):
    __schema__ = auth_api_schema
    __field_names__ = ('list_user', 'total')
    list_user = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='listUser')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class UserWithError(sgqlc.types.Type):
    __schema__ = auth_api_schema
    __field_names__ = ('user', 'info')
    user = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='user')
    info = sgqlc.types.Field(sgqlc.types.non_null(ConflictsState), graphql_name='info')


class User(sgqlc.types.Type, RecordInterface):
    __schema__ = auth_api_schema
    __field_names__ = ('id', 'login', 'first_name', 'last_name', 'fathers_name', 'email', 'is_admin', 'enabled', 'receive_notifications', 'receive_telegram_notifications', 'telegram_chat_id', 'access_level', 'name', 'list_user_group', 'metrics', 'attributes', 'allowed_functions')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')
    first_name = sgqlc.types.Field(String, graphql_name='firstName')
    last_name = sgqlc.types.Field(String, graphql_name='lastName')
    fathers_name = sgqlc.types.Field(String, graphql_name='fathersName')
    email = sgqlc.types.Field(String, graphql_name='email')
    is_admin = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAdmin')
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enabled')
    receive_notifications = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='receiveNotifications')
    receive_telegram_notifications = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='receiveTelegramNotifications')
    telegram_chat_id = sgqlc.types.Field(Long, graphql_name='telegramChatId')
    access_level = sgqlc.types.Field(sgqlc.types.non_null(AccessLevel), graphql_name='accessLevel')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    list_user_group = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserGroup'))), graphql_name='listUserGroup')
    metrics = sgqlc.types.Field(sgqlc.types.non_null(UserMetrics), graphql_name='metrics')
    attributes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(UserAttribute))), graphql_name='attributes', args=sgqlc.types.ArgDict((
        ('show_default', sgqlc.types.Arg(Boolean, graphql_name='showDefault', default=False)),
        ('is_request_from_front', sgqlc.types.Arg(Boolean, graphql_name='isRequestFromFront', default=True)),
))
    )
    allowed_functions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AllowedFunctionsEnum))), graphql_name='allowedFunctions')


class UserGroup(sgqlc.types.Type, RecordInterface):
    __schema__ = auth_api_schema
    __field_names__ = ('id', 'name', 'description', 'attributes', 'list_user', 'metrics')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    attributes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(UserAttribute))), graphql_name='attributes')
    list_user = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(User))), graphql_name='listUser')
    metrics = sgqlc.types.Field(sgqlc.types.non_null(UserGroupMetrics), graphql_name='metrics')



########################################################################
# Unions
########################################################################
class AttributeValue(sgqlc.types.Union):
    __schema__ = auth_api_schema
    __types__ = (IntValue, DoubleValue, StringValue, BooleanValue, IntListValue, DoubleListValue, StringListValue, BooleanListValue)



########################################################################
# Schema Entry Points
########################################################################
auth_api_schema.query_type = Query
auth_api_schema.mutation_type = Mutation
auth_api_schema.subscription_type = None

