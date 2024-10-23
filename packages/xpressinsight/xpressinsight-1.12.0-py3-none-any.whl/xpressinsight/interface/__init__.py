"""
    Xpress Insight Python package
    =============================

    This is an internal file of the 'xpressinsight' package. Do not import it directly.
    'Interface' subpackage defines interface for interacting with Insight server during execution.

    This material is the confidential, proprietary, unpublished property
    of Fair Isaac Corporation.  Receipt or possession of this material
    does not convey rights to divulge, reproduce, use, or allow others
    to use it without the specific written authorization of Fair Isaac
    Corporation and use must conform strictly to the license agreement.

    Copyright (c) 2024-2024 Fair Isaac Corporation. All rights reserved.
"""

from .interface import (
    _raise_interface_error,
    _raise_runtime_error,
    _raise_io_error,
    Attachment,
    AttachmentRules,
    AttachStatus,
    AttachTag,
    AttachTagUsage,
    AttachType,
    AttachUpdateType,
    AppInterface,
    ItemInfo,
    Metric,
    ObjSense,
    InsightContext,
    InsightDmpContext,
    SolutionDatabase,
    ResourceLimits,
    SCENARIO_DATA_CONTAINER,
    InterfaceError,
    ScenarioNotFoundError,
    InvalidEntitiesError,
)
from .interface_rest import (
    AppRestInterface
)
from .interface_test import (
    AppTestInterface,
    XpriAttachmentsCache,
    read_attach_info,
    write_attach_info
)
