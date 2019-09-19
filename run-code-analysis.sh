#!/bin/bash

declare -a RESULT

# specifies a set of variables to declare CLI output color
FAILED_OUT="\033[0;31m"
PASSED_OUT="\033[0;32m"
NONE_OUT="\033[0m"

# specifies a set of variables to declare files to be used for code assessment
PROJECT_FILES="./"
TESTS_FILES="tests"
LIB_FILES="mock"
PY_FILES="*.py"


function store_failures {
    RESULT+=("$1")
}


function remove_pycache_trash {
    local PYCACHE_DIR="__pycache__"
    echo "Removing ${PYCACHE_DIR} directories if present ..."
    ( find . -d -name ${PYCACHE_DIR} | xargs rm -r ) || echo -e "No ${PYCACHE_DIR} found"
}


function remove_analysis_trash {
    local PYTEST_CACHE_DIR='.pytest_cache'
    local MYPY_CACHE_DIR='.mypy_cache'
    echo "Removing code analysis trash if present ..."
    [[ -d "$PYTEST_CACHE_DIR" ]] && rm -rf ${PYTEST_CACHE_DIR} && echo "pytest trash is removed"
    [[ -d "$MYPY_CACHE_DIR" ]] && rm -rf ${MYPY_CACHE_DIR} && echo "mypy trash is removed"
}


function install_dependencies {
   echo "Installing python code analysis packages ..." \
   && ( pip install --no-cache-dir --upgrade pip ) \
   && ( pip install --no-cache-dir -r requirements-dev.txt )
}


function run_unittests {
    echo "Running unittests ..." && ( pytest "${TESTS_FILES}" )
}


function run_flake8_analysis() {
    echo "Running flake8 analysis ..." && ( flake8 "${PROJECT_FILES}" )
}


function run_black_analysis() {
    echo "Running black analysis ..." && ( black --check "${PROJECT_FILES}" )
}


function run_pylint_analysis() {
    echo "Running pylint analysis ..." && ( pylint $(find "${PROJECT_FILES}" -iname "${PY_FILES}") )
}


function run_mypy_analysis() {
    echo "Running mypy analysis ..." && ( mypy --package "${LIB_FILES}" ) && ( mypy --package "${TESTS_FILES}" )
}



function run_code_analysis {
    echo "Running code analysis ..."
    remove_pycache_trash
    run_unittests || store_failures "Unittests are failed!"
    run_pylint_analysis || store_failures "pylint analysis is failed!"
    run_mypy_analysis || store_failures "mypy analysis is failed!"
    run_flake8_analysis || store_failures "flake8 analysis is failed!"
    run_black_analysis || store_failures "black analysis is failed!"

    if [[ ${#RESULT[@]} -ne 0 ]];
        then echo -e "${FAILED_OUT}Some errors occurred while analysing the code quality.${NONE_OUT}"
        for failed_item in "${RESULT[@]}"; do
            echo -e "${FAILED_OUT}- ${failed_item}${NONE_OUT}"
        done
        remove_analysis_trash
        exit 1
    fi
    remove_analysis_trash
    echo -e "${PASSED_OUT}Code analysis is passed${NONE_OUT}"
}


function main() {
    if [[ "$1" == "install-dependencies" ]];
        then install_dependencies || store_failures "Python packages installation is failed!";
    fi
    run_code_analysis
}


main $@