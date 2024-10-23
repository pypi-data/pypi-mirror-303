from typing import Optional
from gql import gql


from primitive.utils.actions import BaseAction
from ..utils.auth import guard


class Organizations(BaseAction):
    @guard
    def get_organizations(
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

            fragment OrganizationFragment on Organization {
                id
                pk
                slug
                name
                createdAt
                updatedAt
            }

            query organizations(
                $before: String
                $after: String
                $first: Int
                $last: Int
                $filters: OrganizationFilters
                $order: OrganizationOrder
            ) {
                organizations(
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
                            ...OrganizationFragment
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
            "order": {
                "createdAt": "DESC",
            },
        }

        result = self.primitive.session.execute(
            query, variable_values=variables, get_execution_result=True
        )
        organizations = [edge["node"] for edge in result.data["organizations"]["edges"]]
        return organizations
