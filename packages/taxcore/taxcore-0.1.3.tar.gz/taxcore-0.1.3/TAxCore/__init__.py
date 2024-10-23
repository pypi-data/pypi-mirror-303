# Import all indicators from ta.py for easier access
from TAxCore import TechnicalAnalysis

# Define a version for your library
__version__ = '0.1.3'

# Optional: Categorize the indicators for users
class MovingAverages:
    sma = TechnicalAnalysis.sma
    ema = TechnicalAnalysis.ema
    wma = TechnicalAnalysis.wma
    vwma = TechnicalAnalysis.vwma
    hma = TechnicalAnalysis.hma
    double_ema = TechnicalAnalysis.double_ema
    alma = TechnicalAnalysis.alma
    lsma = TechnicalAnalysis.least_squares_moving_average
    mcgginley = TechnicalAnalysis.mcginley_dynamic
    twap = TechnicalAnalysis.twap

class Oscillators:
    rsi = TechnicalAnalysis.rsi
    stoch_rsi = TechnicalAnalysis.stochastic_rsi
    macd = TechnicalAnalysis.macd
    tsi = TechnicalAnalysis.tsi
    momentum = TechnicalAnalysis.momentum
    bollinger_bandwidth = TechnicalAnalysis.bollinger_bandwidth
    awesome_oscillator = TechnicalAnalysis.ao
    stochastic_momentum_index = TechnicalAnalysis.stochastic_momentum_index
    stochastic_oscillator = TechnicalAnalysis.stochastic_oscillator

class Volatility:
    atr = TechnicalAnalysis.atr
    bollinger_bands = TechnicalAnalysis.bollinger_bands
    keltner_channel = TechnicalAnalysis.keltner_channels
    envelope = TechnicalAnalysis.envelope
    adr = TechnicalAnalysis.adr
    donchian_channels = TechnicalAnalysis.donchian_channels

class TrendIndicators:
    adx = TechnicalAnalysis.adx
    aroon = TechnicalAnalysis.aroon
    supertrend = TechnicalAnalysis.supertrend
    vortex = TechnicalAnalysis.vortex
    parabolic_sar = TechnicalAnalysis.parabolic_sar
    directional_movement_index = TechnicalAnalysis.dmi
    ichimoku_cloud = TechnicalAnalysis.ichimoku_cloud
    linear_regression = TechnicalAnalysis.linear_regression_channel
    mass_index = TechnicalAnalysis.mass_index
    williams_alligator = TechnicalAnalysis.williams_alligator

class VolumeIndicators:
    chaikin_money_flow = TechnicalAnalysis.chaikin_money_flow
    bop = TechnicalAnalysis.bop

# Export everything
__all__ = [
    'TechnicalAnalysis',
    'MovingAverages',
    'Oscillators',
    'Volatility',
    'TrendIndicators',
    'VolumeIndicators',
]
