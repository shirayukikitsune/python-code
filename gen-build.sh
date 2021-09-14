#!/usr/bin/env bash

TEMPLATE_LIBRARY='py_library(
    name = "src_lib",
    srcs = [${SOURCE_FILES}],
    visibility = ["//visibility:public"],
)'

TEMPLATE_BINARY='py_binary(
    name = "${DIR_NAME}",
    srcs = [${SOURCE_FILES}],
    main = "main.py"
)'

TEMPLATE_TESTS='py_test(
    name = "src_test_${TEST_FILE_NO_EXT}",
    srcs = ["${TEST_FILE}"],
    data = [${DATA_DIRS}
    ],
    deps = [${DEPENDENCIES}
    ],
    main = "${TEST_FILE}"
)'

gen_dir_main() {
  DIR=$1
  export DIR_NAME=$(basename $DIR)
  FILES=$(find $DIR -type f -name '*.py' -print | tr '\n' ' ')
  SOURCE_FILES=""
  HAS_MAIN=0
  for FILE in $FILES ; do
    SOURCE_FILES="\"$(basename $FILE)\",$SOURCE_FILES"
    if [[ "$(basename $FILE)" == "main.py" ]]; then
      HAS_MAIN=1
      echo "Found main.py, generating binary"
    fi
  done
  if [[ "$SOURCE_FILES" == "" ]]; then
    continue
  fi
  export SOURCE_FILES
  echo "$TEMPLATE_LIBRARY" | envsubst '${DIR_NAME},${SOURCE_FILES}' > "${DIR}/BUILD.bazel"
  if [[ $HAS_MAIN == 1 ]]; then
    echo "" >> "${DIR}/BUILD.bazel"
    echo "$TEMPLATE_BINARY" | envsubst '${DIR_NAME},${SOURCE_FILES}' >> "${DIR}/BUILD.bazel"
  fi
}

gen_dir_test() {
  DIR=$1
  export DIR_NAME=$(basename $DIR)
  FILES=$(find $DIR -type f -name '*.py' -print | tr '\n' ' ')

  DIRS=$(find $DIR -type d -depth 1 -name 'case*' -print)
  DATA_DIRS=""
  for DATA_DIR in $DIRS ; do
    DATA_DIRS="
        \"$(basename $DATA_DIR)\",$DATA_DIRS"
    echo "Found data dir $DATA_DIR"
  done
  export DATA_DIRS

  SOURCE_FILES=""
  echo -n "" > "${DIR}/BUILD.bazel"
  for FILE in $FILES ; do
    export TEST_FILE=$(basename $FILE)
    export TEST_FILE_NO_EXT=$(basename $FILE .py)

    DEPS=()
    while IFS= read -r line; do
      IFS=' ' read -ra tokens <<< "$line"
      if [[ "${tokens[0]}" == "import" || "${tokens[0]}" == "from" ]]; then
        DEP=$(echo "${tokens[1]}" | tr '.' '/')
        if [[ ! -d $DEP ]]; then
          DEP=$(dirname $DEP)
        fi
        if [[ ! -d $DEP || $DEP == '.' ]]; then
          continue
        fi
        echo "Found dependency ${tokens[1]}"
        DEPS+=("$DEP")
      fi
    done < $FILE

    DEPENDENCIES=""
    for DEP in ${DEPS[@]} ; do
      DEPENDENCIES="
        \"//${DEP}:src_lib\",$DEPENDENCIES"
    done
    export DEPENDENCIES

    echo "$TEMPLATE_TESTS" | envsubst '${DEPENDENCIES},${TEST_FILE},${TEST_FILE_NO_EXT},${DATA_DIRS}' >> "${DIR}/BUILD.bazel"
    echo "" >> "${DIR}/BUILD.bazel"
  done
}

GEN_TYPE=$(echo "$1" | tr '[:upper:]' '[:lower:]')
PROJECT_PATH=${2:-src/${GEN_TYPE}}

case $GEN_TYPE in
main|test)
  echo "Using generation type $GEN_TYPE"
  ;;

*)
  echo "Unsupported generation type"
  exit 1
  ;;
esac

if [[ ! -d "$PROJECT_PATH" ]]; then
  echo "Directory $PROJECT_PATH does not exist"
  exit 1
fi

echo "Scanning Python files in dir $PROJECT_PATH"

DIRECTORIES=$(find $PROJECT_PATH -type f -name '*.py' -exec dirname {} \;)

for DIR in $DIRECTORIES ; do
  echo "Reading directory $DIR"
  if [[ "$GEN_TYPE" == "main" ]]; then
    gen_dir_main $DIR
  else
    gen_dir_test $DIR
  fi
done
