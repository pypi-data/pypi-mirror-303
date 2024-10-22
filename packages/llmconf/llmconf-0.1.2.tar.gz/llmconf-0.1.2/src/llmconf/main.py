from dataclasses import dataclass, fields, is_dataclass

from .confs.openai_conf import OpenAIConf
from .confs.transf_conf import TransformersConf


@dataclass(kw_only=True)
class LLMConf(OpenAIConf, TransformersConf):
    """Unified configuration for LLMs.

    - No data validation is performed.
    """

    # Shared
    system_message: str | None = None
    query: str | None = None

    def to(self, to_class: object) -> "LLMConf":
        # TODO: Will be replaced
        if not is_dataclass(to_class):
            raise ValueError(f"{to_class.__name__} is not a dataclass.")

        from_fields = {f.name: getattr(self, f.name) for f in fields(self)}
        to_fields = {f.name: from_fields[f.name] for f in fields(to_class) if f.name in from_fields}
        return LLMConf(**to_fields)

    def __repr__(self):
        out = {}
        for key, value in self.__dict__.items():
            if value is not None:
                out[key] = value
        return str(out)
