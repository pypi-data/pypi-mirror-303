import typing
import shutil
import os
from loguru import logger
from pathlib import Path, PurePath
from ..utils.cache import get_artifacts_cache

if typing.TYPE_CHECKING:
    import primitive.client


class Uploader:
    def __init__(
        self,
        primitive: "primitive.client.Primitive",
    ):
        self.primitive = primitive

    def upload_file(self, path: Path, prefix: str, job_run_id: str) -> str:
        file_upload_response = self.primitive.files.file_upload(
            path, key_prefix=prefix, job_run_id=job_run_id
        )
        return file_upload_response.json()["data"]["fileUpload"]["id"]

    def scan(self) -> None:
        # Scan artifacts directory
        artifacts_dir = get_artifacts_cache()

        subdirs = sorted(
            [job_cache for job_cache in artifacts_dir.iterdir() if job_cache.is_dir()],
            key=lambda p: p.stat().st_ctime,
        )

        for job_cache in subdirs:
            job_run_id = job_cache.name

            files = None
            has_walk = getattr(job_cache, "walk", None)
            if has_walk:
                files = sorted(
                    [
                        w_path / file
                        for w_path, _, w_files in job_cache.walk()
                        for file in w_files
                    ],
                    key=lambda p: p.stat().st_size,
                )
            else:
                files = sorted(
                    [
                        Path(Path(w_path) / file)
                        for w_path, _, w_files in os.walk(job_cache)
                        for file in w_files
                    ],
                    key=lambda p: p.stat().st_size,
                )

            file_ids = []
            for file in files:
                upload_id = self.upload_file(
                    file,
                    prefix=str(PurePath(file).relative_to(job_cache.parent).parent),
                    job_run_id=job_run_id,
                )

                if upload_id:
                    file_ids.append(upload_id)
                    continue

                logger.error(f"Unable to upload file {file}")

            # Update job run
            if len(file_ids) > 0:
                self.primitive.jobs.job_run_update(id=job_run_id, file_ids=file_ids)

            # Clean up job cache
            shutil.rmtree(path=job_cache)
