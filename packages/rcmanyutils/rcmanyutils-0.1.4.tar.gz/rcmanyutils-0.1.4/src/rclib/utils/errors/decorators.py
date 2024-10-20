from __future__ import annotations
from functools import wraps
from typing import Any, Callable, Tuple, List, Dict
from pydantic import BaseModel
from type_lens import CallableView, TypeView, ParameterView


# Base class for contract
class Contract(BaseModel):
    name: str

    model_config = {
        "arbitrary_types_allowed": True,
    }

    def enforce(self, **kwargs) -> bool:
        pass


# Type validation rule class
class TypeRule(BaseModel):
    name: str
    types: List[TypeView]
    allow_subclasses: bool = True

    model_config = {
        "arbitrary_types_allowed": True,
    }

    def validate_base_type(self, expected_type: TypeView, value: Any) -> bool:
        """
        Validates base types like int, str, float, etc.
        Also supports subclasses if `allow_subclasses` is set to True.
        """
        value_type = TypeView(type(value))

        if expected_type.is_optional and value is None:
            return True

        if expected_type == value_type:
            return True

        if self.allow_subclasses and value_type.is_subclass_of(expected_type.raw):
            return True

        return False

    def validate_collection(self, expected_type: TypeView, value: Any) -> bool:
        """
        Recursively validates collection types like lists, sets, and tuples.
        Ensures each item in the collection matches the expected type.
        """
        if not isinstance(value, (list, set, tuple)):
            return False

        inner_types = expected_type.inner_types
        if not inner_types:
            return True  # If no inner types defined, assume any type is allowed.

        for item in value:
            if not any(self.is_valid(inner_type, item) for inner_type in inner_types):
                return False

        return True

    def validate_mapping(self, expected_type: TypeView, value: Any) -> bool:
        """
        Validates dictionaries by checking both keys and values.
        Ensures that both conform to the expected types.
        """
        if not isinstance(value, dict):
            return False

        key_type, value_type = expected_type.inner_types
        for k, v in value.items():
            if not self.is_valid(key_type, k) or not self.is_valid(value_type, v):
                return False

        return True

    def validate_union(self, expected_type: TypeView, value: Any) -> bool:
        """
        Validates Union types by checking if the value matches any of the types within the Union.
        """
        for inner_type in expected_type.inner_types:
            if self.is_valid(inner_type, value):
                return True

        return False

    def is_valid(self, expected_type: TypeView, value: Any) -> bool:
        """
        Central validation function that routes the validation to appropriate handler
        based on the type of the expected value (e.g., base type, collection, dict, etc.).
        """
        if expected_type.is_type_var:
            expected_type = TypeView(expected_type.raw.__bound__)

        if expected_type.repr_type == "Any":
            return True

        if expected_type.is_optional and value is None:
            return True

        if expected_type.is_collection and expected_type.origin in (list, set, tuple):
            return self.validate_collection(expected_type, value)

        if expected_type.is_mapping and expected_type.origin is dict:
            return self.validate_mapping(expected_type, value)

        if expected_type.is_union:
            return self.validate_union(expected_type, value)

        return self.validate_base_type(expected_type, value)


# Contract for parameter validation
class ParameterContract(Contract):
    rules: Dict[str, TypeRule]

    model_config = {
        "arbitrary_types_allowed": True,
    }

    def enforce(self, param_name: str, param_value: Any, **kwargs) -> bool:  # type: ignore
        """
        Enforces the parameter contract by validating the value against the expected types in the rules.
        """
        if param_name in self.rules:
            rule = self.rules[param_name]
            # Iterate over every allowed type in rule.types
            for allowed_type in rule.types:
                if rule.is_valid(allowed_type, param_value):
                    return True

        raise TypeError(
            f"Value {param_value} for parameter '{param_name}' does not match the contract."
        )


# Decorator for enforcing type contracts
def enforce_type_hints_contracts(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        callable_view = CallableView.from_callable(func)
        bound_args = callable_view.signature.bind(*args, **kwargs)
        bound_args.apply_defaults()  # Ensure all default values are considered

        rules = {}
        parameters: Tuple[ParameterView, ...] = callable_view.parameters
        for param in parameters:
            if param.name in bound_args.arguments:
                param_value = bound_args.arguments[param.name]
            else:
                param_value = bound_args.args[callable.parameters.index(param)]
            type_view = param.type_view
            contract_name = f"{param.name} is {type_view.repr_type}"
            rules[param.name] = TypeRule(name=contract_name, types=[type_view])

            # Validate parameter value against the rule
            if not rules[param.name].is_valid(type_view, param_value):
                raise TypeError(
                    f"Value {param_value} for parameter '{param.name}' does not match the contract {contract_name}."
                )

        return func(*args, **kwargs)

    return wrapper
