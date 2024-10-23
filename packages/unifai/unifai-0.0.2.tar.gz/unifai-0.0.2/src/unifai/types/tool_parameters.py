from typing import Optional, Union, Sequence, Any, Literal, Mapping, Collection
from pydantic import BaseModel


ToolParameterType = Literal["object", "array", "string", "integer", "number", "boolean", "null"]
ToolParameterPyTypes = Union[str, int, float, bool, None, list[Any], dict[str, Any]]
ToolParameterExcludableKeys = Literal["description", "enum", "required", "additionalProperties", "defs", "refs"]
EXCLUDE_NONE = frozenset()

class ToolParameter(BaseModel):
    type: ToolParameterType = "string"
    name: Optional[str] = None
    description: Optional[str] = None
    enum: Optional[list[ToolParameterPyTypes]] = None
        
    def to_dict(self, exclude: Collection[ToolParameterExcludableKeys] = EXCLUDE_NONE) -> dict:
        self_dict: dict = {"type": self.type}
        if self.description and "description" not in exclude:
            self_dict["description"] = self.description
        if self.enum and "enum" not in exclude:
            self_dict["enum"] = self.enum
        return self_dict


class StringToolParameter(ToolParameter):
    type: Literal["string"] = "string"


class NumberToolParameter(ToolParameter):
    type: Literal["number"] = "number"


class IntegerToolParameter(ToolParameter):
    type: Literal["integer"] = "integer"


class BooleanToolParameter(ToolParameter):
    type: Literal["boolean"] = "boolean"


class NullToolParameter(ToolParameter):
    type: Literal["null"] = "null"

    def to_dict(self, exclude: Collection[Literal['description'] | Literal['enum'] | Literal['required'] | Literal['additionalProperties'] | Literal['defs'] | Literal['refs']] = EXCLUDE_NONE) -> dict:
        return {"type": "null"}


class RefToolParameter(ToolParameter):
    type: Literal["ref"] = "ref"
    ref: str

    def to_dict(self, exclude: Collection[ToolParameterExcludableKeys] = EXCLUDE_NONE) -> dict:
        return {"$ref": self.ref} if "ref" not in exclude else {}


class ArrayToolParameter(ToolParameter):
    type: Literal["array"] = "array"
    items: ToolParameter
    
    def to_dict(self, exclude: Collection[ToolParameterExcludableKeys] = EXCLUDE_NONE) -> dict:
        return {
            **ToolParameter.to_dict(self, exclude),
            "items": self.items.to_dict(exclude) 
        }
    

class ObjectToolParameter(ToolParameter):
    type: Literal["object"] = "object"
    properties: Mapping[str, ToolParameter]
    additionalProperties: bool = False
    defs: Optional[Mapping[str, ToolParameter]] = None

    def __init__(self, 
                 properties: Mapping[str, ToolParameter]|Sequence[ToolParameter], 
                 additionalProperties: bool = False,
                 defs: Optional[Mapping[str, ToolParameter]|Sequence[ToolParameter]] = None, 
                 **kwargs
                 ):
        kwargs["additionalProperties"] = additionalProperties
        for kw in ("properties", "defs"):
            passed_val = locals()[kw]
            if isinstance(passed_val, Mapping):
                kwargs[kw] = passed_val
                continue
            if passed_val is None:
                continue
            if isinstance(passed_val, Sequence):
                kwargs[kw] = {}
                for prop in passed_val:
                    if not prop.name:
                        raise ValueError(f"All {kw} must have a name when passed as a sequence")
                    kwargs[kw][prop.name] = prop
            else:
                raise ValueError(f"Invalid {kw} type: {passed_val}")
        
        for prop_name, prop in kwargs["properties"].items():
            if not prop.name:
                prop.name = prop_name
        
        BaseModel.__init__(self, **kwargs)
    

    def to_dict(self, exclude: Collection[ToolParameterExcludableKeys] = EXCLUDE_NONE) -> dict:
        properties = {prop_name: prop.to_dict(exclude) for prop_name, prop in self.properties.items()}
        self_dict = { 
            **ToolParameter.to_dict(self, exclude),
            "properties": properties,
        }
        if "required" not in exclude:
            self_dict["required"] = list(self.properties.keys())
        if "additionalProperties" not in exclude:
            self_dict["additionalProperties"] = self.additionalProperties
        if self.defs and "defs" not in exclude:
            self_dict["$defs"] = {name: prop.to_dict(exclude) for name, prop in self.defs.items()}
                    
        return self_dict

    
class AnyOfToolParameter(ToolParameter):
    type: Literal["anyOf"] = "anyOf"
    anyOf: list[ToolParameter]

    def __init__(self, 
                 name: Optional[str], 
                 anyOf: list[ToolParameter], 
                 description: Optional[str] = None,
                 **kwargs):
        
        for tool_parameter in anyOf:
            if not tool_parameter.name:
                tool_parameter.name = name
        
        BaseModel.__init__(self, name=name, description=description, anyOf=anyOf, **kwargs)

    def to_dict(self, exclude: Collection[ToolParameterExcludableKeys] = EXCLUDE_NONE) -> dict:
        return {
            "anyOf": [param.to_dict(exclude) for param in self.anyOf]
        }


class OptionalToolParameter(AnyOfToolParameter):
    def __init__(self, tool_parameter: ToolParameter):
        super().__init__(name=tool_parameter.name, anyOf=[tool_parameter, NullToolParameter()])
    


class ToolParameters(ObjectToolParameter):
    def __init__(self, *parameters: ToolParameter, **kwargs):
        super().__init__(properties=parameters, **kwargs)