"db": {
  "name": [
    // the property can only be read by the user itself
    {
      op: "read",
      locks: [{
        lock: "hasType",
        args: ["/user"]
      }, {
        lock: "isOwner"
      }]
    },
    // the property can be set by the user itself
    {
      op: "write",
      locks: [{
        lock: "hasType",
        args: ["/user"]
      }, {
        lock: "isOwner"
      }]
    }
  ],
  "host": [
    // the property can only be read by the user itself
    {
      op: "read",
      locks: [{
        lock: "hasType",
        args: ["/user"]
      }, {
        lock: "isOwner"
      }]
    },
    // the property can be set by the user itself
    {
      op: "write",
      locks: [{
        lock: "hasType",
        args: ["/user"]
      }, {
        lock: "isOwner"
      }]
    }
  ],
  "port": [
    // the property can only be read by the user itself
    {
      op: "read",
      locks: [{
        lock: "hasType",
        args: ["/user"]
      }, {
        lock: "isOwner"
      }]
    },
    // the property can be set by the user itself
    {
      op: "write",
      locks: [{
        lock: "hasType",
        args: ["/user"]
      }, {
        lock: "isOwner"
      }]
    }
  ],
  "user": [
    // the property can only be read by the user itself
    {
      op: "read",
      locks: [{
        lock: "hasType",
        args: ["/user"]
      }, {
        lock: "isOwner"
      }]
    },
    // the property can be set by the user itself
    {
      op: "write",
      locks: [{
        lock: "hasType",
        args: ["/user"]
      }, {
        lock: "isOwner"
      }]
    }
  ],
  "password": [
    // the property can only be read by the user itself
    {
      op: "read",
      locks: [{
        lock: "hasType",
        args: ["/user"]
      }, {
        lock: "isOwner"
      }]
    },
    // the property can be set by the user itself
    {
      op: "write",
      locks: [{
        lock: "hasType",
        args: ["/user"]
      }, {
        lock: "isOwner"
      }]
    }
  ],
  "policy_setting": [
    // the property can only be read by the user itself
    {
      op: "read",
      locks: [{
        lock: "hasType",
        args: ["/user"]
      }, {
        lock: "isOwner"
      }]
    },
    // the property can be set by the user itself
    {
      op: "write",
      locks: [{
        lock: "hasType",
        args: ["/user"]
      }, {
        lock: "isOwner"
      }]
    }
  ]
}
