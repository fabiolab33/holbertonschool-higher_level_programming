import os

def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template and a list of attendees.
    """
    # Check input types
    if not isinstance(template, str):
        print("Error: template is not a string.")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees is not a list of dictionaries.")
        return

    # Handle empty inputs
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for i, attendee in enumerate(attendees, start=1):
        processed_template = template
        
        # Placeholders to replace
        placeholders = ["name", "event_title", "event_date", "event_location"]
        
        for key in placeholders:
            # Get value from dict or use "N/A" if key is missing or None
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            
            # Replace placeholder {key} with the value
            processed_template = processed_template.replace(f"{{{key}}}", str(value))
        
        # Generate output files
        filename = f"output_{i}.txt"
        
        # Write to file
        try:
            with open(filename, 'w') as f:
                f.write(processed_template)
        except Exception as e:
            print(f"Error writing to file {filename}: {e}")

