import collections
import inspect
import logging
from collections import defaultdict
from typing import Any, Optional

import miniworlds.tools.inspection as inspection
import miniworlds.tools.actor_class_inspection as actor_class_inspection
import miniworlds.tools.keys as keys
import miniworlds.tools.method_caller as method_caller
import miniworlds.worlds.world as world_mod
import miniworlds.actors.actor as actor_mod

from miniworlds.base.exceptions import MissingActorPartsError


class EventManager:
    """Processes World Events

    * World Events which can be registered are stored `self.events` variable.
    * World Events which are registered are stored in the dict self.registered_events
    """

    actor_class_events = dict()
    actor_class_events_set = set()
    world_class_events = dict()
    "EventManager.world_class_events Predefined set of all world events"
    world_class_events_set = set()
    class_events = dict()
    class_events_set = set()
    members = set()
    registered_class_events = defaultdict()
    setup = False

    @classmethod
    def setup_event_list(cls):
        specific_key_events = []
        for key, value in keys.KEYS.items():
            specific_key_events.append("on_key_down_" + value.lower())
            specific_key_events.append("on_key_pressed_" + value.lower())
            specific_key_events.append("on_key_up_" + value.lower())
        detecting_actor_methods = []
        not_detecting_actor_methods = []
        for actor_cls in actor_class_inspection.ActorClassInspection(
            actor_mod.Actor
        ).get_subclasses_for_cls():
            detecting_actor_methods.append("on_detecting_" + actor_cls.__name__.lower())
        for actor_cls in actor_class_inspection.ActorClassInspection(
            actor_mod.Actor
        ).get_subclasses_for_cls():
            not_detecting_actor_methods.append(
                "on_not_detecting_" + actor_cls.__name__.lower()
            )

        cls.actor_class_events = {
            "mouse": [
                "on_mouse_left",
                "on_mouse_right",
                "on_mouse_middle",
                "on_mouse_motion",
                "on_mouse_left_released",
                "on_mouse_right_released",
            ],
            "clicked_on_actor": [
                "on_clicked",
                "on_clicked_left",
                "on_clicked_right",
            ],
            "mouse_over": ["on_mouse_over", "on_mouse_leave", "on_mouse_enter"],
            "key": [
                "on_key_down",
                "on_key_pressed",
                "on_key_up",
            ],
            "specific_key": specific_key_events,
            "message": ["on_message"],
            "act": ["act"],
            "setup": ["on_setup"],
            "border": [
                "on_detecting_borders",
                "on_detecting_left_border",
                "on_detecting_right_border",
                "on_detecting_top_border",
                "on_detecting_bottom_border",
            ],
            "on_the_world": [
                "on_detecting_world",
                "on_not_detecting_world",
            ],
            "on_detecting": ["on_detecting", "on_detecting_"] + detecting_actor_methods,
            "on_not_detecting": [
                "on_not_detecting",
                "on_not_detecting_",
            ]
            + not_detecting_actor_methods,
            "focus": ["on_focus", "on_focus_lost"],
        }

        cls.world_class_events = {
            "mouse": [
                "on_mouse_left",
                "on_mouse_right",
                "on_mouse_motion",
                "on_mouse_middle",
                "on_mouse_left_released",
                "on_mouse_right_released",
            ],
            "key": [
                "on_key_down",
                "on_key_pressed",
                "on_key_up",
            ],
            "specific_key": specific_key_events,
            "message": ["on_message"],
            "act": ["act"],
        }
        # Generate
        cls.fill_event_sets()

    @classmethod
    def fill_event_sets(cls):
        cls.class_events = {**cls.actor_class_events, **cls.world_class_events}
        cls.actor_class_events_set = set()
        # Iterate over all events in static dictionary cls.actor_class_event (see above)
        for key in cls.actor_class_events.keys():
            for event in cls.actor_class_events[key]:
                cls.actor_class_events_set.add(event)
        cls.world_class_events_set = set()
        for key in cls.world_class_events.keys():
            for event in cls.world_class_events[key]:
                cls.world_class_events_set.add(event)
        cls.class_events_set = set()
        for key in cls.class_events.keys():
            for event in cls.class_events[key]:
                cls.class_events_set.add(event)

    def __init__(self, world):
        self.__class__.setup_event_list()  # setup static event set/dict
        self.executed_events: set = set()
        self.world = world
        self.registered_events = defaultdict(set)
        self.__class__.members = self._get_members_for_instance(world)
        self.register_events_for_world(world)
        self.focus_actor: Optional[actor_mod.Actor] = None
        self._last_focus_actor = None

    def _get_members_for_instance(self, instance) -> set:
        """Gets all members of an instance

        Gets members from instance class and instance base classes
        """
        if instance.__class__ not in [
            actor_mod.Actor,
            world_mod.World,
        ]:
            members = {
                name
                for name, method in vars(instance.__class__).items()
                if callable(method)
            }
            member_set = set(
                [
                    member
                    for member in members
                    if member.startswith("on_") or member.startswith("act")
                ]
            )
            return member_set.union(
                self._get_members_for_classes(instance.__class__.__bases__)
            )
        else:
            return set()

    def _get_members_for_classes(self, classes) -> set:
        """Get all members for a list of classes

        called recursively in `_get_members for instance` to get all parent class members
        :param classes:
        :return:
        """
        all_members = set()
        for cls in classes:
            if cls not in [
                actor_mod.Actor,
                world_mod.World,
            ]:
                members = {
                    name for name, method in vars(cls).items() if callable(method)
                }
                member_set = set(
                    [
                        member
                        for member in members
                        if member.startswith("on_") or member.startswith("act")
                    ]
                )
                member_set.union(self._get_members_for_classes(cls.__bases__))
                all_members = all_members.union(member_set)
            else:
                all_members = set()
        return all_members

    def register_events_for_world(self, world):
        """Registers all World events."""
        for member in self._get_members_for_instance(world):
            if member in self.__class__.world_class_events_set:  # static
                self.register_event(member, world)

    def register_events_for_actor(self, actor):
        """Registers all World events."""
        for member in self._get_members_for_instance(actor):
            self.register_event(member, actor)

    def get_parent_methods(self, instance):
        parents = inspect.getmro(instance.__class__)
        methods = set()
        for parent in parents:
            if parent in [
                world_mod.World,
                actor_mod.Actor,
            ]:
                methods = methods.union(
                    {
                        method
                        for name, method in vars(parent).items()
                        if callable(method)
                    }
                )
        return methods

    def register_event(self, member, instance):
        """Register event to event manager, IF method exists in instance.

        :param member: the method to register
        :param instance: the instance the method should be registered to (e.g. a world or a actor
        """
        method = inspection.Inspection(instance).get_instance_method(member)
        if method:
            for event in self.__class__.class_events_set:
                if member == event:
                    self.registered_events[event].add(method)
                    return event, method
            # needed for detecting_CLASS_Y methods @TODO: Maybe nod needed anymore
            for event in self.__class__.class_events_set:
                if member.startswith(event):
                    self.registered_events[event].add(method)
                    return event, method
        return

    def register_message_event(self, member, instance, message):
        """Register message event to event manager.

        :param member: the method to register
        :param instance: the instance the method should be registered to (e.g. a world or a actor
        """
        member = inspection.Inspection(instance).get_instance_method(member)
        # Default for self.registered_events["message"] is set, so
        # transform this in a defaultdict
        if self.registered_events["message"] == set():
            self.registered_events["message"] = defaultdict(set)
        # Add member to dict
        if member:
            self.registered_events["message"][message].add(member)
        return

    def register_sensor_event(self, member, instance, target):
        """Register message event to event manager.

        :param member: the method to register
        :param instance: the instance the method should be registered to (e.g. a world or a actor
        """
        member = inspection.Inspection(instance).get_instance_method(member)
        # Default for self.registered_events["message"] is set, so
        # transform this in a defaultdict
        if self.registered_events["sensor"] == set():
            self.registered_events["sensor"] = defaultdict(set)
        # Add member to dict
        if member:
            self.registered_events["sensor"][target].add(member)
        return
    
    def unregister_instance(self, instance) -> collections.defaultdict:
        """unregister an instance (e.g. a Actor) from
        event manager.
        """
        unregister_methods_dict = defaultdict()
        for event, method_set in self.registered_events.items():
            # some events do not contain a set of methods but instead
            # a dictionaray, e.g. {"message_a": set(method_a, method_b, ...]
            methods = set()
            if isinstance(method_set, dict):
                for value in method_set.values():
                    methods.union(value)
                method_set = methods
            for method in method_set:
                if method.__self__ == instance:
                    unregister_methods_dict[event] = method
        for event, method in unregister_methods_dict.items():
            self.registered_events[event].remove(method)
        return unregister_methods_dict

    def act_all(self):
        registered_act_methods = self.registered_events["act"].copy()
        # acting
        for method in registered_act_methods:
            # act method
            instance = method.__self__
            if instance._is_acting:
                method_caller.call_method(method, None, False)
        del registered_act_methods

    def handle_event(self, event: str, data: Any):
        """Call specific event handlers (e.g. "on_mouse_left", "on_mouse_right", ...) for actors

        Args:
            event: A string-identifier for the event, e.g. `reset`, `setup`, `switch_world`
            data: Data for the event, e.g. the mouse-position, the pressed key, ...
        """
        if event == "setup":
            return # Setup is not handled by event manager
        if event in self.executed_events:
            return  # events shouldn't be called more than once per tick
        event = "on_" + event
        registered_event_keys = self.registered_events.keys()
        if (
            event not in registered_event_keys
            and not event.startswith("on_key_down_")
            and not event.startswith("on_key_pressed_")
            and not event.startswith("on_key_up_")
            and not event.startswith("on_mouse_left_")
            and "on_clicked_left" in registered_event_keys
            and not event.startswith("on_mouse_right_")
            and "on_clicked_right" in registered_event_keys
            and not event.startswith("on_mouse_motion")
            and "on_mouse enter" in registered_event_keys
            and not event.startswith("on_mouse_motion")
            and "on_mouse_leave" in registered_event_keys
            
        ):
            return
        # Handle different events
        self.executed_events.add(event)
        if event in [
            "on_mouse_left",
            "on_mouse_right",
            "on_mouse_left_released",
            "on_mouse_right_released",
            "on_mouse_motion",
            "on_clicked_left",
            "on_clicked_right",
            "on_mouse_leave",
        ]:
            return self.handle_mouse_event(event, data)
        if event.startswith("on_key"):
            return self.handle_key_event(event, data)
        if event == "on_message":
            return self.handle_message_event(event, data)
        if event == "on_sensor":
            return self.handle_message_event(event, data)
        # If none of the events above is triggered, handle 
        # all other events in a default way.
        registered_events = self.registered_events[event].copy()
        for method in registered_events:
            if type(data) in [list, str, tuple]:
                if type(data) == tuple and not self.world.camera.get_screen_rect().collidepoint(data):
                    return
                data = [data]
            method_caller.call_method(method, data, allow_none=False)
        registered_events.clear()
        del registered_events

    def handle_message_event(self, event, data):
        if not self.registered_events["message"] == set():
            message_methods = self.registered_events["message"][data]
            # if message_dict == set():
            #   return
            for method in message_methods:
                method_caller.call_method(method, (data,))
        else:
            message_methods = self.registered_events["on_message"]
            for method in message_methods:
                # Handle on_key_down, on_key_pressed, ....
                if event == method.__name__:
                    method_caller.call_method(method, (data,))
                                        
    def handle_key_event(self, event, data):
        key_methods = (
            self.registered_events["on_key_down"]
            .copy()
            .union(self.registered_events["on_key_up"].copy())
            .union(self.registered_events["on_key_pressed"].copy())
        )
        # collect specific items:
        specific_key_methods = set()
        for e, values in self.registered_events.items():
            if e.startswith("on_key_down_"):
                specific_key_methods = specific_key_methods.union(values)
            if e.startswith("on_key_pressed_"):
                specific_key_methods = specific_key_methods.union(values)
            if e.startswith("on_key_up_"):
                specific_key_methods = specific_key_methods.union(values)
        for method in key_methods:
            # Handle on_key_down, on_key_pressed, ....
            if event == method.__name__:
                method_caller.call_method(method, (data,))
        # Handle on_key_pressed_w, on_key_pressed_a, ....
        for method in specific_key_methods:
            if method.__name__ == event:
                method_caller.call_method(method, None)

    def handle_mouse_event(self, event, data):
        if not self.world.camera.is_in_screen(data):
            return False
        mouse_methods = set()
        for e, values in self.registered_events.items():
            if e == event:
                mouse_methods = mouse_methods.union(values)
        for method in mouse_methods:
            method_caller.call_method(method, (data,))
        # Handle additional events like clicked on actor or mouse mouse over
        if event in ["on_mouse_motion"]:
            return self.handle_mouse_over_event(event, data)
        if event in ["on_mouse_left", "on_mouse_right"]:
            self.handle_click_on_actor_event(event, data)

    def handle_mouse_over_event(self, event, data):
        if not self.world.camera.is_in_screen(data):
            return False
        pos = self.world.camera.get_global_coordinates_for_world(
            data
        )  # get global mouse pos by window
        all_mouse_over_methods = (
            self.registered_events["on_mouse_over"]
            .union(self.registered_events["on_mouse_enter"])
            .union(self.registered_events["on_mouse_leave"].copy())
        )
        mouse_over_methods = self.registered_events["on_mouse_over"]
        if not all_mouse_over_methods:
            return
        for method in all_mouse_over_methods:
            break  # get the first method
        actor = method.__self__

        if not hasattr(actor, "_mouse_over"):
            actor._mouse_over = False
        # Store state in actor._mouse over -> Call handle_mouse_enter and mouse_event methods
        is_detecting_pixel = actor.detect_pixel(pos)
        if is_detecting_pixel and not actor._mouse_over:
            self.handle_mouse_enter_event(event, data)
            actor._mouse_over = True
        elif not is_detecting_pixel and actor._mouse_over:
            self.handle_mouse_leave_event(event, data)
            actor._mouse_over = False
        elif is_detecting_pixel:
            actor._mouse_over = True
        else:
            actor._mouse_over = False
        # Handle the mouse over
        if actor._mouse_over:
            for method in mouse_over_methods:
                method_caller.call_method(method, (data,))
        del mouse_over_methods

    def handle_mouse_enter_event(self, event, data):
        mouse_over_methods = self.registered_events["on_mouse_enter"].copy()
        for method in mouse_over_methods:
            method_caller.call_method(method, (data,))

    def handle_mouse_leave_event(self, event, data):
        mouse_over_methods = self.registered_events["on_mouse_leave"].copy()
        for method in mouse_over_methods:
            method_caller.call_method(method, (data,))

    def handle_click_on_actor_event(self, event, data):
        """handles specific methods ``on_clicked_left``,``on_clicked_left``,
        which are called, if actor is detecting mouse position
        """
        pos = data
        if event == "on_mouse_left":
            on_click_methods = (
                self.registered_events["on_clicked_left"]
                .union(self.registered_events["on_clicked"])
                .copy()
            )
        elif event == "on_mouse_right":
            on_click_methods = (
                self.registered_events["on_clicked_right"]
                .union(self.registered_events["on_clicked"])
                .copy()
            )
        else:
            return
        for method in on_click_methods:
            actor = method.__self__
            try:
                if actor.detect_pixel(pos):
                    method_caller.call_method(method, (data,))
            except MissingActorPartsError:
                logging.info("Warning: Actor parts missing from: ", actor.actor_id)
        del on_click_methods
        actors = self.world.detect_actors(pos)
        self.call_focus_methods(actors)

    def set_new_focus(self, actors):
        self._last_focus_actor = self.focus_actor
        if self._last_focus_actor:
            self._last_focus_actor.has_focus = False
        if actors:
            for actor in actors:
                if actor.is_focusable:
                    self.focus_actor = actor
                    actor.has_focus = True
                    return actor
        self.focus_actor = None

    def call_focus_methods(self, actors: list):
        focus_methods = self.registered_events["on_focus"].copy()
        unfocus_methods = self.registered_events["on_focus_lost"].copy()
        self.set_new_focus(actors)
        if self.focus_actor:
            for method in focus_methods:
                if (
                    self.focus_actor == method.__self__
                    and self.focus_actor != self._last_focus_actor
                ):
                    self.focus_actor.focus = True
                    method_caller.call_method(method, None)
        for method in unfocus_methods:
            if (
                self._last_focus_actor == method.__self__
                and self.focus_actor != self._last_focus_actor
            ):
                self._last_focus_actor.focus = False
                method_caller.call_method(method, None)
