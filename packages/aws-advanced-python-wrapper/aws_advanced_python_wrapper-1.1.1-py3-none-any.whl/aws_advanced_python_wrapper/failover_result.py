#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License").
#  You may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from __future__ import annotations

from typing import TYPE_CHECKING, Tuple

if TYPE_CHECKING:
    from aws_advanced_python_wrapper.hostinfo import HostInfo
    from aws_advanced_python_wrapper.pep249 import Connection

from dataclasses import dataclass
from typing import Optional


@dataclass
class ReaderFailoverResult:
    connection: Optional[Connection]
    is_connected: bool
    new_host: Optional[HostInfo]
    exception: Optional[Exception]


@dataclass
class WriterFailoverResult:
    is_connected: bool
    is_new_host: bool
    topology: Optional[Tuple[HostInfo, ...]]
    new_connection: Optional[Connection]
    task_name: Optional[str]
    exception: Optional[Exception]
