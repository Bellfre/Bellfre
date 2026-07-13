"""
Bellfre Example Agent Capability
Calculator Capability v0.3

Purpose:
    Provides deterministic arithmetic operations
    for a Bellfre agent.

Architecture:
    The calculator is a capability, not the agent itself.

    The agent decides:
        "Can this capability handle the request?"

    The calculator decides:
        "How do I execute the calculation?"

Future:
    This capability can be paired with:
        - BAT metadata
        - Capability manifests
        - Agent discovery
        - LLM-based intent routing
"""


class CalculatorCapability:
    """
    Deterministic arithmetic capability.
    """


    capability_id = "arithmetic.calculate"


    name = "Calculator Capability"


    description = (
        "Performs mathematical calculations using "
        "deterministic local execution."
    )


    def can_handle(self, request):
        """
        Determine whether this capability can process a request.
        """

        if not isinstance(request, str):
            return False


        operators = ["+", "-", "*", "/"]


        return any(
            operator in request
            for operator in operators
        )



    def execute_request(self, request):
        """
        Convert a Bellfre request into a calculation.
        """

        try:

            expression = request["input"]


            if "+" in expression:
                a, b = expression.split("+")
                return self.execute(
                    "add",
                    float(a),
                    float(b)
                )


            elif "-" in expression:
                a, b = expression.split("-")
                return self.execute(
                    "subtract",
                    float(a),
                    float(b)
                )


            elif "*" in expression:
                a, b = expression.split("*")
                return self.execute(
                    "multiply",
                    float(a),
                    float(b)
                )


            elif "/" in expression:
                a, b = expression.split("/")
                return self.execute(
                    "divide",
                    float(a),
                    float(b)
                )


            return {
                "success": False,
                "error": "Unable to parse calculation"
            }


        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }



    def execute(self, operation, a, b):
        """
        Execute deterministic calculation.
        """

        try:

            if operation == "add":
                result = a + b

            elif operation == "subtract":
                result = a - b

            elif operation == "multiply":
                result = a * b

            elif operation == "divide":

                if b == 0:
                    return {
                        "success": False,
                        "error": "Cannot divide by zero"
                    }

                result = a / b

            else:

                return {
                    "success": False,
                    "error": f"Unknown operation: {operation}"
                }


            return {
                "success": True,
                "capability": self.capability_id,
                "operation": operation,
                "input": {
                    "a": a,
                    "b": b
                },
                "result": result
            }


        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }



if __name__ == "__main__":

    calc = CalculatorCapability()

    tests = [
        "10+5",
        "10-5",
        "10*5",
        "10/5"
    ]


    for test in tests:

        print(test)

        print(
            calc.execute_request(test)
        )

        print()