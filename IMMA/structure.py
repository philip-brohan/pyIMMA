###
### Data for each attachment type
###

attachment  = [None]*100
parameters  = [None]*100
definitions = [None]*100

#
# Core attachment
#
attachment[0] = 'core'

# List of parameters in core section
# In the order they are in on disc
parameters[0] = ('YR','MO','DY','HR','LAT','LON','IM','ATTC',
                 'TI','LI','DS','VS','NID','II','ID','C1','DI',
                 'D','WI','W','VI','VV','WW','W1','SLP','A',
                 'PPP','IT','AT','WBTI','WBT','DPTI','DPT','SI',
                 'SST','N','NH','CL','HI','H','CM','CH','WD',
                 'WP','WH','SD','SP','SH')

# For each parameter, provide an array specifying:
#    Its length in bytes, on disc,
#    Its minimum value
#    Its maximum value
#    Its minimum value (alternative representation)
#    Its maximum value (alternative representation)
#    Its units scale
#    Its encoding (1 = integer, 3= character, 2= base36)
definitions[0] = {
    'YR'   : ( 4, 1600.,  2024.,   None,    None,  1.,    1 ),
    'MO'   : ( 2, 1.,     12.,     None,    None,  1.,    1 ),
    'DY'   : ( 2, 1.,     31.,     None,    None,  1.,    1 ),
    'HR'   : ( 4, 0.00,   23.99,   None,    None,  0.01,  1 ),
    'LAT'  : ( 5, -90.00, 90.00,   None,    None,  0.01,  1 ),
    'LON'  : ( 6, 0.00,   359.99, -179.99, 180.00, 0.01,  1 ),
    'IM'   : ( 2, 0.,     99.,     None,    None,  1.,    1 ),
    'ATTC' : ( 1, 0.,     9.,      None,    None,  1.,    1 ),
    'TI'   : ( 1, 0.,     3.,      None,    None,  1.,    1 ),
    'LI'   : ( 1, 0.,     6.,      None,    None,  1.,    1 ),
    'DS'   : ( 1, 0.,     9.,      None,    None,  1.,    1 ),
    'VS'   : ( 1, 0.,     9.,      None,    None,  1.,    1 ),
    'NID'  : ( 2, 0.,     99.,     None,    None,  1.,    1 ),
    'II'   : ( 2, 0.,     10.,     None,    None,  1.,    1 ),
    'ID'   : ( 9, 32.,    126.,    None,    None,   None, 3 ),
    'C1'   : ( 2, 48.,    57.,    65.,     90.,     None, 3 ),
    'DI'   : ( 1, 0.,     6.,      None,    None,  1.,    1 ),
    'D'    : ( 3, 1.,     362.,    None,    None,  1.,    1 ),
    'WI'   : ( 1, 0.,     8.,      None,    None,  1.,    1 ),
    'W'    : ( 3, 0.0,    99.9,    None,    None,  0.1,   1 ),
    'VI'   : ( 1, 0.,     2.,      None,    None,  1.,    1 ),
    'VV'   : ( 2, 90.,    99.,     None,    None,  1.,    1 ),
    'WW'   : ( 2, 0.,     99.,     None,    None,  1.,    1 ),
    'W1'   : ( 1, 0.,     9.,      None,    None,  1.,    1 ),
    'SLP'  : ( 5, 870.0,  1074.6,  None,    None,  0.1,   1 ),
    'A'    : ( 1, 0.,     8.,      None,    None,  1.,    1 ),
    'PPP'  : ( 3, 0.0,    51.0,    None,    None,  0.1,   1 ),
    'IT'   : ( 1, 0.,     9.,      None,    None,  1.,    1 ),
    'AT'   : ( 4, -99.9,  99.9,    None,    None,  0.1,   1 ),
    'WBTI' : ( 1, 0.,     3.,      None,    None,  1.,    1 ),
    'WBT'  : ( 4, -99.9,  99.9,    None,    None,  0.1,   1 ),
    'DPTI' : ( 1, 0.,     3.,      None,    None,  1.,    1 ),
    'DPT'  : ( 4, -99.9,  99.9,    None,    None,  0.1,   1 ),
    'SI'   : ( 2, 0.,     12.,     None,    None,  1.,    1 ),
    'SST'  : ( 4, -99.9,  99.9,    None,    None,  0.1,   1 ),
    'N'    : ( 1, 0.,     9.,      None,    None,  1.,    1 ),
    'NH'   : ( 1, 0.,     9.,      None,    None,  1.,    1 ),
    'CL'   : ( 1, 0.,     10.,     None,    None,  1.,    2 ),
    'HI'   : ( 1, 0.,     1.,      None,    None,  1.,    1 ),
    'H'    : ( 1, 0.,     10.,     None,    None,  1.,    2 ),
    'CM'   : ( 1, 0.,     10.,     None,    None,  1.,    2 ),
    'CH'   : ( 1, 0.,     10.,     None,    None,  1.,    2 ),
    'WD'   : ( 2, 0.,     38.,     None,    None,  1.,    1 ),
    'WP'   : ( 2, 0.,     30.,    99.,     99.,    1.,    1 ),
    'WH'   : ( 2, 0.,     99.,     None,    None,  1.,    1 ),
    'SD'   : ( 2, 0.,     38.,     None,    None,  1.,    1 ),
    'SP'   : ( 2, 0.,     30.,    99.,     99.,    1.,    1 ),
    'SH'   : ( 2, 0.,     99.,     None,    None,  1.,    1 )
	}

#
# ICOADS attachment
#

attachment[1] = 'icoads'

# List of parameters in icoads section
# In the order they are in on disc
parameters[1] = ('BSI','B10','B1','DCK','SID','PT','DUPS','DUPC','TC',
	         'PB','WX','SX','C2','SQZ','SQA','AQZ','AQA','UQZ','UQA',
	         'VQZ','VQA','PQZ','PQA','DQZ','DQA','ND','SF','AF',
	         'UF','VF','PF','RF','ZNC','WNC','BNC','XNC','YNC',
	         'PNC','ANC','GNC','DNC','SNC','CNC','ENC','FNC','TNC',
	         'QCE','LZ','QCZ')

# For each parameter, provide an array specifying:
#    Its length in bytes, on disc,
#    Its minimum value
#    Its maximum value
#    Its minimum value (alternative representation)
#    Its maximum value (alternative representation)
#    Its units scale
#    Its encoding (1 = integer, 3= character, 2= base36)
definitions[1] = {
    'BSI'  : ( 1,  None,  None,  None,  None, 1., 1 ),
    'B10'  : ( 3, 1.,    648.,   None,  None, 1., 1 ),
    'B1'   : ( 2, 0.,    99.,    None,  None, 1., 1 ),
    'DCK'  : ( 3, 0.,    999.,   None,  None, 1., 1 ),
    'SID'  : ( 3, 0.,    999.,   None,  None, 1., 1 ),
    'PT'   : ( 2, 0.,    15.,    None,  None, 1., 1 ),
    'DUPS' : ( 2, 0.,    14.,    None,  None, 1., 1 ),
    'DUPC' : ( 1, 0.,    2.,     None,  None, 1., 1 ),
    'TC'   : ( 1, 0.,    1.,     None,  None, 1., 1 ),
    'PB'   : ( 1, 0.,    2.,     None,  None, 1., 1 ),
    'WX'   : ( 1, 1.,    1.,     None,  None, 1., 1 ),
    'SX'   : ( 1, 1.,    1.,     None,  None, 1., 1 ),
    'C2'   : ( 2, 0.,    40.,    None,  None, 1., 1 ),
    'SQZ'  : ( 1, 1.,    35.,    None,  None, 1., 2 ),
    'SQA'  : ( 1, 1.,    21.,    None,  None, 1., 2 ),
    'AQZ'  : ( 1, 1.,    35.,    None,  None, 1., 2 ),
    'AQA'  : ( 1, 1.,    21.,    None,  None, 1., 2 ),
    'UQZ'  : ( 1, 1.,    35.,    None,  None, 1., 2 ),
    'UQA'  : ( 1, 1.,    21.,    None,  None, 1., 2 ),
    'VQZ'  : ( 1, 1.,    35.,    None,  None, 1., 2 ),
    'VQA'  : ( 1, 1.,    21.,    None,  None, 1., 2 ),
    'PQZ'  : ( 1, 1.,    35.,    None,  None, 1., 2 ),
    'PQA'  : ( 1, 1.,    21.,    None,  None, 1., 2 ),
    'DQZ'  : ( 1, 1.,    35.,    None,  None, 1., 2 ),
    'DQA'  : ( 1, 1.,    21.,    None,  None, 1., 2 ),
    'ND'   : ( 1, 1.,    2.,     None,  None, 1., 1 ),
    'SF'   : ( 1, 1.,    15.,    None,  None, 1., 2 ),
    'AF'   : ( 1, 1.,    15.,    None,  None, 1., 2 ),
    'UF'   : ( 1, 1.,    15.,    None,  None, 1., 2 ),
    'VF'   : ( 1, 1.,    15.,    None,  None, 1., 2 ),
    'PF'   : ( 1, 1.,    15.,    None,  None, 1., 2 ),
    'RF'   : ( 1, 1.,    15.,    None,  None, 1., 2 ),
    'ZNC'  : ( 1, 1.,    10.,    None,  None, 1., 2 ),
    'WNC'  : ( 1, 1.,    10.,    None,  None, 1., 2 ),
    'BNC'  : ( 1, 1.,    10.,    None,  None, 1., 2 ),
    'XNC'  : ( 1, 1.,    10.,    None,  None, 1., 2 ),
    'YNC'  : ( 1, 1.,    10.,    None,  None, 1., 2 ),
    'PNC'  : ( 1, 1.,    10.,    None,  None, 1., 2 ),
    'ANC'  : ( 1, 1.,    10.,    None,  None, 1., 2 ),
    'GNC'  : ( 1, 1.,    10.,    None,  None, 1., 2 ),
    'DNC'  : ( 1, 1.,    10.,    None,  None, 1., 2 ),
    'SNC'  : ( 1, 1.,    10.,    None,  None, 1., 2 ),
    'CNC'  : ( 1, 1.,    10.,    None,  None, 1., 2 ),
    'ENC'  : ( 1, 1.,    10.,    None,  None, 1., 2 ),
    'FNC'  : ( 1, 1.,    10.,    None,  None, 1., 2 ),
    'TNC'  : ( 1, 1.,    10.,    None,  None, 1., 2 ),
    'QCE'  : ( 2, 0.,    63.,    None,  None, 1., 1 ),
    'LZ'   : ( 1, 1.,    1.,     None,  None, 1., 1 ),
    'QCZ'  : ( 2, 0.,    31.,    None,  None, 1., 1 )
	}

#
# IMMT2 attachment (now deprecated)
#

attachment[2] = 'immt2'

# List of parameters in IMMT2 section
# In the order they are in on disc
parameters[2] = ('OS','OP','FM','IX','W2','SGN','SGT','SGH',
                 'WMI','SD2','SP2','SH2','IS','ES','RS','IC1',
                 'IC2','IC3','IC4','IC5','IR','RRR','TR','QCI',
                 'QI1','QI2','QI3','QI4','QI5','QI6','QI7','QI8',
                 'QI9','QI10','QI11','QI12','QI13','QI14','QI15',
                 'QI16','QI17','QI18','QI19','QI20','QI21','HDG',
                 'COG','SOG','SLL','SLHH','RWD','RWS')

# For each parameter, provide an array specifying:
#    Its length in bytes, on disc,
#    Its minimum value
#    Its maximum value
#    Its minimum value (alternative representation)
#    Its maximum value (alternative representation)
#    Its units scale
#    Its encoding (1 = integer, 3= character, 2= base36)
definitions[2] = {
    'OS'   : ( 1, 0.,   6.,   None,  None,  1.,  1 ),
    'OP'   : ( 1, 0.,   9.,   None,  None,  1.,  1 ),
    'FM'   : ( 2, 0.,   8.,   None,  None,  1.,  1 ),
    'IX'   : ( 1, 1.,   7.,   None,  None,  1.,  1 ),
    'W2'   : ( 1, 0.,   9.,   None,  None,  1.,  1 ),
    'SGN'  : ( 1, 0.,   9.,   None,  None,  1.,  1 ),
    'SGT'  : ( 1, 0.,   10.,  None,  None,  1.,  2 ),
    'SGH'  : ( 2, 0.,   50.,  56.,   99.,   1.,  1 ),
    'WMI'  : ( 1, 0.,   9.,   None,  None,  1.,  1 ),
    'SD2'  : ( 2, 0.,   38.,  None,  None,  1.,  1 ),
    'SP2'  : ( 2, 0.,   30.,  99.,   99.,   1.,  1 ),
    'SH2'  : ( 2, 0.,   99.,  None,  None,  1.,  1 ),
    'IS'   : ( 1, 1.,   5.,   None,  None,  1.,  1 ),
    'ES'   : ( 2, 0.,   99.,  None,  None,  1.,  1 ),
    'RS'   : ( 1, 0.,   4.,   None,  None,  1.,  1 ),
    'IC1'  : ( 1, 0.,   10.,  None,  None,  1.,  2 ),
    'IC2'  : ( 1, 0.,   10.,  None,  None,  1.,  2 ),
    'IC3'  : ( 1, 0.,   10.,  None,  None,  1.,  2 ),
    'IC4'  : ( 1, 0.,   10.,  None,  None,  1.,  2 ),
    'IC5'  : ( 1, 0.,   10.,  None,  None,  1.,  2 ),
    'IR'   : ( 1, 0.,   4.,   None,  None,  1.,  1 ),
    'RRR'  : ( 3, 0.,   999., None,  None,  1.,  1 ),
    'TR'   : ( 1, 1.,   9.,   None,  None,  1.,  1 ),
    'QCI'  : ( 1, 0.,   9.,   None,  None,  1.,  1 ),
    'QI1'  : ( 1, 0.,   9.,   None,  None,  1.,  1 ),
    'QI2'  : ( 1, 0.,   9.,   None,  None,  1.,  1 ),
    'QI3'  : ( 1, 0.,   9.,   None,  None,  1.,  1 ),
    'QI4'  : ( 1, 0.,   9.,   None,  None,  1.,  1 ),
    'QI5'  : ( 1, 0.,   9.,   None,  None,  1.,  1 ),
    'QI6'  : ( 1, 0.,   9.,   None,  None,  1.,  1 ),
    'QI7'  : ( 1, 0.,   9.,   None,  None,  1.,  1 ),
    'QI8'  : ( 1, 0.,   9.,   None,  None,  1.,  1 ),
    'QI9'  : ( 1, 0.,   9.,   None,  None,  1.,  1 ),
    'QI10' : ( 1, 0.,   9.,   None,  None,  1.,  1 ),
    'QI11' : ( 1, 0.,   9.,   None,  None,  1.,  1 ),
    'QI12' : ( 1, 0.,   9.,   None,  None,  1.,  1 ),
    'QI13' : ( 1, 0.,   9.,   None,  None,  1.,  1 ),
    'QI14' : ( 1, 0.,   9.,   None,  None,  1.,  1 ),
    'QI15' : ( 1, 0.,   9.,   None,  None,  1.,  1 ),
    'QI16' : ( 1, 0.,   9.,   None,  None,  1.,  1 ),
    'QI17' : ( 1, 0.,   9.,   None,  None,  1.,  1 ),
    'QI18' : ( 1, 0.,   9.,   None,  None,  1.,  1 ),
    'QI19' : ( 1, 0.,   9.,   None,  None,  1.,  1 ),
    'QI20' : ( 1, 0.,   9.,   None,  None,  1.,  1 ),
    'QI21' : ( 1, 0.,   9.,   None,  None,  1.,  1 ),
    'HDG'  : ( 3, 0.,   360., None,  None,  1.,  1 ),
    'COG'  : ( 3, 0.,   360., None,  None,  1.,  1 ),
    'SOG'  : ( 2, 0.,   99.,  None,  None,  1.,  1 ),
    'SLL'  : ( 2, 0.,   99.,  None,  None,  1.,  1 ),
    'SLHH' : ( 3, -99., 99.,  None,  None,  1.,  1 ),
    'RWD'  : ( 3, 1.,   362., None,  None,  1.,  1 ),
    'RWS'  : ( 3, 0.0,  99.9, None,  None,  0.1, 1 )
	}

#
# Model Quality Control attachment
#

attachment[3] = 'mqc' # now deprecated

# List of parameters in mqc section
# In the order they are in on disc
parameters[3] = ('CCCC','BUID','BMP','BSWU','SWU','BSWV','SWV','BSAT',
                 'BSRH','SRH','SIX','BSST','MST','MSH','BY','BM','BD',
                 'BH','BFL')

# For each parameter, provide an array specifying:
#    Its length in bytes, on disc,
#    Its minimum value
#    Its maximum value
#    Its minimum value (alternative representation)
#    Its maximum value (alternative representation)
#    Its units scale
#    Its encoding (1 = integer, 3= character, 2= base36)
definitions[3] = {
    'CCCC' : ( 4, 65.,   90.,    None,  None,  None,  3 ),
    'BUID' : ( 6, 48.,   57.,    65.,   90.,   None,  3 ),
    'BMP'  : ( 5, 870.0, 1074.6, None,  None,  0.1,   1 ),
    'BSWU' : ( 4, -99.9, 99.9,   None,  None,  0.1,   1 ),
    'SWU'  : ( 4, -99.9, 99.9,   None,  None,  0.1,   1 ),
    'BSWV' : ( 4, -99.9, 99.9,   None,  None,  0.1,   1 ),
    'SWV'  : ( 4, -99.9, 99.9,   None,  None,  0.1,   1 ),
    'BSAT' : ( 4, -99.9, 99.9,   None,  None,  0.1,   1 ),
    'BSRH' : ( 3, 0.,    100.,   None,  None,  1.,    1 ),
    'SRH'  : ( 3, 0.,    100.,   None,  None,  1.,    1 ),
    'SIX'  : ( 1, 2.,    3.,     None,  None,  1.,    1 ),
    'BSST' : ( 4, -99.9, 99.9,   None,  None,  0.1,   1 ),
    'MST'  : ( 1, 0.,    9.,     None,  None,  1.,    1 ),
    'MSH'  : ( 3, 0.,    999.,   None,  None,  1.,    1 ),
    'BY'   : ( 4, 0.,    9999.,  None,  None,  1.,    1 ),
    'BM'   : ( 2, 1.,    12.,    None,  None,  1.,    1 ),
    'BD'   : ( 2, 1.,    31.,    None,  None,  1.,    1 ),
    'BH'   : ( 2, 0.,    23.,    None,  None,  1.,    1 ),
    'BFL'  : ( 2, 0.,    99.,    None,  None,  1.,    1 )
	}

#
# Metadata attachment
#

attachment[4] = 'metadata' # now deprecated

# List of parameters in metadata section
# In the order they are in on disc
parameters[4] = ('C1M','OPM','KOV','COR','TOB','TOT','EOT','LOT','TOH','EOH',
	         'SIM','LOV','DOS','HOP','HOT','HOB','HOA','SMF','SME','SMV')

# For each parameter, provide an array specifying:
#    Its length in bytes, on disc,
#    Its minimum value
#    Its maximum value
#    Its minimum value (alternative representation)
#    Its maximum value (alternative representation)
#    Its units scale
#    Its encoding (1 = integer, 3= character, 2= base36)
definitions[4] = {
    'C1M' : ( 2, 65., 90.,    None,  None,  None,  3 ),
    'OPM' : ( 2, 0.,  99.,    None,  None,  1.,    1 ),
    'KOV' : ( 2, 32., 126.,   None,  None,  None,  3 ),
    'COR' : ( 2, 65., 90.,    None,  None,  None,  3 ),
    'TOB' : ( 3, 32., 126.,   None,  None,  None,  3 ),
    'TOT' : ( 3, 32., 126.,   None,  None,  None,  3 ),
    'EOT' : ( 2, 32., 126.,   None,  None,  None,  3 ),
    'LOT' : ( 2, 32., 126.,   None,  None,  None,  3 ),
    'TOH' : ( 1, 32., 126.,   None,  None,  None,  3 ),
    'EOH' : ( 2, 32., 126.,   None,  None,  None,  3 ),
    'SIM' : ( 3, 32., 126.,   None,  None,  None,  3 ),
    'LOV' : ( 3, 0.,  999.,   None,  None,  1.,    1 ),
    'DOS' : ( 2, 0.,  99.,    None,  None,  1.,    1 ),
    'HOP' : ( 3, 0.,  999.,   None,  None,  1.,    1 ),
    'HOT' : ( 3, 0.,  999.,   None,  None,  1.,    1 ),
    'HOB' : ( 3, 0.,  999.,   None,  None,  1.,    1 ),
    'HOA' : ( 3, 0.,  999.,   None,  None,  1.,    1 ),
    'SMF' : ( 5, 0.,  99999., None,  None,  1.,    1 ),
    'SME' : ( 5, 0.,  99999., None,  None,  1.,    1 ),
    'SMV' : ( 2, 0.,  99.,    None,  None,  1.,    1 )
    }

#
# IMMT attachment
#

attachment[5] = 'IMMT-5/FM 13'

# List of parameters in historical section
# In the order they are in on disc
parameters[5] = ('OS','OP','FM','IMMV','IX','W2','WMI','SD2',
                 'SP2','SH2','IS','ES','RS','IC1','IC2','IC3',
                 'IC4','IC5','IR','RRR','TR','NU','QCI','QI1',
                 'QI2','QI3','QI4','QI5','QI6','QI7','QI8','QI9',
                 'QI10','QI11','QI12','QI13','QI14','QI15','QI16',
                 'QI17','QI18','QI19','QI20','QI21','HDG','COG',
                 'SOG','SLL','SLHH','RWD','RWS','QI22','QI23',
                 'QI24','QI25','QI26','QI27','QI28','QI29','RH',
                 'RHI','AWSI','IMONO')

# For each parameter, provide an array specifying:
#    Its length in bytes, on disc,
#    Its minimum value
#    Its maximum value
#    Its minimum value (alternative representation)
#    Its maximum value (alternative representation)
#    Its units scale
#    Its encoding (1 = integer, 3= character, 2= base36)
definitions[5] = {
    'OS'   : ( 1,   0.,       6.,     None,    None,   1.,  1 ),
    'OP'   : ( 1,   0.,       9.,     None,    None,   1.,  1 ),
    'FM'   : ( 1,   0.,      36.,     None,    None,   1.,  2 ),
    'IMMV' : ( 1,   0.,      36.,     None,    None,   1.,  2 ),
    'IX'   : ( 1,   1.,       7.,     None,    None,   1.,  1 ),
    'W2'   : ( 1,   0.,       9.,     None,    None,   1.,  1 ),
    'WMI'  : ( 1,   0.,       9.,     None,    None,   1.,  1 ),
    'SD2'  : ( 2,   0.,      38.,     None,    None,   1.,  1 ),
    'SP2'  : ( 2,   0.,      30.,     0.,       99.,   1.,  1 ),
    'SH2'  : ( 2,   0.,      99.,     None,    None,   1.,  1 ),
    'IS'   : ( 1,   1.,       5.,     None,    None,   1.,  1 ),
    'ES'   : ( 2,   0.,      99.,     None,    None,   1.,  1 ),
    'RS'   : ( 1,   0.,       4.,     None,    None,   1.,  1 ),
    'IC1'  : ( 1,   0.,      10.,     None,    None,   1.,  2 ),
    'IC2'  : ( 1,   0.,      10.,     None,    None,   1.,  2 ),
    'IC3'  : ( 1,   0.,      10.,     None,    None,   1.,  2 ),
    'IC4'  : ( 1,   0.,      10.,     None,    None,   1.,  2 ),
    'IC5'  : ( 1,   0.,      10.,     None,    None,   1.,  2 ),
    'IR'   : ( 1,   0.,       4.,     None,    None,   1.,  1 ),
    'RRR'  : ( 3,   0.,     999.,     None,    None,   1.,  1 ),
    'TR'   : ( 1,   1.,       9.,     None,    None,   1.,  1 ),
    'NU'   : ( 1,   None,   None,     None,    None, None,  3 ),
    'QCI'  : ( 1,   0.,       9.,     None,    None,   1.,  1 ),
    'QI1'  : ( 1,   0.,       9.,     None,    None,   1.,  1 ),
    'QI2'  : ( 1,   0.,       9.,     None,    None,   1.,  1 ),
    'QI3'  : ( 1,   0.,       9.,     None,    None,   1.,  1 ),
    'QI4'  : ( 1,   0.,       9.,     None,    None,   1.,  1 ),
    'QI5'  : ( 1,   0.,       9.,     None,    None,   1.,  1 ),
    'QI6'  : ( 1,   0.,       9.,     None,    None,   1.,  1 ),
    'QI7'  : ( 1,   0.,       9.,     None,    None,   1.,  1 ),
    'QI8'  : ( 1,   0.,       9.,     None,    None,   1.,  1 ),
    'QI9'  : ( 1,   0.,       9.,     None,    None,   1.,  1 ),
    'QI10' : ( 1,   0.,       9.,     None,    None,   1.,  1 ),
    'QI11' : ( 1,   0.,       9.,     None,    None,   1.,  1 ),
    'QI12' : ( 1,   0.,       9.,     None,    None,   1.,  1 ),
    'QI13' : ( 1,   0.,       9.,     None,    None,   1.,  1 ),
    'QI14' : ( 1,   0.,       9.,     None,    None,   1.,  1 ),
    'QI15' : ( 1,   0.,       9.,     None,    None,   1.,  1 ),
    'QI16' : ( 1,   0.,       9.,     None,    None,   1.,  1 ),
    'QI17' : ( 1,   0.,       9.,     None,    None,   1.,  1 ),
    'QI18' : ( 1,   0.,       9.,     None,    None,   1.,  1 ),
    'QI19' : ( 1,   0.,       9.,     None,    None,   1.,  1 ),
    'QI20' : ( 1,   0.,       9.,     None,    None,   1.,  1 ),
    'QI21' : ( 1,   0.,       9.,     None,    None,   1.,  1 ),
    'HDG'  : ( 3,   0.,     360.,     None,    None,   1.,  1 ),
    'COG'  : ( 3,   0.,     360.,     None,    None,   1.,  1 ),
    'SOG'  : ( 2,   0.,      99.,     None,    None,   1.,  1 ),
    'SLL'  : ( 2,   0.,      99.,     None,    None,   1.,  1 ),
    'SLHH' : ( 3, -99.,      99.,     None,    None,   1.,  1 ),
    'RWD'  : ( 3,   1.,     362.,     None,    None,   1.,  1 ),
    'RWS'  : ( 3,  0.0,     99.9,     None,    None,   0.1, 1 ),
    'QI22' : ( 1,   0.,       9.,     None,    None,   1.,  1 ),
    'QI23' : ( 1,   0.,       9.,     None,    None,   1.,  1 ),
    'QI24' : ( 1,   0.,       9.,     None,    None,   1.,  1 ),
    'QI25' : ( 1,   0.,       9.,     None,    None,   1.,  1 ),
    'QI26' : ( 1,   0.,       9.,     None,    None,   1.,  1 ),
    'QI27' : ( 1,   0.,       9.,     None,    None,   1.,  1 ),
    'QI28' : ( 1,   0.,       9.,     None,    None,   1.,  1 ),
    'QI29' : ( 1,   0.,       9.,     None,    None,   1.,  1 ),
    'RH'   : ( 4,   0.,     100.,     None,    None,   0.1, 1 ),
    'RHI'  : ( 1,   0.,       4.,     None,    None,   1.,  1 ),
    'AWSI' : ( 1,   0.,       2.,     None,    None,   1.,  1 ),
    'IMONO': ( 7,   0., 9999999.,     None,    None,   1.,  1 )
}

#
# Model quality control attachment
#

attachment[6] = 'Model quality control'

# List of parameters in metadata section
# In the order they are in on disc
parameters[6] = ('CCCC','BUID','FBSRC','BMP','BSWU','SWU','BSWV',
                 'SWV','BSAT','BSRH','SRH','BSST','MST','MSH',
                 'BY','BM','BD','BH','BFL')

# For each parameter, provide an array specifying:
#    Its length in bytes, on disc,
#    Its minimum value
#    Its maximum value
#    Its minimum value (alternative representation)
#    Its maximum value (alternative representation)
#    Its units scale
#    Its encoding (1 = integer, 3= character, 2= base36)
definitions[6] = {
    'CCCC'  : ( 4,    65.,    90.,    None,    None, None,   3 ),
    'BUID'  : ( 6,    48.,    57.,     65.,     90., None,   3 ),
    'FBSRC' : ( 1,     0.,     0.,    None,    None,   1.,   1 ),
    'BMP'   : ( 5,  870.0, 1074.6,    None,    None,   0.1,  1 ),
    'BSWU'  : ( 4,  -99.9,   99.9,    None,    None,   0.1,  1 ),
    'SWU'   : ( 4,  -99.9,   99.9,    None,    None,   0.1,  1 ),
    'BSWV'  : ( 4,  -99.9,   99.9,    None,    None,   0.1,  1 ),
    'SWV'   : ( 4,  -99.9,   99.9,    None,    None,   0.1,  1 ),
    'BSAT'  : ( 4,  -99.9,   99.9,    None,    None,   0.1,  1 ),
    'BSRH'  : ( 3,     0.,   100.,    None,    None,    1.,  1 ),
    'SRH'   : ( 3 ,    0.,   100.,    None,    None,    1.,  1 ),
    'BSST'  : ( 5, -99.99,  99.99,    None,    None,  0.01,  1 ),
    'MST'   : ( 1,     0.,     9.,    None,    None,    1.,  1 ),
    'MSH'   : ( 4,  -999.,  9999.,    None,    None,    1.,  1 ),
    'BY'    : ( 4,     0.,  9999.,    None,    None,    1.,  1 ),
    'BM'    : ( 2,     1.,    12.,    None,    None,    1.,  1 ),
    'BD'    : ( 2,     1.,    31.,    None,    None,    1.,  1 ),
    'BH'    : ( 2,     0.,    23.,    None,    None,    1.,  1 ),
    'BFL'   : ( 2,     0.,    99.,    None,    None,    1.,  1 )
}

#
# Ship metadata attachment
#

attachment[7] = 'Ship metadata'

# List of parameters in metadata section
# In the order they are in on disc
parameters[7] = ('MDS','C1M','OPM','KOV','COR','TOB','TOT','EOT',
                 'LOT','TOH','EOH','SIM','LOV','DOS','HOP','HOT',
                 'HOB','HOA','SMF','SME','SMV')

# For each parameter, provide an array specifying:
#    Its length in bytes, on disc,
#    Its minimum value
#    Its maximum value
#    Its minimum value (alternative representation)
#    Its maximum value (alternative representation)
#    Its units scale
#    Its encoding (1 = integer, 3= character, 2= base36)
definitions[7] = {
    'MDS' : ( 1,    0.,      1.,    None,    None,    1.,  1 ),
    'C1M' : ( 2,    None,  None,    None,    None,  None,  3 ),
    'OPM' : ( 2,    0.,     99.,    None,    None,    1.,  1 ),
    'KOV' : ( 2,    None,  None,    None,    None,  None,  3 ),
    'COR' : ( 2,    None,  None,    None,    None,  None,  3 ),
    'TOB' : ( 3,    None,  None,    None,    None,  None,  3 ),
    'TOT' : ( 3,    None,  None,    None,    None,  None,  3 ),
    'EOT' : ( 2,    None,  None,    None,    None,  None,  3 ),
    'LOT' : ( 2,    None,  None,    None,    None,  None,  3 ),
    'TOH' : ( 1,    None,  None,    None,    None,  None,  3 ),
    'EOH' : ( 2,    None,  None,    None,    None,  None,  3 ),
    'SIM' : ( 3,    None,  None,    None,    None,  None,  3 ),
    'LOV' : ( 3,    0.,    999.,    None,    None,    1.,  1 ),
    'DOS' : ( 2,    0.,     99.,    None,    None,    1.,  1 ),
    'HOP' : ( 3,    0.,    999.,    None,    None,    1.,  1 ),
    'HOT' : ( 3,    0.,    999.,    None,    None,    1.,  1 ),
    'HOB' : ( 3,    0.,    999.,    None,    None,    1.,  1 ),
    'HOA' : ( 3,    0.,    999.,    None,    None,    1.,  1 ),
    'SMF' : ( 5,    0.,  99999.,    None,    None,    1.,  1 ),
    'SME' : ( 5,    0.,  99999.,    None,    None,    1.,  1 ),
    'SMV' : ( 2,    0.,     99.,    None,    None,    1.,  1 )
}

#
# Near-surface oceanographic data attachment
#

attachment[8] = 'NOCN'

# List of parameters in metadata section
# In the order they are in on disc
parameters[8] = ('OTV','OTZ','OSV','OSZ','OOV','OOZ','OPV','OPZ',
                 'OSIV','OSIZ','ONV','ONZ','OPHV','OPHZ','OCV',
                 'OCZ','OAV','OAZ','OPCV','OPCZ','ODV','ODZ','PUID')

# For each parameter, provide an array specifying:
#    Its length in bytes, on disc,
#    Its minimum value
#    Its maximum value
#    Its minimum value (alternative representation)
#    Its maximum value (alternative representation)
#    Its units scale
#    Its encoding (1 = integer, 3= character, 2= base36)
definitions[8] = {
    'OTV'  : (  5,  -3.,  38.999,    None,    None,  0.001,  1 ),
    'OTZ'  : (  4,   0.,   99.99,    None,    None,   0.01,  1 ),
    'OSV'  : (  5,   0.,  40.999,    None,    None,  0.001,  1 ),
    'OSZ'  : (  4,   0.,   99.99,    None,    None,   0.01,  1 ),
    'OOV'  : (  4,   0.,   12.99,    None,    None,   0.01,  1 ),
    'OOZ'  : (  4,   0.,   99.99,    None,    None,   0.01,  1 ),
    'OPV'  : (  4,   0.,   30.99,    None,    None,   0.01,  1 ),
    'OPZ'  : (  4,   0.,   99.99,    None,    None,   0.01,  1 ),
    'OSIV' : (  5,   0.,  250.99,    None,    None,   0.01,  1 ),
    'OSIZ' : (  4,   0.,   99.99,    None,    None,   0.01,  1 ),
    'ONV'  : (  5,   0.,  500.99,    None,    None,   0.01,  1 ),
    'ONZ'  : (  4,   0.,   99.99,    None,    None,   0.01,  1 ),
    'OPHV' : (  3,  6.2,     9.2,    None,    None,   0.01,  1 ),
    'OPHZ' : (  4,   0.,   99.99,    None,    None,   0.01,  1 ),
    'OCV'  : (  4,   0.,   50.99,    None,    None,   0.01,  1 ),
    'OCZ'  : (  4,   0.,   99.99,    None,    None,   0.01,  1 ),
    'OAV'  : (  3,   0.,     3.1,    None,    None,   0.01,  1 ),
    'OAZ'  : (  4,   0.,   99.99,    None,    None,   0.01,  1 ),
    'OPCV' : (  4,   0.,    999.,    None,    None,    0.1,  1 ),
    'OPCZ' : (  4,   0.,   99.99,    None,    None,   0.01,  1 ),
    'ODV'  : (  2,   0.,      4.,    None,    None,    0.1,  1 ),
    'ODZ'  : (  4,   0.,   99.99,    None,    None,   0.01,  1 ),
    'PUID' : ( 10,   None,  None,    None,    None,   None,  3 )
} 

#
# Edited cloud report attachment
#

attachment[9] = 'ECR'

# List of parameters in metadata section
# In the order they are in on disc
parameters[9] = ('CCe','WWe','Ne','NHe','He','CLe','CMe','CHe',
                 'AM','AH','UM','UH','SBI','SA','RI')

# For each parameter, provide an array specifying:
#    Its length in bytes, on disc,
#    Its minimum value
#    Its maximum value
#    Its minimum value (alternative representation)
#    Its maximum value (alternative representation)
#    Its units scale
#    Its encoding (1 = integer, 3= character, 2= base36)
definitions[9] = {
    'CCe' : ( 1,   0.,  13.,    None,    None,    1.,  2 ),
    'WWe' : ( 2,   0.,  99.,    None,    None,    1.,  1 ),
    'Ne'  : ( 1,   0.,   8.,    None,    None,    1.,  1 ),
    'NHe' : ( 1,   0.,   8.,    None,    None,    1.,  1 ),
    'He'  : ( 1,   0.,   9.,    None,    None,    1.,  1 ),
    'CLe' : ( 2,   0.,  11.,    None,    None,    1.,  1 ),
    'CMe' : ( 2,   0.,  12.,    None,    None,    1.,  1 ),
    'CHe' : ( 1,   0.,   9.,    None,    None,    1.,  1 ),
    'AM'  : ( 3,   0.,   8.,    None,    None,  0.01,  1 ),
    'AH'  : ( 3,   0.,   8.,    None,    None,  0.01,  1 ),
    'UM'  : ( 1,   0.,   8.,    None,    None,    1.,  1 ),
    'UH'  : ( 1,   0.,   8.,    None,    None,    1.,  1 ),
    'SBI' : ( 1,   0.,    1,    None,    None,    1.,  1 ),
    'SA'  : ( 4,  -90,   90,    None,    None,   0.1,  1 ),
    'RI'  : ( 4, -1.1, 1.17,    None,    None,  0.01,  1 )
} 

#
# Reanalysis QC/Feedback attachment
#

attachment[95] = 'Rean-qc'

# List of parameters in metadata section
# In the order they are in on disc
parameters[95] = ('ICNR','FNR','DPRO','DPRP','UFR','MFGR','MFGSR',
                  'MAR','MASR','BCR','ARCR','CDR','ASIR')

# For each parameter, provide an array specifying:
#    Its length in bytes, on disc,
#    Its minimum value
#    Its maximum value
#    Its minimum value (alternative representation)
#    Its maximum value (alternative representation)
#    Its units scale
#    Its encoding (1 = integer, 3= character, 2= base36)
definitions[95] = {
    'ICNR'  : ( 2,       0.,      99.,    None,    None,     1,  1 ),
    'FNR'   : ( 2,       1.,      99.,    None,    None,     1,  1 ),
    'DPRO'  : ( 2,       1.,      99.,    None,    None,     1,  1 ),
    'DPRP'  : ( 2,       1.,      99.,    None,    None,     1,  1 ),
    'UFR'   : ( 1,       1.,       6.,    None,    None,     1,  1 ),
    'MFGR'  : ( 7, -999999.,  999999.,    None,    None,     1,  1 ), # Scaling inherited from
    'MFGSR' : ( 7, -999999.,  999999.,    None,    None,     1,  1 ), # variable selected
    'MAR'   : ( 7, -999999.,  999999.,    None,    None,     1,  1 ),  # by ICNR & FNR
    'MASR'  : ( 7, -999999.,  999999.,    None,    None,     1,  1 ),
    'BCR'   : ( 7, -999999.,  999999.,    None,    None,     1,  1 ),
    'ARCR'  : ( 4,     None,     None,    None,    None,  None,  3 ),
    'CDR'   : ( 8, 20140101, 29991231,    None,    None,     1,  1 ), # ISO 8601 date
    'ASIR'  : ( 1,        0,        1,    None,    None,     1,  1 )
}

#
# ICOADS Value-Added Database attachment
#

attachment[96] = 'IVAD'

# List of parameters in metadata section
# In the order they are in on disc
parameters[96] = ('ICNI','FNI','JVAD','VAD','IVAU1','JVAU1','VAU1','IVAU2',
                  'JVAU2','VAU2','IVAU3','JVAU3','VAU3','VQC','ARCI','CDR',
                  'ASII')

# For each parameter, provide an array specifying:
#    Its length in bytes, on disc,
#    Its minimum value
#    Its maximum value
#    Its minimum value (alternative representation)
#    Its maximum value (alternative representation)
#    Its units scale
#    Its encoding (1 = integer, 3= character, 2= base36)
definitions[96] = {
    'ICNI'  : ( 2,        0.,       99.,    None,    None,    1.,  1 ),
    'FNI'   : ( 2,        1.,       99.,    None,    None,    1.,  1 ),
    'JVAD'  : ( 1,        0.,       36.,    None,    None,    1.,  2 ),
    'VAD'   : ( 6,   -99999.,   999999.,    None,    None,    1.,  1 ), # Scaling inherited from
    'IVAU1' : ( 1,        1.,       36.,    None,    None,    1.,  2 ),
    'JVAU1' : ( 1,        0.,       36.,    None,    None,    1.,  2 ),
    'VAU1'  : ( 6,   -99999.,   999999.,    None,    None,    1.,  1 ), # variable selected
    'IVAU2' : ( 1,        1,        36.,    None,    None,    1.,  2 ),
    'JVAU2' : ( 1,        0.,       36.,    None,    None,    1.,  2 ),
    'VAU2'  : ( 6,   -99999.,   999999.,    None,    None,    1.,  1 ), # by ICNI & FNI
    'IVAU3' : ( 1,        1.,       36.,    None,    None,    1.,  2 ),
    'JVAU3' : ( 1,        0.,       36.,    None,    None,    1.,  2 ),
    'VAU3'  : ( 6,   -99999.,   999999.,    None,    None,    1.,  1 ),
    'VQC'   : ( 1,        1.,        9.,    None,    None,    1.,  1 ),
    'ARCI'  : ( 4,      None,      None,    None,    None,  None,  3 ),
    'CDR'   : ( 8, 20140101., 29991231.,    None,    None,    1.,  1 ), # ISO 8601 date
    'ASII'  : ( 1,        0.,        1.,    None,    None,    1.,  1 )
}

#
# Error attachment
#

attachment[97] = 'Error'

# List of parameters in supplemental section
# In the order they are in on disc
parameters[97] = ('ICNE','FNE','CEF','ERRD','ARCE','CDE','ASIE');

# For each parameter, provide an array specifying:
#    Its length in bytes, on disc,
#    Its minimum value
#    Its maximum value
#    Its minimum value (alternative representation)
#    Its maximum value (alternative representation)
#    Its units scale
#    Its encoding (1 = integer, 3= character, 2= base36)
definitions[97] = {
     'ICNE' : (    2,        0.,       99.,    None,    None,    1.,  1 ),
     'FNE'  : (    2,        1.,       99.,    None,    None,    1.,  1 ),
     'CEF'  : (    1,        0.,        1.,    None,    None,    1.,  1 ),
     'ERRD' : (   10,      None,      None,    None,    None,  None,  1 ), # Inherited from ICNE and FNE
     'ARCE' : (    4,      None,      None,    None,    None,  None,  3 ),
     'CDE'  : (    8, 20140101., 29991231.,    None,    None,    1.,  1 ), # ISO 8601 date
     'ASIE' : (    1,        0.,        1.,    None,    None,    1.,  1 )
}

#
# Unique report attachment
#

attachment[98] = 'UIda'

# List of parameters in supplemental section
# In the order they are in on disc
parameters[98] = ('UID','RN1','RN2','RN3','RSA','IRF')

# For each parameter, provide an array specifying:
#    Its length in bytes, on disc,
#    Its minimum value
#    Its maximum value
#    Its minimum value (alternative representation)
#    Its maximum value (alternative representation)
#    Its units scale
#    Its encoding (1 = integer, 3= character, 2= base36)
definitions[98] = {
     'UID' : ( 6,  None,  None,    None,    None,  None,  3 ),
     'RN1' : ( 1,     0,    36,    None,    None,    1.,  2 ),
     'RN2' : ( 1,     0,    36,    None,    None,    1.,  2 ),
     'RN3' : ( 1,     0,    36,    None,    None,    1.,  2 ),
     'RSA' : ( 1,     0,     2,    None,    None,    1.,  1 ),
     'IRF' : ( 1,     0,     1,    None,    None,    1.,  1 )
}

#
# Supplemental data attachment
#

attachment[99] = 'supplemental'

# List of parameters in supplemental section
# In the order they are in on disc
parameters[99] = (['SUPD']);

# For each parameter, provide an array specifying:
#    Its length in bytes, on disc,
#    Its minimum value
#    Its maximum value
#    Its minimum value (alternative representation)
#    Its maximum value (alternative representation)
#    Its units scale
#    Its encoding (1 = integer, 3= character, 2= base36)
definitions[99] = {
    'SUPD' : ( None,  None,  None,  None,  None,  None,  3 )
	}

