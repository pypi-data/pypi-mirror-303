#! /usr/bin/env bash

function abcli_mlflow_tags_get() {
    local object_name=$(abcli_clarify_object $1 .)

    if [[ "$object_name" == "help" ]]; then
        args="[--tag <tag>]"
        abcli_show_usage "@mlflow tags get$ABCUL[.|<object-name>]$ABCUL$args" \
            "get mlflow tags|<tag> for <object-name>."
        return
    fi

    python3 -m blue_objects.mlflow \
        get_tags \
        --object_name $object_name \
        "${@:2}"
}
