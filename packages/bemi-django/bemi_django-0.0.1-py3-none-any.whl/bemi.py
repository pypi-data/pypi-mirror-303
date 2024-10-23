from django.utils.deprecation import MiddlewareMixin
from django.db.backends.postgresql.base import DatabaseWrapper
from django.db import connection
from django.utils.module_loading import import_string
from django.conf import settings
import contextvars
import json
import re

bemi_context_var = contextvars.ContextVar('bemi_context')

def get_bemi_context(request):
    func_path = getattr(settings, 'BEMI_CONTEXT_FUNCTION', None)
    if func_path:
        func = import_string(func_path)
        return func(request)
    return {}

class BemiMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response
        super().__init__(get_response)

    def __call__(self, request):
        context = get_bemi_context(request)
        bemi_context_var.set(context)
        with connection.execute_wrapper(BemiDBWrapper()):
            return self.get_response(request)

class BemiDBWrapper:
    def __call__(self, execute, sql, params, many, context):
        conn = context["connection"]
        if not isinstance(conn, DatabaseWrapper) or 'postgresql' not in conn.settings_dict['ENGINE']:
            return execute(sql, params, many, context)
        
        bemi_context = bemi_context_var.get(None)
        if bemi_context is None or not re.match(r"(INSERT|UPDATE|DELETE)\s", sql, re.IGNORECASE):
            return execute(sql, params, many, context)
        
        sql = sql.rstrip()
        safe_sql = sql.replace('%', '%%')
        sql_comment = " /*Bemi " + json.dumps({ **bemi_context, 'SQL': safe_sql }) + " Bemi*/"
        if sql[-1] == ";":
            sql = sql[:-1] + sql_comment + ";"
        else:
            sql = sql + sql_comment
            
        return execute(sql, params, many, context)
