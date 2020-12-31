#!/bin/bash

iter=$1

mv filestotransfer/* .
cp /eos/user/c/cmantill/samples/CMSSW_5_3_26_phil.tgz .
cp /eos/user/c/cmantill/samples/CMSSW_5_3_32_cristina.tgz .

export SCRAM_ARCH=slc6_amd64_gcc472

scramv1 project CMSSW CMSSW_5_3_32
cd CMSSW_5_3_32/src
eval `scramv1 runtime -sh`
cd -

rnumber=$((1 + $RANDOM % 9999))

cmsRun gen_wqq.py rseed=$rnumber
cmsRun sim.py
cmsRun hlt.py
cmsRun reco.py

cp step2.root /eos/user/c/cmantill/samples/wqq/step2_$iter_$rnumber.root

mkdir phil
cd phil
scramv1 project CMSSW CMSSW_5_3_26
tar -xzf ../CMSSW_5_3_26_phil.tgz
cd CMSSW_5_3_26/src/
eval `scramv1 runtime -sh`
cd -
cd ..
cmsRun bacon.py
cp Bacon.root /eos/user/c/cmantill/samples/wqq/Bacon_$iter_$rnumber.root

mkdir cristina
cd cristina
scramv1 project CMSSW CMSSW_5_3_32
tar -xzf ../CMSSW_5_3_32_cristina.tgz
cd CMSSW_5_3_32/src/
eval `scramv1 runtime -sh`
cd -
cd ..
runDJ -1 Bacon.root 1 cristina/CMSSW_5_3_32/src/BaconAnalyzer/Json/Cert_190456-208686_8TeV_22Jan2013ReReco_Collisions12_JSON.txt 1 59.6
cp Output.root /eos/user/c/cmantill/samples/wqq/Output_$iter_$rnumber.root

rm *.tgz
rm *.root
rm *.tree
rm fort.15
rm -rf phil
rm -rf cristina
