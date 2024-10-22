from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.edit_websocket_trigger_filters_item import EditWebsocketTriggerFiltersItem


T = TypeVar("T", bound="EditWebsocketTrigger")


@_attrs_define
class EditWebsocketTrigger:
    """
    Attributes:
        url (str):
        path (str):
        script_path (str):
        is_flow (bool):
        filters (List['EditWebsocketTriggerFiltersItem']):
    """

    url: str
    path: str
    script_path: str
    is_flow: bool
    filters: List["EditWebsocketTriggerFiltersItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        path = self.path
        script_path = self.script_path
        is_flow = self.is_flow
        filters = []
        for filters_item_data in self.filters:
            filters_item = filters_item_data.to_dict()

            filters.append(filters_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "path": path,
                "script_path": script_path,
                "is_flow": is_flow,
                "filters": filters,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.edit_websocket_trigger_filters_item import EditWebsocketTriggerFiltersItem

        d = src_dict.copy()
        url = d.pop("url")

        path = d.pop("path")

        script_path = d.pop("script_path")

        is_flow = d.pop("is_flow")

        filters = []
        _filters = d.pop("filters")
        for filters_item_data in _filters:
            filters_item = EditWebsocketTriggerFiltersItem.from_dict(filters_item_data)

            filters.append(filters_item)

        edit_websocket_trigger = cls(
            url=url,
            path=path,
            script_path=script_path,
            is_flow=is_flow,
            filters=filters,
        )

        edit_websocket_trigger.additional_properties = d
        return edit_websocket_trigger

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
