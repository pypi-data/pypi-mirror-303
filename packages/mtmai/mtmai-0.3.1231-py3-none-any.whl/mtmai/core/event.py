async def emit_flow_event(event: str, data: dict):
    from prefect.events import emit_event

    event = emit_event(
        event="mtmai.mttask.update_status",
        resource={
            **data,
            "prefect.resource.id": "my.external.resource",
        },
    )
    return event
