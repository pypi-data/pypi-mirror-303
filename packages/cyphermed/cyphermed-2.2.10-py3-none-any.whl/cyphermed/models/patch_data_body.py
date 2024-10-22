from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


if TYPE_CHECKING:
    from ..models.patch_data_body_value_type_0 import PatchDataBodyValueType0


T = TypeVar("T", bound="PatchDataBody")


@_attrs_define
class PatchDataBody:
    """Update group data

    Attributes:
        unicode_1 (Union[Unset, str]): Custom unicode index 1
        unicode_2 (Union[Unset, str]): Custom unicode index 2
        unicode_3 (Union[Unset, str]): Custom unicode index 3
        unicode_4 (Union[Unset, str]): Custom unicode index 4
        unicode_5 (Union[Unset, str]): Custom unicode index 5
        unicode_6 (Union[Unset, str]): Custom unicode index 6
        unicode_7 (Union[Unset, str]): Custom unicode index 7
        unicode_8 (Union[Unset, str]): Custom unicode index 8
        unicode_9 (Union[Unset, str]): Custom unicode index 9
        unicode_10 (Union[Unset, str]): Custom unicode index 10
        number_1 (Union[Unset, float, int]): Custom number index 1
        number_2 (Union[Unset, float, int]): Custom number index 2
        value (Union['PatchDataBodyValueType0', Unset, str]): Data value to store at this path
    """

    unicode_1: Union[Unset, str] = UNSET
    unicode_2: Union[Unset, str] = UNSET
    unicode_3: Union[Unset, str] = UNSET
    unicode_4: Union[Unset, str] = UNSET
    unicode_5: Union[Unset, str] = UNSET
    unicode_6: Union[Unset, str] = UNSET
    unicode_7: Union[Unset, str] = UNSET
    unicode_8: Union[Unset, str] = UNSET
    unicode_9: Union[Unset, str] = UNSET
    unicode_10: Union[Unset, str] = UNSET
    number_1: Union[Unset, float, int] = UNSET
    number_2: Union[Unset, float, int] = UNSET
    value: Union["PatchDataBodyValueType0", Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.patch_data_body_value_type_0 import PatchDataBodyValueType0

        unicode_1 = self.unicode_1

        unicode_2 = self.unicode_2

        unicode_3 = self.unicode_3

        unicode_4 = self.unicode_4

        unicode_5 = self.unicode_5

        unicode_6 = self.unicode_6

        unicode_7 = self.unicode_7

        unicode_8 = self.unicode_8

        unicode_9 = self.unicode_9

        unicode_10 = self.unicode_10

        number_1: Union[Unset, float, int]
        if isinstance(self.number_1, Unset):
            number_1 = UNSET
        else:
            number_1 = self.number_1

        number_2: Union[Unset, float, int]
        if isinstance(self.number_2, Unset):
            number_2 = UNSET
        else:
            number_2 = self.number_2

        value: Union[Dict[str, Any], Unset, str]
        if isinstance(self.value, Unset):
            value = UNSET
        elif isinstance(self.value, PatchDataBodyValueType0):
            value = self.value.to_dict()
        else:
            value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unicode_1 is not UNSET:
            field_dict["unicode_1"] = unicode_1
        if unicode_2 is not UNSET:
            field_dict["unicode_2"] = unicode_2
        if unicode_3 is not UNSET:
            field_dict["unicode_3"] = unicode_3
        if unicode_4 is not UNSET:
            field_dict["unicode_4"] = unicode_4
        if unicode_5 is not UNSET:
            field_dict["unicode_5"] = unicode_5
        if unicode_6 is not UNSET:
            field_dict["unicode_6"] = unicode_6
        if unicode_7 is not UNSET:
            field_dict["unicode_7"] = unicode_7
        if unicode_8 is not UNSET:
            field_dict["unicode_8"] = unicode_8
        if unicode_9 is not UNSET:
            field_dict["unicode_9"] = unicode_9
        if unicode_10 is not UNSET:
            field_dict["unicode_10"] = unicode_10
        if number_1 is not UNSET:
            field_dict["number_1"] = number_1
        if number_2 is not UNSET:
            field_dict["number_2"] = number_2
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patch_data_body_value_type_0 import PatchDataBodyValueType0

        d = src_dict.copy()
        unicode_1 = d.pop("unicode_1", UNSET)

        unicode_2 = d.pop("unicode_2", UNSET)

        unicode_3 = d.pop("unicode_3", UNSET)

        unicode_4 = d.pop("unicode_4", UNSET)

        unicode_5 = d.pop("unicode_5", UNSET)

        unicode_6 = d.pop("unicode_6", UNSET)

        unicode_7 = d.pop("unicode_7", UNSET)

        unicode_8 = d.pop("unicode_8", UNSET)

        unicode_9 = d.pop("unicode_9", UNSET)

        unicode_10 = d.pop("unicode_10", UNSET)

        def _parse_number_1(data: object) -> Union[Unset, float, int]:
            if isinstance(data, Unset):
                return data
            return cast(Union[Unset, float, int], data)

        number_1 = _parse_number_1(d.pop("number_1", UNSET))

        def _parse_number_2(data: object) -> Union[Unset, float, int]:
            if isinstance(data, Unset):
                return data
            return cast(Union[Unset, float, int], data)

        number_2 = _parse_number_2(d.pop("number_2", UNSET))

        def _parse_value(data: object) -> Union["PatchDataBodyValueType0", Unset, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_0 = PatchDataBodyValueType0.from_dict(data)

                return value_type_0
            except:  # noqa: E722
                pass
            return cast(Union["PatchDataBodyValueType0", Unset, str], data)

        value = _parse_value(d.pop("value", UNSET))

        patch_data_body = cls(
            unicode_1=unicode_1,
            unicode_2=unicode_2,
            unicode_3=unicode_3,
            unicode_4=unicode_4,
            unicode_5=unicode_5,
            unicode_6=unicode_6,
            unicode_7=unicode_7,
            unicode_8=unicode_8,
            unicode_9=unicode_9,
            unicode_10=unicode_10,
            number_1=number_1,
            number_2=number_2,
            value=value,
        )

        patch_data_body.additional_properties = d
        return patch_data_body

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
