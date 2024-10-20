#! /usr/bin/env bash

export MLFLOW_TRACKING_URI="databricks"

function abcli_mlflow() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ "$task" == "help" ]; then
        abcli_mlflow_browse "$@"
        abcli_mlflow_cache "$@"
        abcli_mlflow get_id "$@"
        abcli_mlflow get_run_id "$@"
        abcli_mlflow_list_registered_models "$@"
        abcli_mlflow_log_artifacts "$@"
        abcli_mlflow_log_run "$@"
        abcli_mlflow rm "$@"
        abcli_mlflow_run "$@"
        abcli_mlflow_tags "$@"
        abcli_mlflow_test "$@"
        abcli_mlflow_transition "$@"
        return
    fi

    local function_name=abcli_mlflow_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    if [[ ",get_id,get_run_id,rm," == *",$task,"* ]]; then
        local object_name=$(abcli_clarify_object $2 .)

        if [[ "$object_name" == "help" ]]; then
            local args

            if [[ "$task" == "get_id" ]]; then
                abcli_show_usage "@mlflow get_id$ABCUL[.|<object-name>]" \
                    "get mlflow id for <object-name>."

            elif [[ "$task" == "get_run_id" ]]; then
                args="[--count <1>]$ABCUL[--delim <space>]$ABCUL[--offset <0>]"

                abcli_show_usage "@mlflow get_run_id$ABCUL[.|<object-name>]$ABCUL$args" \
                    "get mlflow run ids for <object-name>."

            elif [[ "$task" == "rm" ]]; then
                abcli_show_usage "@mlflow rm$ABCUL[.|<object-name>]" \
                    "rm <object-name> from mlflow."

            else
                # should never reach here
                abcli_log_error "@mlflow: $task: command not found."
                return 1
            fi
            return 0
        fi

        python3 -m blue_objects.mlflow \
            $task \
            --object_name $object_name \
            "${@:3}"
        return
    fi

    abcli_log_error "@mlflow: $task: command not found."
    return 1
}

abcli_source_caller_suffix_path /mlflow
