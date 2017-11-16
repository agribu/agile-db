const fs = require("fs");
const argv = require('yargs').argv;
const proxy = require('agile-sdk-proxy');

const project_dir = "../../../";
var db_conf = project_dir + "conf/db_conf.json";

function inputHandler() {
  if (typeof argv.conf === 'string') {
      db_conf = project_dir + argv.conf;
      proxy.configure(db_conf);
  }

  if (argv.createDatabaseTable) {
      var id, type, database, table;
      if (typeof argv.id === 'number') { id = argv.id.toString(); }
      if (typeof argv.type === 'string') { type = argv.type; }
      if (typeof argv.database === 'string') { database = argv.database; }
      if (typeof argv.table === 'string') { table = argv.table; }
      proxy.createDatabaseTable(id, type, database, table);
  }

  if (argv.createDatabaseColumn) {
      var id, type, database, table, column;
      if (typeof argv.id === 'number') { id = argv.id.toString(); }
      if (typeof argv.type === 'string') { type = argv.type; }
      if (typeof argv.database === 'string') { database = argv.database; }
      if (typeof argv.table === 'string') { table = argv.table; }
      if (typeof argv.column === 'string') { column = argv.column; }
      proxy.createDatabaseColumn(id, type, database, table, column);
  }

  if (argv.createEntity) {
      var id, type, name;
      if (typeof argv.id === 'number') { id = argv.id.toString(); }
      if (typeof argv.type === 'string') { type = argv.type; }
      if (typeof argv.name === 'string') { name = argv.name; }
      proxy.createEntity(id, type, name);
  }

  if (argv.deleteEntity) {
      var id, type;
      if (typeof argv.id === 'number') { id = argv.id.toString(); }
      if (typeof argv.type === 'string') { type = argv.type; }
      proxy.deleteEntity(id, type);
  }

  if (argv.setEntityAttribute) {
      var id, type, attr, value;
      if (typeof argv.id === 'number') { id = argv.id.toString(); }
      if (typeof argv.type === 'string') { type = argv.type; }
      if (typeof argv.attr === 'string') { attr = argv.attr; }
      if (typeof argv.value === 'string') { value = argv.value; }
      proxy.setEntityAttribute(id, type, attr, value);
  }

  if (argv.deleteEntityAttribute) {
      var id, type, attr;
      if (typeof argv.id === 'number') { id = argv.id.toString(); }
      if (typeof argv.type === 'string') { type = argv.type; }
      if (typeof argv.attr === 'string') { attr = argv.attr; }
      proxy.deleteEntityAttribute(id, type, attr);
  }

  if (argv.getEntity) {
      var id, type;
      if (typeof argv.id === 'number') { id = argv.id.toString(); }
      if (typeof argv.type === 'string') { type = argv.type; }
      proxy.getEntity(id, type);
  }

  if (argv.getEntityByType) {
      var type;
      if (typeof argv.type === 'string') { type = argv.type; }
      proxy.getEntityByType(type);
  }

}

inputHandler();

/**
 * Test functions
 * node agile-sdk-handler.js --createEntity --id 0 --type 'database' --name 'db_test' (check first if id is not used)
 * node agile-sdk-handler.js --deleteEntity --id 0 --type 'database'
 * node agile-sdk-handler.js --getEntityByType --type="database"
 * node agile-sdk-handler.js --setEntityAttribute --id 0 --type 'database' --attr user --value 'root'
 * node agile-sdk-handler.js --deleteEntityAttribute --id 0 --type 'database' --attr addres
 * node agile-sdk-handler.js --getEntity --id 0 --type 'database'
 * node agile-sdk-handler.js --getEntityByType --type 'database'
 */
