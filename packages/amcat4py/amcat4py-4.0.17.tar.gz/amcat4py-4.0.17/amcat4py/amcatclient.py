from datetime import datetime, date, time
from json import dumps
from multiprocessing import Value
from typing import Any, List, Iterable, Optional, Union, Dict, Sequence

import logging
from pathlib import Path
import requests
from requests import HTTPError
from .auth import _get_token, _check_token, token_refresh


class AmcatError(HTTPError):
    """Superclass for errors originating from AmCAT API with a better message / string representation"""

    def __init__(self, response, request, **kargs):
        super().__init__(response=response, request=request, **kargs)
        if self.response is not None:
            try:
                d = self.response.json()
                self.message = d["detail"] if "detail" in d else repr(d)
            except ValueError:
                self.message = self.response.text
        else:
            self.message = f"HTTPError {self.response}"

    def __str__(self):
        return f"Error from server ({self.response.status_code}): {self.message}"


def serialize(obj):
    """JSON serializer that accepts datetime & date"""
    if isinstance(obj, date) and not isinstance(obj, datetime):
        obj = datetime.combine(obj, time.min)
    if isinstance(obj, datetime):
        return obj.isoformat()
    if isinstance(obj, set):
        return sorted(obj)
    if "numpy.float32" in str(type(obj)):
        return float(obj)


class AmcatClient:
    def __init__(self, host: str, refresh_token: dict | str = None, ignore_tz=True):
        """
        :param host: The host name of the API endpoint to connect to
        :param refresh_token: A refresh token
        :param ignore_tz: Do we ignore time zones when querying articles
        """
        self.host = host
        self.ignore_tz = ignore_tz
        self.server_config = self.get_server_config()
        # If we have a token cached, load it. Otherwise, only log in if explicitly requested
        if self.server_config["authorization"] == "no_auth":
            self.token = None
        elif refresh_token:
            if isinstance(refresh_token, str):
                refresh_token = dict(refresh_token=refresh_token, refresh_rotate=False)
            self.token = token_refresh(refresh_token, host)
        else:
            self.token = _get_token(self.host, login_if_needed=False)

    def login(self, force_refresh=False):
        self.token = _get_token(self.host, force_refresh=force_refresh)

    def login_required(self):
        return self.server_config["authorization"] in (
            "_authenticated_guests",
            "authorized_users_only",
        )

    def get_server_config(self):
        r = requests.get(self._url("config"))
        r.raise_for_status()
        config = r.json()
        if "warnings" in config:
            for w in config["warnings"]:
                if w:
                    logging.warning(w)
        return config

    @staticmethod
    def _chunks(items: Iterable, chunk_size=100) -> Iterable[List]:
        """utility method for uploading documents in batches"""
        buffer = []
        for item in items:
            buffer.append(item)
            if len(buffer) > chunk_size:
                yield buffer
                buffer = []
        if buffer:
            yield buffer

    def _url(self, url=None, index=None):
        url_parts = [self.host] + (["index", index] if index else []) + ([url] if url else [])
        return "/".join(url_parts)

    def _request(self, method, url=None, ignore_status=None, headers=None, **kargs):
        if headers is None:
            headers = {}
        if self.token is None:
            if self.login_required():
                raise Exception("This server requires a user to be authenticated. Please call .login() first")
        else:
            self.token = _check_token(self.token, self.host)
            headers["Authorization"] = f"Bearer {self.token['access_token']}"
        r = requests.request(method, url, headers=headers, **kargs)
        if not (ignore_status and r.status_code in ignore_status):
            try:
                r.raise_for_status()
            except HTTPError as e:
                raise AmcatError(e.response, e.request) from e
        return r

    def _get(self, url=None, index=None, params=None, ignore_status=None):
        return self._request("get", url=self._url(url, index), params=params, ignore_status=ignore_status)

    def _post(self, url=None, index=None, json=None, ignore_status=None):
        if json:
            data = dumps(json, default=serialize)
            headers = {"Content-Type": "application/json"}
        else:
            data = None
            headers = {}

        return self._request(
            "post",
            url=self._url(url, index),
            data=data,
            headers=headers,
            ignore_status=ignore_status,
        )

    def _put(self, url=None, index=None, json=None, ignore_status=None):
        return self._request("put", url=self._url(url, index), json=json, ignore_status=ignore_status)

    def _delete(self, url=None, index=None, ignore_status=None):
        return self._request("delete", url=self._url(url, index), ignore_status=ignore_status)

    def get_user(self, user: str = "me"):
        """Get information on the given user, or on self if no user is given

        Args:
            user (string, optional): Username (email) to get information on. Defaults to 'me'.
        """
        return self._get(f"users/{user}")

    def list_indices(self) -> List[dict]:
        """
        List all indices on this server
        :return: a list of index dicts with keys name and (your) role
        """
        return self._get("index/").json()

    def list_users(self) -> List[dict]:
        """
        List users and their global roles
        """
        return self._get("users").json()

    def list_index_users(self, index: str) -> List[dict]:
        """
        List users and their roles in an index
        """
        return self._get(f"index/{index}/users").json()

    def documents(
        self,
        index: str,
        q: Optional[str] = None,
        *,
        fields=("date", "title", "url"),
        scroll="2m",
        per_page=100,
        **params,
    ) -> Iterable[dict]:
        """
        Perform a query on this server, scrolling over the results to get all hits

        :param index: The name of the index
        :param q: An optional query
        :param fields: A list of fields to retrieve (use None for all fields, '_id' for id only)
        :param scroll: type to keep scroll cursor alive
        :param per_page: Number of results per page
        :param params: Any other parameters passed as query arguments
        :return: an iterator over the found documents with the requested (or all) fields
        """
        params["scroll"] = scroll
        params["per_page"] = per_page
        if fields:
            params["fields"] = ",".join(fields)
        if q:
            params["q"] = q
        while True:
            r = self._get("documents", index=index, params=params, ignore_status=[404])
            if r.status_code == 404:
                break
            d = r.json()
            yield from d["results"]
            params["scroll_id"] = d["meta"]["scroll_id"]

    def query(
        self,
        index: str,
        *,
        scroll="2m",
        per_page=100,
        sort: Union[str, dict, list] = None,
        fields: Sequence[str] = ("date", "title", "url"),
        queries: Union[str, list, dict] = None,
        filters: Dict[str, Union[str, list, dict]] = None,
        date_fields: Sequence[str] = ("date",),
    ):
        """
        Execute a search query on this server

        :param index: The name of the index to search
        :param scroll: type to keep scroll cursor alive
        :param per_page: Number of results per page
        :param sort: Sorting for the query
        :param fields: A list of fields to retrieve (use None for all fields, '_id' for id only)
        :param queries: One or more query strings or objects to search for
        :param filters: A dictionary of filters to apply to the search
        :param date_fields: A list of fields to treat as dates, which will be converted to datetime objects
        :return: an iterator over the search results, with the requested (or all) fields
        """
        body = dict(
            filters=filters,
            queries=queries,
            fields=fields,
            sort=sort,
            scroll=scroll,
            per_page=per_page,
        )
        body = {k: v for (k, v) in body.items() if v is not None}
        while True:
            r = self._post("query", index=index, json=body, ignore_status=[404])
            if r.status_code == 404:
                break
            d = r.json()
            for res in d["results"]:
                for date_field in date_fields:
                    if res.get(date_field):
                        date = res[date_field][:10] if self.ignore_tz else res[date_field]
                        res[date_field] = datetime.fromisoformat(date)
                yield res
            body["scroll_id"] = d["meta"]["scroll_id"]

    def update_by_query(
        self,
        index: str,
        field: str,
        value: Any,
        *,
        queries: Union[str, list, dict] = None,
        filters: Dict[str, Union[str, list, dict]] = None,
    ):
        """
        Update the index by query

        :param index: The name of the index to search
        :param field: A field name to update
        :param value: The value to set for the selected documents (or None to delete the field)
        :param queries: One or more query strings or objects to search for
        :param filters: A dictionary of filters to apply to the search
        """
        body = {"field": field, "value": value, "queries": queries, "filters": filters}
        return self._post(f"index/{index}/update_by_query", json=body).json()

    def query_aggregate(
        self,
        index: str,
        *,
        axes: Union[str, list, dict] = None,
        queries: Union[str, list, dict] = None,
        filters: Dict[str, Union[str, list, dict]] = None,
    ):
        """
        Execute a search query on this server and aggregate results

        :param index: The name of the index to search
        :param axes: The aggregation axes, e.g. [{"field": "publisher", [{"field": "date", "interval": "year"}]}]
        :param queries: One or more query strings or objects to search for
        :param filters: A dictionary of filters to apply to the search
        :return: an iterator over the search results, with the requested (or all) fields
        """
        body = {"axes": axes, "queries": queries, "filters": filters}
        return self._post(f"index/{index}/aggregate", json=body).json()["data"]

    def create_index(
        self,
        index: str,
        name: str = None,
        description: str = None,
        guest_role: Optional[str] = None,
    ):
        r"""
        Create an index

        Parameters:
            index (str): Short name of the index to create (follows naming conventions of Elasticsearch, see details).
            name (str, optional): Optional more descriptive name of the index to create (all characters are allowed here).
            description (str, optional): Optional description of the index to create.
            guest_role (str, optional): Role for unauthorized users. Options are "admin", "writer", "reader", and "metareader".
            credentials (Any, optional): The credentials to use. If not given, uses last login information.

        Details:
            The short name for the new index (`index` argument) must meet these criteria:

            - Lowercase only
            - Cannot include `\`, `/`, `*`, `?`, `"`, `<`, `>`, `|`, `:`, ` `(space), `,` (comma), `#`
            - Cannot start with -, _, +
            - Cannot be `.` or `..`
            - Cannot be longer than 255 characters (note that some symbols like emojis take up two characters)
            - If names start with ., the index will be hidden and non-accessible
        """
        body = {"id": index, "name": name or index}
        if guest_role:
            body["guest_role"] = guest_role
        if description:
            body["description"] = description
        return self._post("index/", json=body).json()

    def modify_index(
        self,
        index: str,
        name: str = None,
        description: str = None,
        guest_role: Optional[str] = None,
        summary_field: Optional[str] = None,
    ):
        """
        Modify an index

        for parameters see create_index
        """
        body = {"id": index, "name": name or index}
        if guest_role:
            body["guest_role"] = guest_role
        if description:
            body["description"] = description
        if summary_field:
            body["summary_field"] = summary_field
        return self._put(f"index/{index}", json=body).json()

    def get_index(self, index: str):
        return self._get(index=index).json()

    def create_user(self, email, role="NONE"):
        """
        Create a new user
        :param email: Email address of the new user to add
        :param role: global role of the user ("writer" or "admin")
        """
        body = {
            "email": email,
            "role": role,
        }
        return self._post("users/", json=body).json()

    def delete_user(self, email):
        """
        Delete a user from the instance
        :param email: Email address of the new user to add
        """
        self._delete(f"users/{email}")

    def add_index_user(self, index: str, email: str, role: str):
        """
        add new user to an index
        :param index: name of the index
        :param email: Email address of the user to add
        :param role: role of the user for this index. One of "admin", "writer", "reader" "metareader".
        """
        body = {"email": email, "role": role.upper()}
        return self._post(f"index/{index}/users", json=body).json()

    def modify_index_user(self, index: str, email: str, role: str):
        """
        modify user role for index
        :param index: name of the index
        :param email: The email of an (existing) user
        :param role: role of the user for this index. One of "admin", "writer", "reader" "metareader".
        """
        body = {"role": role.upper()}
        return self._put(f"index/{index}/users/{email}", json=body).json()

    def check_index(self, ix: str) -> Optional[dict]:
        r = self._get(index=ix, ignore_status=[404])
        if r.status_code == 404:
            return None
        return r.json()

    def refresh_index(self, ix: str) -> None:
        """Refresh (flush) this index"""
        self._get(f"index/{ix}/refresh")

    def delete_index(self, index: str) -> bool:
        """Delete this index"""
        r = self._delete(index=index, ignore_status=[404])
        return r.status_code != 404

    def delete_index_user(self, index: str, email: str) -> bool:
        """
        delete user from an index
        :param index: name of the index
        :param email: The email of an (existing) user
        """
        r = self._delete(f"index/{index}/users/{email}", ignore_status=[404])
        return r.status_code != 404

    def upload_documents(
        self,
        index: str,
        articles: Iterable[dict],
        columns: dict = None,
        chunk_size=100,
        show_progress=False,
        allow_unknown_fields=False,
    ) -> None:
        """
        Upload documents to the server. First argument is the name of the index where the new documents should be inserted.
        Second argument is an iterable (e.g., a list) of dictionaries. Each dictionary represents a single document.
        Required keys are: `title`, `text`, `date`, and `url`.
        You can optionally specify the column types with a dictionary.
        If the articles contain unknown fields, a ValueError is raised unless allow_unknown_fields is set to True.
        By default, the articles are uploaded in chunks of 100 documents. You can adjust this accordingly.
        For larger uploads, you have the option to show a progress bar (make sure tqdm is installed).

        :param index: The name of the index
        :param articles: Documents to upload (a list of dictionaries)
        :param columns: an optional dictionary of field types.
        :param chunk_size: number of documents to upload per batch (default: 100)
        :param show_progress: show a progress bar when uploading documents (default: False)
        :param allow_new_fields: if set, documents with unknown fields are allowed (default: False)
        """
        body = {}
        if columns:
            body["columns"] = columns
        if not allow_unknown_fields:
            known_fields = set(self.get_fields(index).keys())
            if columns:
                known_fields |= set(columns.keys())
        if show_progress:
            from tqdm import tqdm
            import math

            generator = tqdm(
                self._chunks(articles, chunk_size=chunk_size),
                total=math.ceil(len(articles) / chunk_size),
                unit="chunks",
            )
        else:
            generator = self._chunks(articles, chunk_size=chunk_size)
        successes, failures = 0, []
        for chunk in generator:
            if not allow_unknown_fields:
                for doc in chunk:
                    if unknown := (set(doc.keys()) - known_fields):
                        raise ValueError(f"Document contained unknown fields: {unknown}")
            body = {"documents": chunk}
            result = self._post("documents", index=index, json=body).json()
            successes += result["successes"]
            failures += result["failures"]
        if failures:
            for failure in failures[:10]:
                logging.warning(list(failure.values())[0]["error"])
            if len(failures) > 10:
                logging.warning(f"{len(failures) - 10} more errors")
            if not successes:
                raise ValueError("Uploading failed for all documents")
            else:
                logging.warning(f"{len(failures)} failed to upload, see individual warnings above")
        return successes, failures

    def update_document(self, index: str, doc_id, body):
        self._put(f"documents/{doc_id}", index, json=body)

    def get_document(self, index: str, doc_id):
        return self._get(f"documents/{doc_id}", index).json()

    def delete_document(self, index: str, doc_id):
        self._delete(f"documents/{doc_id}", index)

    def set_fields(self, index: str, body):
        self._post("fields", index, json=body)

    def get_fields(self, index: str) -> dict:
        return self._get("fields", index).json()

    def tags_update(
        self,
        index: str,
        action: str,
        field: str,
        tag: str,
        ids=None,
        queries=None,
        filters=None,
    ):
        body = dict(
            field=field,
            action=action,
            tag=tag,
            ids=ids,
            queries=queries,
            filters=filters,
        )
        self._post("tags_update", index, json=body)

    def get_preprocessing_tasks(self):
        return self._get("preprocessing_tasks").json()

    def add_preprocessing_instruction(
        self,
        index: str,
        field: str,
        task: str,
        endpoint: str,
        arguments: List[dict],
        outputs: List[dict],
    ):
        body = dict(
            field=field,
            task=task,
            endpoint=endpoint,
            arguments=arguments,
            outputs=outputs,
        )
        self._post(f"index/{index}/preprocessing", json=body)

    def get_preprocessing_instruction(self, index: str, field: str):
        return self._get(f"index/{index}/preprocessing/{field}").json()

    def multimedia_list(
        self,
        index: str,
        n=10,
        prefix: str = None,
        start_after: str = None,
        recursive=False,
        presigned_get=False,
        metadata=False,
        all_pages=True,
    ):
        """Get a list of multimedia files in the storage for this index
        See https://min.io/docs/minio/linux/developers/python/API.html#list_objects

        :param n: Number of items to return (ordered alphabetically)
        :param start_after: Start after the given key (for pagination)
        :param prefix: Filter on this prefix (e.g. a folder name/)
        :param recursive: If True, list all objects rather than per-folder
        :param metadata: Include metadata in results (separately retrieved per object by the backend)
        :param presigned_get: Include a pre-signed GET url for each object (separately retrieved per object by the backend)
        """
        params = dict(
            n=n,
            prefix=prefix,
            start_after=start_after,
            presigned_get=presigned_get,
            metadata=metadata,
            recursive=recursive,
        )
        while True:
            res = self._get(f"index/{index}/multimedia/list", params=params).json()
            yield from res
            if (not all_pages) or (len(res) < n):
                break
            params["start_after"] = res[-1]["key"]

    def multimedia_presigned_post(self, index):
        return self._get(f"index/{index}/multimedia/presigned_post").json()

    def multimedia_upload_files(self, index, files: Iterable[Path | str], prefix=None):
        res = self.multimedia_presigned_post(index)
        files = [(Path(file) if not isinstance(file, Path) else file) for file in files]
        missing = [file for file in files if not file.exists()]
        if missing:
            raise ValueError(f"File(s) not found: {missing}")
        url = res["url"]
        form_data = res["form_data"]
        for file in files:
            with file.open("rb") as f:
                requests.post(
                    url=url,
                    data={"key": f"{prefix}{file.name}", **form_data},
                    files={"file": f},
                )
