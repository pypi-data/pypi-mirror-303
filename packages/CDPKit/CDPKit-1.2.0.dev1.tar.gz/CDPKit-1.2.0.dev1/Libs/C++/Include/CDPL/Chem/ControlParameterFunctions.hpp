/* 
 * ControlParameterFunctions.hpp 
 *
 * This file is part of the Chemical Data Processing Toolkit
 *
 * Copyright (C) 2003 Thomas Seidel <thomas.seidel@univie.ac.at>
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this library; see the file COPYING. If not, write to
 * the Free Software Foundation, Inc., 59 Temple Place - Suite 330,
 * Boston, MA 02111-1307, USA.
 */

/**
 * \file
 * \brief Declaration of convenience functions for control-parameter handling.
 */

#ifndef CDPL_CHEM_CONTROLPARAMETERFUNCTIONS_HPP
#define CDPL_CHEM_CONTROLPARAMETERFUNCTIONS_HPP

#include <string>
#include <cstddef>

#include "CDPL/Chem/APIPrefix.hpp"

#include "CDPL/Chem/MultiConfMoleculeInputProcessor.hpp"


namespace CDPL
{

    namespace Base
    {

        class ControlParameterContainer;
    }

    namespace Chem
    {

        CDPL_CHEM_API bool getOrdinaryHydrogenDepleteParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setOrdinaryHydrogenDepleteParameter(Base::ControlParameterContainer& cntnr, bool deplete);

        CDPL_CHEM_API bool hasOrdinaryHydrogenDepleteParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearOrdinaryHydrogenDepleteParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API std::size_t getCoordinatesDimensionParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setCoordinatesDimensionParameter(Base::ControlParameterContainer& cntnr, std::size_t dim);

        CDPL_CHEM_API bool hasCoordinatesDimensionParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearCoordinatesDimensionParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API bool getStrictErrorCheckingParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setStrictErrorCheckingParameter(Base::ControlParameterContainer& cntnr, bool strict);

        CDPL_CHEM_API bool hasStrictErrorCheckingParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearStrictErrorCheckingParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API const std::string& getRecordSeparatorParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setRecordSeparatorParameter(Base::ControlParameterContainer& cntnr, const std::string& sep);

        CDPL_CHEM_API bool hasRecordSeparatorParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearRecordSeparatorParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API bool getBondMemberSwapStereoFixParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setBondMemberSwapStereoFixParameter(Base::ControlParameterContainer& cntnr, bool fix);

        CDPL_CHEM_API bool hasBondMemberSwapStereoFixParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearBondMemberSwapStereoFixParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API bool getCheckLineLengthParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setCheckLineLengthParameter(Base::ControlParameterContainer& cntnr, bool check);

        CDPL_CHEM_API bool hasCheckLineLengthParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearCheckLineLengthParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API unsigned int getMDLCTABVersionParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setMDLCTABVersionParameter(Base::ControlParameterContainer& cntnr, unsigned int version);

        CDPL_CHEM_API bool hasMDLCTABVersionParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearMDLCTABVersionParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API bool getMDLIgnoreParityParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setMDLIgnoreParityParameter(Base::ControlParameterContainer& cntnr, bool ignore);

        CDPL_CHEM_API bool hasMDLIgnoreParityParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearMDLIgnoreParityParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API bool getMDLUpdateTimestampParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setMDLUpdateTimestampParameter(Base::ControlParameterContainer& cntnr, bool update);

        CDPL_CHEM_API bool hasMDLUpdateTimestampParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearMDLUpdateTimestampParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API bool getMDLTrimStringsParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setMDLTrimStringsParameter(Base::ControlParameterContainer& cntnr, bool trim);

        CDPL_CHEM_API bool hasMDLTrimStringsParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearMDLTrimStringsParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API bool getMDLTrimLinesParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setMDLTrimLinesParameter(Base::ControlParameterContainer& cntnr, bool trim);

        CDPL_CHEM_API bool hasMDLTrimLinesParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearMDLTrimLinesParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API bool getMDLTruncateStringsParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setMDLTruncateStringsParameter(Base::ControlParameterContainer& cntnr, bool trunc);

        CDPL_CHEM_API bool hasMDLTruncateStringsParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearMDLTruncateStringsParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API bool getMDLTruncateLinesParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setMDLTruncateLinesParameter(Base::ControlParameterContainer& cntnr, bool trunc);

        CDPL_CHEM_API bool hasMDLTruncateLinesParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearMDLTruncateLinesParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API unsigned int getMDLRXNFileVersionParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setMDLRXNFileVersionParameter(Base::ControlParameterContainer& cntnr, unsigned int version);

        CDPL_CHEM_API bool hasMDLRXNFileVersionParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearMDLRXNFileVersionParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API bool getMDLOutputConfEnergyToEnergyFieldParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setMDLOutputConfEnergyToEnergyFieldParameter(Base::ControlParameterContainer& cntnr, bool output);

        CDPL_CHEM_API bool hasMDLOutputConfEnergyToEnergyFieldParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearMDLOutputConfEnergyToEnergyFieldParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API bool getMDLOutputConfEnergyAsSDEntryParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setMDLOutputConfEnergyAsSDEntryParameter(Base::ControlParameterContainer& cntnr, bool output);

        CDPL_CHEM_API bool hasMDLOutputConfEnergyAsSDEntryParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearMDLOutputConfEnergyAsSDEntryParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API const std::string& getMDLConfEnergySDTagParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setMDLConfEnergySDTagParameter(Base::ControlParameterContainer& cntnr, const std::string& tag);

        CDPL_CHEM_API bool hasMDLConfEnergySDTagParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearMDLConfEnergySDTagParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API bool getJMESeparateComponentsParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setJMESeparateComponentsParameter(Base::ControlParameterContainer& cntnr, bool separate);

        CDPL_CHEM_API bool hasJMESeparateComponentsParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearJMESeparateComponentsParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API const std::string& getSMILESRecordFormatParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setSMILESRecordFormatParameter(Base::ControlParameterContainer& cntnr, const std::string& format);

        CDPL_CHEM_API bool hasSMILESRecordFormatParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearSMILESRecordFormatParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API bool getSMILESWriteCanonicalFormParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setSMILESWriteCanonicalFormParameter(Base::ControlParameterContainer& cntnr, bool write);

        CDPL_CHEM_API bool hasSMILESWriteCanonicalFormParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearSMILESWriteCanonicalFormParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API bool getSMILESWriteKekuleFormParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setSMILESWriteKekuleFormParameter(Base::ControlParameterContainer& cntnr, bool write);

        CDPL_CHEM_API bool hasSMILESWriteKekuleFormParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearSMILESWriteKekuleFormParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API bool getSMILESWriteAtomStereoParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setSMILESWriteAtomStereoParameter(Base::ControlParameterContainer& cntnr, bool write);

        CDPL_CHEM_API bool hasSMILESWriteAtomStereoParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearSMILESWriteAtomStereoParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API bool getSMILESWriteBondStereoParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setSMILESWriteBondStereoParameter(Base::ControlParameterContainer& cntnr, bool write);

        CDPL_CHEM_API bool hasSMILESWriteBondStereoParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearSMILESWriteBondStereoParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API bool getSMILESWriteRingBondStereoParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setSMILESWriteRingBondStereoParameter(Base::ControlParameterContainer& cntnr, bool write);

        CDPL_CHEM_API bool hasSMILESWriteRingBondStereoParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearSMILESWriteRingBondStereoParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API std::size_t getSMILESMinStereoBondRingSizeParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setSMILESMinStereoBondRingSizeParameter(Base::ControlParameterContainer& cntnr, std::size_t min_size);

        CDPL_CHEM_API bool hasSMILESMinStereoBondRingSizeParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearSMILESMinStereoBondRingSizeParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API bool getSMILESWriteIsotopeParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setSMILESWriteIsotopeParameter(Base::ControlParameterContainer& cntnr, bool write);

        CDPL_CHEM_API bool hasSMILESWriteIsotopeParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearSMILESWriteIsotopeParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API bool getSMILESMolWriteAtomMappingIDParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setSMILESMolWriteAtomMappingIDParameter(Base::ControlParameterContainer& cntnr, bool write);

        CDPL_CHEM_API bool hasSMILESMolWriteAtomMappingIDParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearSMILESMolWriteAtomMappingIDParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API bool getSMILESRxnWriteAtomMappingIDParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setSMILESRxnWriteAtomMappingIDParameter(Base::ControlParameterContainer& cntnr, bool write);

        CDPL_CHEM_API bool hasSMILESRxnWriteAtomMappingIDParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearSMILESRxnWriteAtomMappingIDParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API bool getSMILESWriteSingleBondsParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setSMILESWriteSingleBondsParameter(Base::ControlParameterContainer& cntnr, bool write);

        CDPL_CHEM_API bool hasSMILESWriteSingleBondsParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearSMILESWriteSingleBondsParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API bool getSMILESWriteAromaticBondsParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setSMILESWriteAromaticBondsParameter(Base::ControlParameterContainer& cntnr, bool write);

        CDPL_CHEM_API bool hasSMILESWriteAromaticBondsParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearSMILESWriteAromaticBondsParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API bool getSMILESNoOrganicSubsetParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setSMILESNoOrganicSubsetParameter(Base::ControlParameterContainer& cntnr, bool no_subset);

        CDPL_CHEM_API bool hasSMILESNoOrganicSubsetParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearSMILESNoOrganicSubsetParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API const std::string& getINCHIInputOptionsParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setINCHIInputOptionsParameter(Base::ControlParameterContainer& cntnr, const std::string& opts);

        CDPL_CHEM_API bool hasINCHIInputOptionsParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearINCHIInputOptionsParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API const std::string& getINCHIOutputOptionsParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setINCHIOutputOptionsParameter(Base::ControlParameterContainer& cntnr, const std::string& opts);

        CDPL_CHEM_API bool hasINCHIOutputOptionsParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearINCHIOutputOptionsParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API bool getMultiConfImportParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setMultiConfImportParameter(Base::ControlParameterContainer& cntnr, bool multi_conf);

        CDPL_CHEM_API bool hasMultiConfImportParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearMultiConfImportParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API bool getMultiConfExportParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setMultiConfExportParameter(Base::ControlParameterContainer& cntnr, bool multi_conf);

        CDPL_CHEM_API bool hasMultiConfExportParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearMultiConfExportParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API bool getOutputConfEnergyAsCommentParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setOutputConfEnergyAsCommentParameter(Base::ControlParameterContainer& cntnr, bool output);

        CDPL_CHEM_API bool hasOutputConfEnergyAsCommentParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearOutputConfEnergyAsCommentParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API const std::string& getConfIndexNameSuffixPatternParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setConfIndexNameSuffixPatternParameter(Base::ControlParameterContainer& cntnr, const std::string& pattern);

        CDPL_CHEM_API bool hasConfIndexNameSuffixPatternParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearConfIndexNameSuffixPatternParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API const MultiConfMoleculeInputProcessor::SharedPointer& getMultiConfInputProcessorParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setMultiConfInputProcessorParameter(Base::ControlParameterContainer& cntnr, const MultiConfMoleculeInputProcessor::SharedPointer& proc);

        CDPL_CHEM_API bool hasMultiConfInputProcessorParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearMultiConfInputProcessorParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API bool getCDFWriteSinglePrecisionFloatsParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setCDFWriteSinglePrecisionFloatsParameter(Base::ControlParameterContainer& cntnr, bool single_prec);

        CDPL_CHEM_API bool hasCDFWriteSinglePrecisionFloatsParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearCDFWriteSinglePrecisionFloatsParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API bool getMOL2EnableExtendedAtomTypesParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setMOL2EnableExtendedAtomTypesParameter(Base::ControlParameterContainer& cntnr, bool enable);

        CDPL_CHEM_API bool hasMOL2EnableExtendedAtomTypesParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearMOL2EnableExtendedAtomTypesParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API bool getMOL2EnableAromaticBondTypesParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setMOL2EnableAromaticBondTypesParameter(Base::ControlParameterContainer& cntnr, bool enable);

        CDPL_CHEM_API bool hasMOL2EnableAromaticBondTypesParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearMOL2EnableAromaticBondTypesParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API bool getMOL2CalcFormalChargesParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setMOL2CalcFormalChargesParameter(Base::ControlParameterContainer& cntnr, bool calc);

        CDPL_CHEM_API bool hasMOL2CalcFormalChargesParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearMOL2CalcFormalChargesParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API unsigned int getMOL2ChargeTypeParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setMOL2ChargeTypeParameter(Base::ControlParameterContainer& cntnr, unsigned int type);

        CDPL_CHEM_API bool hasMOL2ChargeTypeParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearMOL2ChargeTypeParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API unsigned int getMOL2MoleculeTypeParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setMOL2MoleculeTypeParameter(Base::ControlParameterContainer& cntnr, unsigned int type);

        CDPL_CHEM_API bool hasMOL2MoleculeTypeParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearMOL2MoleculeTypeParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API bool getMOL2OutputSubstructuresParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setMOL2OutputSubstructuresParameter(Base::ControlParameterContainer& cntnr, bool output);

        CDPL_CHEM_API bool hasMOL2OutputSubstructuresParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearMOL2OutputSubstructuresParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API bool getXYZCommentIsNameParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setXYZCommentIsNameParameter(Base::ControlParameterContainer& cntnr, bool is_name);

        CDPL_CHEM_API bool hasXYZCommentIsNameParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearXYZCommentIsNameParameter(Base::ControlParameterContainer& cntnr);

        
        CDPL_CHEM_API bool getXYZPerceiveConnectivityParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setXYZPerceiveConnectivityParameter(Base::ControlParameterContainer& cntnr, bool perceive);

        CDPL_CHEM_API bool hasXYZPerceiveConnectivityParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearXYZPerceiveConnectivityParameter(Base::ControlParameterContainer& cntnr);

 
        CDPL_CHEM_API bool getXYZPerceiveBondOrdersParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setXYZPerceiveBondOrdersParameter(Base::ControlParameterContainer& cntnr, bool perceive);

        CDPL_CHEM_API bool hasXYZPerceiveBondOrdersParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearXYZPerceiveBondOrdersParameter(Base::ControlParameterContainer& cntnr);


        CDPL_CHEM_API bool getXYZCalcFormalChargesParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void setXYZCalcFormalChargesParameter(Base::ControlParameterContainer& cntnr, bool calc);

        CDPL_CHEM_API bool hasXYZCalcFormalChargesParameter(const Base::ControlParameterContainer& cntnr);

        CDPL_CHEM_API void clearXYZCalcFormalChargesParameter(Base::ControlParameterContainer& cntnr);

    } // namespace Chem
} // namespace CDPL

#endif // CDPL_CHEM_CONTROLPARAMETERFUNCTIONS_HPP
