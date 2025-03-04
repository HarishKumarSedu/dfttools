from ..glob import g

from ..ops.readstoreops import ReadStoreOperation

# FIXME: make signal and reference actual python names by importing pin names
def READSTORE(field_name: str, variable: str, restore:bool=False, comment: str = ''):

    g.output.append(ReadStoreOperation(  field_name=field_name,
                                         variable=variable,
                                         restore=restore,
                                         comment=comment))