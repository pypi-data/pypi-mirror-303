#! /usr/bin/env bash

function abcli_mlflow_tags() {
    local task=$1

    if [[ "$task" == "help" ]]; then
        abcli_mlflow_tags_clone "$@"
        abcli_mlflow_tags_get "$@"
        abcli_mlflow_tags_search "$@"
        abcli_mlflow_tags_set "$@"
        return
    fi

    local function_name=abcli_mlflow_tags_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    abcli_log_error "@mlflow: tags: $task: command not found."
    return 1
}

abcli_source_caller_suffix_path /tags
