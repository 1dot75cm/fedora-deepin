#!/bin/bash

ARCHS=("fedora-24-i386" "fedora-24-x86_64" "fedora-25-i386" "fedora-25-x86_64" "fedora-rawhide-i386" "fedora-rawhide-x86_64")
PACKAGE=$1
RESULT_DIR=/tmp/build_$(date +%Y%m%d_%H%M)
# COPR specific config
COPR_PROJECT=deepin

function buildPackage()
{
  local package=$1

  # Download source for given package
  spectool -g -R SPECS/${package}.spec
  
  if [ $? == 0 ]; then
    for arch in ${ARCHS[@]}; do
      rm -rf ${RESULT_DIR}
      mkdir -p ${RESULT_DIR}
      mock -r ${arch} --spec=SPECS/${package}.spec --sources=SOURCES/ --buildsrpm --resultdir=${RESULT_DIR}
      ###
      rpmfile=$(grep 'src.rpm' ${RESULT_DIR}/build.log | head -n 1 | sed -e 's#^.*/##g')
      upload2Copr "${arch}" "${RESULT_DIR}/${rpmfile}"
      exit
    done
  else
    echo "An error occured. Exiting..."
    exit 1
  fi
}

function upload2Copr()
{
  local arch=$1
  local package=$2

  copr-cli build -r ${arch} ${COPR_PROJECT} ${package}
}

buildPackage $PACKAGE

#for pkg in $(ls -1 ./SPECS/*.spec); do
#  spectool -g -R $pkg
  # rpmbuild -ba $pkg
# done

