#! /usr/bin/env bash

function blue_objects() {
    local task=$(abcli_unpack_keyword $1 help)

    if [[ "$2" == help ]]; then
        abcli_show_usage_2 blue_objects $task
        return
    fi

    abcli_generic_task \
        plugin=blue_objects,task=$task \
        "${@:2}"
}

abcli_log $(blue_objects version --show_icon 1)
