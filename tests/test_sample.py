from navability.entities.NavAbilityClient import (
    NavAbilityHttpsClient,
    NavAbilityWebsocketClient,
)


def test_client_creds_token_query_params_regression(
    navability_wss_client: NavAbilityWebsocketClient
):
    pass