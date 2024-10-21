import asyncio
import time
from random import randint
from types import SimpleNamespace
from typing import Optional, Callable, List, Dict, Union

from aiohttp import ClientSession

from . import dummies

__all__ = ["Connection"]


class Endpoints:

    base: str = "https://www.reddit.com"
    user: str = f"{base}/u"
    users: str = f"{base}/users"
    subreddit: str = f"{base}/r"
    subreddits: str = f"{base}/subreddits"
    username_available: str = f"{base}/api/username_available.json"
    infra_status: str = "https://www.redditstatus.com/api/v2/status.json"
    infra_components: str = "https://www.redditstatus.com/api/v2/components.json"


class Connection:
    def __init__(self, headers: Dict):
        self._headers = headers
        self.endpoints = Endpoints()

    async def send_request(
        self,
        session: ClientSession,
        endpoint: str,
        params: Optional[Dict] = None,
    ) -> Union[Dict, List, bool, None]:

        try:
            async with session.get(
                url=endpoint, headers=self._headers, params=params
            ) as response:
                response.raise_for_status()
                response_data: Union[Dict, List] = await response.json()
                return response_data

        except Exception as error:
            raise error

    async def paginate_response(
        self,
        session: ClientSession,
        endpoint: str,
        limit: int,
        parser: Callable,
        message: Optional[dummies.Message] = None,
        status: Optional[dummies.Status] = None,
        params: Optional[Dict] = None,
        is_post_comments: Optional[bool] = False,
    ) -> List[SimpleNamespace]:

        # Initialise an empty list to store all items across paginated requests.
        all_items: List = []
        # Initialise the ID of the last item fetched to None (used for pagination).
        last_item_id = None

        # Continue fetching data until the limit is reached or no more items are available.
        while len(all_items) < limit:
            # Make an asynchronous request to the endpoint.
            response = await self.send_request(
                session=session,
                endpoint=(
                    f"{endpoint}?after={last_item_id}&count={len(all_items)}"
                    if last_item_id
                    else endpoint
                ),
                params=params,
            )

            if is_post_comments:
                items = await self._process_post_comments(
                    session=session,
                    endpoint=endpoint,
                    response=parser(response[1]),
                    parser=parser,
                    limit=limit,
                    status=status,
                    message=message,
                )
            else:

                # If not handling comments, simply extract the items from the response.
                items = parser(response=response).children

            # If no items are found, break the loop as there's nothing more to fetch.
            if not items:
                break

            # Determine how many more items are needed to reach the limit.
            items_to_limit = limit - len(all_items)

            # Add the processed items to the all_items list, up to the specified limit.
            all_items.extend(items[:items_to_limit])

            # Update the last_item_id to the ID of the last fetched item for pagination.

            last_item_id = (
                parser(response=response[1]).after
                if is_post_comments
                else parser(response=response).after
            )

            # If we've reached the specified limit, break the loop.
            if len(all_items) == limit:
                break

            # Introduce a random sleep duration between 1 and 5 seconds to avoid rate-limiting.
            sleep_duration = randint(1, 5)

            # If a status object is provided, use it to display a countdown timer.
            if status:
                await self._pagination_countdown_timer(
                    status=status,
                    duration=sleep_duration,
                    current_count=len(all_items),
                    overall_count=limit,
                )
            else:
                # Otherwise, just sleep for the calculated duration.
                await asyncio.sleep(sleep_duration)

        # Return the list of all fetched and processed items (without duplicates).
        return all_items

    async def _paginate_more_items(
        self,
        session: ClientSession,
        more_items_ids: List[str],
        endpoint: str,
        parser: Callable,
        fetched_items: List[Dict],
        limit: int,
        status: Optional[dummies.Status] = None,
        message: Optional[dummies.Message] = None,
    ):
        # Track how many more items are needed to meet the overall limit
        remaining_items = limit - len(fetched_items)

        if remaining_items <= 0:
            return  # Stop if we've already hit the limit

        message.ok(f"Found {len(more_items_ids)} comments on post")
        for more_id in more_items_ids:
            # Check if we still need more items, and stop if we've reached the limit.
            if len(fetched_items) >= limit:
                break

            # Construct the endpoint for each additional comment ID.
            more_endpoint = f"{endpoint}?comment={more_id}"
            # Make an asynchronous request to fetch the additional comments.
            more_response = await self.send_request(
                session=session, endpoint=more_endpoint
            )
            # Extract the items (comments) from the response.
            more_items = parser(response=more_response[1])

            # Determine how many more items we can add without exceeding the limit.
            items_to_add = min(remaining_items, len(more_items.children))

            # Add the allowed number of items to the main items list.
            fetched_items.extend(more_items.children[:items_to_add])

            # Update the remaining items to be fetched.
            remaining_items -= items_to_add

            # Stop if we've reached the limit.
            if remaining_items <= 0:
                break

            # Introduce a random sleep duration to avoid rate-limiting.
            sleep_duration = randint(1, 5)
            await self._pagination_countdown_timer(
                duration=sleep_duration,
                overall_count=limit,
                current_count=len(fetched_items),
                status=status,
            )

    async def _process_post_comments(self, **kwargs):
        # If the request is for post comments, handle the response accordingly.
        items = []  # Initialise a list to store fetched items.
        more_items_ids = []  # Initialise a list to store IDs from "more" items.

        # Iterate over the children in the response to extract comments or "more" items.
        for item in kwargs.get("response").children:
            if item.kind == "t1":
                # If the item is a comment (kind == "t1"), add it to the items list.
                items.append(item)
            elif item.kind == "more":
                # If the item is of kind "more", extract the IDs for additional comments.
                more_items_ids.extend(item.data.children)

        # If there are more items to fetch (kind == "more"), make additional requests.
        if more_items_ids:
            await self._paginate_more_items(
                session=kwargs.get("session"),
                message=kwargs.get("message"),
                status=kwargs.get("status"),
                fetched_items=items,
                more_items_ids=more_items_ids,
                endpoint=kwargs.get("endpoint"),
                limit=kwargs.get("limit"),
                parser=kwargs.get("parser"),
            )

        return items

    @staticmethod
    async def _pagination_countdown_timer(
        duration: int,
        current_count: int,
        overall_count: int,
        status: Optional[dummies.Status] = None,
    ):

        end_time: float = time.time() + duration
        while time.time() < end_time:
            remaining_time: float = end_time - time.time()
            remaining_seconds: int = int(remaining_time)
            remaining_milliseconds: int = int(
                (remaining_time - remaining_seconds) * 100
            )

            countdown_text: str = (
                f"Gotten [cyan]{current_count}[/] of [cyan]{overall_count}[/] items so far. "
                f"Resuming in [cyan]{remaining_seconds}.{remaining_milliseconds:02}[/] seconds"
            )

            (
                status.update(countdown_text)
                if status
                else print(countdown_text.strip("[,],/,cyan"))
            )
            await asyncio.sleep(0.01)  # Sleep for 10 milliseconds


# -------------------------------- END ----------------------------------------- #
