/**
 * Documentation available: https://github.com/Agile-IoT/agile-sdk/blob/master/DOCUMENTATION.md
 */

const fs = require("fs");
const stringify = require('json-stringify');
const agile = require('agile-sdk')({
    api: 'http://localhost:8080',
    idm: 'http://localhost:3000',
    data: 'http://localhost:1338',
    token: "kl9PkkTCanr05c72ProQCcKVbGVUv9LgwNooPofy8STisEKWygU64juNUhxHHI0Y"
});

/**
 * #######################################
 *  helper functions
 * #######################################
 */
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

/**
 * #######################################
 *  database functions extends idm.entity
 * #######################################
 */
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

/**
 * #######################################
 *  idm.entity functions
 * #######################################
 */
exports.getEntityByType = function(type) {
    agile.idm.entity.getByType(type).then(function(entities) {
        console.log(pretty(entities));
    });
}

exports.getEntityByAttributeValue = function(attr, value) {
    agile.idm.entity.getByAttributeValue([{attributeType:attr,attributeValue:value}]).then(function(entities) {
        console.log(entities);
    });
}

exports.getEntity = function(id, type) {
	agile.idm.entity.get(id, type).then(function(result) {
        console.log(pretty(result));
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

exports.getEntitiesSchema = function() {
	agile.idm.entity.getEntitiesSchema().then(function(jsonschema) {
        console.log('Entities schema:\n' + pretty(jsonschema));
	});
}

/**
 * #######################################
 *  idm.group functions
 * #######################################
 */
exports.getGroup = function(ownerid, group) {
    agile.idm.group.get(ownerid, group).then(function(result) {
        console.log('Group ' + group + ' owned by ' + ownerid + ':\n' + pretty(result));
    });
}

exports.getAllGroups = function() {
    agile.idm.group.get().then(function(groups) {
        console.log('List of all groups:\n' + pretty(groups));
    });
}

exports.createGroup = function(name) {
    agile.idm.group.create(name).then(function(group) {
        console.log('Group created:\n' + pretty(group));
    });
}

exports.deleteGroup = function(ownerid, name) {
    agile.idm.group.delete(ownerid, name).then(function() {
        console.log('Group removed:\n' + pretty(name));
    });
}

exports.groupAddEntity = function(ownerid, group, entityid, type) {
    console.log('proxy: ' + ownerid + ', ' + group + ', ' + entityid + ', ' + type);
    agile.idm.group.addEntity({
        owner: ownerid,
        name: group,
        entityId: entityid,
        entityType: type
    }).then(function(updated) {
        console.log('Group updated!\n' + pretty(updated));
    });
}

exports.groupRemoveEntity = function(ownerid, group, entityid, type) {
    agile.idm.group.removeEntity({
        owner: ownerid,
        name: group,
        entityId: entityid,
        entityType: type
    }).then(function(updated) {
        console.log('Group updated!\n' + pretty(updated));
    });
}

/**
 * #######################################
 *  idm.pdp functions
 * #######################################
 */
exports.pdpEvaluate = function(entityid, type, attr, method) {
    agile.policies.pdp.evaluate([{
            entityId: entityid,
            entityType: type,
            field : attr,
            method : method
        }]).then(function(results) {
            console.log(results);
    });
}
