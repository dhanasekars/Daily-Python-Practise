import sgqlc.types
import sgqlc.operation
import instrospection_schema

_schema = instrospection_schema
_schema_root = _schema.instrospection_schema

__all__ = ('Operations',)


def query_me():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='Me')
    _op_me = _op.me()
    _op_me.id()
    _op_me.name()
    _op_me.email()
    _op_me.age()
    _op_posts = _op.posts()
    _op_posts.id()
    _op_posts.title()
    _op_posts.body()
    _op_posts.published()
    _op_users = _op.users()
    _op_users.id()
    _op_users.name()
    _op_users.email()
    _op_users.age()
    _op_comments = _op.comments()
    _op_comments.id()
    _op_comments.text()
    return _op


class Query:
    me = query_me()


class Operations:
    query = Query
