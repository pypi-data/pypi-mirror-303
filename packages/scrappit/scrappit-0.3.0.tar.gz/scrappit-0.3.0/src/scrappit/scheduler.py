# Scrappit, Simple Reddit Scraper
# Copyright (C) 2024  Natan Junges <natanajunges@gmail.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from queue import Empty, Queue
from threading import Thread

from .common import ScrappitTask, ScrappitResult
from .api import SubredditSort, SubredditT, UserWhere, UserSort, UserT, CommentsSort
from .dispatcher import ScrappitDispatcherTask, ScrappitDispatcher


class ScrappitScheduler(Thread):
    IDLE_SLEEP: float = 1 / 60

    def __init__(self) -> None:
        super().__init__()
        self.dispatcher = ScrappitDispatcher()
        self.task_queue: Queue[ScrappitTask] = Queue()
        self.result_queue: Queue[ScrappitResult] = Queue()

    def run(self) -> None:
        self.dispatcher.start()
        self.dispatcher.running.wait()

        while self.dispatcher.running.is_set():
            pass

    def stop(self) -> None:
        self.dispatcher.stop()

    def put_task(self, task: ScrappitTask) -> ScrappitTask:
        self.task_queue.put(task)
        return task

    def get_result(self) -> ScrappitResult | None:
        try:
            result = self.result_queue.get_nowait()
            self.result_queue.task_done()
            return result
        except Empty:
            return None

    def get(self, endpoint: str, **params: str) -> ScrappitDispatcherTask:
        return self.dispatcher.get(0, endpoint, **params)

    def listing(self, endpoint: str, before: str | None = None, after: str | None = None, **params: str) -> ScrappitDispatcherTask:
        return self.dispatcher.listing(0, endpoint, before, after, **params)

    def listing_full(self, endpoint: str, limit: int = 0, **params: str) -> ScrappitTask:
        return self.put_task(ScrappitTask("listing_full", (endpoint, limit), params))

    def r_about(self, subreddit: str) -> ScrappitDispatcherTask:
        return self.dispatcher.r_about(0, subreddit)

    def r(
        self,
        subreddit: str,
        sort: SubredditSort = SubredditSort.HOT,
        t: SubredditT = SubredditT.DAY,
        before: str | None = None,
        after: str | None = None
    ) -> ScrappitDispatcherTask:
        return self.dispatcher.r(0, subreddit, sort, t, before, after)

    def r_full(self, subreddit: str, sort: SubredditSort = SubredditSort.HOT, t: SubredditT = SubredditT.DAY, limit: int = 0) -> ScrappitTask:
        return self.put_task(ScrappitTask("r_full", (subreddit, sort, t, limit)))

    def user_about(self, username: str) -> ScrappitDispatcherTask:
        return self.dispatcher.user_about(0, username)

    def user(
        self,
        username: str,
        where: UserWhere = UserWhere.OVERVIEW,
        sort: UserSort = UserSort.NEW,
        t: UserT = UserT.ALL,
        before: str | None = None,
        after: str | None = None
    ) -> ScrappitDispatcherTask:
        return self.dispatcher.user(0, username, where, sort, t, before, after)

    def user_full(
        self, username: str, where: UserWhere = UserWhere.OVERVIEW, sort: UserSort = UserSort.NEW, t: UserT = UserT.ALL, limit: int = 0
    ) -> ScrappitTask:
        return self.put_task(ScrappitTask("user_full", (username, where, sort, t, limit)))

    def comments(self, article: str, sort: CommentsSort = CommentsSort.CONFIDENCE, comment: str | None = None) -> ScrappitDispatcherTask:
        return self.dispatcher.comments(0, article, sort, comment)

    def api_morechildren(self, link_id: str, children: list[str], sort: CommentsSort = CommentsSort.CONFIDENCE) -> ScrappitDispatcherTask:
        return self.dispatcher.api_morechildren(0, link_id, children, sort)

    def comments_full(self, article: str, sort: CommentsSort = CommentsSort.CONFIDENCE, comment: str | None = None, limit: int = 0) -> ScrappitTask:
        return self.put_task(ScrappitTask("comments_full", (article, sort, comment, limit)))
