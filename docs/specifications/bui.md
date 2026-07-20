BUI Format

MAJOR.PUBLISHER.PRODUCT.INSTANCE

Example:

1.000.0000.0001* SEE BELOW

Components:

Segment	Purpose	Example
Version	BUI format version	1
Publisher	Organization identifier	000
Product/Agent Family	Agent grouping	0000
Instance	Specific agent identity	0001
Examples
Bellfre examples
1.000.0000.0001

Publisher:

000 = Bellfre examples
Calculator

Current:

1.301.0304.B42.001

Problem:

This is not machine-clean.

We need to normalize it.

Possible:

1.001.0304.0001

or:

1.301.0304.0001

But we need to decide what 301 means.

Right now it is historical data, not a defined allocation.

4. Update manifest docs

The manifest spec should state:

agent:
  name:
  bui:
  version:

where:

bui:
  REQUIRED
  MUST follow Bellfre BUI specification

## re-defined as of 7-20 

My preference: lock the grammar now as fixed width.

I would lean:

N.AAAA.AAAA.AAAAA.NNNN

because the authority/org block is the one most likely to need expansion:

1.0301.0304.00B42.0001

That gives:

category: 4 chars
locale: 4 chars
authority: 5 chars
entity: 4 digits

The important thing: this belongs in the BUI specification, then AgentIdentity validation enforces it. The registry and discovery layers should remain completely unaware of the internal BUI grammar.
