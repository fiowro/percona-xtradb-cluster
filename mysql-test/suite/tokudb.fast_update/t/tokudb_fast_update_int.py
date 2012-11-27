#!/usr/bin/env python

import sys

def main():
    print "# generated by tokudb_fast_update_int.py"
    print "source include/have_tokudb.inc;"
    print "set default_storage_engine='tokudb';"
    print "disable_warnings;"
    print "drop table if exists t;"
    print "enable_warnings;"

    for t in [ 'tinyint', 'smallint', 'mediumint', 'int', 'bigint' ]:
        for u in [ '', 'unsigned' ]:
            for n in [ 'null', 'not null' ]:
                test_int(t, u, n)
    return 0

def test_int(t, u, n):
    print "create table t ("
    print "    id %s %s %s primary key," % (t, u, n)
    print "    x %s %s %s" % (t, u, n)
    print ");"

    print "insert into t values (1,0),(2,0),(3,0);"
    print "select * from t;"

    print "set tokudb_enable_fast_update=1;"
    print "set tokudb_disable_slow_update=1;"

    # set is fast
    print "update t set x=100 where id=2;"
    print "select * from t;"

    # increment is fast
    print "update t set x=x+1 where id=3;"
    print "select * from t;"

    # decrement is fast
    print "update t set x=x-1 where id=3;"
    print "select * from t;"

    # field=field+constant is fast
    print "update t set x=x+100 where id=3;"
    print "select * from t;"

    # field=field-constant is fast
    print "update t set x=x-100 where id=3;"
    print "select * from t;"

    # field=constant+field is not yet fast
    print "replace_regex /MariaDB/XYZ/ /MySQL/XYZ/;"
    print "error ER_UNSUPPORTED_EXTENSION;"
    print "update t set x=1+x where id=1;"

    # field=-field is not yet fast
    print "replace_regex /MariaDB/XYZ/ /MySQL/XYZ/;"
    print "error ER_UNSUPPORTED_EXTENSION;"
    print "update t set x=-x where id=1;"

    # yes, we can update a field in a non-existent row and the row is not inserted
    print "update t set x=x+1 where id=1000000;"
    print "select * from t;"

    # range updates are not yet fast
    print "replace_regex /MariaDB/XYZ/ /MySQL/XYZ/;"
    print "error ER_UNSUPPORTED_EXTENSION;"
    print "update t set x=x+1 where 1 <= id and id < 1000;"

    # full table updates are not yet fast
    print "replace_regex /MariaDB/XYZ/ /MySQL/XYZ/;"
    print "error ER_UNSUPPORTED_EXTENSION;"
    print "update t set x=x+1;"

    print "drop table t;"

sys.exit(main())
