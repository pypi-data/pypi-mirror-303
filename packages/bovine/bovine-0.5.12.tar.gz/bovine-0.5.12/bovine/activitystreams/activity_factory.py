# SPDX-FileCopyrightText: 2023 Helge
# SPDX-FileCopyrightText: 2024 helge
#
# SPDX-License-Identifier: MIT

"""

<!--
```
>>> bovine.utils.now_isoformat = lambda: '2024-09-26T18:35:42Z'

```
-->
"""

from dataclasses import dataclass, field
from typing import Optional, Set, Callable

import bovine.utils
from .utils import id_for_object


@dataclass
class Activity:
    """A dataclass representing an [ActivityStreams Activity](https://www.w3.org/TR/activitystreams-vocabulary/#activity-types).

    ```pycon
    >>> activity=Activity(
    ...  type="Like",
    ...  actor="http://actor.example",
    ... object="http://some.object.example")
    >>> activity.build()
    {'@context': 'https://www.w3.org/ns/activitystreams',
        'type': 'Like',
        'actor': 'http://actor.example',
        'object': 'http://some.object.example'}

    ```

    """

    type: str
    actor: Optional[str] = None
    followers: Optional[str] = None
    id: Optional[str] = None
    published: Optional[str] = None
    to: Set[str] = field(default_factory=set)
    cc: Set[str] = field(default_factory=set)

    name: Optional[str] = None
    summary: Optional[str] = None
    content: Optional[str] = None

    target: Optional[str] = None
    object: Optional[str] = None

    def as_public(self):
        """makes the activity public, i.e. public in to and followers in cc

        ```pycon
        >>> activity = Activity(type="Like",
        ...     actor="http://actor.example",
        ...     followers="http://actor.example/followers")
        >>> activity.as_public().build()
        {'@context': 'https://www.w3.org/ns/activitystreams',
            'type': 'Like',
            'actor': 'http://actor.example',
            'to': ['https://www.w3.org/ns/activitystreams#Public'],
            'cc': ['http://actor.example/followers']}

        ```
        """
        self.to.add("https://www.w3.org/ns/activitystreams#Public")
        if self.followers:
            self.cc.add(self.followers)
        return self

    def as_followers(self):
        """addresses the activity to followers, if they are set

        ```pycon
        >>> activity = Activity(type="Like",
        ...     actor="http://actor.example",
        ...     followers="http://actor.example/followers")
        >>> activity.as_followers().build()
        {'@context': 'https://www.w3.org/ns/activitystreams',
            'type': 'Like',
            'actor': 'http://actor.example',
            'to': ['http://actor.example/followers']}

        ```
        """
        if self.followers:
            self.to.add(self.followers)
        return self

    def as_unlisted(self):
        """makes the activity unlisted, i.e. public in cc and followers in to

        ```pycon
        >>> activity = Activity(type="Like",
        ...     actor="http://actor.example",
        ...     followers="http://actor.example/followers")
        >>> activity.as_unlisted().build()
        {'@context': 'https://www.w3.org/ns/activitystreams',
            'type': 'Like',
            'actor': 'http://actor.example',
            'to': ['http://actor.example/followers'],
            'cc': ['https://www.w3.org/ns/activitystreams#Public']}

        ```
        """
        if self.followers:
            self.to.add(self.followers)
        self.cc.add("https://www.w3.org/ns/activitystreams#Public")
        return self

    def build(self) -> dict:
        """converts the activity into a dict, that can be serialized to JSON"""
        result = {
            "@context": "https://www.w3.org/ns/activitystreams",
            "type": self.type,
            "actor": self.actor,
            "to": list(self.to),
            "cc": list(self.cc - self.to),
        }

        extra_fields = {
            "id": self.id,
            "published": self.published,
            "name": self.name,
            "summary": self.summary,
            "content": self.content,
            "target": self.target,
            "object": self.object,
        }

        if result["to"] is not None and len(result["to"]) == 0:
            del result["to"]
        if result["cc"] is not None and len(result["cc"]) == 0:
            del result["cc"]

        for key, value in extra_fields.items():
            if value:
                result[key] = value

        return result


def recipient(value):
    if isinstance(value, str):
        return {value}
    return set(value)


@dataclass
class ActivityFactory:
    """Basic factory for Activity objects.
    Can created by [BovineClient.activity_factory][bovine.BovineClient.activity_factory]

    ```pycon
    >>> activity_factory = ActivityFactory({"id": "http://actor.example"})
    >>> activity_factory.like("http://object.example").build()
    {'@context': 'https://www.w3.org/ns/activitystreams',
        'type': 'Like',
        'actor': 'http://actor.example',
        'published': '2024-09-26T18:35:42Z',
        'object': 'http://object.example'}

    ```

    By setting id_generator, one can provide a function that will automatically set the id property:

    ```pycon
    >>> activity_factory = ActivityFactory({"id": "http://actor.example"},
    ...     id_generator=lambda: "http://actor.example/id")
    >>> activity_factory.like("http://object.example").build()
    {'@context': 'https://www.w3.org/ns/activitystreams',
        'type': 'Like',
        'actor': 'http://actor.example',
        'id': 'http://actor.example/id',
        'published': '2024-09-26T18:35:42Z',
        'object': 'http://object.example'}

    ```
    """

    actor_information: dict
    id_generator: Callable[[], str] | None = None

    def _defaults_for_object(self, obj, kwargs):
        result = {
            "actor": self.actor_information.get("id", obj.get("attributedTo")),
            "object": obj,
            "cc": recipient(obj.get("cc", [])),
            "to": recipient(obj.get("to", [])),
            "published": bovine.utils.now_isoformat(),
            **kwargs,
        }
        if self.id_generator:
            result["id"] = self.id_generator()
        return result

    def create(self, obj, **kwargs):
        """Activity of type Create from Object

        ```pycon
        >>> activity_factory = ActivityFactory({"id": "http://actor.example"})
        >>> obj = {"type": "Note", "content": "hello world!", "to": "http://you.example"}
        >>> activity_factory.create(obj).build()
        {'@context': 'https://www.w3.org/ns/activitystreams',
            'type': 'Create',
            'actor': 'http://actor.example',
            'to': ['http://you.example'],
            'published': '2024-09-26T18:35:42Z',
            'object': {'type': 'Note',
                'content': 'hello world!',
                'to': 'http://you.example'}}

        ```
        """
        return Activity(
            type="Create",
            **self._defaults_for_object(obj, kwargs),
        )

    def update(self, obj, **kwargs):
        """Activity of type Update from Object"""
        return Activity(
            type="Update",
            **self._defaults_for_object(obj, kwargs),
        )

    def _base_defaults(self, kwargs):
        result = {
            "actor": self.actor_information["id"],
            "published": bovine.utils.now_isoformat(),
            **kwargs,
        }
        if self.actor_information.get("followers") and not result.get("followers"):
            result["followers"] = self.actor_information.get("followers")

        if self.id_generator:
            result["id"] = self.id_generator()

        return result

    def _defaults(self, target, kwargs):
        return {"object": target, **self._base_defaults(kwargs)}

    def like(self, target, **kwargs):
        """Like for target

        ```pycon
        >>> activity_factory = ActivityFactory({"id": "http://actor.example"})
        >>> activity_factory.like("http://object.example").build()
        {'@context': 'https://www.w3.org/ns/activitystreams',
            'type': 'Like',
            'actor': 'http://actor.example',
            'published': '2024-09-26T18:35:42Z',
            'object': 'http://object.example'}

        ```


        """
        return Activity(type="Like", **self._defaults(target, kwargs))

    def delete(self, target, **kwargs):
        """Delete for target

        ```pycon
        >>> activity_factory = ActivityFactory({"id": "http://actor.example"})
        >>> activity_factory.delete("http://bad.example", to={"http://you.example"}).build()
        {'@context': 'https://www.w3.org/ns/activitystreams',
            'type': 'Delete',
            'actor': 'http://actor.example',
            'to': ['http://you.example'],
            'published': '2024-09-26T18:35:42Z',
            'object': 'http://bad.example'}

        ```
        """
        return Activity(type="Delete", **self._defaults(target, kwargs))

    def accept(self, activity, include_activity=False, **kwargs):
        """Accept for object

        ```pycon
        >>> follow = ActivityFactory({"id":
        ...     "http://you.example"}).follow("http://actor.example",
        ...     id="http://actor.example/follow_id").build()
        >>> follow
        {'@context': 'https://www.w3.org/ns/activitystreams',
            'type': 'Follow',
            'actor': 'http://you.example',
            'to': ['http://actor.example'],
            'id': 'http://actor.example/follow_id',
            'published': '2024-09-26T18:35:42Z',
            'object': 'http://actor.example'}

        >>> activity_factory = ActivityFactory({"id": "http://actor.example"})
        >>> activity_factory.accept(follow).build()
        {'@context': 'https://www.w3.org/ns/activitystreams',
            'type': 'Accept',
            'actor': 'http://actor.example',
            'to': ['http://you.example'],
            'published': '2024-09-26T18:35:42Z',
            'object': 'http://actor.example/follow_id'}

        ```
        """

        if isinstance(activity, str):
            return Activity(type="Accept", **self._defaults(activity, kwargs))

        obj = id_for_object(activity)
        if obj is None or include_activity:
            obj = activity

        return Activity(
            type="Accept",
            **self._defaults(obj, kwargs),
            to={id_for_object(activity.get("actor"))},
        )

    def reject(self, activity, include_activity=False, **kwargs):
        """Reject for object

        ```pycon
        >>> follow = ActivityFactory({"id":
        ...     "http://you.example"}).follow("http://actor.example",
        ...     id="http://actor.example/follow_id").build()
        >>> follow
        {'@context': 'https://www.w3.org/ns/activitystreams',
            'type': 'Follow',
            'actor': 'http://you.example',
            'to': ['http://actor.example'],
            'id': 'http://actor.example/follow_id',
            'published': '2024-09-26T18:35:42Z',
            'object': 'http://actor.example'}

        >>> activity_factory = ActivityFactory({"id": "http://actor.example"})
        >>> activity_factory.reject(follow).build()
        {'@context': 'https://www.w3.org/ns/activitystreams',
            'type': 'Reject',
            'actor': 'http://actor.example',
            'to': ['http://you.example'],
            'published': '2024-09-26T18:35:42Z',
            'object': 'http://actor.example/follow_id'}

        ```
        """

        if isinstance(activity, str):
            return Activity(type="Reject", **self._defaults(activity, kwargs))

        obj = id_for_object(activity)
        if obj is None or include_activity:
            obj = activity

        return Activity(
            type="Reject",
            **self._defaults(obj, kwargs),
            to={id_for_object(activity.get("actor"))},
        )

    def announce(self, obj, **kwargs):
        """Announce for object

        ```pycon
        >>> activity_factory = ActivityFactory({"id": "http://actor.example",
        ...     "followers": "http://actor.example/followers"})
        >>> activity_factory.announce("http://object.example").as_public().build()
        {'@context': 'https://www.w3.org/ns/activitystreams',
            'type': 'Announce',
            'actor': 'http://actor.example',
            'to': ['https://www.w3.org/ns/activitystreams#Public'],
            'cc': ['http://actor.example/followers'],
            'published': '2024-09-26T18:35:42Z',
            'object': 'http://object.example'}

        ```
        """
        return Activity(
            type="Announce",
            **self._defaults(obj, kwargs),
        )

    def follow(self, obj: str | dict, **kwargs):
        """Follow for object

        ```pycon
        >>> activity_factory = ActivityFactory({"id": "http://actor.example"})
        >>> activity_factory.follow("http://you.example").build()
        {'@context': 'https://www.w3.org/ns/activitystreams',
            'type': 'Follow',
            'actor': 'http://actor.example',
            'to': ['http://you.example'],
            'published': '2024-09-26T18:35:42Z',
            'object': 'http://you.example'}

        ```

        If the object is an actor, its id is used

        ```pycon
        >>> activity_factory = ActivityFactory({"id": "http://actor.example"})
        >>> actor = {"type": "Person", "id": "http://you.example"}
        >>> activity_factory.follow(actor).build()
        {'@context': 'https://www.w3.org/ns/activitystreams',
            'type': 'Follow',
            'actor': 'http://actor.example',
            'to': ['http://you.example'],
            'published': '2024-09-26T18:35:42Z',
            'object': 'http://you.example'}

        ```


        :param obj: Object to be followed
        :param **kwargs: Passed to [Activity][bovine.activitystreams.activity_factory.Activity]'s constructor

        """

        obj = id_for_object(obj)

        return Activity(
            type="Follow",
            **self._defaults(obj, kwargs),
            to={obj},
        )

    def undo(self, activity, include_activity=False, **kwargs):
        """Undo for activity

        ```pycon
        >>> activity_factory = ActivityFactory({"id": "http://actor.example"})
        >>> follow = activity_factory.follow("http://you.example",
        ...     id="http://actor.example/follow_id").build()
        >>> activity_factory.undo(follow).build()
        {'@context': 'https://www.w3.org/ns/activitystreams',
            'type': 'Undo',
            'actor': 'http://actor.example',
            'to': ['http://you.example'],
            'published': '2024-09-26T18:35:42Z',
            'object': 'http://actor.example/follow_id'}

        ```

        If the activity doesn't have an id, it is fully included.


        ```pycon
        >>> activity_factory = ActivityFactory({"id": "http://actor.example",
        ...     "followers": "http://actor.example/followers"})
        >>> announce = activity_factory.announce("http://object.example").as_public().build()
        >>> activity_factory.undo(announce).build()
        {'@context': 'https://www.w3.org/ns/activitystreams',
            'type': 'Undo',
            'actor': 'http://actor.example',
            'to': ['https://www.w3.org/ns/activitystreams#Public'],
            'cc': ['http://actor.example/followers'],
            'published': '2024-09-26T18:35:42Z',
            'object': {'@context': 'https://www.w3.org/ns/activitystreams',
                'type': 'Announce',
                'actor': 'http://actor.example',
                'to': ['https://www.w3.org/ns/activitystreams#Public'],
                'cc': ['http://actor.example/followers'],
                'published': '2024-09-26T18:35:42Z',
                'object': 'http://object.example'}}


        ```
        """

        obj = id_for_object(activity)
        if obj is None or include_activity:
            obj = activity

        return Activity(
            type="Undo",
            **self._defaults(obj, kwargs),
            to={id_for_object(x) for x in activity.get("to", [])},
            cc={id_for_object(x) for x in activity.get("cc", [])},
        )

    def custom(self, **kwargs):
        """Allows creating a custom activity

        ```pycon
        >>> activity_factory = ActivityFactory({"id": "http://actor.example"})
        >>> activity_factory.custom(type="AnimalSound", content="moo").build()
        {'@context': 'https://www.w3.org/ns/activitystreams',
            'type': 'AnimalSound',
            'actor': 'http://actor.example',
            'published': '2024-09-26T18:35:42Z',
            'content': 'moo'}

        ```

        Or ready to send to your followers

        ```pycon
        >>> activity_factory = ActivityFactory({"id": "http://actor.example",
        ...     "followers": "http://actor.example/followers"})
        >>> activity_factory.custom(type="AnimalSound", content="moo").as_public().build()
        {'@context': 'https://www.w3.org/ns/activitystreams',
            'type': 'AnimalSound',
            'actor': 'http://actor.example',
            'to': ['https://www.w3.org/ns/activitystreams#Public'],
            'cc': ['http://actor.example/followers'],
            'published': '2024-09-26T18:35:42Z',
            'content': 'moo'}

        ```


        """

        return Activity(**self._base_defaults(kwargs))
