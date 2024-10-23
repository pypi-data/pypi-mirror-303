from ..graphql.sdk import create_session
import sys


def guard(func):
    def wrapper(self, *args, **kwargs):
        if self.primitive.session is None:
            token = self.primitive.host_config.get("token")
            transport = self.primitive.host_config.get("transport")
            fingerprint = self.primitive.host_config.get("fingerprint")

            if not token or not transport:
                print(
                    "CLI is not configured. Run primitive config to add an auth token."
                )
                sys.exit(1)

            self.primitive.session = create_session(
                host=self.primitive.host,
                token=token,
                transport=transport,
                fingerprint=fingerprint,
            )

        return func(self, *args, **kwargs)

    return wrapper
