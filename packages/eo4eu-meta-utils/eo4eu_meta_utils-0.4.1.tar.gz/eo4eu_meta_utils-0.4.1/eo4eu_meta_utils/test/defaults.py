
def default_kafka() -> dict:
    return {
        "image": "confluentinc/confluent-local:7.4.1",
        "hostname": "kafka",
        "container_name": "kafka",
        "ports": ["9092:9092"],
        "environment": {
            "KAFKA_ADVERTISED_LISTENERS": "PLAINTEXT://kafka:29092,PLAINTEXT_HOST://localhost:9092",
            "KAFKA_CONTROLLER_QUORUM_VOTERS": "1@kafka:29093",
            "KAFKA_LISTENERS": "PLAINTEXT://kafka:29092,CONTROLLER://kafka:29093,PLAINTEXT_HOST://0.0.0.0:9092",
        },
        "healthcheck": {
            "test": ["CMD", "sleep", "1"],
            "retries": 0,
            "start_period": "15s",
            "start_interval": "0s"
        }
    }


def default_autotest(
    config_path: str = "${PWD}/test_config.py",
    name: str = "at-service",
    command: str = "autotest-setup",
    depends_on: dict|None = None,
    healthcheck: dict|None = None
) -> dict:
    if depends_on is None:
        depends_on = {}

    result = {
        "hostname": name,
        "container_name": name,
        "image": "autotest-service:latest",
        "command": command,
        "environment": [
            "BOOTSTRAP_SERVERS=kafka:29092",
            "GROUP_ID=autotest-service",
        ],
        "depends_on": {
            "kafka": {"condition": "service_healthy"},
        } | depends_on,
        "volumes": [
            f"{config_path}:/var/config/test_config.py"
        ]
    }
    if healthcheck is not None:
        result["healthcheck"] = healthcheck

    return result
