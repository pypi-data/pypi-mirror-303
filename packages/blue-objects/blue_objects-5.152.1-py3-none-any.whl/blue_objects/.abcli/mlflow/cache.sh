#! /usr/bin/env bash

function abcli_mlflow_cache() {
    local task=$(abcli_unpack_keyword $1 help)
    local keyword=$2

    if [ "$task" == "help" ]; then
        abcli_mlflow_cache read "$@"
        abcli_mlflow_cache write "$@"
        return
    fi

    if [ "$task" == "read" ]; then
        if [[ "$keyword" == "help" ]]; then
            abcli_show_usage "@mlflow cache read$ABCUL<keyword>" \
                "read mlflow.cache[<keyword>]."
            return
        fi

        abcli_mlflow_tags get \
            $keyword \
            --tag referent \
            "${@:3}"

        return
    fi

    if [ "$task" == "write" ]; then
        if [[ "$keyword" == "help" ]]; then
            abcli_show_usage "@mlflow cache write$ABCUL<keyword> <value>" \
                "write mlflow.cache[<keyword>]=value."
            return
        fi

        local value=$3

        abcli_mlflow_tags set \
            $keyword \
            referent=$value \
            "${@:4}"

        return
    fi

    abcli_log_error "@mlflow: cache: $task: command not found."
    return 1
}
