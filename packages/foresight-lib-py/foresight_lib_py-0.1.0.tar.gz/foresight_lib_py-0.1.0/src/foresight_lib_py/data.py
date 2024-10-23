"""Access to Foresight timeseries data."""

from datetime import datetime, timezone
from typing import Optional
from uuid import UUID

from gql import Client, gql
from pandas import DataFrame, Series, to_datetime


def get_value(
    client: Client, entity_id: UUID, moment: Optional[datetime] = None
) -> float:
    """Retrieve the latest value of a `foresight:Datapoint` entity before a point in time (default=now).

    Parameters
    ----------
    client : Client
        The GQL client to use.
    entity_id : str
        The ID of the entity.
    moment : Optional[datetime], optional
        The point in time to retrieve a value for, by default `datetime.now(tz=timezone.utc)`.

    Returns
    -------
    float
        _description_

    Raises
    ------
    RuntimeError
        _description_
    RuntimeError
        _description_

    """
    if not moment:
        moment = datetime.now(tz=timezone.utc)
    query = gql("""
    query value($entityId: ID!, $eventTime: DateTime) {
        entity(id: $entityId) {
            trait(id: "foresight:Datapoint") {
                quantity(key: "Value") {
                    value(eventTime: $eventTime) {
                        value
                    }
                }
            }
        }
    }
    """)
    variables = {"entityId": entity_id, "eventTime": moment.isoformat()}
    response = client.execute(query, variables)
    try:
        return float(response["entity"]["trait"]["quantity"]["value"]["value"])
    except KeyError:
        raise RuntimeError("Cloud not retrieve value.")
    except ValueError:
        raise RuntimeError(
            f"Could not parse value {response['entity']['trait']['quantity']['value']['value']}"
        )


def get_values(
    client: Client, entity_id: UUID, start: datetime, end: Optional[datetime] = None
) -> Series:
    """Retrieve values of a `foresight:Datapoint` entity for a time range. The most recent value before 'start' is included, 'end' defaults to 'now'.

    Parameters
    ----------
    client : Client
        The GQL client to use.
    entity_id : str
        The ID of the entity.
    start : datetime
        The starting point in time from which to received values. Must include timezone info.
        The most recent value before this point is also included in the response.
    end : Optional[datetime], optional
        The end point in time until which to receive values. Must include timezone info. By default `datetime.now(tz=timezone.utc)`.

    Returns
    -------
    Series
        The Pandas Series with the values received.

    """
    if not end:
        end = datetime.now(tz=timezone.utc)
    if start.tzinfo is None or start.tzinfo.utcoffset(start) is None:
        raise ValueError("The start parameter must be timezone aware.")
    if end.tzinfo is None or end.tzinfo.utcoffset(end) is None:
        raise ValueError("The end parameter must be timezone aware.")
    query = gql("""
    query value($entityId: ID!, $startEventTime: DateTime!, $endEventTime: DateTime!) {
        entity(id: $entityId) {
            name
            trait(id: "foresight:Datapoint") {
                quantity(key: "Value") {
                    values(startEventTime: $startEventTime endEventTime: $endEventTime) {
                        eventTime
                        value
                    }
                }
            }
        }
    }
    """)
    variables = {
        "entityId": entity_id,
        "startEventTime": start.isoformat(),
        "endEventTime": end.isoformat(),
    }
    response = client.execute(query, variables)
    try:
        values = response["entity"]["trait"]["quantity"]["values"]
        name = response["entity"]["name"]
    except KeyError:
        raise RuntimeError("Cloud not retrieve value.")
    frame = DataFrame(values).set_index("eventTime")
    frame.index = to_datetime(frame.index)
    frame["value"] = frame["value"].astype(float)
    series = frame["value"]
    series.name = name
    return series
