#! /usr/bin/env bash

function abcli_mlflow_tags_set() {
    local object_name=$(abcli_clarify_object $1 .)

    if [[ "$object_name" == "help" ]]; then
        options="<keyword-1>=<value>,<keyword-2>,~<keyword-3>"
        abcli_show_usage "@mlflow tags set$ABCUL[.|<object-name>]$ABCUL[$options]" \
            "set tags in mlflow."
        return
    fi

    local tags=$2

    python3 -m blue_objects.mlflow \
        set_tags \
        --object_name $object_name \
        --tags "$tags" \
        "${@:3}"
}
