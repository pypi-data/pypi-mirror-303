#! /usr/bin/env bash

function notebooks_and_scripts_workflow_submit() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local options="$EOP~download,dryrun,${EOPE}to=$NBS_RUNNERS_LIST$EOP,~upload"
        abcli_show_usage "workflow submit$ABCUL$options$ABCUL.|<job-name>$EOPE" \
            "submit workflow."
        return
    fi

    local do_download=$(abcli_option_int "$options" download 1)
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_upload=$(abcli_option_int "$options" upload 1)
    local runner_type=$(abcli_option "$options" to generic)

    local job_name=$(abcli_clarify_object $2 .)

    [[ "$do_download" == 1 ]] &&
        abcli_download - $job_name

    abcli_log "📜 workflow.submit: $job_name -> $runner_type"

    python3 -m notebooks_and_scripts.workflow.runners \
        submit \
        --dryrun $do_dryrun \
        --job_name $job_name \
        --runner_type $runner_type
    local status="$?"

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $job_name

    [[ "$status" -ne 0 ]] && return $status

    if [[ "$runner_type" == local ]]; then
        abcli_cat $ABCLI_OBJECT_ROOT/$job_name/$job_name.sh

        abcli_eval dryrun=$do_dryrun \
            source $ABCLI_OBJECT_ROOT/$job_name/$job_name.sh
        status="$?"
    fi

    return $status
}
