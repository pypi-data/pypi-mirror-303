from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ValidationInfo, field_validator


class PropertyOption(BaseModel):
    name: str
    color: Optional[str] = None

    def to_notion_format(self):
        data = {'name': self.name}
        if self.color is not None:
            data['color'] = self.color
        return data


class PropertyConfig(BaseModel):
    property_type: str
    options: Optional[List[PropertyOption]] = None

    @field_validator('property_type')
    def validate_property_type(cls, v, info: ValidationInfo):
        allowed_types = ['title', 'select', 'date', 'rich_text', 'number', 'multi_select', 'checkbox']
        if v not in allowed_types:
            raise ValueError(f"Unsupported property type: {v}")
        return v

    def to_notion_format(self):
        if self.property_type == "title":
            return {"title": {}}
        elif self.property_type == "select":
            return {
                "select": {
                    "options": [option.to_notion_format() for option in self.options or []]
                }
            }
        elif self.property_type == "multi_select":
            return {
                "multi_select": {
                    "options": [option.to_notion_format() for option in self.options or []]
                }
            }
        elif self.property_type == "date":
            return {"date": {}}
        elif self.property_type == "rich_text":
            return {"rich_text": {}}
        elif self.property_type == "number":
            return {"number": {}}
        elif self.property_type == "checkbox":  # Handle 'checkbox'
            return {"checkbox": {}}
        else:
            raise ValueError(f"Unsupported property type: {self.property_type}")

class SchemaConfig(BaseModel):
    title: str
    properties: Dict[str, PropertyConfig]

    def to_notion_properties(self):
        return {name: prop.to_notion_format() for name, prop in self.properties.items()}


class EntryProperty(BaseModel):
    type: str
    value: Any = None

    @field_validator('type')
    def validate_property_type(cls, v, info: ValidationInfo):
        allowed_types = ['title', 'select', 'date', 'rich_text', 'number', 'multi_select', 'checkbox']
        if v not in allowed_types:
            raise ValueError(f"Unsupported entry property type: {v}")
        return v

    @staticmethod
    def from_value(name: str, value: Any, schema_properties: Dict[str, PropertyConfig]):
        prop_config = schema_properties.get(name)
        if not prop_config:
            raise ValueError(f"Property '{name}' is not defined in the schema.")
        return EntryProperty(type=prop_config.property_type, value=value)

    def to_notion_format(self):
        if self.type == "title":
            return {
                "title": [{
                    "type": "text",
                    "text": {"content": str(self.value)}
                }]
            }
        elif self.type == "rich_text":
            return {
                "rich_text": [{
                    "type": "text",
                    "text": {"content": str(self.value)}
                }]
            }
        elif self.type == "multi_select":
            if not isinstance(self.value, list):
                raise ValueError("Value for multi_select must be a list.")
            return {
                "multi_select": [{"name": str(v)} for v in self.value]
            }
        elif self.type == "select":
            return {
                "select": {"name": str(self.value)}
            }
        elif self.type == "number":
            return {
                "number": float(self.value)
            }
        elif self.type == "date":
            return {
                "date": {"start": str(self.value)}
            }
        elif self.type == "checkbox":
            if not isinstance(self.value, bool):
                raise ValueError("Value for checkbox must be a boolean.")
            return {
                "checkbox": self.value
            }
        else:
            # Corrected error message
            raise ValueError(f"Unsupported entry property type: {self.type}")

class EntryConfig(BaseModel):
    properties: Dict[str, EntryProperty]

    def to_notion_properties(self):
        return {name: prop.to_notion_format() for name, prop in self.properties.items()}
