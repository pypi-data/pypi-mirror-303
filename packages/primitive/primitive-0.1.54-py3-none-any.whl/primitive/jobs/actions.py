from typing import List, Optional
from gql import gql


from primitive.utils.actions import BaseAction
from ..utils.auth import guard


class Jobs(BaseAction):
    @guard
    def get_jobs(
        self,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        job_id: Optional[str] = None,
        slug: Optional[str] = None,
        first: Optional[int] = 1,
        last: Optional[int] = None,
    ):
        query = gql(
            """ 
            fragment PageInfoFragment on PageInfo {
                hasNextPage
                hasPreviousPage
                startCursor
                endCursor
            }

            fragment JobFragment on Job {
                id
                pk
                slug
                name
                createdAt
                updatedAt
            }

            query jobs(
                $before: String
                $after: String
                $first: Int
                $last: Int
                $filters: JobFilters
            ) {
                jobs(
                    before: $before
                    after: $after
                    first: $first
                    last: $last
                    filters: $filters
                ) {
                    totalCount
                    pageInfo {
                        ...PageInfoFragment
                    }
                    edges {
                        cursor
                        node {
                            ...JobFragment
                        }
                    }
                }
            }
            """
        )

        filters = {}
        if organization_id:
            filters["organization"] = {"id": organization_id}
        if project_id:
            filters["project"] = {"id": project_id}
        if job_id:
            filters["id"] = job_id
        if slug:
            filters["slug"] = {"exact": slug}

        variables = {
            "first": first,
            "last": last,
            "filters": filters,
            "order": {
                "createdAt": "DESC",
            },
        }

        result = self.primitive.session.execute(
            query, variable_values=variables, get_execution_result=True
        )
        jobs = [edge["node"] for edge in result.data["jobs"]["edges"]]
        return jobs

    def get_job_runs(
        self,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        job_id: Optional[str] = None,
        reservation_id: Optional[str] = None,
        git_commit_id: Optional[str] = None,
        status: Optional[str] = None,
        conclusion: Optional[str] = None,
        first: Optional[int] = 1,
        last: Optional[int] = None,
    ):
        query = gql(
            """
fragment PageInfoFragment on PageInfo {
  hasNextPage
  hasPreviousPage
  startCursor
  endCursor
}

fragment JobRunFragment on JobRun {
  id
  pk
  createdAt
  updatedAt
  completedAt
  startedAt
  status
  conclusion
  job {
    id
    pk
    slug
    name
    createdAt
    updatedAt
  }
  jobSettings {
    containerArgs
    rootDirectory
  }
  gitCommit {
    sha
    branch
    repoFullName
  }
}

query jobRuns(
  $before: String
  $after: String
  $first: Int
  $last: Int
  $filters: JobRunFilters
  $order: JobRunOrder
) {
  jobRuns(
    before: $before
    after: $after
    first: $first
    last: $last
    filters: $filters
    order: $order
  ) {
    totalCount
    pageInfo {
      ...PageInfoFragment
    }
    edges {
      cursor
      node {
        ...JobRunFragment
      }
    }
  }
}
"""
        )

        filters = {}
        if organization_id:
            filters["organization"] = {"id": organization_id}
        if project_id:
            filters["project"] = {"id": project_id}
        if job_id:
            filters["job"] = {"id": job_id}
        if reservation_id:
            filters["reservation"] = {"id": reservation_id}
        if git_commit_id:
            filters["gitCommit"] = {"id": git_commit_id}
        if status:
            filters["status"] = {"exact": status}
        if conclusion:
            filters["conclusion"] = {"exact": status}

        variables = {
            "first": first,
            "last": last,
            "filters": filters,
            "order": {
                "createdAt": "DESC",
            },
        }

        result = self.primitive.session.execute(query, variable_values=variables)
        return result

    @guard
    def get_job_run(self, id: str):
        query = gql(
            """
            fragment JobRunFragment on JobRun {
                id
                pk
                createdAt
                updatedAt
                completedAt
                startedAt
                status
                conclusion
                job {
                    id
                    pk
                    slug
                    name
                    createdAt
                    updatedAt
                }
                gitCommit {
                    sha
                    branch
                    repoFullName
                }
                jobSettings {
                    containerArgs
                    rootDirectory
                }
            }

            query jobRun($id: GlobalID!) {
                jobRun(id: $id) {
                    ...JobRunFragment
                }
            }
            """
        )
        variables = {"id": id}
        result = self.primitive.session.execute(query, variable_values=variables)
        return result

    @guard
    def job_run_update(
        self,
        id: str,
        status: str = None,
        conclusion: str = None,
        file_ids: Optional[List[str]] = [],
    ):
        mutation = gql(
            """
            mutation jobRunUpdate($input: JobRunUpdateInput!) {
                jobRunUpdate(input: $input) {
                    ... on JobRun {
                        id
                        status
                        conclusion
                    }
                }
            }
        """
        )
        input = {"id": id}
        if status:
            input["status"] = status
        if conclusion:
            input["conclusion"] = conclusion
        if file_ids and len(file_ids) > 0:
            input["files"] = file_ids
        variables = {"input": input}
        result = self.primitive.session.execute(mutation, variable_values=variables)
        return result

    @guard
    def github_access_token_for_job_run(self, job_run_id: str):
        query = gql(
            """
query ghAppTokenForJobRun($jobRunId: GlobalID!) {
    ghAppTokenForJobRun(jobRunId: $jobRunId)
}
"""
        )
        variables = {"jobRunId": job_run_id}
        result = self.primitive.session.execute(query, variable_values=variables)
        return result["ghAppTokenForJobRun"]

    def get_latest_job_run_for_job(
        self, job_slug: Optional[str] = None, job_id: Optional[str] = None
    ):
        if not job_slug and not job_id:
            raise ValueError("job_slug or job_id is required")
        jobs_results = self.get_jobs(slug=job_slug)
        jobs = [edge["node"] for edge in jobs_results.data["jobs"]["edges"]]

        job_id = jobs.id
        job_run_results = self.get_job_runs(job_id=job_id, first=1)
        job_run = [edge["node"] for edge in job_run_results.data["job_runs"]["edges"]][
            0
        ]
        return job_run

    def job_run_start(
        self,
        job_slug: str,
        job_id: str,
    ):
        if not job_slug and not job_id:
            raise ValueError("job_slug or job_id is required")

        self.get_jobs(slug=job_slug)

    @guard
    def get_job_status(self, id: str):
        query = gql(
            """
            fragment JobRunFragment on JobRun {
                id
                status
            }

            query jobRun($id: GlobalID!) {
                jobRun(id: $id) {
                    ...JobRunFragment
                }
            }
            """
        )
        variables = {"id": id}
        result = self.primitive.session.execute(query, variable_values=variables)
        return result
