from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="PatchEmailTemplateBody")


@_attrs_define
class PatchEmailTemplateBody:
    """Which Template fields to include in request bodies

    Attributes:
        from_address (Union[Unset, str]): From email address to use with this template
        description (Union[Unset, str]): Description of the template
        project_id (Union[Unset, str]): ID of the project this template belongs to, if any
        is_delete_protected (Union[Unset, bool]): This must be set false before the template can be deleted
        tags (Union[Unset, List[str]]): List of tags on this template
        custom_args (Union[Unset, List[str]]): List of custom arguments on this template
        for_account_recovery (Union[Unset, bool]): If true, the template is used for forgot password emails
        for_new_users (Union[Unset, bool]): If true, the template is used for new user emails
        locale (Union[Unset, str]): Locale for the template, defaults to project or org locale
        name (Union[Unset, str]): Name of the template
        subject (Union[Unset, str]): Subject of the template
        body_txt (Union[Unset, str]): Plain text body of the template
        body_html (Union[Unset, str]): HTML body of the template
        is_active (Union[Unset, bool]): If false, all template operations are disabled
    """

    from_address: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    project_id: Union[Unset, str] = UNSET
    is_delete_protected: Union[Unset, bool] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    custom_args: Union[Unset, List[str]] = UNSET
    for_account_recovery: Union[Unset, bool] = UNSET
    for_new_users: Union[Unset, bool] = UNSET
    locale: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    subject: Union[Unset, str] = UNSET
    body_txt: Union[Unset, str] = UNSET
    body_html: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from_address = self.from_address

        description = self.description

        project_id = self.project_id

        is_delete_protected = self.is_delete_protected

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        custom_args: Union[Unset, List[str]] = UNSET
        if not isinstance(self.custom_args, Unset):
            custom_args = self.custom_args

        for_account_recovery = self.for_account_recovery

        for_new_users = self.for_new_users

        locale = self.locale

        name = self.name

        subject = self.subject

        body_txt = self.body_txt

        body_html = self.body_html

        is_active = self.is_active

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_address is not UNSET:
            field_dict["from_address"] = from_address
        if description is not UNSET:
            field_dict["description"] = description
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if is_delete_protected is not UNSET:
            field_dict["is_delete_protected"] = is_delete_protected
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_args is not UNSET:
            field_dict["custom_args"] = custom_args
        if for_account_recovery is not UNSET:
            field_dict["for_account_recovery"] = for_account_recovery
        if for_new_users is not UNSET:
            field_dict["for_new_users"] = for_new_users
        if locale is not UNSET:
            field_dict["locale"] = locale
        if name is not UNSET:
            field_dict["name"] = name
        if subject is not UNSET:
            field_dict["subject"] = subject
        if body_txt is not UNSET:
            field_dict["body_txt"] = body_txt
        if body_html is not UNSET:
            field_dict["body_html"] = body_html
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        from_address = d.pop("from_address", UNSET)

        description = d.pop("description", UNSET)

        project_id = d.pop("project_id", UNSET)

        is_delete_protected = d.pop("is_delete_protected", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        custom_args = cast(List[str], d.pop("custom_args", UNSET))

        for_account_recovery = d.pop("for_account_recovery", UNSET)

        for_new_users = d.pop("for_new_users", UNSET)

        locale = d.pop("locale", UNSET)

        name = d.pop("name", UNSET)

        subject = d.pop("subject", UNSET)

        body_txt = d.pop("body_txt", UNSET)

        body_html = d.pop("body_html", UNSET)

        is_active = d.pop("is_active", UNSET)

        patch_email_template_body = cls(
            from_address=from_address,
            description=description,
            project_id=project_id,
            is_delete_protected=is_delete_protected,
            tags=tags,
            custom_args=custom_args,
            for_account_recovery=for_account_recovery,
            for_new_users=for_new_users,
            locale=locale,
            name=name,
            subject=subject,
            body_txt=body_txt,
            body_html=body_html,
            is_active=is_active,
        )

        patch_email_template_body.additional_properties = d
        return patch_email_template_body

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
