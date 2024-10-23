"""
    Xpress Insight Python package
    =============================

    This is an internal file of the 'xpressinsight' package. Do not import it directly.
    Interface base class.

    This material is the confidential, proprietary, unpublished property
    of Fair Isaac Corporation.  Receipt or possession of this material
    does not convey rights to divulge, reproduce, use, or allow others
    to use it without the specific written authorization of Fair Isaac
    Corporation and use must conform strictly to the license agreement.

    Copyright (c) 2020-2024 Fair Isaac Corporation. All rights reserved.
"""

import itertools
import os
import sys
from typing import Optional, Union, Iterable, Callable, final
from abc import ABC, abstractmethod

from .interface import AppInterface
from .. import IndexBase, Column, Param
from ..entities import EntityBase, Entity, Indexed, Manage, get_non_composed_entities
from ..entities_config import EntitiesContainer
from ..exec_mode import ExecMode
from ..scenario import InsightRestClient, BearerToken

if sys.version_info < (3, 12):
    from typing_extensions import override
else:
    from typing import override


class AppInterfaceBase(AppInterface, ABC):
    """ AppInterface implementation common to all subclasses. """

    def __init__(
            self,
            app_id: str = "",
            app_name: str = "",
            scenario_id: str = "",
            scenario_name: str = "",
            scenario_path: str = "",
            exec_mode: str = ExecMode.NONE,
            test_mode: bool = True,
            test_attach_dir: str = "",
            test_cfile_path: str = "",
            force_wdir_to_temp: Optional[bool] = None,  #
            tmp_dir: Optional[str] = None,   #
            work_dir: str = os.path.join("work_dir", "insight"),
            app=None,
    ):
        super().__init__(
            app_id=app_id,
            app_name=app_name,
            scenario_id=scenario_id,
            scenario_name=scenario_name,
            scenario_path=scenario_path,
            exec_mode=exec_mode,
            test_mode=test_mode,
            test_attach_dir=test_attach_dir,
            test_cfile_path=test_cfile_path,
            force_wdir_to_temp=force_wdir_to_temp,
            tmp_dir=tmp_dir,
            work_dir=work_dir,
            app=app
        )
        self.__input_entities_populated = False

    @override
    @final
    def populate(self,
                 entities: Union[Iterable[str], Iterable[EntityBase]] = None,
                 *,
                 entity_filter: Callable[[Entity], bool] = None,
                 fetch_individual_series: bool = False) -> None:
        #
        #
        if not self._app.app_cfg.partial_populate:
            raise RuntimeError("AppInterface.populate may only be called if the app is configured with "
                               "partial_populate=True")

        #
        exec_mode = self._app.app_cfg.get_exec_mode(self.exec_mode)
        if not exec_mode:
            raise RuntimeError("AppInterface.populate may not be called outside an execution mode")
        if exec_mode.clear_input:
            raise RuntimeError("AppInterface.populate may not be called from an execution mode where clear_input=True")

        #
        #
        self._set_inputs_populated()

        #
        entities_to_populate = self._get_and_verify_entities_to_populate(entities=entities, entity_filter=entity_filter)
        self._populate_input_entities(entities_to_populate, fetch_individual_series)

    def _get_and_verify_entities_to_populate(self,
                                            entities: Union[Iterable[str], Iterable[EntityBase]] = None,
                                            entity_filter: Callable[[Entity], bool] = None
                                            ) -> Iterable[Entity]:
        """ Given specification of entities to capture, verify the list is valid and return
            iterable of entities. """
        app: EntitiesContainer = self._app
        app_cfg = app.entities_cfg

        #
        if entities:
            entities_by_entity_name = {e.entity_name: e for e in get_non_composed_entities(app_cfg.entities)}
            for entity in entities:
                if isinstance(entity, str):
                    entity_name = entity
                    entity = app_cfg.get_entity(entity_name)
                    if entity is None:
                        if entity_name not in entities_by_entity_name:
                            raise KeyError(f'Unrecognized entity "{entity_name}".')
                        entity = entities_by_entity_name[entity_name]

                if not isinstance(entity, EntityBase):
                    raise TypeError(f'"{entity}" has type {type(entity)} when EntityBase was expected.')

                #
                if isinstance(entity, Param):
                    raise TypeError(f'Entity "{entity.name}" cannot be populated as it has type Param.')

                #
                if not entity.is_managed(Manage.INPUT):
                    raise TypeError(
                        f'Entity "{entity.name}" cannot be populated as it is not managed as input.')

        #
        # noinspection PyProtectedMember
        # pylint: disable-next=protected-access
        entities = app_cfg._get_entities(entities=entities, entity_filters=list(itertools.chain(
            [lambda e: e.is_managed(Manage.INPUT) and not isinstance(e, Param)],
            [entity_filter] if entity_filter else []
        )))

        #
        #
        #
        #
        entities = set(entities).union(itertools.chain.from_iterable(
            [entity.index for entity in entities if isinstance(entity, Indexed)]
        )).union(itertools.chain.from_iterable(
            # pylint: disable-next=protected-access
            [entity._data_frame.index for entity in entities if isinstance(entity, Column)]
        ))

        #
        #
        return sorted(entities, key=lambda e: e.entity_name)

    def _set_inputs_populated(self):
        if self.__input_entities_populated:
            raise RuntimeError("Entities may not be populated more than once per execution mode.")
        self.__input_entities_populated = True

    def _reset_inputs_populated(self):
        self.__input_entities_populated = False

    @abstractmethod
    def _populate_input_entities(self, entities: Iterable[Entity], fetch_individual_series: bool) -> None:
        """ Populate the input entities. """

    @override
    @final
    def capture(self,
                entities: Union[Iterable[str], Iterable[EntityBase]] = None,
                *,
                entity_filter: Callable[[Entity], bool] = None) -> None:
        #
        #
        exec_mode = self._app.app_cfg.get_exec_mode(self.exec_mode)
        if exec_mode and exec_mode.clear_input:
            raise RuntimeError("AppInterface.capture may not be called from an execution mode where clear_input=True")

        #
        entities_to_capture = self._get_and_verify_entities_to_capture(entities=entities, entity_filter=entity_filter)
        self._app.data_connector.set_result_entities_to_save(entities_to_capture)

        #
        self._set_result_entities_to_send_to_insight(entities_to_capture)

    def _get_and_verify_entities_to_capture(self,
                                            entities: Union[Iterable[str], Iterable[EntityBase]] = None,
                                            entity_filter: Callable[[Entity], bool] = None
                                            ) -> Iterable[Entity]:
        """ Given specification of entities to capture, verify the list is valid and return
            iterable of entities. """
        app: EntitiesContainer = self._app
        app_cfg = app.entities_cfg

        #
        if entities:
            entities_by_entity_name = {e.entity_name: e for e in get_non_composed_entities(app_cfg.entities)}
            allowed_index_entities = set(itertools.chain.from_iterable(
                [entity.index for entity in app_cfg.entities
                 if isinstance(entity, Indexed) and isinstance(entity, EntityBase) and entity.is_managed(Manage.RESULT)]
            ))

            for entity in entities:
                if isinstance(entity, str):
                    entity_name = entity
                    entity = app_cfg.get_entity(entity_name)
                    if entity is None:
                        if entity_name not in entities_by_entity_name:
                            raise KeyError(f'Unrecognized entity "{entity_name}".')
                        entity = entities_by_entity_name[entity_name]

                if not isinstance(entity, EntityBase):
                    raise TypeError(f'"{entity}" has type {type(entity)} when EntityBase was expected.')

                #
                if entity.is_managed(Manage.RESULT):
                    pass

                #
                elif isinstance(entity, IndexBase) and entity in allowed_index_entities:
                    pass

                #
                else:
                    raise TypeError(
                        f'Entity "{entity.name}" cannot be captured as it is not result or updatable input.')

        #
        # noinspection PyProtectedMember
        # pylint: disable-next=protected-access
        entities = app_cfg._get_entities(entities=entities, entity_filters=list(itertools.chain(
            [lambda e: e.is_managed(Manage.RESULT)],
            [entity_filter] if entity_filter else []
        )))

        #
        #
        #
        #
        entities = set(entities).union(itertools.chain.from_iterable(
            [entity.index for entity in entities if isinstance(entity, Indexed)]
        )).union(itertools.chain.from_iterable(
            # pylint: disable-next=protected-access
            [entity._data_frame.index for entity in entities if isinstance(entity, Column)]
        ))

        #
        #
        return sorted(entities, key=lambda e: e.entity_name)

    @abstractmethod
    def _set_result_entities_to_send_to_insight(self, entities: Iterable[Entity]):
        """ Inform mminsight of the entities to send to insight """

    @override
    def get_rest_client(self, *,
                        client_id: Optional[str] = None,
                        secret: Optional[str] = None,
                        max_retries: int = 5) -> InsightRestClient:
        #
        #
        context = self.get_insight_context()
        if context.dmp is not None and client_id is None and secret is None:
            #
            return InsightRestClient(
                context.insight_url,
                bearer_token_provider=self.__get_bearer_token_from_context,
                max_retries=max_retries
            )

        #
        return InsightRestClient(
            context.insight_url,
            client_id=client_id,
            secret=secret,
            max_retries=max_retries
        )

    def __get_bearer_token_from_context(self) -> BearerToken:
        context = self.get_insight_context()
        if not context.dmp:
            raise RuntimeError("Insight is not running in DMP")
        return BearerToken(token=context.dmp.solution_token, expires=context.dmp.solution_token_expiry_time)
