#! /usr/bin/env bash

function test_blue_objects_help() {
    local options=$1

    local module
    for module in \
        "abcli cache" \
        "abcli clone" \
        "abcli download" \
        "abcli gif" \
        "abcli host" \
        "abcli metadata" \
        \
        "abcli mlflow" \
        "abcli mlflow browse" \
        "abcli mlflow cache" \
        "abcli mlflow get_id" \
        "abcli mlflow get_run_id" \
        "abcli mlflow list_registered_models" \
        "abcli mlflow log_artifacts" \
        "abcli mlflow log_run" \
        "abcli mlflow rm" \
        "abcli mlflow run" \
        "abcli mlflow tags" \
        "abcli mlflow tags clone" \
        "abcli mlflow tags get" \
        "abcli mlflow tags search" \
        "abcli mlflow tags set" \
        "abcli mlflow test" \
        "abcli mlflow transition" \
        \
        "abcli mysql" \
        "abcli mysql_cache" \
        "abcli mysql_relations" \
        "abcli mysql_tags" \
        \
        "abcli object" \
        "abcli publish" \
        "abcli select" \
        "abcli storage" \
        "abcli tags" \
        "abcli upload" \
        "blue_objects" \
        "blue_objects pytest"; do
        abcli_eval ,$options \
            $module help
        [[ $? -ne 0 ]] && return 1
    done

    return 0
}
