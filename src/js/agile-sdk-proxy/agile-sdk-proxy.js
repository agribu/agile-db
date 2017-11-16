const fs = require("fs");
const stringify = require('json-stringify');
const agile = require('agile-sdk')({
    api: 'http://localhost:8080',
  	idm: 'http://localhost:3000',
  	data: 'http://localhost:1338',
  	token: "cuMQQYdMbrdSUBbWrACYQKrNouRRbWJpIParagC1eELMdZSmZYOTXyVN7mvhnoyz"
});

/**
 * @param {Object} obj - json object
 * @returns {Object} - formatted json object
 */
function pretty(obj) {
    return stringify(obj, null, 2);
}

/**
 * @param {String} db - path to db_conf.json
 * @param {String} agile - path to agile_conf.json
 */
exports.configure = function(db) {
    db_conf = JSON.parse(fs.readFileSync(db));
}

exports.createDatabaseColumn = function(id, type, database, table,  column) {
		agile.idm.entity.create(id, type, {'database':database, 'table':table, 'column':column}).then(function(result) {
		  	console.log('Database column created!\n' + pretty(result));
		});
}

exports.createDatabaseTable = function(id, type, database, table) {
		agile.idm.entity.create(id, type, {'database':database, 'table':table}).then(function(result) {
		  	console.log('Database table created!\n' + pretty(result));
		});
}

exports.createEntity = function(id, type, name) {
		agile.idm.entity.create(id, type, {'name':name}).then(function(result) {
		  	console.log('Entity created!\n' + pretty(result));
		});
}

exports.deleteEntity = function(id, type) {
	  agile.idm.entity.delete(id, type).then(function() {
	    	console.log('Entity removed!');
	  });
}

exports.setEntityAttribute = function(id, type, attr, value) {
		agile.idm.entity.setAttribute({
        entityId: id,
        entityType: type,
        attributeType: attr,
        attributeValue: value,
    }).then(function(result) {
				console.log('Entity attribute added!\n' + pretty(result));
		});
}

exports.deleteEntityAttribute = function(id, type, attr) {
		agile.idm.entity.deleteAttribute(id, type, attr).then(function(result) {
		  	console.log('Entity updated!\n' + pretty(result));
		});
}

exports.getEntity = function(id, type) {
		agile.idm.entity.get(id, type).then(function(result) {
		  	console.log(pretty(result));
		});
}

exports.getEntityByType = function(type) {
		agile.idm.entity.getByType(type).then(function(entities) {
		  	console.log(pretty(entities));
		});
}

exports.getEntitiesSchema = function() {
		agile.idm.entity.getEntitiesSchema().then(function(jsonschema) {
		  	console.log('Entities schema:\n' + pretty(jsonschema));
		});
}
