# -*- coding: utf-8 -*-
from importlib import metadata
from importlib.metadata import version
import warnings

warnings.warn("This package has been deprecated. Please install the `jira-assistant` package instead")

__version__ = version("sharry_jira_tool")

del metadata
