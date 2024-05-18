# Tests splitting functions.

import types
from io import StringIO

import pytest

import sqlparse

sql="""
update test set name="
" ( " + a + " == null || " + b + " == \"\" ) "
"
where id =1;
update test set name="
" ( " + a + " == null || " + b + " == \"\" ) "
"
where id =2;
update test set name="
" ( " + a + " == null || " + b + " == \"\" ) "
"
where id =3;
"""
# print(len(sqlparse.split(sql)))


sql = """SELECT val1 || val2 ||--;
continuedvals;
"""

formatted = sqlparse.format(sql, strip_comments=True)
print(len(sqlparse.split(processed)))