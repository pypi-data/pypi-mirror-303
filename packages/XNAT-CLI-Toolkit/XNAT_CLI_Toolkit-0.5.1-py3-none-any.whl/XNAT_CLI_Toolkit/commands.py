def list_commands():
    """
    List all available commands in the XNAT CLI toolkit.
    """
    commands = [
        "xnat-share : Share subjects between projects.",
        "xnat-upload : Upload data to XNAT repository.",
        "xnat-list : List subjects or experiments in XNAT.",
        "xnat-prearchive : Uploads the data into the prearchive.",
        "xnat-archive : Archives the uploaded data from prearhive to a specific project.",
        "xnat-updatedemographics : Updates the demographic variables for the recently uploaded subjects.",
        "xnat-authenticate : Authenticates a new user for 1 hour."
    ]
    
    print("Available commands:")
    for command in commands:
        print(f"  - {command}")