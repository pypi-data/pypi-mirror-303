from gql import gql

from typing import Optional
from primitive.utils.actions import BaseAction
from ..utils.auth import guard


class Projects(BaseAction):
    @guard
    def get_projects(
        self,
        organization_id: Optional[str] = None,
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

            fragment ProjectFragment on Project {
                id
                pk
                slug
                name
                createdAt
                updatedAt
            }

            query projects(
                $before: String
                $after: String
                $first: Int
                $last: Int
                $filters: ProjectFilters
            ) {
                projects(
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
                            ...ProjectFragment
                        }
                    }
                }
            }
            """
        )

        filters = {}
        if organization_id:
            filters["organization"] = {"id": organization_id}
        if slug:
            filters["slug"] = {"exact": slug}

        variables = {
            "first": first,
            "last": last,
            "filters": filters,
        }

        result = self.primitive.session.execute(
            query, variable_values=variables, get_execution_result=True
        )
        projects = [edge["node"] for edge in result.data["projects"]["edges"]]
        return projects
