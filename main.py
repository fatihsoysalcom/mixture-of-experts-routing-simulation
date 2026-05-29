import time

# --- Simulate "Experts" ---
# Each expert is a specialized function that processes specific types of input.
# In a real MoE model, these would be neural network sub-modules.

def math_expert(data):
    """
    Simulates an expert specialized in mathematical operations.
    Only activated for numerical or math-related string inputs.
    """
    print(f"  [EXPERT: Math] Processing input: '{data}'")
    try:
        if isinstance(data, (int, float)):
            result = data * 2 # Simple math operation
            print(f"  [EXPERT: Math] Doubled value: {result}")
            return result
        elif isinstance(data, str) and "sum" in data.lower():
            numbers = [int(s) for s in data.split() if s.isdigit()]
            result = sum(numbers) if numbers else 0
            print(f"  [EXPERT: Math] Summed numbers: {result}")
            return result
        else:
            print(f"  [EXPERT: Math] Cannot process non-numeric or non-sum string: '{data}'")
            return None
    except ValueError:
        print(f"  [EXPERT: Math] Error processing math input: '{data}'")
        return None

def language_expert(data):
    """
    Simulates an expert specialized in natural language processing.
    Activated for text-based inputs, especially greetings or simple queries.
    """
    print(f"  [EXPERT: Language] Processing input: '{data}'")
    if isinstance(data, str):
        data_lower = data.lower()
        if "hello" in data_lower or "hi" in data_lower:
            response = "Hello there! How can I help you today?"
        elif "how are you" in data_lower:
            response = "I'm a model, so I don't have feelings, but I'm ready to assist!"
        else:
            response = "I can help with general language queries."
        print(f"  [EXPERT: Language] Response: '{response}'")
        return response
    else:
        print(f"  [EXPERT: Language] Cannot process non-string input: '{data}'")
        return None

def general_expert(data):
    """
    Simulates a general-purpose expert, acting as a fallback for inputs
    not specifically handled by other experts.
    """
    print(f"  [EXPERT: General] Processing input: '{data}'")
    response = f"This is a general response for input: '{data}'. I'm here to assist with broad topics."
    print(f"  [EXPERT: General] Response: '{response}'")
    return response

# --- Simulate the "Router" ---
# The router determines which expert(s) are most suitable for a given input.
# In a real MoE, this would be a trainable neural network (e.g., a gating network).
# Here, it's simplified conditional logic for demonstration.

def moe_router(input_data):
    """
    The router function that directs the input to the most appropriate expert(s).
    This demonstrates the core MoE principle of sparse activation, where only
    a subset of experts are engaged for any given input.
    """
    print(f"\n[ROUTER] Receiving input: '{input_data}'")
    activated_experts = []
    output = None

    # --- MoE Routing Logic ---
    # This is where the router decides which expert(s) to activate.
    # Only the selected experts will perform computations, saving resources.
    if isinstance(input_data, (int, float)):
        print("[ROUTER] Input is numeric. Routing to Math Expert.")
        activated_experts.append("Math")
        output = math_expert(input_data)
    elif isinstance(input_data, str):
        input_lower = input_data.lower()
        if "hello" in input_lower or "hi" in input_lower or "how are you" in input_lower:
            print("[ROUTER] Input contains a greeting. Routing to Language Expert.")
            activated_experts.append("Language")
            output = language_expert(input_data)
        elif "calculate" in input_lower or "sum" in input_lower or any(char.isdigit() for char in input_data):
            print("[ROUTER] Input contains numbers or math keywords. Routing to Math Expert.")
            activated_experts.append("Math")
            output = math_expert(input_data)
        else:
            print("[ROUTER] Input is general text. Routing to General Expert.")
            activated_experts.append("General")
            output = general_expert(input_data)
    else:
        print("[ROUTER] Input type not recognized. Routing to General Expert.")
        activated_experts.append("General")
        output = general_expert(input_data)
    # --- End MoE Routing Logic ---

    print(f"[ROUTER] Experts activated for this input: {', '.join(activated_experts) if activated_experts else 'None'}")
    print(f"[ROUTER] Final output: {output}")
    return output

# --- Main Demonstration ---
if __name__ == "__main__":
    print("--- Mixture-of-Experts (MoE) Simulation ---")
    print("This example demonstrates how a 'router' directs inputs to specialized 'experts',")
    print("activating only a subset of the model for each query, reducing computational cost.")

    test_inputs = [
        10, # Numeric input
        "Hello, how are you?", # Greeting input
        "Please calculate the sum of 5 and 12.", # Math-related string input
        "What is the capital of France?", # General language query
        "Hi there!", # Another greeting
        3.14, # Floating point numeric input
        "Tell me something interesting." # Another general language query
    ]

    for i, input_val in enumerate(test_inputs):
        print(f"\n--- Processing Test Input {i+1}/{len(test_inputs)} ---")
        moe_router(input_val)
        time.sleep(0.5) # Small delay for readability

    print("\n--- MoE Simulation Complete ---")
