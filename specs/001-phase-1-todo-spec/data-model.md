# Data Model: Todo Application

This document defines the data entities for the Todo application as referenced in the implementation plan.

## Task Entity

Represents a single todo item in the application.

### Attributes

| Attribute   | Type    | Description                               | Constraints      |
|-------------|---------|-------------------------------------------|------------------|
| `id`        | integer | A unique numeric identifier for the task. | Required, Unique |
| `description`| string  | The text content of the task.             | Required, Not an empty string |
| `completed` | boolean | The completion status of the task.        | Required, Defaults to `false` |

### Example

```json
{
  "id": 1,
  "description": "Write the specification for the Todo app",
  "completed": true
}
```
