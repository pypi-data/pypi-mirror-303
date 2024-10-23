from pathlib import Path
from gql import gql
from primitive.graphql.sdk import create_requests_session
from ..utils.auth import guard

from primitive.utils.actions import BaseAction


class Files(BaseAction):
    @guard
    def trace_create(
        self,
        file_id: str,
        signal_id: str,
        signal_name: str,
        module_name: str,
        is_vector: bool,
        size: int,
    ):
        mutation = gql(
            """
            mutation createTrace($input: TraceCreateInput!) {
                traceCreate(input: $input) {
                    ... on Trace {
                        id
                        signalId
                        signalName
                    }
                }
            }
        """
        )
        input = {
            "fileId": file_id,
            "signalId": signal_id,
            "signalName": signal_name,
            "moduleName": module_name,
            "isVector": is_vector,
            "size": size,
        }
        variables = {"input": input}
        result = self.primitive.session.execute(mutation, variable_values=variables)
        return result

    @guard
    def file_upload(
        self,
        path: Path,
        is_public: bool = False,
        key_prefix: str = "",
        job_run_id: str = "",
    ):
        file_path = str(path.resolve())
        if path.exists() is False:
            raise FileNotFoundError(f"File not found at {file_path}")

        if is_public:
            operations = (
                """{ "query": "mutation fileUpload($input: FileUploadInput!) { fileUpload(input: $input) { ... on File { id } } }", "variables": { "input": { "fileObject": null, "isPublic": true, "filePath": \""""
                + file_path
                + """\", "keyPrefix": \""""
                + key_prefix
                + """\", "jobRunId": \""""
                + job_run_id
                + """\" } } }"""
            )  # noqa

        else:
            operations = (
                """{ "query": "mutation fileUpload($input: FileUploadInput!) { fileUpload(input: $input) { ... on File { id } } }", "variables": { "input": { "fileObject": null, "isPublic": false, "filePath": \""""
                + file_path
                + """\", "keyPrefix": \""""
                + key_prefix
                + """\", "jobRunId": \""""
                + job_run_id
                + """\" } } }"""
            )  # noqa
        body = {
            "operations": ("", operations),
            "map": ("", '{"fileObject": ["variables.input.fileObject"]}'),
            "fileObject": (path.name, open(path, "rb")),
        }

        session = create_requests_session(self.primitive.host_config)
        transport = self.primitive.host_config.get("transport")
        url = f"{transport}://{self.primitive.host}/"
        response = session.post(url, files=body)
        return response
