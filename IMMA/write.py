# Read in IMMA records from files.

import re     #  Regular Expressions
from structure import attachment
from structure import parameters
from structure import definitions

# Write out a record to a file
def write(record,fh):           # fh is a filehandle
    """Write the given record to a file.

    File should be result of  :func:`open` (or anything with a ``write`` method).

    Args:
        record (:obj:`dict`): One IMMA record.
        fh (:obj:`file`): File to write to (from :func:`open` function).

    """

    Result = ""
    for attachment_n in record['attachments']:
        Result += _encode(record,attachment_n)
    fh.write( Result+"\n" )

# Make a string representation of an attachment
def _encode (attachment,
             attachment_n):    # Attachment number
    params=parameters["%02d" % attachment_n]
    defns=definitions["%02d" % attachment_n]
    Result = ""
    for i in range(len(params)):
        if ( attachment[params[i]] != None):
            Tmp = attachment[params[i]]

            # Scale to integer units for output
            if ( defns[params[i]][5] != None ):
                Tmp = float(Tmp)/defns[params[i]][5];
                Tmp = int(round(Tmp))  # nint

            # Encode as base36 if required
            if ( defns[params[i]][6] == 2 ):
                Tmp = _encode_base36(Tmp);

            # Print as an string of the correct length
            if ( defns[params[i]][6] == 1 ):  # Integer

                if ( defns[params[i]][0] != None ):
                    Lstring = "%%%dd" % (defns[params[i]][0])
                    Tmp = Lstring % (Tmp)
                else:
                    # Undefined length - don't try to constrain it
                    Tmp = "%d" % (Tmp)

            else:                                      # String

                if ( defns[params[i]][0] != None ):
                    Lstring = "%%-%ds" % (defns[params[i]][0])
                    Tmp = Lstring % (Tmp)
                else:
                    Tmp = "%-s" % (Tmp)

            Result += Tmp

        else:  # Undefined data - make a blank string of the corect length

            if ( defns[params[i]][0] != None ):
                Lstring = "%%%ds" % (defns[params[i]][0])
                Result += Lstring % (" ")

            else: # Undefined data with unknown length - should never happen
                Result += " ";

# Done all the parameters, add the ID and length to the start
# (except for core)
    if ( attachment_n != 0 ):
        if ( attachment_n == 99 ):
            Result = "%2d 0%s" % (attachment_n, Result)
        elif attachment_n == 8:
            Result = "%2d2U%s" % (attachment_n, Result)
        else:
            Result = "%2d%2d%s" % (attachment_n, len(Result) + 4, Result)

    return Result

# Convert a base 10 value in the range 0-35 to base36
def _encode_base36(t):
    return '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[t:t+1]
