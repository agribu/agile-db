{
  "id": "/db-table",
  "additionalProperties": false,
  "type": "object",
  "properties": {
    "database": {
      "type": "string"
    },
    "table": {
      "type": "string"
    },
    "policy_setting": {
      "type": "string"
    }
  },
  "required": ["database", "table"]
}
