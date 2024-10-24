# wraps osparc_client.api.files_api

import asyncio
import json
import logging
import math
import random
import shutil
import string
from pathlib import Path
from typing import Any, Iterator, List, Optional, Tuple, Union

import httpx
from httpx import Response
from osparc_client.api.files_api import FilesApi as _FilesApi
from tqdm.asyncio import tqdm
from tqdm.contrib.logging import logging_redirect_tqdm

from ._api_client import ApiClient
from ._http_client import AsyncHttpClient
from .models import (
    BodyAbortMultipartUploadV0FilesFileIdAbortPost,
    BodyCompleteMultipartUploadV0FilesFileIdCompletePost,
    ClientFile,
    ClientFileUploadData,
    File,
    FileUploadCompletionBody,
    FileUploadData,
    UploadedPart,
)
from ._utils import (
    DEFAULT_TIMEOUT_SECONDS,
    PaginationGenerator,
    compute_sha256,
    dev_features_enabled,
    file_chunk_generator,
)

_logger = logging.getLogger(__name__)


class FilesApi(_FilesApi):
    _dev_features = [
        "get_jobs_page",
    ]

    def __init__(self, api_client: ApiClient):
        """Construct object

        Args:
            api_client (ApiClient, optinal): osparc.ApiClient object
        """
        super().__init__(api_client)
        user: Optional[str] = self.api_client.configuration.username
        passwd: Optional[str] = self.api_client.configuration.password
        self._auth: Optional[httpx.BasicAuth] = (
            httpx.BasicAuth(username=user, password=passwd)
            if (user is not None and passwd is not None)
            else None
        )

    def __getattr__(self, name: str) -> Any:
        if (name in FilesApi._dev_features) and (not dev_features_enabled()):
            raise NotImplementedError(f"FilesApi.{name} is still under development")
        return super().__getattribute__(name)

    def download_file(
        self, file_id: str, *, destination_folder: Optional[Path] = None, **kwargs
    ) -> str:
        if destination_folder is not None and not destination_folder.is_dir():
            raise RuntimeError(
                f"destination_folder: {destination_folder} must be a directory"
            )
        downloaded_file: Path = Path(super().download_file(file_id, **kwargs))
        if destination_folder is not None:
            dest_file: Path = destination_folder / downloaded_file.name
            while dest_file.is_file():
                new_name = (
                    downloaded_file.stem
                    + "".join(random.choices(string.ascii_letters, k=8))
                    + downloaded_file.suffix
                )
                dest_file = destination_folder / new_name
            shutil.move(downloaded_file, dest_file)
            downloaded_file = dest_file
        return str(downloaded_file.resolve())

    def upload_file(
        self,
        file: Union[str, Path],
        timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS,
        **kwargs,
    ):
        return asyncio.run(
            self.upload_file_async(file=file, timeout_seconds=timeout_seconds, **kwargs)
        )

    async def upload_file_async(
        self,
        file: Union[str, Path],
        timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS,
        **kwargs,
    ) -> File:
        if isinstance(file, str):
            file = Path(file)
        if not file.is_file():
            raise RuntimeError(f"{file} is not a file")
        checksum: str = compute_sha256(file)
        for file_result in self._search_files(
            sha256_checksum=checksum, timeout_seconds=timeout_seconds
        ):
            if file_result.filename == file.name:
                # if a file has the same sha256 checksum
                # and name they are considered equal
                return file_result
        client_file: ClientFile = ClientFile(
            filename=file.name,
            filesize=file.stat().st_size,
            sha256_checksum=checksum,
        )
        client_upload_schema: ClientFileUploadData = super().get_upload_links(
            client_file=client_file, _request_timeout=timeout_seconds, **kwargs
        )
        chunk_size: int = client_upload_schema.upload_schema.chunk_size
        links: FileUploadData = client_upload_schema.upload_schema.links
        url_iter: Iterator[Tuple[int, str]] = enumerate(
            iter(client_upload_schema.upload_schema.urls), start=1
        )
        n_urls: int = len(client_upload_schema.upload_schema.urls)
        if n_urls < math.ceil(file.stat().st_size / chunk_size):
            raise RuntimeError(
                "Did not receive sufficient number of upload URLs from the server."
            )

        uploaded_parts: list[UploadedPart] = []
        async with AsyncHttpClient(
            configuration=self.api_client.configuration, timeout=timeout_seconds
        ) as session:
            with logging_redirect_tqdm():
                _logger.debug("Uploading %s in %i chunk(s)", file.name, n_urls)
                async for chunck, size in tqdm(
                    file_chunk_generator(file, chunk_size),
                    total=n_urls,
                    disable=(not _logger.isEnabledFor(logging.DEBUG)),
                ):
                    index, url = next(url_iter)
                    uploaded_parts.append(
                        await self._upload_chunck(
                            http_client=session,
                            chunck=chunck,
                            chunck_size=size,
                            upload_link=url,
                            index=index,
                        )
                    )

            abort_body = BodyAbortMultipartUploadV0FilesFileIdAbortPost(
                client_file=client_file
            )
            async with AsyncHttpClient(
                configuration=self.api_client.configuration,
                request_type="post",
                url=links.abort_upload,
                body=abort_body.to_dict(),
                base_url=self.api_client.configuration.host,
                follow_redirects=True,
                auth=self._auth,
                timeout=timeout_seconds,
            ) as session:
                _logger.debug(
                    (
                        "Completing upload of %s "
                        "(this might take a couple of minutes)..."
                    ),
                    file.name,
                )
                server_file: File = await self._complete_multipart_upload(
                    session, links.complete_upload, client_file, uploaded_parts
                )
                _logger.debug("File upload complete: %s", file.name)
                return server_file

    async def _complete_multipart_upload(
        self,
        http_client: AsyncHttpClient,
        complete_link: str,
        client_file: ClientFile,
        uploaded_parts: List[UploadedPart],
    ) -> File:
        complete_payload = BodyCompleteMultipartUploadV0FilesFileIdCompletePost(
            client_file=client_file,
            uploaded_parts=FileUploadCompletionBody(parts=uploaded_parts),
        )
        response: Response = await http_client.post(
            complete_link,
            json=complete_payload.to_dict(),
        )
        response.raise_for_status()
        payload: dict[str, Any] = response.json()
        return File(**payload)

    async def _upload_chunck(
        self,
        http_client: AsyncHttpClient,
        chunck: bytes,
        chunck_size: int,
        upload_link: str,
        index: int,
    ) -> UploadedPart:
        response: Response = await http_client.put(
            upload_link,
            content=chunck,
            headers={"Content-Length": f"{chunck_size}"},
        )
        response.raise_for_status()
        assert response.headers  # nosec
        assert "Etag" in response.headers  # nosec
        etag: str = json.loads(response.headers["Etag"])
        return UploadedPart(number=index, e_tag=etag)

    def _search_files(
        self,
        file_id: Optional[str] = None,
        sha256_checksum: Optional[str] = None,
        timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS,
    ) -> PaginationGenerator:
        def _pagination_method():
            return super(FilesApi, self).search_files_page(
                file_id=file_id,
                sha256_checksum=sha256_checksum,
                _request_timeout=timeout_seconds,
            )

        return PaginationGenerator(
            first_page_callback=_pagination_method,
            api_client=self.api_client,
            base_url=self.api_client.configuration.host,
            auth=self._auth,
        )
