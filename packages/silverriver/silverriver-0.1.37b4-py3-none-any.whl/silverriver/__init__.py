# This module defines the public API for the silverriver package.
# It provides core components for creating and interacting with
# web automation agents, including abstract interfaces and client classes.

from silverriver.client import Crux, BrowserSession
from silverriver.interfaces.base_agent import AbstractAgent
from silverriver.interfaces.chat import AgentChatInterface
from silverriver.traces.trace_impl import record_trace

__all__ = [
    "AbstractAgent",
    "AgentChatInterface",
    "Crux",
    "BrowserSession",
    "record_trace",
]
