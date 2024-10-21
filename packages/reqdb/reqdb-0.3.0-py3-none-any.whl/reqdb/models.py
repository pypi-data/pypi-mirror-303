"""
Models for the ReqDB objects.
The models are used to have a proper object to work with
"""

class Base():
    """
    The base model. Does just contain the object id.
    """
    def __init__(self, id: int = None):
        """
        Constructor for the base model. Sets the id.

        :param id: Object Id. This is only needed for updates, defaults to None
        :type id: int, optional
        """
        self.id: int = id


class ExtraEntry(Base):
    """
    ExtraEntry object. Represents an ExtraEntry.

    :param Base: Base model
    :type Base: Base
    """

    def __init__(self, content: str, extraTypeId: int, requirementId: int, id: int = None):
        """
        Constructor for an ExtraEntry.

        :param content: The content of the extra entry
        :type content: str
        :param extraTypeId: Id from the ExtraType which this entry represents
        :type extraTypeId: int
        :param requirementId: The requirement id which this extra entry is mapped to
        :type requirementId: int
        :param id: Database Id of the extra entry, defaults to None
        :type id: int, optional
        """
        super().__init__(id)
        self.content: str = content
        self.extraTypeId: int = extraTypeId
        self.requirementId: int = requirementId


class ExtraType(Base):
    """
    ExtraType object. Represents an ExtraType

    :param Base: Base model
    :type Base: Base
    """
    def __init__(self, title: str, description: str, extraType: int, children: list[dict] = [], id: int = None):
        """
        Constructor for an ExtraType

        :param title: Title of the extra type
        :type title: str
        :param description: Description of the extra type
        :type description: str
        :param extraType: The extra type type: 1: Plain, 2: Markdown, 3: Labels
        :type extraType: int
        :param children: List of extra entry children, defaults to []
        :type children: list[dict], optional
        :param id: Database Id of the extra type, defaults to None
        :type id: int, optional
        """
        super().__init__(id)
        self.title: str = title
        self.description: str = description
        self.extraType: int = extraType
        self.children: list[dict] = children


class Requirement(Base):
    """
    Requirements object. Represents a requirement

    :param Base: Base model
    :type Base: Base
    """
    def __init__(self, key: str, title: str, description: str, tags: list[dict], parent: dict = None, visible: bool = True, id: int = None):
        """
        Constructor for a requirement

        :param key: Requirement key, must be unique
        :type key: str
        :param title: Title of the requirement, must be unique
        :type title: str
        :param description: Description if the requirement
        :type description: str
        :param tags: List of tags for the requirement
        :type tags: list[dict]
        :param parent: Parent topic for the requirement, defaults to None
        :type parent: dict, optional
        :param visible: Sets if the requirement is visible, defaults to True
        :type visible: bool, optional
        :param id: Database Id for the requirement, defaults to None
        :type id: int, optional
        """
        super().__init__(id)
        self.key: str = key
        self.title: str = title
        self.description: str = description
        self.visible: bool = visible
        self.tags: list = tags
        self.parent: dict = parent
        self.parentId: int = parent["id"] if parent is not None else None


class Tag(Base):
    """
    Tag object. Represents a tag

    :param Base: Base model
    :type Base: Base
    """
    def __init__(self, name: str, requirement: list[int] = [], id: int = None):
        super().__init__(id)
        self.name = name
        self.requirement = requirement


class Topic(Base):
    """
    Topic object. Represents a topic

    :param Base: Base model
    :type Base: Base
    """
    def __init__(self, key: str, title: str, description: str, parent: int = None, id: int = None):
        super().__init__(id)
        self.key: str = key
        self.title: str = title
        self.description: str = description
        self.parent: int = parent
        self.parentId: int = parent["id"] if parent is not None else None


class Catalogue(Base):
    """
    Catalogue object. Represents a catalogues

    :param Base: Base model
    :type Base: Base
    """
    def __init__(self, title: str, description: str, topics: str, id: int = None):
        super().__init__(id)
        self.title: str = title
        self.description: str = description
        self.topics: str = topics

class Comment(Base):
    """
    Comment object. Represents a comment

    :param Base: Base model
    :type Base: Base
    """
    def __init__(self, comment: str, requirementId: int, completed: bool = False):
        self.comment: str = comment
        self.requirementId: int = requirementId
        self.completed: bool = completed
