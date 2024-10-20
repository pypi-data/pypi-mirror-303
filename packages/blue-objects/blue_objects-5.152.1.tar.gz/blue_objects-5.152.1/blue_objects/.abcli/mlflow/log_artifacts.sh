#! /usr/bin/env bash

function abcli_mlflow_log_artifacts() {
    local object_name=$1

    if [[ "$object_name" == "help" ]]; then
        local args="[--model_name <model-name>]"
        abcli_show_usage "@mlflow log_artifacts$ABCUL[.|<object-name>]$ABCUL$args" \
            "<object-name> -artifacts-> mlflow."
        return
    fi

    object_name=$(abcli_clarify_object $object_name .)

    python3 -m blue_objects.mlflow \
        log_artifacts \
        --object_name $object_name \
        "${@:2}"
}
