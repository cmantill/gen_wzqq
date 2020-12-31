# Auto generated configuration file
# using: 
# Revision: 1.381.2.28 
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: Hadronizer_MgmMatchTuneZ2star_8TeV_madgraph_tauola_cff.py --step GEN --beamspot Realistic8TeVCollision --conditions START50_V13::All --pileup NoPileUp --datamix NODATAMIXER --eventcontent RAWSIM --datatier GEN-SIM --no_exec --filein events.lhe
import FWCore.ParameterSet.Config as cms
import random

process = cms.Process('GEN')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

# Input source
process.source = cms.Source("EmptySource")


process.options = cms.untracked.PSet(

)

# Output definition
#random.seed(123456)
ran=random.randint(1,123456)
process.LHEoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.LHEEventContent.outputCommands,
    fileName = cms.untracked.string('file:lhe.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('LHE')
    )
)

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'START53_V7C::All', '')
process.GlobalTag = GlobalTag(process.GlobalTag, 'START53_V14B::All', '')

# Path and EndPath definitions
process.externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
                                             args = cms.vstring('/afs/cern.ch/user/c/cmantill/work/public/samples/genproductions/bin/MadGraph5_aMCatNLO/ZJetsToQQ_HT400ToInf_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz','100','%i'%ran,'slc7_amd64_gcc700','CMSSW_10_6_19'),
                                             nEvents = cms.untracked.uint32(100),
                                             numberOfParameters = cms.uint32(5),
                                             outputFile = cms.string('cmsgrid_final.lhe'),
                                             scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)

process.lhe_step = cms.Path(process.externalLHEProducer)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.LHEoutput_step = cms.EndPath(process.LHEoutput)

# Schedule definition
process.schedule = cms.Schedule(process.lhe_step,process.endjob_step,process.LHEoutput_step)

process.RandomNumberGeneratorService.externalLHEProducer.initialSeed = 123456
