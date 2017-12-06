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
