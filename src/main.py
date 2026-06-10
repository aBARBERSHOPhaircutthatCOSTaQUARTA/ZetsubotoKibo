# Zetsubo to Kibo - Main entry point
# Transform despair (zetsubo) into hope (kibo)

def transform_despair_to_hope(message):
    """Transform a message by reversing it as a metaphor for change."""
    reversed_message = message[::-1]
    return f'From despair: "{message}" → To hope: "{reversed_message}"'


if __name__ == '__main__':
    print('Welcome to Zetsubo to Kibo')
    print('Starting application...\n')
    
    # Main execution
    example_message = 'Zetsubo'
    print(transform_despair_to_hope(example_message))
