from datetime import date, datetime
from typing import Optional

from langchain_core.tools import tool
from pydantic import BaseModel, Field

from mtmai.agents.tools.web_search import search_engine
from mtmai.core.logging import get_logger

logger = get_logger()


class ToFlightBookingAssistant(BaseModel):
    """Transfers work to a specialized assistant to handle flight updates and cancellations."""

    request: str = Field(
        description="Any necessary followup questions the update flight assistant should clarify before proceeding."
    )


class ToBookCarRental(BaseModel):
    """Transfers work to a specialized assistant to handle car rental bookings."""

    location: str = Field(
        description="The location where the user wants to rent a car."
    )
    start_date: str = Field(description="The start date of the car rental.")
    end_date: str = Field(description="The end date of the car rental.")
    request: str = Field(
        description="Any additional information or requests from the user regarding the car rental."
    )

    class Config:
        json_schema_extra = {
            "example": {
                "location": "Basel",
                "start_date": "2023-07-01",
                "end_date": "2023-07-05",
                "request": "I need a compact car with automatic transmission.",
            }
        }


@tool
def search_flights(
    departure_airport: Optional[str] = None,
    arrival_airport: Optional[str] = None,
    start_time: Optional[date | datetime] = None,
    end_time: Optional[date | datetime] = None,
    limit: int = 20,
) -> list[dict]:
    """Search for flights based on departure airport, arrival airport, and departure time range."""
    logger.info(
        f"调用工具： search_flights: {departure_airport}, {arrival_airport}, {start_time}, {end_time}, {limit}"
    )
    return [{"title": "flight", "id": "id1"}]


def get_tools(tools_name: str | list[str]):
    """
    根据工具名称获取工具函数
    """
    tools = []
    if isinstance(tools_name, str):
        tools_name = [tools_name]

    for tool_name in tools_name:
        if tool_name == "search_flights":
            tools.append(search_flights)
        elif tool_name == "search_engine":
            tools.append(search_engine)
    return tools
