//from https://github.com/SEDARI/ulocks
// TODO: Review isOpen, lub and le operations
// they should be able to respect type hierarchies, e.g. flow to an client
// should also allow flow of a message to its subcomponents, i.e. variables
// apis, ...

var w = require('winston');
w.level = process.env.LOG_LEVEL;

module.exports = function (Lock) {
  "use strict";

  var IsGroupMemberLock = function (lock) {
    // call the super class constructor
    Lock.call(this, lock);
  };

  IsGroupMemberLock.meta = {
    arity: 1,
    descr: "This lock is open iff the entity to which this lock is applied to is a member of a specified group",
    name: "is group member",
    args: [
      "group_name"
    ]
  }

  Lock.registerLock("isGroupMember", IsGroupMemberLock);

  IsGroupMemberLock.prototype = Object.create(Lock.prototype);

  IsGroupMemberLock.prototype.le = function (other) {
    w.debug("IsGroupMemberLock.prototype.le: " + this + " <= " + other);

    if (this.eq(other))
      return true;
    else {
      w.debug("\t====> false");
      return false;
    }
  };

  IsGroupMemberLock.prototype.copy = function () {
    var c = new IsGroupMemberLock(this);
    return c;
  }

  IsGroupMemberLock.prototype.isOpen = function (context, scope) {
    w.debug("IsGroupMemberLock.prototype.isOpen");
    if (valid(context)) {
      if (!context.isStatic) {
        if (valid(context.entity) && valid(context.entity.type)) {
            if (context.entity.data.hasOwnProperty("groups") &&
            context.entity.data.groups[0].group_name == this.args[0]) {
              // w.debug("GROUPLOCK: groups equal");
              return Promise.resolve({
                open: true,
                cond: false
              });
            } else {
              // w.debug("GROUPLOCK: groups don't equal");
              return Promise.resolve({
                open: false,
                cond: false,
                lock: this
              });
            }
        }
      } else {
        return Promise.reject(new Error("IsGroupMemberLock.prototype.isOpen not implemented for static analysis, yet"));
      }
    } else
      return Promise.reject(new Error("IsGroupMemberLock.prototype.isOpen: Context is invalid"));
  };

  IsGroupMemberLock.prototype.lub = function (lock) {
    if (this.eq(lock))
      return this;
    else {
      if (this.lock == lock.lock)
        return Lock.closedLock();
      else
        return null;
    }
  }

  function valid(o) {
    return o !== undefined && o !== null;
  }
}
