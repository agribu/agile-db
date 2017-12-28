This folder includes several source files for interacting with an AGILE gateway.

* `agile-db-policies.py`: Provides functions to translate schematic policies (e.g. in `PROJECT_DIR/schemes/policies`) into AGILE policies.
* `agile-db.py`: Provides functions to translate schematic entities (e.g. in `PROJECT_DIR/schemes/entities`) into database-related AGILE entities based on a configuration file for the database that should be used (e.g. `PROJECT_DIR/conf/db_conf.json`)
* `agile-pep.py`: Provides functions to enforce defined AGILE policies to defined database-related AGILE entities.
* `agile-u+g.py`: Provides functions to translate examplary entities and groups into AGILE entities and groups (e.g. in `PROJECT_DIR/examples/users`, `PROJECT_DIR/examples/groups`).
* `/conf`: Includes a main configuration file that points to the definitions of configuration settings, schemes and example structures that are places in the `PROJECT_DIR` root.
* `/utils`: Includes source files that are utilised for connecting to a database and for implementing policy enforcement in `agile_pep.py`.
* `/test`: Includes some basic tests for the provided source files.
