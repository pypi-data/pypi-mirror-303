import typing
import shutil
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

    def upload_file(self, path: Path, prefix: str) -> str:
        file_upload_response = self.primitive.files.file_upload(path, key_prefix=prefix)
        return file_upload_response.json()["data"]["fileUpload"]["id"]

    def scan(self) -> None:
        # Scan artifacts directory
        artifacts_dir = get_artifacts_cache()

        subdirs = [
            job_cache for job_cache in artifacts_dir.iterdir() if job_cache.is_dir()
        ]

        for job_cache in subdirs:
            job_run_id = job_cache.name
            files = [file for file in job_cache.rglob("*") if file.is_file()]

            file_ids = []
            for file in files:
                file_ids.append(
                    self.upload_file(
                        file,
                        prefix=str(PurePath(file).relative_to(job_cache.parent).parent),
                    )
                )

            # Update job run
            self.primitive.jobs.job_run_update(id=job_run_id, file_ids=file_ids)

            # Clean up job cache
            shutil.rmtree(path=job_cache)
