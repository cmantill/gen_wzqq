#!/bin/bash

N=$2
exe=$1
echo  "submitting "$N"  using "$exe
echo "executable              = "$exe > tmp.sub
echo "arguments               = \$(ProcId)" >> tmp.sub
echo "transfer_input_files    = filestotransfer" >> tmp.sub
echo "output                  = output/\$(ClusterId).\$(ProcId).out" >> tmp.sub
echo "error                   = error/\$(ClusterId).\$(ProcId).err"  >> tmp.sub
echo "log                     = log/\$(ClusterId).\$(ProcId).log" >> tmp.sub
echo "x509userproxy           = ${X509_USER_PROXY}" >> tmp.sub
echo "use_x509userproxy       = True" >> tmp.sub
echo "+JobFlavour = \"nextweek\"  " >> tmp.sub
echo "queue "$N 
echo "queue "$N >> tmp.sub
condor_submit tmp.sub
