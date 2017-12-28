This folder containes configuration files.

* `agile_conf.json`: Defines configuration settings for utilising the AGILE SDK that is provided by a deployed AGILE gateway. Used by `PROJECT_DIR/src/js/agile-sdk-proxy` and `PROJECT_DIR/src/js/agile-sdk-handler`.
* `db_conf.json`: Defines configuration settings for connecting to a database and building an AGILE database entitiy. The `policy_setting` attribute indicates the policy schema type that should be applied initially to an AGILE database entitiy. Used by `PROJECT_DIR/src/py/utils/mysqlc.py`, `PROJECT_DIR/src/py/agile-db.py`, `PROJECT_DIR/src/py/agile-pep.py`.
