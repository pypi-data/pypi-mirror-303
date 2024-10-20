#! /usr/bin/env bash

function abcli_mlflow_log_run() {
    local object_name=$1

    if [[ "$object_name" == "help" ]]; then
        abcli_show_usage "@mlflow log_run$ABCUL[.|<object-name>]" \
            "<object-name> -run-> mlflow."
        return
    fi

    object_name=$(abcli_clarify_object $object_name .)

    python3 -m blue_objects.mlflow \
        log_run \
        --object_name $object_name \
        "${@:2}"
}
