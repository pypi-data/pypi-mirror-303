/* 
 * ControlParameter.cpp 
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


#include "StaticInit.hpp"

#include "CDPL/Base/LookupKeyDefinition.hpp"
#include "CDPL/Chem/ControlParameter.hpp"


namespace CDPL 
{

    namespace Chem
    {

        namespace ControlParameter
        {
    
        
            CDPL_DEFINE_LOOKUP_KEY(STRICT_ERROR_CHECKING);
            CDPL_DEFINE_LOOKUP_KEY(RECORD_SEPARATOR);
            CDPL_DEFINE_LOOKUP_KEY(ORDINARY_HYDROGEN_DEPLETE);
            CDPL_DEFINE_LOOKUP_KEY(COORDINATES_DIMENSION);
            CDPL_DEFINE_LOOKUP_KEY(BOND_MEMBER_SWAP_STEREO_FIX);
            CDPL_DEFINE_LOOKUP_KEY(CHECK_LINE_LENGTH);

            CDPL_DEFINE_LOOKUP_KEY(MDL_CTAB_VERSION);
            CDPL_DEFINE_LOOKUP_KEY(MDL_IGNORE_PARITY);
            CDPL_DEFINE_LOOKUP_KEY(MDL_UPDATE_TIMESTAMP);
            CDPL_DEFINE_LOOKUP_KEY(MDL_TRIM_STRINGS);
            CDPL_DEFINE_LOOKUP_KEY(MDL_TRIM_LINES);
            CDPL_DEFINE_LOOKUP_KEY(MDL_TRUNCATE_STRINGS);
            CDPL_DEFINE_LOOKUP_KEY(MDL_TRUNCATE_LINES);
            CDPL_DEFINE_LOOKUP_KEY(MDL_RXN_FILE_VERSION);
            CDPL_DEFINE_LOOKUP_KEY(MDL_OUTPUT_CONF_ENERGY_TO_ENERGY_FIELD);
            CDPL_DEFINE_LOOKUP_KEY(MDL_OUTPUT_CONF_ENERGY_AS_SD_ENTRY);
            CDPL_DEFINE_LOOKUP_KEY(MDL_CONF_ENERGY_SD_TAG);

            CDPL_DEFINE_LOOKUP_KEY(JME_SEPARATE_COMPONENTS);

            CDPL_DEFINE_LOOKUP_KEY(SMILES_RECORD_FORMAT);
            CDPL_DEFINE_LOOKUP_KEY(SMILES_WRITE_CANONICAL_FORM);
            CDPL_DEFINE_LOOKUP_KEY(SMILES_WRITE_KEKULE_FORM);
            CDPL_DEFINE_LOOKUP_KEY(SMILES_WRITE_ISOTOPE);
            CDPL_DEFINE_LOOKUP_KEY(SMILES_WRITE_ATOM_STEREO);
            CDPL_DEFINE_LOOKUP_KEY(SMILES_WRITE_BOND_STEREO);
            CDPL_DEFINE_LOOKUP_KEY(SMILES_WRITE_RING_BOND_STEREO);
            CDPL_DEFINE_LOOKUP_KEY(SMILES_RXN_WRITE_ATOM_MAPPING_ID);
            CDPL_DEFINE_LOOKUP_KEY(SMILES_MOL_WRITE_ATOM_MAPPING_ID);
            CDPL_DEFINE_LOOKUP_KEY(SMILES_WRITE_SINGLE_BONDS);
            CDPL_DEFINE_LOOKUP_KEY(SMILES_WRITE_AROMATIC_BONDS);
            CDPL_DEFINE_LOOKUP_KEY(SMILES_NO_ORGANIC_SUBSET);
            CDPL_DEFINE_LOOKUP_KEY(SMILES_MIN_STEREO_BOND_RING_SIZE);

            CDPL_DEFINE_LOOKUP_KEY(INCHI_INPUT_OPTIONS);
            CDPL_DEFINE_LOOKUP_KEY(INCHI_OUTPUT_OPTIONS);

            CDPL_DEFINE_LOOKUP_KEY(MULTI_CONF_IMPORT);
            CDPL_DEFINE_LOOKUP_KEY(MULTI_CONF_EXPORT);
            CDPL_DEFINE_LOOKUP_KEY(MULTI_CONF_INPUT_PROCESSOR);
            CDPL_DEFINE_LOOKUP_KEY(OUTPUT_CONF_ENERGY_AS_COMMENT);
            CDPL_DEFINE_LOOKUP_KEY(CONF_INDEX_NAME_SUFFIX_PATTERN);

            CDPL_DEFINE_LOOKUP_KEY(CDF_WRITE_SINGLE_PRECISION_FLOATS);

            CDPL_DEFINE_LOOKUP_KEY(MOL2_ENABLE_EXTENDED_ATOM_TYPES);
            CDPL_DEFINE_LOOKUP_KEY(MOL2_ENABLE_AROMATIC_BOND_TYPES);
            CDPL_DEFINE_LOOKUP_KEY(MOL2_CALC_FORMAL_CHARGES);
            CDPL_DEFINE_LOOKUP_KEY(MOL2_CHARGE_TYPE);
            CDPL_DEFINE_LOOKUP_KEY(MOL2_MOLECULE_TYPE);
            CDPL_DEFINE_LOOKUP_KEY(MOL2_OUTPUT_SUBSTRUCTURES);

            CDPL_DEFINE_LOOKUP_KEY(XYZ_COMMENT_IS_NAME);
            CDPL_DEFINE_LOOKUP_KEY(XYZ_PERCEIVE_CONNECTIVITY);
            CDPL_DEFINE_LOOKUP_KEY(XYZ_PERCEIVE_BOND_ORDERS);
            CDPL_DEFINE_LOOKUP_KEY(XYZ_CALC_FORMAL_CHARGES);
        }

        void initControlParameters() {}
    }
}
