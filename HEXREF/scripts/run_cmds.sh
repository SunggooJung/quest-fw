#!/bin/csh

if !($?BUILD_ROOT) then
    set curdir = "${PWD}"
    setenv BUILD_ROOT `dirname $0`/../..
    cd $BUILD_ROOT
    setenv BUILD_ROOT ${PWD}
    cd ${curdir}
endif

${BUILD_ROOT}/Gse/bin/run_cmds.sh --addr 192.168.2.1 --port 50010 --dictionary ${BUILD_ROOT}/Gse/generated/HEXREF $*
