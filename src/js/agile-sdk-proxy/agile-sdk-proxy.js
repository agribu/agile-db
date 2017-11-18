/**
 * Documentation available: https://github.com/agribu/agile-db/wiki/AGILE-SDK-Proxy
 */

const fs = require("fs");
const stringify = require('json-stringify');
var agile;

module.exports = Proxy;

function Proxy(config) {
    agile = require('agile-sdk')(config);
}

/**
 * #######################################
 *  helper functions
 * #######################################
 */
function pretty(obj) {
    return stringify(obj, null, 2);
}

/**
 * #######################################
 *  database functions extends idm.entity
 * #######################################
 */
Proxy.prototype.createDatabaseColumn = function(id, type, database, table,  column) {
    agile.idm.entity.create(id, type, {'database':database, 'table':table, 'column':column}).then(function(result) {
        console.log(pretty(result));
    });
}

Proxy.prototype.createDatabaseTable = function(id, type, database, table) {
	agile.idm.entity.create(id, type, {'database':database, 'table':table}).then(function(result) {
        console.log(pretty(result));
	});
}

/**
 * #######################################
 *  idm.entity functions
 * #######################################
 */
Proxy.prototype.getEntityByType = function(type) {
    agile.idm.entity.getByType(type).then(function(entities) {
        console.log(pretty(entities));
    });
}

Proxy.prototype.getEntityByAttributeValue = function(attr, value) {
    agile.idm.entity.getByAttributeValue([{attributeType:attr,attributeValue:value}]).then(function(entities) {
        console.log(entities);
    });
}

Proxy.prototype.getEntityByMultiAttributeValue = function(constraints) {
    agile.idm.entity.getByAttributeValue(constraints).then(function(entities) {
        console.log(entities);
    });
}

Proxy.prototype.getEntity = function(id, type) {
	agile.idm.entity.get(id, type).then(function(result) {
        console.log(pretty(result));
	});
}

Proxy.prototype.createEntity = function(id, type, name) {
	agile.idm.entity.create(id, type, {'name':name}).then(function(result) {
        console.log(pretty(result));
	});
}

Proxy.prototype.deleteEntity = function(id, type) {
    agile.idm.entity.delete(id, type).then(function() {
        console.log('Entity removed!');
    });
}

Proxy.prototype.setEntityAttribute = function(id, type, attr, value) {
	agile.idm.entity.setAttribute({
        entityId: id,
        entityType: type,
        attributeType: attr,
        attributeValue: value,
    }).then(function(result) {
        console.log(pretty(result));
	});
}

Proxy.prototype.deleteEntityAttribute = function(id, type, attr) {
	agile.idm.entity.deleteAttribute(id, type, attr).then(function(result) {
        console.log(pretty(result));
	});
}

Proxy.prototype.getEntitiesSchema = function() {
	agile.idm.entity.getEntitiesSchema().then(function(jsonschema) {
        console.log(pretty(jsonschema));
	});
}

/**
 * #######################################
 *  idm.group functions
 * #######################################
 */
Proxy.prototype.getGroup = function(ownerid, group) {
    agile.idm.group.get(ownerid, group).then(function(result) {
        console.log(pretty(result));
    });
}

Proxy.prototype.getAllGroups = function() {
    agile.idm.group.get().then(function(groups) {
        console.log(pretty(groups));
    });
}

Proxy.prototype.createGroup = function(name) {
    agile.idm.group.create(name).then(function(group) {
        console.log(pretty(group));
    });
}

Proxy.prototype.deleteGroup = function(ownerid, name) {
    agile.idm.group.delete(ownerid, name).then(function() {
        console.log('Group removed!');
    });
}

Proxy.prototype.groupAddEntity = function(ownerid, group, entityid, type) {
    agile.idm.group.addEntity({
        owner: ownerid,
        name: group,
        entityId: entityid,
        entityType: type
    }).then(function(updated) {
        console.log(pretty(updated));
    });
}

Proxy.prototype.groupRemoveEntity = function(ownerid, group, entityid, type) {
    agile.idm.group.removeEntity({
        owner: ownerid,
        name: group,
        entityId: entityid,
        entityType: type
    }).then(function(updated) {
        console.log(pretty(updated));
    });
}

/**
 * #######################################
 *  idm.pdp functions
 * #######################################
 */
Proxy.prototype.pdpEvaluate = function(entityid, type, attr, method) {
    console.log(agile);
    agile.policies.pdp.evaluate([{
            entityId: entityid,
            entityType: type,
            field : attr,
            method : method
        }]).then(function(results) {
            console.log(results);
    });
}

/**
 * #######################################
 *  idm.pap functions
 * #######################################
 */
Proxy.prototype.papGetPolicy = function(entityid, type, attr) {
    agile.policies.pap.get({
        entityId : entityid,
        entityType: type,
        field : attr
    }).then(function(results) {
        console.log(pretty(results));
    });
}

Proxy.prototype.papSetPolicy = function(entityid, type, attr, policy) {
    agile.policies.pap.set({
        entityId : entityid,
        entityType: type,
        field : attr,
        policy : policy
    }).then(function(results) {
        console.log(pretty(results));
    });
}

Proxy.prototype.papDeletePolicy = function(entityid, type, attr) {
    agile.policies.pap.delete({
        entityId : entityid,
        entityType: type,
        field : attr
    }).then(function(results) {
        console.log(pretty(results));
    });
}
