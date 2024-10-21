def get_version():
    import importlib.metadata

    try:
        # To be used in a package
        version = importlib.metadata.version('dotfile-manager-a')
    except:
        version = '0.0'

    return version
