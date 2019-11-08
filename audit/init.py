from ext.mysqlsh_plugins_common import register_plugin
from ext.audit import trx
from ext.audit import queries


register_plugin("showTrxSize", trx.show_trx_size,
           {"brief": "Prints Transactions Size from a binlog",
             "parameters": [{
                "name": "binlog",
                "brief": "The binlog file to extract transactions from.",
                "type": "string",
                "required": False
            },{
                "name": "session",
                "brief": "The session to be used on the operation.",
                "type": "object",
                "classes": ["Session", "ClassicSession"],
                "required": False
            }
            ]
           },
           "audit",
           {
             "brief": "Audit management and utilities.",
             "details": [
                 "A collection of Audit management tools and utilities"
             ]
           }
     )

register_plugin("showTrxSizeSort", trx.show_trx_size_sort,
           {"brief": "Prints Transactions Size from a binlog",
             "parameters": [{
                "name": "limit",
                "brief": "The maximum transactions to show, default is 10",
                "type": "integer",
                "required": False
            },{
                "name": "binlog",
                "brief": "The binlog file to extract transactions from.",
                "type": "string",
                "required": False
            },{
                "name": "session",
                "brief": "The session to be used on the operation.",
                "type": "object",
                "classes": ["Session", "ClassicSession"],
                "required": False
            }
            ]
           },
           "audit",
           {
             "brief": "Audit management and utilities.",
             "details": [
                 "A collection of Audit management tools and utilities"
             ]
           }
     )

register_plugin("getBinlogs", trx.show_binlogs,
           {"brief": "Prints the list of binary logs available on the server",
             "parameters": [{
                "name": "session",
                "brief": "The session to be used on the operation.",
                "type": "object",
                "classes": ["Session", "ClassicSession"],
                "required": False
            }
            ]
           },
           "audit",
           {
             "brief": "Audit management and utilities.",
             "details": [
                 "A collection of Audit management tools and utilities"
             ]
           }
     )

register_plugin("getBinlogsIO", trx.show_binlogs_io,
           {"brief": "Prints the IO statistics of binary logs files available on the server",
             "parameters": [{
                "name": "session",
                "brief": "The session to be used on the operation.",
                "type": "object",
                "classes": ["Session", "ClassicSession"],
                "required": False
            }
            ]
           },
           "audit",
           {
             "brief": "Audit management and utilities.",
             "details": [
                 "A collection of Audit management tools and utilities"
             ]
           }
     )

register_plugin("getSlowerQuery", queries.get_queries_95_perc,
           {"brief": "Prints the slowest queries. If the limit is one you can also see all the details about the query",
             "parameters": [{
                   "name": "limit",
                   "brief": "The amount of query to return. Default is 1.",
                   "type": "integer",
                   "required": False
                },{
                   "name": "select",
                   "brief": "Returns queries only with SELECT.",
                   "type": "bool",
                   "required": False
                },{
                   "name": "schema",
                   "brief": "The name of the schema to look at.",
                   "type": "string",
                   "required": False
#                },{
#                   "name": "session",
#                   "brief": "The session to be used on the operation.",
#                   "type": "object",
#                   "classes": ["Session", "ClassicSession"],
#                   "required": False
                }
            ]
           },
           "audit",
           {
             "brief": "Audit management and utilities.",
             "details": [
                 "A collection of Audit management tools and utilities"
             ]
           }
     )


register_plugin("getQueryTempDisk", queries.get_queries_temp_disk,
           {"brief": "Prints the queries using temporary tables on disk",
             "parameters": [{
                   "name": "limit",
                   "brief": "The amount of query to return. Default is 1.",
                   "type": "integer",
                   "required": False
                },{
                   "name": "schema",
                   "brief": "The name of the schema to look at.",
                   "type": "string",
                   "required": False
                },{
                   "name": "session",
                   "brief": "The session to be used on the operation.",
                   "type": "object",
                   "classes": ["Session", "ClassicSession"],
                   "required": False
                }
            ]
           },
           "audit",
           {
             "brief": "Audit management and utilities.",
             "details": [
                 "A collection of Audit management tools and utilities"
             ]
           }
     )


register_plugin("getFullTableScanQuery", queries.get_queries_ft_scan,
           {"brief": "Prints the queries performing full table scans",
             "parameters": [{
                   "name": "limit",
                   "brief": "The amount of query to return. Default is 1.",
                   "type": "integer",
                   "required": False
                },{
                   "name": "schema",
                   "brief": "The name of the schema to look at.",
                   "type": "string",
                   "required": False
                },{
                   "name": "session",
                   "brief": "The session to be used on the operation.",
                   "type": "object",
                   "classes": ["Session", "ClassicSession"],
                   "required": False
                }
            ]
           },
           "audit",
           {
             "brief": "Audit management and utilities.",
             "details": [
                 "A collection of Audit management tools and utilities"
             ]
           }
     )

