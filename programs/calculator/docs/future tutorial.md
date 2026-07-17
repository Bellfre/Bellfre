For Bellfre 1.3.0, the calculator agent becomes our reference agent, so I would keep the implementation simple and intentional:

Calculator Agent MVP Target

Current goal:

Calculator Agent
        |
        +-- Arithmetic Capability
        |       + add
        |       + subtract
        |       + multiply
        |       + divide
        |
        +-- Knowledge Capability
                + math explanations
                + history/context questions
                + LLM fallback

The immediate step is finish the non-LLM calculator core first. The LLM adapter should plug into the same capability structure afterward.

Suggested Calculator Agent Structure

Assuming our Bellfre repo structure:

/examples
    /calculator-agent
        README.md
        calculator.php
        config.php

/sdk
    /php
        /src
            Agent.php
            Capability.php
            Manifest.php

For now:

calculator-agent

is the working example.

First Implementation Layer
Calculator capability

Interface:

CalculatorCapability
{
    add($a,$b)
    subtract($a,$b)
    multiply($a,$b)
    divide($a,$b)
}

Input:

{
  "operation": "multiply",
  "values": [
    12,
    5
  ]
}

Output:

{
  "result": 60,
  "capability": "arithmetic.calculate"
}
Then Add Agent Wrapper

The agent should not know "calculator".

It should know:

"I have capabilities."

Example:

$agent = new BellfreAgent(
    "calculator-agent"
);

$agent->registerCapability(
    "arithmetic.calculate",
    new CalculatorCapability()
);

The agent receives:

User Request
      |
      v
Agent
      |
      v
Capability Match
      |
      v
Calculator
Then Add LLM Capability

Later:

$agent->registerCapability(
    "mathematics.explain",
    new LLMCapability()
);

Now:

Question:

25 * 25

routes:

arithmetic.calculate

Question:

Why did humans invent zero?

routes:

mathematics.explain
Immediate Next Step

Let's pick up exactly where the calculator currently sits.

Send me:

Current calculator agent folder tree
Current files (especially the main PHP file)
Current SDK files it already uses

I’ll map the changes into the existing structure rather than redesigning it.

For this milestone, we want incremental evolution, not another architecture rewrite.