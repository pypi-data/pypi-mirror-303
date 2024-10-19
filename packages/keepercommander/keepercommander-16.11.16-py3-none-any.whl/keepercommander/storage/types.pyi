from typing import Optional, TypeVar, Iterable, Generic, Tuple, Union

T = TypeVar('T')

class IRecordStorage(Generic[T]):
    def load(self) -> Optional[T]: ...
    def store(self, record: T) -> None: ...
    def delete(self) -> None: ...

class IUid:
    def uid(self) -> str: ...

U = TypeVar('U', bound=IUid)

class IEntityStorage(Generic[U]):
    def get_entity(self, uid: str) -> Optional[U]:  ...
    def get_all(self) -> Iterable[U]: ...
    def put_entities(self, entities: Iterable[U]) -> None:  ...
    def delete_uids(self, uids: Iterable[str]) -> None: ...

class IUidLink:
    def subject_uid(self) -> str: ...
    def object_uid(self) -> str: ...

L = TypeVar('L', bound=IUidLink)

class ILinkStorage(Generic[L]):
    def put_links(self, links: Iterable[L]) -> None: ...
    def delete_links(self, links: Iterable[Union[Tuple[str, str], IUidLink]]) -> None: ...
    def delete_links_for_subjects(self, subject_uids: Iterable[str]) -> None: ...
    def delete_links_for_objects(self, object_uids: Iterable[str]) -> None: ...
    def get_links_for_subject(self, subject_uid: str) -> Iterable[L]: ...
    def get_links_for_object(self, object_uid: str) -> Iterable[L]: ...
    def get_all_links(self) -> Iterable[L]: ...

class UidLink(IUidLink):
    def __init__(self, subject_uid: str, object_uid: str): ...
