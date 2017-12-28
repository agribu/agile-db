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

{
  "id": "/db",
  "additionalProperties": false,
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "host": {
      "type": "string"
    },
    "port": {
      "type": "string"
    },
    "user": {
      "type": "string"
    },
    "password": {
      "type": "string"
    },
    "policy_setting": {
      "type": "string"
    }
  },
  "required": ["name"]
}
