/**
 * \file
 * \author R. Bocchino, K. Dinkel
 * \brief Defines a file class to validate files or generate a file validator file
 *
 * \copyright
 * Copyright 2009-2016, by the California Institute of Technology.
 * ALL RIGHTS RESERVED.  United States Government Sponsorship
 * acknowledged. Any commercial use must be negotiated with the Office
 * of Technology Transfer at the California Institute of Technology.
 *
 * This software may be subject to U.S. export control laws and
 * regulations.  By accepting this document, the user agrees to comply
 * with all U.S. export laws and regulations.  User has the
 * responsibility to obtain export licenses, or other export authority
 * as may be required before exporting such information to foreign
 * countries or providing access to foreign persons.
 */

#ifndef _ValidateFile_hpp_
#define _ValidateFile_hpp_

#define VFILE_HASH_CHUNK_SIZE (256)

namespace Os {
    
    namespace ValidateFile {

        // This class encapsulates a very simple file interface for validating files against their hash files 
        // and creating validation files

        typedef enum {
            // Did the validation hash match the file hash or not?
            VALIDATION_OK, //!<  The validation of the file passed
            VALIDATION_FAIL, //!<  The validation of the file did not pass
            // Did we have issues reading in the file?
            FILE_DOESNT_EXIST, //!<  File doesn't exist (for read)
            FILE_NO_PERMISSION, //!<  No permission to read/write file
            FILE_BAD_SIZE, //!<  Invalid size parameter
            // Did we have issues reading in the hash file?
            VALIDATION_FILE_DOESNT_EXIST, //!<  Validation file doesn't exist (for read)
            VALIDATION_FILE_NO_PERMISSION, //!<  No permission to read/write file
            VALIDATION_FILE_BAD_SIZE, //!<  Invalid size parameter
            // Did something else go wrong?
            NO_SPACE, //!<  No space left on the device for writing
            OTHER_ERROR, //!<  A catch-all for other errors. Have to look in implementation-specific code
        } Status;

        Status validate(const char* fileName, const char* hashFileName); //!< Validate the contents of a file 'fileName' against its hash
                                                                                   //!< stored in 'hashFileName'

        Status createValidation(const char* fileName, const char* hashFileName);   //!< Create a validation of the file 'fileName' and store it in
                                                                                             //!< in a file 'hashFileName'
    }
}

#endif
