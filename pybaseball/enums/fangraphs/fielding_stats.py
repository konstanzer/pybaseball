from enum import Enum
from typing import List


class FanGraphsFieldingStat(Enum):
    LINE_BREAK                       = '-1'
    NAME                             = '0'
    TEAM                             = '1'
    SEASON                           = '2'
    POS                              = '3'
    POSITION                         = POS
    G                                = '4'
    GAMES                            = G
    GS                               = '5'
    GAMES_STARTED                    = GS
    INN                              = '6'
    INNINGS                          = INN
    PO                               = '7'
    PUT_OUTS                         = PO
    A                                = '8'
    ASSISTS                          = A
    E                                = '9'
    ERRORS                           = E
    FE                               = '10'
    FORCED_ERRORS                    = FE
    TE                               = '11' # ?
    DP                               = '12' # ?
    DPS                              = '13' # ?
    DPT                              = '14' # ?
    DPF                              = '15' # ?
    SCP                              = '16' # ?
    SB                               = '17' # ?
    CS                               = '18' # ?
    PB                               = '19' # ?
    WP                               = '20' # ?
    FP                               = '21'
    FIELDING_PCT                     = FP
    TZ                               = '22' # ?
    RSB                              = '23' # ?
    RGDP                             = '24' # ?
    RARM                             = '25' # ?
    RGFP                             = '26' # ?
    RPM                              = '27' # ?
    DRS                              = '28' # ?
    BIZ                              = '29' # ?
    PLAYS                            = '30'
    RZR                              = '31' # ?
    OOZ                              = '32' # ?
    TZL                              = '33' # ?
    FSR                              = '34' # ?
    ARM                              = '35' # ?
    DPR                              = '36' # ?
    RNGR                             = '37' # ?
    ERRR                             = '38' # ?
    UZR                              = '39'
    ULTIMATE_ZONE_RATING             = UZR
    UZR_150                          = '40' # UZR/150
    ULTIMATE_ZONE_RATING_PER_150     = UZR_150
    CPP                              = '41' # ?
    RPP                              = '42' # ?
    DEF                              = '43' # ?
    ZERO_PCT                         = '44' # 0%
    MADE_ZERO_PCT                    = ZERO_PCT
    NUMBER_ZERO_PCT                  = '45' # '# 0%'
    PLAYS_ZERO_PCT                   = NUMBER_ZERO_PCT
    ONE_TO_TEN_PCT                   = '46' # 1-10%
    MADE_ONE_TO_TEN_PCT              = ONE_TO_TEN_PCT
    NUMBER_ONE_TO_TEN_PCT            = '47' # '# 1-10%'
    PLAYS_ONE_TO_TEN_PCT             = NUMBER_ONE_TO_TEN_PCT
    TEN_TO_FORTY_PCT                 = '48' # 10-40%
    MADE_TEN_TO_FORTY_PCT            = TEN_TO_FORTY_PCT
    NUMBER_TEN_TO_FORTY_PCT          = '49' # '# 10-40%'
    PLAYS_TEN_TO_FORTY_PCT           = NUMBER_TEN_TO_FORTY_PCT
    FORTY_TO_SIXTY_PCT               = '50' # 40-60%
    MADE_FORTY_TO_SIXTY_PCT          = FORTY_TO_SIXTY_PCT
    NUMBER_FORTY_TO_SIXTY_PCT        = '51' # '# 40-60%'
    PLAYS_FORTY_TO_SIXTY_PCT         = NUMBER_FORTY_TO_SIXTY_PCT
    SIXTY_TO_NINETY_PCT              = '52' # 60-90%
    MADE_SIXTY_TO_NINETY_PCT         = SIXTY_TO_NINETY_PCT
    NUMBER_SIXTY_TO_NINETY_PCT       = '53' # '# 60-90%'
    PLAYS_SIXTY_TO_NINETY_PCT        = NUMBER_SIXTY_TO_NINETY_PCT
    NINETY_TO_ONE_HUNDRED_PCT        = '54' # 90-100%
    MADE_NINETY_TO_ONE_HUNDRED_PCT   = NINETY_TO_ONE_HUNDRED_PCT
    NUMBER_NINETY_TO_ONE_HUNDRED_PCT = '55' # '# 90-100%'
    PLAYS_NINETY_TO_ONE_HUNDRED_PCT  = NUMBER_NINETY_TO_ONE_HUNDRED_PCT
    RSZ                              = '56' # ?
    RCERA                            = '57' # ?
    RTS                              = '58' # ?
    FRM                              = '59'
    FRAMING                          = FRM

    @staticmethod
    def ALL() -> str:
        common_columns = ['0', '1']
        column_list: List[str] = list(set(
            [column.value for column in FanGraphsFieldingStat if column.value not in common_columns]
        ))
        column_list.sort(key=lambda x: int(x) if x.isdigit() else -2)
        return ','.join(['c'] + column_list)
