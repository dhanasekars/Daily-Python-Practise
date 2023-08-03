import sgqlc.types


instrospection_schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
Boolean = sgqlc.types.Boolean

ID = sgqlc.types.ID

Int = sgqlc.types.Int

String = sgqlc.types.String


########################################################################
# Input Objects
########################################################################
class CreateCommentInput(sgqlc.types.Input):
    __schema__ = instrospection_schema
    __field_names__ = ('text', 'post', 'author')
    text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='text')
    post = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='post')
    author = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='author')


class CreatePostInput(sgqlc.types.Input):
    __schema__ = instrospection_schema
    __field_names__ = ('title', 'body', 'published', 'author')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    published = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='published')
    author = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='author')


class CreateUserInput(sgqlc.types.Input):
    __schema__ = instrospection_schema
    __field_names__ = ('name', 'email', 'age')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    age = sgqlc.types.Field(Int, graphql_name='age')


class UpdateCommentInput(sgqlc.types.Input):
    __schema__ = instrospection_schema
    __field_names__ = ('text',)
    text = sgqlc.types.Field(String, graphql_name='text')


class UpdatePostInput(sgqlc.types.Input):
    __schema__ = instrospection_schema
    __field_names__ = ('title', 'body', 'published')
    title = sgqlc.types.Field(String, graphql_name='title')
    body = sgqlc.types.Field(String, graphql_name='body')
    published = sgqlc.types.Field(Boolean, graphql_name='published')


class UpdateUserInput(sgqlc.types.Input):
    __schema__ = instrospection_schema
    __field_names__ = ('name', 'email', 'age')
    name = sgqlc.types.Field(String, graphql_name='name')
    email = sgqlc.types.Field(String, graphql_name='email')
    age = sgqlc.types.Field(Int, graphql_name='age')



########################################################################
# Output Objects and Interfaces
########################################################################
class Comment(sgqlc.types.Type):
    __schema__ = instrospection_schema
    __field_names__ = ('id', 'text', 'author', 'post')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='text')
    author = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='author')
    post = sgqlc.types.Field(sgqlc.types.non_null('Post'), graphql_name='post')


class Mutation(sgqlc.types.Type):
    __schema__ = instrospection_schema
    __field_names__ = ('create_user', 'delete_user', 'update_user', 'create_post', 'delete_post', 'update_post', 'create_comment', 'delete_comment', 'update_comment')
    create_user = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='createUser', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(CreateUserInput, graphql_name='data', default=None)),
))
    )
    delete_user = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='deleteUser', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    update_user = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='updateUser', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(UpdateUserInput), graphql_name='data', default=None)),
))
    )
    create_post = sgqlc.types.Field(sgqlc.types.non_null('Post'), graphql_name='createPost', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(CreatePostInput, graphql_name='data', default=None)),
))
    )
    delete_post = sgqlc.types.Field(sgqlc.types.non_null('Post'), graphql_name='deletePost', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    update_post = sgqlc.types.Field(sgqlc.types.non_null('Post'), graphql_name='updatePost', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(UpdatePostInput), graphql_name='data', default=None)),
))
    )
    create_comment = sgqlc.types.Field(sgqlc.types.non_null(Comment), graphql_name='createComment', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(CreateCommentInput, graphql_name='data', default=None)),
))
    )
    delete_comment = sgqlc.types.Field(sgqlc.types.non_null(Comment), graphql_name='deleteComment', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    update_comment = sgqlc.types.Field(sgqlc.types.non_null(Comment), graphql_name='updateComment', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(UpdateCommentInput), graphql_name='data', default=None)),
))
    )


class Post(sgqlc.types.Type):
    __schema__ = instrospection_schema
    __field_names__ = ('id', 'title', 'body', 'published', 'author', 'comments')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    body = sgqlc.types.Field(String, graphql_name='body')
    published = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='published')
    author = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='author')
    comments = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Comment))), graphql_name='comments')


class PostSubscriptionPayload(sgqlc.types.Type):
    __schema__ = instrospection_schema
    __field_names__ = ('mutation', 'data')
    mutation = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='mutation')
    data = sgqlc.types.Field(sgqlc.types.non_null(Post), graphql_name='data')


class Query(sgqlc.types.Type):
    __schema__ = instrospection_schema
    __field_names__ = ('me', 'posts', 'users', 'comments')
    me = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='me')
    posts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Post))), graphql_name='posts', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
))
    )
    users = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='users', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
))
    )
    comments = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Comment))), graphql_name='comments')


class Subscription(sgqlc.types.Type):
    __schema__ = instrospection_schema
    __field_names__ = ('count', 'comment', 'post')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count')
    comment = sgqlc.types.Field(sgqlc.types.non_null(Comment), graphql_name='comment', args=sgqlc.types.ArgDict((
        ('post_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='postId', default=None)),
))
    )
    post = sgqlc.types.Field(sgqlc.types.non_null(PostSubscriptionPayload), graphql_name='post')


class User(sgqlc.types.Type):
    __schema__ = instrospection_schema
    __field_names__ = ('id', 'name', 'email', 'age', 'posts', 'comments')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    age = sgqlc.types.Field(Int, graphql_name='age')
    posts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Post))), graphql_name='posts')
    comments = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Comment))), graphql_name='comments')



########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
instrospection_schema.query_type = Query
instrospection_schema.mutation_type = Mutation
instrospection_schema.subscription_type = Subscription

