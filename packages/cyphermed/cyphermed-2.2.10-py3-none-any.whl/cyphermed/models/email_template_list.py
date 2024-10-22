from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.email_template_schema import EmailTemplateSchema


T = TypeVar("T", bound="EmailTemplateList")


@_attrs_define
class EmailTemplateList:
    """List of email templates

    Attributes:
        templates (Union[Unset, List['EmailTemplateSchema']]):
        page_count (Union[Unset, int]):
        object_count (Union[Unset, int]):
    """

    templates: Union[Unset, List["EmailTemplateSchema"]] = UNSET
    page_count: Union[Unset, int] = UNSET
    object_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        templates: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.templates, Unset):
            templates = []
            for templates_item_data in self.templates:
                templates_item = templates_item_data.to_dict()
                templates.append(templates_item)

        page_count = self.page_count

        object_count = self.object_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if templates is not UNSET:
            field_dict["templates"] = templates
        if page_count is not UNSET:
            field_dict["page_count"] = page_count
        if object_count is not UNSET:
            field_dict["object_count"] = object_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.email_template_schema import EmailTemplateSchema

        d = src_dict.copy()
        templates = []
        _templates = d.pop("templates", UNSET)
        for templates_item_data in _templates or []:
            templates_item = EmailTemplateSchema.from_dict(templates_item_data)

            templates.append(templates_item)

        page_count = d.pop("page_count", UNSET)

        object_count = d.pop("object_count", UNSET)

        email_template_list = cls(
            templates=templates,
            page_count=page_count,
            object_count=object_count,
        )

        email_template_list.additional_properties = d
        return email_template_list

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
