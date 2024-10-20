def get_CN_connections_by_best_methods(
    best_methods, conncetions: dict
) -> dict:
    """
    Retrieve connections limited by the number of vertices (CN_value)
    for each label.
    """
    CN_connections = {}

    for label, data in best_methods.items():
        CN_value = data[
            "number_of_vertices"
        ]  # Extract the limit for the number of vertices
        # Limit the connections for this label using CN_value
        CN_connections[label] = conncetions[label][:CN_value]

    return CN_connections
