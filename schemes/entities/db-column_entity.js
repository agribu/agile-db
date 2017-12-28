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
  "id": "/db-column",
  "additionalProperties": false,
  "type": "object",
  "properties": {
    "database": {
      "type": "string"
    },
    "table": {
      "type": "string"
    },
    "column": {
      "type": "string"
    },
    "policy_setting": {
      "type": "string"
    }
  },
  "required": ["database", "table", "column"]
}
