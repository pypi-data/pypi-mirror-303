import aiohttp
from datetime import datetime, timedelta
from typing import Optional, List, Dict

from .const import (
  SL_TRANSPORT_URL,
  SL_DEVIATIONS_URL,
  SL_ROUTE_PLANNER_URL 
)

# Custom exceptions for API errors
class APIError(Exception):
    """Base class for other exceptions"""
    pass

class BadRequestError(APIError):
    """Raised when a 400 Bad Request error occurs"""
    pass

class UnauthorizedError(APIError):
    """Raised when a 401 Unauthorized error occurs"""
    pass

class ForbiddenError(APIError):
    """Raised when a 403 Forbidden error occurs"""
    pass

class NotFoundError(APIError):
    """Raised when a 404 Not Found error occurs"""
    pass

class MethodNotAllowedError(APIError):
    """Raised when a 405 Method Not Allowed error occurs"""
    pass

class NotAcceptableError(APIError):
    """Raised when a 406 Not Acceptable error occurs"""
    pass

class UnsupportedMediaTypeError(APIError):
    """Raised when a 415 Unsupported Media Type error occurs"""
    pass

class TooManyRequestsError(APIError):
    """Raised when a 429 Too Many Requests error occurs"""
    pass

class InternalServerError(APIError):
    """Raised when a 500 Internal Server Error occurs"""
    pass

class NotImplementedError(APIError):
    """Raised when a 501 Not Implemented error occurs"""
    pass

class BadGatewayError(APIError):
    """Raised when a 502 Bad Gateway error occurs"""
    pass

class ServiceUnavailableError(APIError):
    """Raised when a 503 Service Unavailable error occurs"""
    pass

class GatewayTimeoutError(APIError):
    """Raised when a 504 Gateway Timeout error occurs"""
    pass

class SLAPIClient:
    def __init__(self, journey_planner_key: str, cache_duration_minutes: int = 60):
        self.journey_planner_key = journey_planner_key
        self.session = aiohttp.ClientSession()

        # Cache and cache expiry settings for sites and lines
        self.cache_duration = timedelta(minutes=cache_duration_minutes)
        self._sites_cache = None
        self._sites_cache_time = None
        self._lines_cache: Dict[int, dict] = {}
        self._lines_cache_time: Dict[int, datetime] = {}

    def calculate_time_from_now(self, minute_offset: int) -> (str, str):
        """
        Calculate the date and time based on the given minute offset from now,
        and return them as separate strings in the formats 'YYYY-MM-DD' and 'HH:MM'.

        :param minute_offset: The number of minutes to offset from the current time.
                            Positive value for future, negative for past.
        :return: A tuple with formatted date and time strings.
        """
        now = datetime.now()  # Current time in UTC
        new_time = now + timedelta(minutes=minute_offset)  # Calculate new time

        formatted_date = new_time.strftime('%Y-%m-%d')  # Format date as 'YYYY-MM-DD'
        formatted_time = new_time.strftime('%H:%M')     # Format time as 'HH:MM'
        
        return formatted_date, formatted_time
        
    def _is_cache_valid(self, cache_time: Optional[datetime]) -> bool:
        """Check if the cache is still valid based on the cache time."""
        if cache_time is None:
            return False
        return datetime.utcnow() - cache_time < self.cache_duration
    
    async def _handle_response(self, response):
        """Handles HTTP responses and raises exceptions based on status codes."""
        if response.status == 400:
            raise BadRequestError("Bad request: Check your parameters.")
        elif response.status == 401:
            raise UnauthorizedError("Unauthorized: Check your API key.")
        elif response.status == 403:
            raise ForbiddenError("Forbidden: Access denied.")
        elif response.status == 404:
            raise NotFoundError("Not found: The requested resource was not found.")
        elif response.status == 405:
            raise MethodNotAllowedError("Method not allowed: Check the HTTP method.")
        elif response.status == 406:
            raise NotAcceptableError("Not acceptable: The requested resource is not available in the requested format.")
        elif response.status == 415:
            raise UnsupportedMediaTypeError("Unsupported media type: Check the request content type.")
        elif response.status == 429:
            raise TooManyRequestsError("Too many requests: You are being rate-limited.")
        elif response.status == 500:
            raise InternalServerError("Internal server error: Something went wrong on the server.")
        elif response.status == 501:
            raise NotImplementedError("Not implemented: The requested method is not implemented.")
        elif response.status == 502:
            raise BadGatewayError("Bad gateway: Received an invalid response from the upstream server.")
        elif response.status == 503:
            raise ServiceUnavailableError("Service unavailable: The server is currently unable to handle the request.")
        elif response.status == 504:
            raise GatewayTimeoutError("Gateway timeout: The server did not receive a timely response.")
        else:
            response.raise_for_status()  # Raise for any other status codes

    async def fetch(self, url, params=None):
        """
        Fetches data from the given URL with optional query parameters.

        :param url: The URL to fetch.
        :param params: A dictionary of query parameters to be sent with the request.
        """
        # Print the URL and all the parameters being sent
        # print(f"Requesting URL: {url}")
        # if params:
        #     print("Parameters:")
        #     for key, value in params.items():
        #         print(f"  {key}: {value}")

        async with self.session.get(url, params=params) as response:
            await self._handle_response(response)  # Handle errors
            return await response.json()

    
    async def get_lines(self, transport_authority_id: int):
        """
        Fetches lines for a specific transport authority, uses cache if not older than cache duration.

        :param transport_authority_id: The ID of the transport authority to fetch lines for.
        """
        # Check if cache for this transport_authority_id is valid
        if self._is_cache_valid(self._lines_cache_time.get(transport_authority_id)):
            return self._lines_cache.get(transport_authority_id)

        # Make request to API if cache is invalid or doesn't exist
        url = f"{SL_TRANSPORT_URL}/lines"
        params = {"transport_authority_id": transport_authority_id}
        lines_data = await self.fetch(url, params)

        self._lines_cache[transport_authority_id] = lines_data
        self._lines_cache_time[transport_authority_id] = datetime.utcnow()

        return lines_data
            
    async def get_sites(self, expand: bool = True):
        """Fetches all sites, uses cache if not older than cache duration."""
        if self._is_cache_valid(self._sites_cache_time):
            return self._sites_cache

        url = f"{SL_TRANSPORT_URL}/sites"
        params = {"expand": str(expand).lower()}
        self._sites_cache = await self.fetch(url, params)
        self._sites_cache_time = datetime.utcnow()  # Update cache time
        return self._sites_cache


    async def get_stop_points(self):
        """Fetches all stop points."""
        url = f"{SL_TRANSPORT_URL}/stop-points"
        return await self.fetch(url)

    async def get_transport_authorities(self):
        """Fetches all transport authorities."""
        url = f"{SL_TRANSPORT_URL}/transport-authorities"
        return await self.fetch(url)

    async def get_deviation_messages(self, future: bool = True, sites: Optional[List[int]] = None, lines: Optional[List[int]] = None, transport_modes: Optional[List[str]] = None):
        """Fetches deviation messages based on the parameters provided."""
        url = f"{SL_DEVIATIONS_URL}/messages"
        params = {
            "future": str(future).lower(),
            "site": ",".join(map(str, sites)) if sites else None,
            "line": ",".join(map(str, lines)) if lines else None,
            "transport_mode": ",".join(transport_modes) if transport_modes else None
        }
        return await self.fetch(url, params={k: v for k, v in params.items() if v is not None})

    async def get_departures(self, site_id: int, transport: Optional[str] = None, 
                            direction: Optional[int] = None, line: Optional[int] = None,  
                            offset: Optional[int] = 0, forecast: Optional[int] = 60) :
        """
        Fetches departures for a given site with optional filters for transport mode, direction, line, and forecast.ite with optional filters for transport mode, direction, line, and forecast.

        :param site_id: The ID of the site to fetch departures for.te to fetch departures for.
        :param transport: Optional filtering by transportModeEnum (BUS, TRAM, METRO, TRAIN, FERRY, SHIP, TAXI).ring by transportModeEnum (BUS, TRAM, METRO, TRAIN, FERRY, SHIP, TAXI).
        :param direction: Optional filtering by lineDirectionCode.ring by lineDirectionCode.
        :param line: Optional filtering by lineId.by lineId.
        :param forecast: Optional forecast window in minutes (default is 60).st window in minutes (default is 60).
        """
        url = f"{SL_TRANSPORT_URL}/sites/{site_id}/departures"
        params = {
            "transport": transport,
            "direction": direction,
            "line": line,
            "forecast": forecast
        }
        # Filter out None values from paramsrams
        params = {k: v for k, v in params.items() if v is not None}

        return await self.fetch(url, params={k: v for k, v in params.items() if v is not None})

    async def get_journey_plan(self, format: str = "json", **parameters):
        """
        Fetches journey plan data based on the parameters provided.
        This API requires the journey planner key.
        """
        url = f"{SL_ROUTE_PLANNER_URL}/trip.{format}"
        # If an offset is provided, calculate the date and time
        if  parameters["offset"] is not None:
            formatted_date, formatted_time = self.calculate_time_from_now(parameters["offset"])
            # Add the calculated date and time to the parameters
            parameters["date"] = formatted_date
            parameters["time"] = formatted_time

        params = {
            "key": self.journey_planner_key,
            **parameters,
        }

        return await self.fetch(url, params={k: v for k, v in params.items() if v is not None})
    
    async def close(self):
        """Closes the underlying HTTP session."""
        await self.session.close()


