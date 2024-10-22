import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset


T = TypeVar("T", bound="EmailTemplateSchema")


@_attrs_define
class EmailTemplateSchema:
    """Which Template fields to include in response bodies

    Attributes:
        id (str): ID of the template
        is_delete_protected (bool): This must be set false before the template can be deleted
        is_active (bool): If false, all template operations are disabled
        created_date (datetime.datetime): Date and time the template was created
        created_by (str): ID of the user who created the template
        tags (List[str]): List of tags on this template
        name (str): Name of the template
        subject (str): Subject of the template
        body_txt (str): Plain text body of the template
        body_html (str): HTML body of the template
        locale (str): Locale for the template
        custom_args (List[str]): List of custom arguments on this template
        for_account_recovery (bool): If true, the template is used for forgot password emails
        for_new_users (bool): If true, the template is used for new user emails
        last_updated_by (Union[Unset, str]): ID of the user who last updated the template
        last_updated_date (Union[Unset, datetime.datetime]): Date and time the template was last updated
        from_address (Union[Unset, str]): From email address to use with this template
        description (Union[Unset, str]): Description of the template
        project_id (Union[Unset, str]): ID of the project this template belongs to, if any
    """

    id: str
    is_delete_protected: bool
    is_active: bool
    created_date: datetime.datetime
    created_by: str
    tags: List[str]
    name: str
    subject: str
    body_txt: str
    body_html: str
    locale: str
    custom_args: List[str]
    for_account_recovery: bool
    for_new_users: bool
    last_updated_by: Union[Unset, str] = UNSET
    last_updated_date: Union[Unset, datetime.datetime] = UNSET
    from_address: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    project_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        is_delete_protected = self.is_delete_protected

        is_active = self.is_active

        created_date = self.created_date.isoformat()

        created_by = self.created_by

        tags = self.tags

        name = self.name

        subject = self.subject

        body_txt = self.body_txt

        body_html = self.body_html

        locale = self.locale

        custom_args = self.custom_args

        for_account_recovery = self.for_account_recovery

        for_new_users = self.for_new_users

        last_updated_by = self.last_updated_by

        last_updated_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated_date, Unset):
            last_updated_date = self.last_updated_date.isoformat()

        from_address = self.from_address

        description = self.description

        project_id = self.project_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "is_delete_protected": is_delete_protected,
                "is_active": is_active,
                "created_date": created_date,
                "created_by": created_by,
                "tags": tags,
                "name": name,
                "subject": subject,
                "body_txt": body_txt,
                "body_html": body_html,
                "locale": locale,
                "custom_args": custom_args,
                "for_account_recovery": for_account_recovery,
                "for_new_users": for_new_users,
            }
        )
        if last_updated_by is not UNSET:
            field_dict["last_updated_by"] = last_updated_by
        if last_updated_date is not UNSET:
            field_dict["last_updated_date"] = last_updated_date
        if from_address is not UNSET:
            field_dict["from_address"] = from_address
        if description is not UNSET:
            field_dict["description"] = description
        if project_id is not UNSET:
            field_dict["project_id"] = project_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        is_delete_protected = d.pop("is_delete_protected")

        is_active = d.pop("is_active")

        created_date = isoparse(d.pop("created_date"))

        created_by = d.pop("created_by")

        tags = cast(List[str], d.pop("tags"))

        name = d.pop("name")

        subject = d.pop("subject")

        body_txt = d.pop("body_txt")

        body_html = d.pop("body_html")

        locale = d.pop("locale")

        custom_args = cast(List[str], d.pop("custom_args"))

        for_account_recovery = d.pop("for_account_recovery")

        for_new_users = d.pop("for_new_users")

        last_updated_by = d.pop("last_updated_by", UNSET)

        _last_updated_date = d.pop("last_updated_date", UNSET)
        last_updated_date: Union[Unset, datetime.datetime]
        if isinstance(_last_updated_date, Unset):
            last_updated_date = UNSET
        else:
            last_updated_date = isoparse(_last_updated_date)

        from_address = d.pop("from_address", UNSET)

        description = d.pop("description", UNSET)

        project_id = d.pop("project_id", UNSET)

        email_template_schema = cls(
            id=id,
            is_delete_protected=is_delete_protected,
            is_active=is_active,
            created_date=created_date,
            created_by=created_by,
            tags=tags,
            name=name,
            subject=subject,
            body_txt=body_txt,
            body_html=body_html,
            locale=locale,
            custom_args=custom_args,
            for_account_recovery=for_account_recovery,
            for_new_users=for_new_users,
            last_updated_by=last_updated_by,
            last_updated_date=last_updated_date,
            from_address=from_address,
            description=description,
            project_id=project_id,
        )

        email_template_schema.additional_properties = d
        return email_template_schema

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
