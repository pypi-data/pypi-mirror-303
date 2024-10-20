#! /usr/bin/env bash

function abcli_mlflow_tags_search() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local args="[--count <-1>]$ABCUL[--delim <space>]$ABCUL[--log <0>]$ABCUL[--offset <0>]"

        options="explicit"
        abcli_show_usage "@mlflow tags search$ABCUL[$options]$ABCUL$args$ABCUL[--filter_string <filter-string>]" \
            "search mlflow for <filter-string>${ABCUL2}https://www.mlflow.org/docs/latest/search-experiments.html."

        options="<keyword-1>=<value-1>,<keyword-2>,~<keyword-3>"
        abcli_show_usage "@mlflow tags search$ABCUL[$options]$ABCUL$args" \
            "search mlflow."
        return
    fi

    local is_explicit=$(abcli_option_int "$options" explicit 0)

    python3 -m blue_objects.mlflow \
        search \
        --explicit_query $is_explicit \
        --tags "$options" \
        "${@:2}"
}
