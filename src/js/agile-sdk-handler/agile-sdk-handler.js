/**
 * Documentation available: https://github.com/agribu/agile-db/wiki/agile%E2%80%90sdk%E2%80%90handler.js
 */

const fs = require("fs");
const argv = require('yargs').argv;
var proxy;

function inputHandler() {
    /**
     * #######################################
     *  idm.group functions
     * #######################################
     */
    if (argv.getGroup) {
        var ownerid, group;
        if (typeof argv.ownerid === 'string') { ownerid = argv.ownerid; }
        if (typeof argv.group === 'string') { name = argv.group; }
        proxy.getGroup(ownerid, group);
    }

    if (argv.getAllGroups) {
        proxy.getAllGroups();
    }

    if (argv.createGroup) {
        var name;
        if (typeof argv.name === 'string') { name = argv.name; }
        proxy.createGroup(name);
    }

    if (argv.deleteGroup) {
        var ownerid, name;
        if (typeof argv.ownerid === 'string') { ownerid = argv.ownerid; }
        if (typeof argv.name === 'string') { name = argv.name; }
        proxy.deleteGroup(ownerid, name);
    }

    if (argv.groupAddEntity) {
        var ownerid, group, entityid, type;
        if (typeof argv.ownerid === 'string') { ownerid = argv.ownerid; }
        if (typeof argv.group === 'string') { group = argv.group; }
        if (typeof argv.entityid === 'string') { entityid = argv.entityid; }
        if (typeof argv.entityid === 'number') { entityid = argv.entityid.toString(); }
        if (typeof argv.type === 'string') { type = argv.type; }
        proxy.groupAddEntity(ownerid, group, entityid, type);
    }

    if (argv.groupRemoveEntity) {
        var ownerid, group, entityid, type;
        if (typeof argv.ownerid === 'string') { ownerid = argv.ownerid; }
        if (typeof argv.group === 'string') { group = argv.group; }
        if (typeof argv.entityid === 'string') { entityid = argv.entityid; }
        if (typeof argv.entityid === 'number') { entityid = argv.entityid.toString(); }
        if (typeof argv.type === 'string') { type = argv.type; }
        proxy.groupRemoveEntity(ownerid, group, entityid, type);
    }

    /**
     * #######################################
     *  user functions
     * #######################################
     */
    if (argv.getCurrentUserInfo) {
        proxy.getCurrentUserInfo();
    }

    if (argv.getUser) {
        var username, authtype;
        if (typeof argv.username === 'string') { username = argv.username; }
        if (typeof argv.authtype === 'string') { authtype = argv.authtype; }
        proxy.getUser(username, authtype);
    }

    if (argv.createUser) {
        var username, authtype, role, password;
        if (typeof argv.username === 'string') { username = argv.username; }
        if (typeof argv.authtype === 'string') { authtype = argv.authtype; }
        if (typeof argv.role === 'string') { role = argv.role; }
        if (typeof argv.password === 'string') { password = argv.password; }
        proxy.createUser(username, authtype, role, password);
    }

    if (argv.deleteUser) {
        var username, authtype;
        if (typeof argv.username === 'string') { username = argv.username; }
        if (typeof argv.authtype === 'string') { authtype = argv.authtype; }
        proxy.deleteUser(username, authtype);
    }

    if (argv.resetUserPassword) {
        var username, authtype, password;
        if (typeof argv.username === 'string') { username = argv.username; }
        if (typeof argv.authtype === 'string') { authtype = argv.authtype; }
        if (typeof argv.password === 'string') { password = argv.password; }
        proxy.resetUserPassword(username, authtype, password);
    }

    if (argv.updateUserPassword) {
        var oldPassword, newPassword;
        if (typeof argv.oldPassword === 'string') { oldPassword = argv.oldPassword; }
        if (typeof argv.newPassword === 'string') { newPassword = argv.newPassword; }
        proxy.updateUserPassword(oldPassword, newPassword);
    }

    /**
     * #######################################
     *  database functions extends idm.entity
     * #######################################
     */
    if (argv.createDatabaseTable) {
        var id, type, database, table;
        if (typeof argv.id === 'string') { id = argv.id; }
        if (typeof argv.id === 'number') { id = argv.id.toString(); }
        if (typeof argv.type === 'string') { type = argv.type; }
        if (typeof argv.database === 'string') { database = argv.database; }
        if (typeof argv.table === 'string') { table = argv.table; }
        proxy.createDatabaseTable(id, type, database, table);
    }

    if (argv.createDatabaseColumn) {
        var id, type, database, table, column;
        if (typeof argv.id === 'string') { id = argv.id; }
        if (typeof argv.id === 'number') { id = argv.id.toString(); }
        if (typeof argv.type === 'string') { type = argv.type; }
        if (typeof argv.database === 'string') { database = argv.database; }
        if (typeof argv.table === 'string') { table = argv.table; }
        if (typeof argv.column === 'string') { column = argv.column; }
        proxy.createDatabaseColumn(id, type, database, table, column);
    }

    /**
     * #######################################
     *  idm.entity functions
     * #######################################
     */
    if (argv.getEntityByType) {
        var type;
        if (typeof argv.type === 'string') { type = argv.type; }
        proxy.getEntityByType(type);
    }

    if (argv.getEntityByAttributeValue) {
        var attr, value;
        if (typeof argv.attr === 'string') { attr = argv.attr; }
        if (typeof argv.value === 'string') { value = argv.value; }
        proxy.getEntityByAttributeValue(attr, value);
    }

    if (argv.getEntityByMultiAttributeValue) {
        var constraints;
        if (typeof argv.constraints) {
            if (typeof argv.file === 'string') {
                constraints = JSON.parse(fs.readFileSync(argv.file));
            } else if (typeof argv.constraints === 'string') {
                constraints = JSON.parse(argv.constraints);
            }
        }
        proxy.getEntityByMultiAttributeValue(constraints);
    }

    if (argv.getEntity) {
        var id, type;
        if (typeof argv.id === 'string') { id = argv.id; }
        if (typeof argv.id === 'number') { id = argv.id.toString(); }
        if (typeof argv.type === 'string') { type = argv.type; }
        proxy.getEntity(id, type);
    }

    if (argv.createEntity) {
        var id, type, name;
        if (typeof argv.id === 'string') { id = argv.id; }
        if (typeof argv.id === 'number') { id = argv.id.toString(); }
        if (typeof argv.type === 'string') { type = argv.type; }
        if (typeof argv.name === 'string') { name = argv.name; }
        proxy.createEntity(id, type, name);
    }

    if (argv.deleteEntity) {
        var id, type;
        if (typeof argv.id === 'string') { id = argv.id; }
        if (typeof argv.id === 'number') { id = argv.id.toString(); }
        if (typeof argv.type === 'string') { type = argv.type; }
        proxy.deleteEntity(id, type);
    }

    if (argv.setEntityAttribute) {
        var id, type, attr, value;
        if (typeof argv.id === 'string') { id = argv.id; }
        if (typeof argv.id === 'number') { id = argv.id.toString(); }
        if (typeof argv.type === 'string') { type = argv.type; }
        if (typeof argv.attr === 'string') { attr = argv.attr; }
        if (typeof argv.value === 'string') { value = argv.value; }
        proxy.setEntityAttribute(id, type, attr, value);
    }

    if (argv.deleteEntityAttribute) {
        var id, type, attr;
        if (typeof argv.id === 'string') { id = argv.id; }
        if (typeof argv.id === 'number') { id = argv.id.toString(); }
        if (typeof argv.type === 'string') { type = argv.type; }
        if (typeof argv.attr === 'string') { attr = argv.attr; }
        proxy.deleteEntityAttribute(id, type, attr);
    }

    if (argv.getEntitiesSchema) {
        proxy.getEntitiesSchema();
    }

    /**
     * #######################################
     *  idm.pdp functions
     * #######################################
     */
    if (argv.pdpEvaluate) {
        var entityid, type, attr, method;
        if (typeof argv.entityid === 'string') { entityid = argv.entityid; }
        if (typeof argv.entityid === 'number') { entityid = argv.entityid.toString(); }
        if (typeof argv.type === 'string') { type = argv.type; }
        if (typeof argv.attr === 'string') { attr = argv.attr; }
        if (typeof argv.method === 'string') { method = argv.method; }
        proxy.pdpEvaluate(entityid, type, attr, method);
    }

    /**
     * #######################################
     *  idm.pap functions
     * #######################################
     */
    if (argv.papGetPolicy) {
        var entityid, type, attr;
        if (typeof argv.entityid === 'string') { entityid = argv.entityid; }
        if (typeof argv.entityid === 'number') { entityid = argv.entityid.toString(); }
        if (typeof argv.type === 'string') { type = argv.type; }
        if (typeof argv.attr === 'string') { attr = argv.attr; }
        proxy.papGetPolicy(entityid, type, attr);
    }

    if (argv.papSetPolicy) {
        var entityid, type, attr, policy;
        if (typeof argv.entityid === 'string') { entityid = argv.entityid; }
        if (typeof argv.entityid === 'number') { entityid = argv.entityid.toString(); }
        if (typeof argv.type === 'string') { type = argv.type; }
        if (typeof argv.attr === 'string') { attr = argv.attr; }
        if (typeof argv.policy) {
            if (typeof argv.file === 'string') {
                policy = JSON.parse(fs.readFileSync(argv.file));
            } else if (typeof argv.policy === 'string') {
                policy = JSON.parse(argv.policy);
            }
        }
        proxy.papSetPolicy(entityid, type, attr, policy);
    }

    if (argv.papDeletePolicy) {
        var entityid, type, attr;
        if (typeof argv.entityid === 'string') { entityid = argv.entityid; }
        if (typeof argv.entityid === 'number') { entityid = argv.entityid.toString(); }
        if (typeof argv.type === 'string') { type = argv.type; }
        if (typeof argv.attr === 'string') { attr = argv.attr; }
        proxy.papDeletePolicy(entityid, type, attr);
    }

    if (argv.idmTokenSet) {
        var token;
        if (typeof argv.token === 'string') { token = argv.token; }
        proxy.idmTokenSet(token);
    }

    if (argv.idmTokenGet) {
        proxy.idmTokenGet();
    }

    if (argv.idmTokenDelete) {
        proxy.idmTokenDelete();
    }
}

function init() {
    /**
     * #######################################
     *  helper function
     * #######################################
     */
    if (typeof argv.conf === 'string') {
        var agile_conf = argv.conf;
        var config = JSON.parse(fs.readFileSync(agile_conf));
        var Proxy = require('agile-sdk-proxy');
        proxy = new Proxy(config);
    }
}

init();
inputHandler();
