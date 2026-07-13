"""
Bellfre Example Agent
Configuration

Purpose:
    Central configuration for the Bellfre Calculator example.

Business Rules:
    - No provider-specific settings.
    - No API keys.
    - No application logic.
    - Controls how the example agent operates.

Future:
    Provider-specific configuration will move into the
    provider implementation (OpenAI, Claude, Ollama, etc.).
"""

import os 
from dotenv import load_dotenv

load_dotenv()


#
# Agent Information
#

AGENT_NAME = "Bellfre Calculator"
AGENT_VERSION = "0.1.0"

#
# Runtime
#

DEBUG = True

#
# Capability Configuration
#

ENABLE_CALCULATOR = True
ENABLE_REASONING = True

#
# Reasoning Configuration
#

#
# Active reasoning provider
#
# Supported providers:
#
#   mock
#   openai
#   claude
#   gemini
#   ollama
#   discovery
#

REASONING_PROVIDER = "openai"

#
# OpenAI
#

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

OPENAI_MODEL = os.getenv(
    "OPENAI_MODEL",
    "gpt-5.5"
)
#
# Claude
#

CLAUDE_MODEL = ""

CLAUDE_API_KEY = ""

#
# Gemini
#

GEMINI_MODEL = ""

GEMINI_API_KEY = ""

#
# Ollama
#

OLLAMA_URL = "http://localhost:11434"

OLLAMA_MODEL = ""

#
# Bellfre Discovery
#

DISCOVERY_NODE = ""

#
# Logging
#

LOG_ROUTING = True
LOG_CAPABILITY_SELECTION = True