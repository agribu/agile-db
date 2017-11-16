**agile-sdk-proxy.js**
* A fresh user token must be set in `agile-sdk-proxy.js`. This accounts also if the token expires.
* `$PROJECT_PATH/conf/agile_conf.json` is **not used** in `agile-sdk-proxy.js`. Instead, the values are configured manually.

**agile-sdk-handler.js**
* `$PROJECT_PATH/conf/db_conf.json` is set statically in `agile-sdk-handler.js`.
* Usage of `agile-sdk-handler.js` (outputs from `agile-sdk-proxy.js` are displayed):

``` java
/**
 * Test functions
 * node agile-sdk-handler.js --createDatabaseColumn --id '0' --type 'db-table' --database 'db_test' --table 'table_test'
 * node agile-sdk-handler.js --createDatabaseColumn --id '0' --type 'db-column' --database 'db_test' --table 'table_test' --column 'column_test'
 * node agile-sdk-handler.js --createEntity --id 0 --type 'database' --name 'db_test' (check first if id is not used)
 * node agile-sdk-handler.js --deleteEntity --id 0 --type 'database'
 * node agile-sdk-handler.js --getEntityByType --type="database"
 * node agile-sdk-handler.js --setEntityAttribute --id 0 --type 'database' --attr user --value 'root'
 * node agile-sdk-handler.js --deleteEntityAttribute --id 0 --type 'database' --attr user
 * node agile-sdk-handler.js --getEntity --id 0 --type 'database'
 * node agile-sdk-handler.js --getEntityByType --type 'database'
 */
```
