class Request:
    """
    Class that represents a request to process a file.

    Attributes:
        request_type (str): Type of the request.
        file_id (str): ID of the file to process.
        user_id (int): ID of the user who sent the request.
        duration (int): Duration of the file in seconds.
    """

    def __init__(
        self, request_type: str, file_id: str, user_id: int, duration: int
    ) -> None:
        """
        Create a new request.

        Args:
            request_type (str): Type of the request.
            file_id (str): ID of the file to process.
            user_id (int): ID of the user who sent the request.
            duration (int): Duration of the file in seconds.

        Raises:
            ValueError: If the request type is invalid.
        """
        if request_type not in ["to_note", "to_text"]:
            raise ValueError("Invalid request type.")

        self.__file_id = file_id
        self.__user_id = user_id
        self.__request_type = request_type
        self.__duration = duration

    @property
    def request_type(self) -> str:
        """
        Return the request type.

        Returns:
            str: The request type.
        """
        return self.__request_type

    @property
    def file_id(self) -> str:
        """
        Return the file ID.

        Returns:
            str: The file ID.
        """
        return self.__file_id

    @property
    def user_id(self) -> int:
        """
        Return the user ID.

        Returns:
            int: The user ID.
        """
        return self.__user_id

    @property
    def duration(self) -> int:
        """
        Return the duration of the file in seconds.

        Returns:
            int: The duration of the file in seconds.
        """
        return self.__duration
