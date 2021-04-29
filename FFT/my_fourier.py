"""Implementation of different algorithms for
Fourier Transformation

The time needed for dft and fft is being compared 
"""

__author__ = "Jakob Greiling"
__date__ = "2020-12"
# Python 3.7.3


# import standard packages
import matplotlib.pyplot as plt
import numpy as np
import time


def my_dft(in_signal: np.ndarray, in_vector: np.ndarray,
           direction: bool = True, optimzation: bool = True):
    ''' Implementation of a discrete fourier transformation 

    Parameters
    ----------
    in_signal: 
         signal that is processed by this function
    in_vector: 
         frequency or time vector of the signal
    inverse: 
         flag for direction of this transformation
         True: forward transformation
         False: inverse transformation
    optimzation:


    Returns
    -------
    out_signal: complex
         Transformed Signal
    out_vector: complex
         Transformed vector
    '''

    # setup parameters
    N = len(in_vector)
    size_vector = np.arange(0, N)
    span = in_vector[-1] - in_vector[0]

    # define direction
    if direction:
        zeta = np.exp(-2 * np.pi * 1j / N)
    else:
        zeta = np.exp(2 * np.pi * 1j / N)

    # Transformation
    if optimzation:
        out_signal = my_sumdft(in_signal, zeta)
    else:
        out_signal = my_loopdft(in_signal, zeta)

    # x-vector
    out_vector = size_vector / span

    return out_signal, out_vector


def my_sumdft(in_signal: np.ndarray, zeta: complex) -> np.ndarray:
    ''' Implementation of a discrete fouriere transformation with matrixes

    Paremeters
    ----------
    in_signal: double
         signal that is processed by this function
    zeta: complex
        exponential for discrete fouriere transformation

    Returns
    -------
    out_signal: complex
         Transformed Signal
    '''

    # Setup Transformation
    N = len(in_signal)
    k = np.arange(0, N)

    # Transformation
    out_signal = 1 / N * \
        np.sum(in_signal[k] * np.power(zeta, np.outer(k, k)),
               axis=1, dtype=complex)

    return out_signal


def my_loopdft(in_signal: np.ndarray, zeta: complex) -> complex:
    '''Implementation of a discrete fourier transformation with loops 

    Parameters
    ----------
    in_signal: double
         signal that is processed by this function
    zeta: complex
        exponential for discrete fouriere transformation

    Returns
    -------
    out_signal: complex
         Transformed Signal
    '''

    # Setup Transformation
    N = len(in_signal)
    size_vector = np.arange(N)

    # Transformation
    out_signal = np.zeros_like(size_vector, dtype='complex')
    for n in size_vector:
        for k in size_vector:
            out_signal[n] += 1 / N * in_signal[k] * np.power(zeta, (n * k))

    return out_signal


def my_fft(in_signal: np.ndarray) -> np.ndarray:
    ''' Implementation of fast fourier transformation

    Parameters
    ----------
    in_signal: double
        Signal that is processed by the function

    Returns
    -------
    out_signal: complex
         Transformed Signal
    '''

    # final recursion
    n = len(in_signal)
    if n == 1:
        return in_signal

    zeta = np.exp(-2 * np.pi * 1j / n)

    in_signal_even = in_signal[::2]
    in_signal_odd = in_signal[1::2]
    out_signal_even = my_fft(in_signal_even)
    out_signal_odd = my_fft(in_signal_odd)

    n_half = int(n / 2)
    out_signal = np.zeros(n, dtype="complex")
    for k in range(n_half):
        out_signal[k] = out_signal_even[k] \
            + np.power(zeta, k) * out_signal_odd[k]
        out_signal[k + n_half] = out_signal_even[k] \
            - np.power(zeta, k) * out_signal_odd[k]

    return out_signal


def print_time(transformation: str, time: float):
    ''' Prints time time of all Transformations 

    Parameters
    ----------
    transformation: str
        String of all Transformation types in the same order as time
    time: float
        Vector of all time values for Transformations

    '''

    for (trans, t) in zip(transformation, time):
        print(f"{trans}: {t:.10f} s")


if __name__ == '__main__':
    # parameters for sine-wave
    elements = np.power(2, 12)  # Hz
    max_time = 10  # s
    frequencies = [4, 8, 20]
    amplitudes = [2, 1, 3]

    # setup signal to be transformed
    time_vector = np.linspace(0, max_time, elements)

    signal = np.zeros_like(time_vector)

    for (amp, freq) in zip(amplitudes, frequencies):
        omega = 2 * np.pi * freq
        signal += amp * np.sin(omega * time_vector)

    # display signal
    plt.plot(time_vector, signal)
    plt.xlabel("time in s")
    plt.ylabel("Amplitude in mV")
    plt.show()

    # setup time measurement
    timer = np.zeros(4)
    transformation_type = np.empty(4, dtype=object)

    # optimized DFT with matrix multiplication
    transformation_type[0] = "Discrete Fourier Transformation - optimized"
    tic = time.perf_counter()
    mydft_signal, mydft_vector = my_dft(
        signal, time_vector, optimzation=True)
    toc = time.perf_counter()
    timer[0] = toc - tic

    # display data
    plt.plot(mydft_vector, np.abs(mydft_signal))
    plt.xlabel("Frequency in Hz")
    plt.ylabel("Amplitude in mV")
    plt.title(transformation_type[0])
    plt.show()

    # Bad DFT with loops
    transformation_type[1] = "Discrete Fourier Transformation - not optimized"
    tic = time.perf_counter()
    mydft_signal, mydft_vector = my_dft(
        signal, time_vector, optimzation=False)
    toc = time.perf_counter()
    timer[1] = toc - tic

# display data
    plt.plot(mydft_vector, np.abs(mydft_signal))
    plt.xlabel("Frequency in Hz")
    plt.ylabel("Amplitude in mV")
    plt.title(transformation_type[1])
    plt.show()

    # Numpy FFT
    transformation_type[2] = ("Fast Fourier Transformation")
    tic = time.perf_counter()
    mydft_signal = np.fft.fft(signal)
    toc = time.perf_counter()
    timer[2] = toc - tic

    # display data
    plt.plot(mydft_vector, np.abs(mydft_signal))
    plt.xlabel("Frequency in Hz")
    plt.ylabel("Amplitude in mV")
    plt.title(transformation_type[2])
    plt.show()

    # my FFT
    transformation_type[3] = ("My Fast Fourier Transformation")
    tic = time.perf_counter()
    mydft_signal = my_fft(signal)
    toc = time.perf_counter()
    timer[3] = toc - tic

    # display data
    plt.plot(mydft_vector, np.abs(mydft_signal))
    plt.xlabel("Frequency in Hz")
    plt.ylabel("Amplitude in mV")
    plt.title(transformation_type[3])
    plt.show()

    # display times
    print_time(transformation_type, timer)


