from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field


if TYPE_CHECKING:
    from ..models.new_email_template_schema import NewEmailTemplateSchema


T = TypeVar("T", bound="NewEmailTemplateInfo")


@_attrs_define
class NewEmailTemplateInfo:
    """Info on one specific email template

    Attributes:
        template (NewEmailTemplateSchema): Which Template fields to include in response bodies
    """

    template: "NewEmailTemplateSchema"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        template = self.template.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "template": template,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.new_email_template_schema import NewEmailTemplateSchema

        d = src_dict.copy()
        template = NewEmailTemplateSchema.from_dict(d.pop("template"))

        new_email_template_info = cls(
            template=template,
        )

        new_email_template_info.additional_properties = d
        return new_email_template_info

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
