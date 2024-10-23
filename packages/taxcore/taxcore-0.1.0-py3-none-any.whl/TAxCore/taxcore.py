import numpy as np
import pandas as pd

class TechnicalAnalysis:
    @staticmethod
    def sma(prices, period):
        if len(prices) < period:
            raise ValueError("Not enough data points to calculate SMA.")

        sma_values = np.convolve(prices, np.ones(period)/period, mode='valid')
        # Prepend NaN values for the first 'period - 1' entries
        return [np.nan] * (period - 1) + sma_values.tolist()
    
    @staticmethod
    def sma_for_williams(prices, period):
        """
        Calculate Simple Moving Average (SMA).
        
        :param prices: List or NumPy array of prices.
        :param period: The number of periods for the SMA calculation.
        :return: NumPy array of SMA values.
        """
        return np.convolve(prices, np.ones(period)/period, mode='valid')

    @staticmethod
    def ema(data, length):
        """
        Calculate the Exponential Moving Average (EMA).
        
        :param data: List or NumPy array of prices.
        :param length: The period for the EMA.
        :return: NumPy array of EMA values.
        """
        data = np.array(data)
        alpha = 2 / (length + 1)
        ema_values = np.zeros(len(data))
        ema_values[length - 1] = np.mean(data[:length])

        for i in range(length, len(data)):
            ema_values[i] = (data[i] * alpha) + (ema_values[i - 1] * (1 - alpha))

        return ema_values

    @staticmethod
    def atr(high_prices, low_prices, close_prices, period=10):
        """
        Calculate the Average True Range (ATR).
        
        :param high_prices: List or NumPy array of high prices.
        :param low_prices: List or NumPy array of low prices.
        :param close_prices: List or NumPy array of closing prices.
        :param period: The number of periods for the ATR calculation.
        :return: NumPy array of ATR values.
        """
        high_prices = np.array(high_prices)
        low_prices = np.array(low_prices)
        close_prices = np.array(close_prices)

        tr = np.maximum(high_prices[1:] - low_prices[1:], 
                        np.maximum(np.abs(high_prices[1:] - close_prices[:-1]), 
                                   np.abs(low_prices[1:] - close_prices[:-1])))
        atr_values = np.zeros(len(close_prices))
        atr_values[period-1] = np.mean(tr[:period])

        for i in range(period, len(tr)):
            atr_values[i] = (atr_values[i - 1] * (period - 1) + tr[i - 1]) / period

        return atr_values

    @staticmethod
    def double_ema(prices, period):
        """Calculate Double EMA by applying EMA twice."""
        ema1 = TechnicalAnalysis.ema(prices, period)
        ema2 = TechnicalAnalysis.ema(ema1, period)
        return ema2

    @staticmethod
    def double_smooth(prices, long, short):
        """
        Double smooth the prices using EMA.
        
        :param prices: List or NumPy array of prices.
        :param long: Long period for EMA.
        :param short: Short period for EMA.
        :return: Double smoothed prices.
        """
        first_smooth = TechnicalAnalysis.ema(prices, long)
        return TechnicalAnalysis.ema(first_smooth, short)

    @staticmethod
    def wma(prices, length):
        """
        Calculate the Weighted Moving Average (WMA) for a given list of prices and length.

        :param prices: List of closing prices.
        :param length: The period for the WMA calculation.
        :return: List of WMA values.
        """
        if len(prices) < length:
            return [np.nan] * len(prices)

        wma_values = []
        weight_total = sum(range(1, length + 1))
        for i in range(len(prices)):
            if i < length - 1:
                wma_values.append(np.nan)
            else:
                weighted_sum = sum(prices[i - length + 1:i + 1] * np.arange(1, length + 1))
                wma_values.append(weighted_sum / weight_total)

        return wma_values
    
    @staticmethod
    def vwma(prices, volumes, period):
        """
        Calculate Volume Weighted Moving Average (VWMA).
        
        :param prices: List or NumPy array of prices (e.g., closing prices).
        :param volumes: List or NumPy array of volumes corresponding to the prices.
        :param period: The number of periods for the VWMA calculation.
        :return: NumPy array of VWMA values.
        """
        vwma_values = np.zeros(len(prices))
        
        for i in range(period - 1, len(prices)):
            weighted_sum = np.sum(prices[i - period + 1:i + 1] * volumes[i - period + 1:i + 1])
            volume_sum = np.sum(volumes[i - period + 1:i + 1])
            vwma_values[i] = weighted_sum / volume_sum if volume_sum != 0 else 0

        return vwma_values
    
    @staticmethod
    def hma(prices, length=9):
        """
        Calculate the Hull Moving Average (HMA) for a given list of prices.

        :param prices: List of closing prices.
        :param length: The period for the HMA calculation.
        :return: List of HMA values.
        """
        if len(prices) < length:
            raise ValueError("Not enough data points to calculate HMA.")

        half_length = max(int(length / 2), 1)
        sqrt_length = max(int(np.sqrt(length)), 1)

        wma_half_length = TechnicalAnalysis.wma(prices, half_length)
        wma_full_length = TechnicalAnalysis.wma(prices, length)

        raw_hma = []
        for i in range(len(prices)):
            if np.isnan(wma_half_length[i]) or np.isnan(wma_full_length[i]):
                raw_hma.append(np.nan)
            else:
                raw_hma.append(2 * wma_half_length[i] - wma_full_length[i])

        hma_values = TechnicalAnalysis.wma(raw_hma, sqrt_length)

        return hma_values
    
    @staticmethod
    def rsi(prices, period=14):
        """
        Calculate the Relative Strength Index (RSI) for a given list of prices.
        
        :param prices: List of prices (closing prices).
        :param period: The number of periods to use for the RSI calculation.
        :return: List of RSI values.
        """
        if len(prices) < period:
            raise ValueError("Not enough data points to calculate RSI.")

        changes = np.diff(prices)
        up = np.where(changes > 0, changes, 0)
        down = np.where(changes < 0, -changes, 0)

        up_avg = np.zeros(len(prices))
        down_avg = np.zeros(len(prices))

        up_avg[0] = np.mean(up[:period])
        down_avg[0] = np.mean(down[:period])

        for i in range(1, len(prices)):
            up_avg[i] = (up_avg[i-1] * (period - 1) + up[i-1]) / period
            down_avg[i] = (down_avg[i-1] * (period - 1) + down[i-1]) / period

        rs = up_avg / down_avg
        rsi = 100 - (100 / (1 + rs))

        rsi_values = [np.nan] * (period - 1) + rsi[period-1:].tolist()

        return rsi_values
    
    @staticmethod
    def aroon(highs, lows, period=14):
        """
        Calculate the Aroon Up and Aroon Down indicators for a given list of highs and lows.

        :param highs: List of high prices.
        :param lows: List of low prices.
        :param period: The number of periods to use for the Aroon calculation.
        :return: Two lists containing the Aroon Up and Aroon Down values.
        """
        if len(highs) < period or len(lows) < period:
            raise ValueError("Not enough data points to calculate Aroon.")

        aroon_up = []
        aroon_down = []

        for i in range(period, len(highs) + 1):
            high_period = highs[i - period:i]
            low_period = lows[i - period:i]

            days_since_high = np.argmax(high_period) + period
            days_since_low = np.argmin(low_period) + period

            aroon_up_value = 100 * (days_since_high / period)
            aroon_down_value = 100 * (days_since_low / period)

            aroon_up.append(aroon_up_value)
            aroon_down.append(aroon_down_value)
        
        aroon_up = [np.nan] * (period - 1) + aroon_up
        aroon_down = [np.nan] * (period - 1) + aroon_down

        return aroon_up, aroon_down

    @staticmethod
    def alma(prices, period=10, offset=0.85, sigma=6):
        """
        Calculate the Arnaud Legoux Moving Average (ALMA) for a given list of prices.

        :param prices: List of prices (closing prices).
        :param period: The number of periods to use for the ALMA calculation.
        :param offset: Controls the smoothness (between 0 and 1). Closer to 1 shifts it closer to the end of the period.
        :param sigma: Determines the flatness of the weight curve. Higher sigma leads to a flatter curve.
        :return: List of ALMA values.
        """
        if len(prices) < period:
            raise ValueError("Not enough data points to calculate ALMA.")

        alma_values = []
        m = offset * (period - 1)
        s = period / sigma

        weights = np.array([np.exp(-((i - m) ** 2) / (2 * s ** 2)) for i in range(period)])
        weights /= np.sum(weights)

        for i in range(period - 1, len(prices)):
            price_segment = prices[i - period + 1:i + 1]
            alma_value = np.dot(price_segment, weights)
            alma_values.append(alma_value)

        alma_values = [np.nan] * (period - 1) + alma_values

        return alma_values
    
    @staticmethod
    def adx(highs, lows, closes, period=14, di_period=14):
        """
        Calculate the Average Directional Movement Index (ADX).

        :param highs: List of high prices.
        :param lows: List of low prices.
        :param closes: List of closing prices.
        :param period: The number of periods to use for the ADX calculation.
        :param di_period: The number of periods to use for the DI calculation.
        :return: List of ADX values.
        """
        highs = np.array(highs)
        lows = np.array(lows)
        closes = np.array(closes)

        if len(highs) < period or len(lows) < period or len(closes) < period:
            raise ValueError("Not enough data points to calculate ADX.")

        tr = np.maximum(highs[1:] - lows[1:], 
                        np.maximum(np.abs(highs[1:] - closes[:-1]),
                                    np.abs(lows[1:] - closes[:-1])))

        up = np.where(highs[1:] > highs[:-1], highs[1:] - highs[:-1], 0)
        down = np.where(lows[:-1] > lows[1:], lows[:-1] - lows[1:], 0)
        plus_dm = np.where(up > down, up, 0)
        minus_dm = np.where(down > up, down, 0)

        tr_smooth = np.zeros(len(tr))
        plus_dm_smooth = np.zeros(len(plus_dm))
        minus_dm_smooth = np.zeros(len(minus_dm))

        for i in range(len(tr)):
            if i < period:
                tr_smooth[i] = np.sum(tr[:i+1]) / (i+1) if i > 0 else tr[i]
                plus_dm_smooth[i] = np.sum(plus_dm[:i+1]) / (i+1) if i > 0 else plus_dm[i]
                minus_dm_smooth[i] = np.sum(minus_dm[:i+1]) / (i+1) if i > 0 else minus_dm[i]
            else:
                tr_smooth[i] = (tr_smooth[i-1] * (period - 1) + tr[i]) / period
                plus_dm_smooth[i] = (plus_dm_smooth[i-1] * (period - 1) + plus_dm[i]) / period
                minus_dm_smooth[i] = (minus_dm_smooth[i-1] * (period - 1) + minus_dm[i]) / period

        plus_di = 100 * plus_dm_smooth / tr_smooth
        minus_di = 100 * minus_dm_smooth / tr_smooth

        dx = np.abs(plus_di - minus_di) / (plus_di + minus_di)
        adx = np.zeros(len(dx))

        for i in range(len(dx)):
            if i < di_period:
                adx[i] = np.nan
            else:
                adx[i] = np.mean(dx[i-di_period:i])

        return adx
    
    @staticmethod
    def adr(highs, lows, period=14):
        """
        Calculate the Average Day Range (ADR) for a given list of highs and lows.

        :param highs: List of high prices.
        :param lows: List of low prices.
        :param period: The number of periods to use for the ADR calculation.
        :return: List of ADR values.
        """
        if len(highs) < period or len(lows) < period:
            raise ValueError("Not enough data points to calculate ADR.")

        day_ranges = np.array(highs) - np.array(lows)
        weights = np.ones(period) / period
        adr_values = np.convolve(day_ranges, weights, mode='valid')

        adr_values = [np.nan] * (period - 1) + adr_values.tolist()

        return adr_values
    
    @staticmethod
    def ao(highs, lows, short_period=5, long_period=34):
        """
        Calculate the Awesome Oscillator (AO) for a given list of highs and lows.

        :param highs: List of high prices.
        :param lows: List of low prices.
        :param short_period: The short period for the AO calculation.
        :param long_period: The long period for the AO calculation.
        :return: List of AO values.
        """
        if len(highs) < long_period or len(lows) < long_period:
            raise ValueError("Not enough data points to calculate AO.")

        hl2 = (np.array(highs) + np.array(lows)) / 2
        ao_values = np.zeros(len(highs))
        ao_values[long_period-1:] = np.array([np.mean(hl2[i-short_period+1:i+1]) for i in range(long_period-1, len(highs))]) - np.array([np.mean(hl2[i-long_period+1:i+1]) for i in range(long_period-1, len(highs))])

        ao_values = [np.nan] * (long_period - 1) + ao_values[long_period-1:].tolist()

        return ao_values
    
    @staticmethod
    def bop(closes, opens, highs, lows):
        """
        Calculate the Balance of Power (BOP) indicator for a given list of prices.

        :param closes: List of closing prices.
        :param opens: List of opening prices.
        :param highs: List of high prices.
        :param lows: List of low prices.
        :return: List of BOP values.
        """
        if len(closes) != len(opens) or len(opens) != len(highs) or len(highs) != len(lows):
            raise ValueError("All input lists must have the same length.")

        bop_values = (np.array(closes) - np.array(opens)) / (np.array(highs) - np.array(lows))
        
        bop_values[np.isnan(bop_values)] = 0

        return bop_values
    
    @staticmethod
    def bollinger_bands(prices, length=20, mult=2.0, ma_type='SMA'):
        """
        Calculate the Bollinger Bands for a given list of prices.

        :param prices: List of prices (closing prices).
        :param length: The number of periods to use for the moving average.
        :param mult: The multiplier for the standard deviation.
        :param ma_type: Type of moving average to use ('SMA', 'EMA', 'SMMA', 'WMA', 'VWMA').
        :return: Tuple containing the basis, upper band, and lower band lists.
        """
        if len(prices) < length:
            raise ValueError("Not enough data points to calculate Bollinger Bands.")

        prices = np.array(prices)

        if ma_type == 'SMA':
            basis = np.convolve(prices, np.ones(length)/length, mode='valid')
        elif ma_type == 'EMA':
            basis = pd.Series(prices).ewm(span=length, adjust=False).mean().to_numpy()
        elif ma_type == 'SMMA':
            basis = np.zeros(len(prices))
            basis[:length] = np.mean(prices[:length])
            for i in range(length, len(prices)):
                basis[i] = (basis[i-1] * (length - 1) + prices[i]) / length
        elif ma_type == 'WMA':
            weights = np.arange(1, length + 1)
            basis = np.convolve(prices, weights/weights.sum(), mode='valid')
        elif ma_type == 'VWMA':
            weights = prices[-length:] * np.arange(1, length + 1)
            basis = np.convolve(weights, np.ones(length)/length, mode='valid') / np.convolve(np.ones(length), np.arange(1, length + 1), mode='valid')
        else:
            raise ValueError("Invalid moving average type.")

        std_dev = mult * np.array([np.std(prices[i-length:i]) for i in range(length, len(prices)+1)])

        upper = basis + std_dev
        lower = basis - std_dev

        basis = np.concatenate((np.full(length - 1, np.nan), basis))
        upper = np.concatenate((np.full(length - 1, np.nan), upper))
        lower = np.concatenate((np.full(length - 1, np.nan), lower))

        return basis, upper, lower
    
    @staticmethod
    def bollinger_bandwidth(prices, length=20, mult=2.0, expansion_length=125, contraction_length=125, ma_type='SMA'):
        """
        Calculate the Bollinger Band Width (BBW) for a given list of prices.

        :param prices: List of prices (closing prices).
        :param length: The number of periods to use for the moving average.
        :param mult: The multiplier for the standard deviation.
        :param expansion_length: Length for highest expansion calculation.
        :param contraction_length: Length for lowest contraction calculation.
        :param ma_type: Type of moving average to use ('SMA', 'EMA', 'SMMA', 'WMA', 'VWMA').
        :return: Tuple containing the BBW values, highest expansion, and lowest contraction values.
        """
        if len(prices) < length:
            raise ValueError("Not enough data points to calculate Bollinger Band Width.")

        prices = np.array(prices)

        if ma_type == 'SMA':
            basis = np.convolve(prices, np.ones(length)/length, mode='valid')
        elif ma_type == 'EMA':
            basis = pd.Series(prices).ewm(span=length, adjust=False).mean().to_numpy()
        elif ma_type == 'SMMA':
            basis = np.zeros(len(prices))
            basis[:length] = np.mean(prices[:length])
            for i in range(length, len(prices)):
                basis[i] = (basis[i-1] * (length - 1) + prices[i]) / length
        elif ma_type == 'WMA':
            weights = np.arange(1, length + 1)
            basis = np.convolve(prices, weights/weights.sum(), mode='valid')
        elif ma_type == 'VWMA':
            weights = prices[-length:] * np.arange(1, length + 1)
            basis = np.convolve(weights, np.ones(length)/length, mode='valid') / np.convolve(np.ones(length), np.arange(1, length + 1), mode='valid')
        else:
            raise ValueError("Invalid moving average type.")

        std_dev = mult * np.array([np.std(prices[i-length:i]) for i in range(length, len(prices)+1)])

        upper = basis + std_dev
        lower = basis - std_dev

        bbw = ((upper - lower) / basis) * 100

        bbw = [np.nan] * (length - 1) + bbw.tolist()
        upper = np.concatenate((np.full(length - 1, np.nan), upper))
        lower = np.concatenate((np.full(length - 1, np.nan), lower))
        basis = np.concatenate((np.full(length - 1, np.nan), basis))

        highest_expansion = [np.nan] * (length - 1) + [np.nanmax(bbw[i-expansion_length:i]) if i >= expansion_length else np.nan for i in range(length - 1, len(bbw))]
        lowest_contraction = [np.nan] * (length - 1) + [np.nanmin(bbw[i-contraction_length:i]) if i >= contraction_length else np.nan for i in range(length - 1, len(bbw))]

        return bbw, highest_expansion, lowest_contraction
    
    @staticmethod
    def chaikin_money_flow(closes, highs, lows, volumes, length=20):
        """
        Calculate the Chaikin Money Flow (CMF) indicator for a given list of prices and volumes.

        :param closes: List of closing prices.
        :param highs: List of high prices.
        :param lows: List of low prices.
        :param volumes: List of volumes.
        :param length: The number of periods to use for the CMF calculation.
        :return: List of CMF values.
        """
        if len(closes) != len(highs) or len(highs) != len(lows) or len(lows) != len(volumes):
            raise ValueError("All input lists must have the same length.")

        if len(closes) < length:
            raise ValueError("Not enough data points to calculate CMF.")

        ad = np.where((highs == lows) | (closes == highs) | (closes == lows), 0,
                      ((2 * closes - lows - highs) / (highs - lows)) * volumes)

        cmf = np.array([np.sum(ad[i-length+1:i+1]) / np.sum(volumes[i-length+1:i+1]) if i >= length - 1 else np.nan for i in range(len(ad))])

        return cmf
    
    @staticmethod
    def dmi(highs, lows, closes, period=14, adx_period=14):
        """
        Calculate the Directional Movement Index (DMI) and ADX.

        :param highs: List of high prices.
        :param lows: List of low prices.
        :param closes: List of closing prices.
        :param period: The number of periods to use for the DI calculation.
        :param adx_period: The number of periods to use for the ADX calculation.
        :return: Tuple containing the +DI, -DI, and ADX values.
        """
        highs = np.array(highs)
        lows = np.array(lows)
        closes = np.array(closes)

        if len(highs) < period or len(lows) < period or len(closes) < period:
            raise ValueError("Not enough data points to calculate DMI.")

        up = np.maximum(highs[1:] - highs[:-1], 0)
        down = np.maximum(lows[:-1] - lows[1:], 0)

        plus_dm = np.where((up > down) & (up > 0), up, 0)
        minus_dm = np.where((down > up) & (down > 0), down, 0)

        tr = np.maximum(highs[1:] - lows[1:], 
                        np.maximum(np.abs(highs[1:] - closes[:-1]),
                                   np.abs(lows[1:] - closes[:-1])))

        tr_smooth = np.zeros(len(tr))
        plus_dm_smooth = np.zeros(len(plus_dm))
        minus_dm_smooth = np.zeros(len(minus_dm))

        for i in range(len(tr)):
            if i < period:
                tr_smooth[i] = np.sum(tr[:i+1]) / (i+1) if i > 0 else tr[i]
                plus_dm_smooth[i] = np.sum(plus_dm[:i+1]) / (i+1) if i > 0 else plus_dm[i]
                minus_dm_smooth[i] = np.sum(minus_dm[:i+1]) / (i+1) if i > 0 else minus_dm[i]
            else:
                tr_smooth[i] = (tr_smooth[i-1] * (period - 1) + tr[i]) / period
                plus_dm_smooth[i] = (plus_dm_smooth[i-1] * (period - 1) + plus_dm[i]) / period
                minus_dm_smooth[i] = (minus_dm_smooth[i-1] * (period - 1) + minus_dm[i]) / period

        plus_di = 100 * plus_dm_smooth / tr_smooth
        minus_di = 100 * minus_dm_smooth / tr_smooth

        adx = TechnicalAnalysis.adx(highs, lows, closes, period, adx_period)

        return plus_di, minus_di, adx
    
    @staticmethod
    def donchian_channels(prices, length=20):
        """
        Calculate the Donchian Channels for a given list of prices.

        :param prices: List of prices (closing prices).
        :param length: The number of periods to use for the Donchian Channels calculation.
        :return: Tuple containing the lower, upper, and basis values.
        """
        if len(prices) < length:
            raise ValueError("Not enough data points to calculate Donchian Channels.")

        lower = [np.nan] * (length - 1) + [min(prices[i-length+1:i+1]) for i in range(length-1, len(prices))]
        upper = [np.nan] * (length - 1) + [max(prices[i-length+1:i+1]) for i in range(length-1, len(prices))]
        basis = [(u + l) / 2 for u, l in zip(upper, lower)]

        return lower, upper, basis
    
    @staticmethod
    def envelope(prices, length=20, percent=10.0, exponential=False):
        """
        Calculate the Envelope indicator for a given list of prices.

        :param prices: List of closing prices.
        :param length: The number of periods to use for the moving average.
        :param percent: The percentage for the envelope calculation.
        :param exponential: If True, use EMA; if False, use SMA.
        :return: Tuple containing the basis, upper band, and lower band lists.
        """
        if len(prices) < length:
            raise ValueError("Not enough data points to calculate Envelope.")

        prices = np.array(prices)

        if exponential:
            basis = pd.Series(prices).ewm(span=length, adjust=False).mean().to_numpy()
        else:
            basis = np.convolve(prices, np.ones(length)/length, mode='valid')

        k = percent / 100.0

        upper = basis * (1 + k)
        lower = basis * (1 - k)

        basis = np.concatenate((np.full(length - 1, np.nan), basis))
        upper = np.concatenate((np.full(length - 1, np.nan), upper))
        lower = np.concatenate((np.full(length - 1, np.nan), lower))

        return basis, upper, lower
    
    @staticmethod
    def donchian(prices, length):
        """
        Calculate the Donchian Channel for a given list of prices.
        
        :param prices: List of prices (closing prices).
        :param length: The number of periods to use for the Donchian calculation.
        :return: The average of the highest high and lowest low over the period.
        """
        if len(prices) < length:
            raise ValueError("Not enough data points to calculate Donchian Channel.")

        highest_high = pd.Series(prices).rolling(window=length).max()
        lowest_low = pd.Series(prices).rolling(window=length).min()
        return (highest_high + lowest_low) / 2

    @staticmethod
    def ichimoku_cloud(prices, conversion_periods=9, base_periods=26, lagging_span2_periods=52, displacement=26):
        """
        Calculate the Ichimoku Cloud for a given list of prices.

        :param prices: List of closing prices.
        :param conversion_periods: Length for the Conversion Line.
        :param base_periods: Length for the Base Line.
        :param lagging_span2_periods: Length for the Leading Span B.
        :param displacement: Displacement for the Lagging Span.
        :return: A dictionary with Conversion Line, Base Line, Leading Span A, Leading Span B, and Lagging Span.
        """
        if len(prices) < max(conversion_periods, base_periods, lagging_span2_periods):
            raise ValueError("Not enough data points to calculate Ichimoku Cloud.")

        conversion_line = TechnicalAnalysis.donchian(prices, conversion_periods)
        base_line = TechnicalAnalysis.donchian(prices, base_periods)
        lead_line1 = (conversion_line + base_line) / 2
        lead_line2 = TechnicalAnalysis.donchian(prices, lagging_span2_periods)
        lagging_span = prices.shift(-displacement)

        result = {
            'conversion_line': conversion_line,
            'base_line': base_line,
            'lead_line1': lead_line1,
            'lead_line2': lead_line2,
            'lagging_span': lagging_span
        }

        return result
    
    @staticmethod
    def keltner_channels(prices, length=20, multiplier=2.0, atr_length=10, use_ema=True):
        """
        Calculate Keltner Channels for a given list of prices.

        :param prices: List of closing prices.
        :param length: Length for the moving average.
        :param multiplier: Multiplier for the range.
        :param atr_length: Length for the Average True Range.
        :param use_ema: Boolean to use Exponential Moving Average (EMA) or Simple Moving Average (SMA).
        :return: A dictionary with Upper Band, Basis, and Lower Band.
        """
        prices = pd.Series(prices)
        high = prices.rolling(window=length).max()
        low = prices.rolling(window=length).min()
        close = prices

        if use_ema:
            ma = close.ewm(span=length, adjust=False).mean()
        else:
            ma = close.rolling(window=length).mean()

        tr = pd.concat([high - low, 
                        abs(high - close.shift(1)), 
                        abs(low - close.shift(1))], axis=1).max(axis=1)
        atr = tr.rolling(window=atr_length).mean()

        upper_band = ma + (atr * multiplier)
        lower_band = ma - (atr * multiplier)

        return {
            'upper_band': upper_band,
            'basis': ma,
            'lower_band': lower_band
        }
    
    @staticmethod
    def average_true_range(high, low, close, period=14):
        """
        Calculate the Average True Range (ATR).

        :param high: Series of high prices.
        :param low: Series of low prices.
        :param close: Series of closing prices.
        :param period: The period to calculate the ATR.
        :return: A Series representing the ATR.
        """
        high = pd.Series(high)
        low = pd.Series(low)
        close = pd.Series(close)

        tr1 = high - low
        tr2 = abs(high - close.shift(1))
        tr3 = abs(low - close.shift(1))
        true_range = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)

        atr = true_range.rolling(window=period).mean()

        return atr
    
    @staticmethod
    def linear_regression_channel(prices, length=30, upper_mult=2.0, lower_mult=2.0):
        """
        Calculate the Linear Regression Channel for a given list of prices over a specified length.

        :param prices: List of prices (closing prices).
        :param length: The number of periods to use for the regression calculation (e.g., last 30 days).
        :param upper_mult: Multiplier for the upper deviation.
        :param lower_mult: Multiplier for the lower deviation.
        :return: A dictionary containing the regression line, upper band, and lower band.
        """
        if len(prices) < length:
            raise ValueError("Not enough data points to calculate Linear Regression Channel.")

        recent_prices = prices[-length:]

        x = np.arange(length)
        y = recent_prices

        A = np.vstack([x, np.ones(length)]).T
        m, b = np.linalg.lstsq(A, y, rcond=None)[0]

        regression_line = m * x + b

        residuals = y - regression_line
        std_dev = np.std(residuals)

        upper_band = regression_line + upper_mult * std_dev
        lower_band = regression_line - lower_mult * std_dev

        return {
            'regression_line': regression_line,
            'upper_band': upper_band,
            'lower_band': lower_band
        }
    
    @staticmethod
    def least_squares_moving_average(src, length=25, offset=0):
        """
        Calculate the Least Squares Moving Average (LSMA) for a given source data.

        :param src: List or array of source data (e.g., closing prices).
        :param length: The number of periods to use for the LSMA calculation.
        :param offset: The number of periods to offset the LSMA.
        :return: A numpy array containing the LSMA values.
        """
        if len(src) < length:
            raise ValueError("Not enough data points to calculate LSMA.")

        lsma = np.full_like(src, np.nan) 

        for i in range(length, len(src)):
            x = np.arange(length)
            y = src[i-length:i]

            A = np.vstack([x, np.ones(length)]).T
            m, b = np.linalg.lstsq(A, y, rcond=None)[0]

            lsma[i] = m * (length - 1 + offset) + b

        return lsma
    
    @staticmethod
    def mass_index(high, low, length=10):
        """
        Calculate the Mass Index for a given high and low price series.

        :param high: List or array of high prices.
        :param low: List or array of low prices.
        :param length: The number of periods to use for the Mass Index calculation.
        :return: A numpy array containing the Mass Index values.
        """
        if len(high) != len(low):
            raise ValueError("High and low price arrays must have the same length.")
        
        span = high - low

        ema_span = TechnicalAnalysis.ema(span, 9)

        ema_ema_span = TechnicalAnalysis.ema(ema_span, 9)

        mi = np.zeros(len(ema_span))
        for i in range(len(ema_span)):
            if ema_ema_span[i] != 0:
                mi[i] = ema_span[i] / ema_ema_span[i]

        mass_index = np.zeros(len(mi))
        for i in range(length - 1, len(mi)):
            mass_index[i] = np.sum(mi[i - length + 1:i + 1])

        return mass_index
    
    @staticmethod
    def mcginley_dynamic(close, length=14):
        """
        Calculate the McGinley Dynamic for a given closing price series.

        :param close: List or array of closing prices.
        :param length: The number of periods to use for the McGinley Dynamic calculation.
        :return: A numpy array containing the McGinley Dynamic values.
        """
        mg = np.zeros(len(close))
        mg[0] = np.mean(close[:length])
        
        for i in range(1, len(close)):
            if mg[i-1] != 0:
                mg[i] = mg[i-1] + (close[i] - mg[i-1]) / (length * (close[i] / mg[i-1]) ** 4)
            else:
                mg[i] = close[i]

        return mg
    
    @staticmethod
    def momentum(prices, length=10):
        """
        Calculate the Momentum Indicator for a given list of prices.
        
        :param prices: List of prices (closing prices).
        :param length: The number of periods to use for the momentum calculation.
        :return: List of momentum values.
        """
        if len(prices) < length:
            raise ValueError("Not enough data points to calculate Momentum.")
        
        mom_values = np.array(prices[length:]) - np.array(prices[:-length])
        
        mom_values = [np.nan] * length + mom_values.tolist()
        
        return mom_values
    
    @staticmethod
    def parabolic_sar(high, low, initial_af=0.02, increment=0.02, max_af=0.2):
        """
        Calculate the Parabolic SAR for a given high and low price series.

        :param high: List or array of high prices.
        :param low: List or array of low prices.
        :param initial_af: Initial acceleration factor.
        :param increment: Increment of the acceleration factor.
        :param max_af: Maximum acceleration factor.
        :return: List of Parabolic SAR values.
        """
        sar = [0] * len(high)
        ep = high[0]
        af = initial_af
        trend = 1

        for i in range(1, len(high)):
            if trend == 1:
                sar[i] = sar[i-1] + af * (ep - sar[i-1])
                sar[i] = min(sar[i], low[i-1], low[i-2])
                if high[i] > ep:
                    ep = high[i]
                    af = min(af + increment, max_af)
                if low[i] < sar[i]:
                    trend = -1
                    sar[i] = ep
                    ep = low[i]
                    af = initial_af
            else:
                sar[i] = sar[i-1] + af * (ep - sar[i-1])
                sar[i] = max(sar[i], high[i-1], high[i-2])
                if low[i] < ep:
                    ep = low[i]
                    af = min(af + increment, max_af)
                if high[i] > sar[i]:
                    trend = 1
                    sar[i] = ep
                    ep = high[i]
                    af = initial_af

        return sar
    
    @staticmethod
    def sma_with_nan(data, period):
        """SMA that handles NaN values."""
        sma = np.full_like(data, np.nan)
        for i in range(period - 1, len(data)):
            if not np.isnan(data[i - period + 1:i + 1]).any():
                sma[i] = np.mean(data[i - period + 1:i + 1])
        return sma

    @staticmethod
    def stochastic_rsi(prices, rsi_length=14, stoch_length=14, smooth_k=3, smooth_d=3):
        """
        Calculate the Stochastic RSI for a given list of prices.
        
        :param prices: List of closing prices.
        :param rsi_length: The number of periods to use for the RSI calculation.
        :param stoch_length: The number of periods to use for the Stochastic calculation.
        :param smooth_k: The smoothing period for the %K line.
        :param smooth_d: The smoothing period for the %D line (signal line).
        :return: Tuple containing %K and %D values.
        """
        rsi_values = TechnicalAnalysis.rsi(prices, period=rsi_length)

        stoch_rsi = np.zeros(len(rsi_values))
        for i in range(stoch_length - 1, len(rsi_values)):
            rsi_slice = rsi_values[i - stoch_length + 1:i + 1]
            stoch_rsi[i] = (rsi_values[i] - np.nanmin(rsi_slice)) / (np.nanmax(rsi_slice) - np.nanmin(rsi_slice)) * 100

        smooth_k_values = TechnicalAnalysis.sma_with_nan(stoch_rsi, smooth_k)

        smooth_d_values = TechnicalAnalysis.sma_with_nan(smooth_k_values, smooth_d)

        return smooth_k_values, smooth_d_values
    
    @staticmethod
    def stochastic_momentum_index(prices, high_prices, low_prices, length_k=10, length_d=3, length_ema=3):
        """
        Calculate the Stochastic Momentum Index (SMI).
        
        :param prices: List of closing prices.
        :param high_prices: List of high prices.
        :param low_prices: List of low prices.
        :param length_k: The number of periods for %K calculation.
        :param length_d: The number of periods for smoothing %D.
        :param length_ema: The number of periods for the SMI-based EMA.
        :return: Tuple containing SMI and SMI-based EMA values.
        """
        prices = np.array(prices)
        high_prices = np.array(high_prices)
        low_prices = np.array(low_prices)

        highest_high = np.zeros(len(prices))
        lowest_low = np.zeros(len(prices))

        for i in range(length_k - 1, len(prices)):
            highest_high[i] = np.max(high_prices[i - length_k + 1:i + 1])
            lowest_low[i] = np.min(low_prices[i - length_k + 1:i + 1])

        highest_lowest_range = highest_high - lowest_low
        relative_range = prices - (highest_high + lowest_low) / 2

        smi = 200 * (TechnicalAnalysis.double_ema(relative_range, length_d) / TechnicalAnalysis.double_ema(highest_lowest_range, length_d))
        smi_based_ema = TechnicalAnalysis.ema(smi, length_ema)

        return smi, smi_based_ema
    
    @staticmethod
    def supertrend(high_prices, low_prices, close_prices, atr_period=10, factor=3.0):
        """
        Calculate the Supertrend indicator.
        
        :param high_prices: List or NumPy array of high prices.
        :param low_prices: List or NumPy array of low prices.
        :param close_prices: List or NumPy array of closing prices.
        :param atr_period: The number of periods for the ATR calculation.
        :param factor: The factor for the Supertrend calculation.
        :return: Tuple containing Supertrend values and trend direction.
        """
        atr_values = TechnicalAnalysis.atr(high_prices, low_prices, close_prices, atr_period)
        supertrend = np.zeros(len(close_prices))
        direction = np.zeros(len(close_prices))

        for i in range(1, len(close_prices)):
            if i == 1:
                supertrend[i] = close_prices[i] + (factor * atr_values[i])
            else:
                supertrend[i] = supertrend[i-1]
                if close_prices[i] > supertrend[i-1]:
                    supertrend[i] = max(supertrend[i], close_prices[i] - (factor * atr_values[i]))
                    direction[i] = 1
                elif close_prices[i] < supertrend[i-1]:
                    supertrend[i] = min(supertrend[i], close_prices[i] + (factor * atr_values[i]))
                    direction[i] = -1

        return supertrend, direction
    
    @staticmethod
    def twap(prices, anchor_period):
        """
        Calculate the Time Weighted Average Price (TWAP).
        
        :param prices: List or NumPy array of prices (OHLC average).
        :param anchor_period: The period for calculating TWAP.
        :return: List of TWAP values.
        """
        prices = np.array(prices)
        
        twap_values = np.zeros(len(prices))
        cumulative_sum = 0
        count = 0
        
        for i in range(len(prices)):
            cumulative_sum += prices[i]
            count += 1
            
            if i < anchor_period:
                twap_values[i] = cumulative_sum / (i + 1)
            else:
                twap_values[i] = cumulative_sum / anchor_period
            
            if i >= anchor_period - 1:
                cumulative_sum -= prices[i - anchor_period + 1]
        
        return twap_values
    
    @staticmethod
    def tsi(prices, long_length=25, short_length=13, signal_length=13):
        """
        Calculate the True Strength Index (TSI).
        
        :param prices: List or NumPy array of prices (e.g., closing prices).
        :param long_length: Long length for TSI calculation.
        :param short_length: Short length for TSI calculation.
        :param signal_length: Signal length for TSI.
        :return: Tuple containing TSI values and signal line.
        """
        price_changes = np.diff(prices, prepend=prices[0])
        double_smoothed_pc = TechnicalAnalysis.ema(TechnicalAnalysis.ema(price_changes, long_length), short_length)
        double_smoothed_abs_pc = TechnicalAnalysis.ema(TechnicalAnalysis.ema(np.abs(price_changes), long_length), short_length)

        tsi_values = 100 * (double_smoothed_pc / double_smoothed_abs_pc)
        signal_values = TechnicalAnalysis.ema(tsi_values, signal_length)

        return tsi_values, signal_values
    
    @staticmethod
    def williams_alligator(prices, jaw_period=13, teeth_period=8, lips_period=5):
        """
        Calculate Williams Alligator indicator.
        
        :param prices: List or NumPy array of prices (e.g., closing prices).
        :param jaw_period: Period for the Alligator's Jaw.
        :param teeth_period: Period for the Alligator's Teeth.
        :param lips_period: Period for the Alligator's Lips.
        :return: Tuple containing Jaw, Teeth, and Lips values.
        """
        jaw = TechnicalAnalysis.sma_for_williams(prices, jaw_period)
        teeth = TechnicalAnalysis.sma_for_williams(prices, teeth_period)
        lips = TechnicalAnalysis.sma_for_williams(prices, lips_period)

        jaw = np.pad(jaw, (jaw_period - 1, 0), 'constant', constant_values=np.nan)
        teeth = np.pad(teeth, (teeth_period - 1, 0), 'constant', constant_values=np.nan)
        lips = np.pad(lips, (lips_period - 1, 0), 'constant', constant_values=np.nan)

        return jaw, teeth, lips
    
    @staticmethod
    def vortex(highs, lows, period=14):
        """
        Calculate Vortex Indicator (VI).
        
        :param highs: List or NumPy array of high prices.
        :param lows: List or NumPy array of low prices.
        :param period: Length of the Vortex Indicator.
        :return: Tuple containing VI+ and VI- values.
        """
        VMP = np.zeros(len(highs))
        VMM = np.zeros(len(lows))

        for i in range(1, len(highs)):
            VMP[i] = np.abs(highs[i] - lows[i - 1])
            VMM[i] = np.abs(lows[i] - highs[i - 1])

        VIP = np.convolve(VMP, np.ones(period), mode='valid') / np.convolve(np.abs(highs - lows), np.ones(period), mode='valid')
        VIM = np.convolve(VMM, np.ones(period), mode='valid') / np.convolve(np.abs(highs - lows), np.ones(period), mode='valid')

        VIP = np.pad(VIP, (period - 1, 0), 'constant', constant_values=np.nan)
        VIM = np.pad(VIM, (period - 1, 0), 'constant', constant_values=np.nan)

        return VIP, VIM
    
    @staticmethod
    def stochastic_oscillator(prices, high_prices, low_prices, k_period=14, d_period=3):
        """
        Calculate the Stochastic Oscillator (%K and %D).

        :param prices: List of closing prices.
        :param high_prices: List of high prices.
        :param low_prices: List of low prices.
        :param k_period: The number of periods for %K calculation.
        :param d_period: The number of periods for %D calculation (smoothing).
        :return: Tuple containing %K and %D values.
        """
        if len(prices) < k_period or len(high_prices) < k_period or len(low_prices) < k_period:
            raise ValueError("Not enough data points to calculate Stochastic Oscillator.")

        prices = np.array(prices)
        high_prices = np.array(high_prices)
        low_prices = np.array(low_prices)

        highest_high = np.array([np.max(high_prices[i - k_period + 1:i + 1]) for i in range(k_period - 1, len(prices))])
        lowest_low = np.array([np.min(low_prices[i - k_period + 1:i + 1]) for i in range(k_period - 1, len(prices))])
        k_values = 100 * (prices[k_period - 1:] - lowest_low) / (highest_high - lowest_low)

        d_values = np.array([np.mean(k_values[i - d_period + 1:i + 1]) for i in range(d_period - 1, len(k_values))])

        k_values = np.concatenate((np.full(k_period - 1, np.nan), k_values))
        d_values = np.concatenate((np.full(d_period - 1 + k_period - 1, np.nan), d_values))

        return k_values, d_values
    
    @staticmethod
    def macd(prices, fast_length=12, slow_length=26, signal_length=9, ma_type='EMA'):
        """
        Calculate the Moving Average Convergence Divergence (MACD) for a given list of prices.

        :param prices: List or NumPy array of prices (e.g., closing prices).
        :param fast_length: Length of the fast moving average.
        :param slow_length: Length of the slow moving average.
        :param signal_length: Length of the signal line.
        :param ma_type: Type of moving average to use ('SMA' or 'EMA').
        :return: Tuple containing MACD line, Signal line, and Histogram values.
        """
        if len(prices) < slow_length:
            raise ValueError("Not enough data points to calculate MACD.")

        prices = np.array(prices)

        if ma_type == 'EMA':
            fast_ma = pd.Series(prices).ewm(span=fast_length, adjust=False).mean().to_numpy()
            slow_ma = pd.Series(prices).ewm(span=slow_length, adjust=False).mean().to_numpy()
        else:
            fast_ma = np.convolve(prices, np.ones(fast_length) / fast_length, mode='valid')
            slow_ma = np.convolve(prices, np.ones(slow_length) / slow_length, mode='valid')

            fast_ma = np.concatenate((np.full(fast_length - 1, np.nan), fast_ma))
            slow_ma = np.concatenate((np.full(slow_length - 1, np.nan), slow_ma))

        macd_line = fast_ma - slow_ma

        signal_line = pd.Series(macd_line).ewm(span=signal_length, adjust=False).mean().to_numpy()

        histogram = macd_line - signal_line

        macd_line = np.concatenate((np.full(slow_length - 1, np.nan), macd_line))
        signal_line = np.concatenate((np.full(slow_length + signal_length - 2, np.nan), signal_line))
        histogram = np.concatenate((np.full(slow_length + signal_length - 2, np.nan), histogram))

        return macd_line, signal_line, histogram