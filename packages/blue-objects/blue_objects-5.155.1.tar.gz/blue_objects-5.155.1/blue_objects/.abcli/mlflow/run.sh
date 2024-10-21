#! /usr/bin/env bash

function abcli_mlflow_run() {
    local object_name=$1

    if [[ "$object_name" == "help" ]]; then
        abcli_show_usage "@mlflow run start|end$ABCUL[.|<object-name>]" \
            "start|end mlflow run."
        return
    fi

    object_name=$(abcli_clarify_object $object_name .)

    python3 -m blue_objects.mlflow \
        start_end_run \
        --object_name $object_name \
        --start_end "$2" \
        "${@:3}"
}
