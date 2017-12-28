/*******************************************************************************
 * Copyright (c) Benjamin Schuermann.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * which accompanies this distribution, and is available at
 * http://www.eclipse.org/legal/epl-v10.html
 *
 * Contributors:
 *     Benjamin Schuermann
 ******************************************************************************/

"db-table": {
  "database": [
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
  "table": [
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
