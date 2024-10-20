#! /usr/bin/env bash

function abcli_mlflow_list_registered_models() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        abcli_show_usage "@mlflow list_registered_models" \
            "list mlflow registered models."
        return
    fi

    python3 -m blue_objects.mlflow \
        list_registered_models \
        "${@:2}"
}
