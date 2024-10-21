import pandas as pd

def json_to_csv_bytes(json_data):
    """
    Converts JSON data to CSV byte array.

    Args:
        json_data (list[dict]): A list of dictionaries representing JSON data.

    Returns:
        bytes: CSV formatted data as a byte array.
    """
    # Convert JSON to DataFrame
    df = pd.DataFrame(json_data)
    
    # Create a buffer
    buffer = BytesIO()
    
    # Convert DataFrame to CSV and save it to buffer
    df.to_csv(buffer, index=False)
    buffer.seek(0)  # Rewind the buffer to the beginning
    
    # Return bytes
    return buffer.getvalue()
        
def handle_response_data(response, object_class=None, export_csv=False, export_df=False):
    """
    Processes API response data dynamically, converting it to the requested format (CSV, DataFrame, or object list/raw data).
    Returns an empty list, empty DataFrame, or empty CSV byte string when the response payload is empty.

    Args:
        response (list[dict]): The raw response data from the API.
        object_class (type, optional): The class to instantiate for each item in the response. If None, raw data will be returned.
        export_csv (bool): If True, exports data as CSV.
        export_df (bool): If True, exports data as pandas DataFrame.

    Returns:
        list[object_class] | list[dict] | bytes | pd.DataFrame: List of object instances, raw data (list of dictionaries), CSV data, 
                                                               or DataFrame depending on the export flag.
    """
    if not response:
        # Return empty objects based on export format
        if export_csv:
            return b''
        elif export_df:
            return pd.DataFrame()
        else:
            return []

    if export_csv:
        return json_to_csv_bytes(response)
    elif export_df:
        return pd.DataFrame(response)
    elif object_class:
        # Convert response to a list of object instances if an object class is provided
        return [object_class(**item) for item in response]
    else:
        # Return the raw data (list of dictionaries) if no object class is provided
        return response
