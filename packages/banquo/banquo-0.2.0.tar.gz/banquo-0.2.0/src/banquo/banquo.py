#!/usr/bin/env python3
"""The module contains building blocks for Nonparanormal models."""

###############################################################################
# Imports #####################################################################
###############################################################################


from dataclasses import dataclass, field
from typing import Any

from array_api_compat import array_namespace, device


###############################################################################
# Custom types for annotation #################################################
###############################################################################


array = Any
"""Type annotation for array objects.

    For more information, please refer to `array-api
    <https://data-apis.org/array-api/latest/API_specification/array_object.html>`__.
"""


###############################################################################
# Exceptions ##################################################################
###############################################################################


class BanquoError(Exception):
    """Base class for exceptions in Banquo."""


class MinMaxNormalizationError(BanquoError):
    """Base class for min-max normalization exceptions in Banquo."""


@dataclass
class DataRangeExceedsSupportBoundError(MinMaxNormalizationError):
    """Exception for data range exceeding support's boundary."""

    support: array = field()
    data_range: array = field()
    msg_data: str = field(init=False, repr=False)
    msg_support: str = field(init=False, repr=False)

    def __post_init__(self) -> None:
        """Set error message's parameters."""
        self.msg_data: str = f"range {(self.data_range[0], self.data_range[1])}"
        self.msg_support: str = f"boundary {(self.support[0], self.support[1])}"

    def __str__(self) -> str:
        """Set error message."""
        return f"Data {self.msg_data} exceeds the support's {self.msg_support}."


@dataclass
class DataMinExceedsSupportLowerBoundError(DataRangeExceedsSupportBoundError):
    """Exception for data minimum exceeding support's lower bound."""

    def __post_init__(self) -> None:
        """Set error message's parameters."""
        self.msg_data: str = f"minimum {self.data_range[0]}"
        self.msg_support: str = f"lower boundary {self.support[0]}"


@dataclass
class DataMaxExceedsSupportUpperBoundError(DataRangeExceedsSupportBoundError):
    """Exception for data maximum exceeding support's upper bound."""

    def __post_init__(self) -> None:
        """Set error message's parameters."""
        self.msg_data: str = f"maximum {self.data_range[1]}"
        self.msg_support: str = f"upper boundary {self.support[1]}"


###############################################################################
# Auxiliary functions #########################################################
###############################################################################


def chol2inv(spd_chol: array) -> array:
    r"""Invert a SPD square matrix from its Choleski decomposition.

    Given a Choleski decomposition :math:`\Sigma` of a matrix :math:`\Sigma`,
    i.e. :math:`\Sigma = LL^T`, this function returns the inverse
    :math:`\Sigma^{-1}`.

    Parameters
    ----------
    spd_chol : array
        Cholesky factor of the correlation/covariance matrix.

    Returns
    -------
    array
        Inverse matrix.
    """
    xp = array_namespace(spd_chol)  # Get the array API namespace
    spd_chol_inv = xp.linalg.inv(spd_chol)
    return spd_chol_inv.T @ spd_chol_inv


def diag(x: array) -> array:
    """Generate a diagonal matrix from array `x`.

    Parameters
    ----------
    x : array
        One-dimensional array.

    Returns
    -------
    array
        Diagonal matrix from input array.
    """
    xp = array_namespace(x)  # Get the array API namespace
    n = x.shape[0]
    res = xp.zeros((n, n), dtype=x.dtype, device=device(x))
    ii = xp.arange(n, device=device(x))  # Generate indices for the diagonal
    res[ii, ii] = x  # Set the diagonal elements
    return res


def normalize_covariance(cov: array) -> array:
    r"""Normalize a covariance matrix.

    Assuming a covariance matrix :math:`\Sigma`, the correlation matrix
    :math:`\Omega` entries are given by:

    .. math::
        \Omega_{ij} = \Sigma_{ij}/\sqrt{\Sigma_{ii} \Sigma_{jj}}\,.

    Parameters
    ----------
    cov : array
        SPD covariance matrix

    Returns
    -------
    array
        SPD correlation matrix.
    """
    xp = array_namespace(cov)  # Get the array API namespace

    # Get the standard deviations (sqrt of diagonal elements)
    std_devs = xp.sqrt(xp.diagonal(cov))

    # Create a diagonal matrix with the reciprocal of the standard deviations
    inv_stddev_matrix = diag(1 / std_devs)

    # Transform covariance matrix to correlation matrix
    return inv_stddev_matrix @ cov @ inv_stddev_matrix


def std_ns(x: array, axis: int | None = None) -> array | float:
    """Numerically stable calculation of standard deviation.

    If the standard deviation tends to infinity,
    it is substituted by the interquartile range (IQR).

    Parameters
    ----------
    x : array
        Elements to extract the standard deviation.
    axis : int | None, optional
        Axis or axes along which the standard deviation calculation
        is performed. If axis is negative it counts from the last
        to the first axis, by default None will sum all of
        the elements of the input array.

    Returns
    -------
    array | float
        An array with the same shape as a, with the specified axis removed.
        If a is a 0-d array, or if axis is None, a scalar is returned.
        If an output array is specified, a reference to out is returned.
    """
    xp = array_namespace(x)  # Get the array API namespace

    x_std = xp.std(x, axis=axis)

    if xp.isinf(x_std):
        # Compute Q1 (25th percentile) and Q3 (75th percentile)
        q1 = xp.percentile(x, 25, axis=axis)
        q3 = xp.percentile(x, 75, axis=axis)

        # Compute IQR (Interquartile Range)
        iqr = q3 - q1

        # Use IQR as a measure of spread instead of std
        x_std = 20 * iqr / 27  # IQR can be scaled to approximate std

    return x_std


def kahan_sum(x1: array, x2: array) -> array:
    r"""Element-wise Kahan summation algorithm.

    Given two arrays of the same shape, `x1` and `x2`, this function
    performs a numerically stable element-wise summation `x1 + x2`.
    For the subtraction :math:`x_1 - x_2`, it is sufficient to
    use :func:`kahan_sum` with parameters `x1` and `-x2`.

    Parameters
    ----------
    x1 : array
        First term.
    x2 : array
        Second term.

    Returns
    -------
    array
        Sum of x1 and x2.
    """
    temp = x1 + x2
    compensation = (
        x1 - temp
    ) + x2  # Here we perform compensation for floating-point errors
    result = temp + compensation
    return result


def divide_ns(x1: array, x2: array) -> array:
    r"""Numerically stable division.

    Given two arrays of the same shape, `x1` and `x2`, this function
    performs a numerically stable element-wise division :math:`x_1 / x_2`.
    The function relies on the formula:

    .. math::
        \\frac{x_1}{x_2} = \\text{sign}(x_1)\\text{sign}(x_2) \\exp\\left(\\log(\\lvert x_1\\rvert) - \\log(\\lvert x_2\\rvert)\\right)\\,.

    Parameters
    ----------
    x1 : array
        Numerator.
    x2 : array
        Denominator.

    Returns
    -------
    array
        Quotient.
    """  # noqa: B950
    xp = array_namespace(x1, x2)  # Get the array API namespace

    # Handle signs of x1 and x2, using absolute values for log
    sign = xp.sign(x1) * xp.sign(x2)
    log_x1 = xp.log(xp.abs(x1))
    log_x2 = xp.log(xp.abs(x2))

    return sign * xp.exp(log_x1 - log_x2)


def multiply_ns(x1: array, x2: array | None = None) -> array | float:
    r"""Numerically stable multiplication.

    Given two arrays of the same shape, `x1` and `x2`, this function
    performs a numerically stable element-wise division :math:`x_1 \\times x_2`.
    The function relies on the formula:

    .. math::
        x_1 \\times x_2 = \\text{sign}(x_1)\\text{sign}(x_2) \\exp\\left(\\log(\\lvert x_1\\rvert) + \\log(\\lvert x_2\\rvert)\\right)\\,.

    Parameters
    ----------
    x1 : array
        Factor.
    x2 : array | None, optional
        Factor, by default None. If None, the product will be
        performed through array `x1`.

    Returns
    -------
    array | float
        Product. If `x2` is None, the product will be performed in
        array `x1`, resulting in a float. If otherwise, the function returns
        the element-wise multiplication between `x1` and `x2` resulting in an
        array of the same shape.
    """  # noqa: B950
    if x2 is None:
        xp = array_namespace(x1)  # Get the array API namespace
        sign = xp.prod(xp.sign(x1))
        log_x1 = xp.log(xp.abs(x1))
        return sign * xp.exp(xp.sum(log_x1))
    else:
        xp = array_namespace(x1, x2)  # Get the array API namespace
        sign = xp.sign(x1) * xp.sign(x2)
        log_x1 = xp.log(xp.abs(x1))
        log_x2 = xp.log(xp.abs(x2))
        return sign * xp.exp(log_x1 + log_x2)


def homographic_ns(x: array) -> array:
    r"""Numerically stable homographic function.

    Given an array `x`, this function
    performs a numerically stable calculation of :math:`1/(1+x)`.
    The function applies :func:`divide_ns` with
    :math:`x_1 = 1` and :math:`x_2 = 1 + x`.

    Parameters
    ----------
    x : array
        Elements to extract the homographic function.

    Returns
    -------
    array
        homographic function, :math:`1/(1+x)`.
    """
    xp = array_namespace(x)  # Get the array API namespace
    one = xp.ones_like(x, device=device(x))
    y = one + x
    return divide_ns(one, y)


def add_intercept_column(x: array, const: float | int = 1) -> array:
    """Include intercept column to array `x`.

    The intercept can be any constant number.

    Parameters
    ----------
    x : array
        Array to add a constant (intercept) column.
    const : float | int, optional
        constant to be included into array `x`, by default 1.

    Returns
    -------
    array
        For an input `x` with dimensions :math:`(n, d)`, it includes a
        constant column to `x`, resulting in an array with dimensions
        :math:`(n, d+1)`.
    """
    xp = array_namespace(x)  # Get the array API namespace

    n = x.shape[0]  # Get the number of rows in x

    return xp.concat(
        (const * xp.ones((n, 1), dtype=x.dtype, device=device(x)), x[:, xp.newaxis]),
        axis=1,
    )


###############################################################################
# Data transform ##############################################################
###############################################################################


def extract_minmax_parameters(x: array, support: array | None = None) -> array:
    r"""Extract the intercept and slop from `x` for the support :math:`[0, 1]`.

    These parameters can be applied into the linear transformation, given by,

    .. math::
        y = \\frac{-a}{b-a} + \\frac{1}{b-a} x,

    to make the data bounded by :math:`[0, 1]`. Where :math:`a` and
    :math:`b`. are given by:

    .. math::

        a & = \\max\\{X_{(1)} - \\sqrt{S^2/n}, a'\\},\\\\
        b & = \\min\\{X_{(n)} + \\sqrt{S^2/n}, b'\\},

    with :math:`S^2` representing the sample variance, and
    :math:`X_{(1)}` and :math:`X_{(n)}` denoting the first and last
    order statistics, respectively. In this formula :math:`x \\in [a', b']`


    Parameters
    ----------
    x : array
        Elements to be transformed.
    support : array | None, optional
        Two-elements array containing the lower and upper bounds
        for the elements, by default None. If None, `support`
        is the unbounded interval :math:`(-\\infty, \\infty)`.

    Returns
    -------
    array
        Two-elements array containing the intercept and slope for
        a linear transformation.

    Raises
    ------
    DataRangeExceedsSupportBoundError
        If the data range exceeds support's boundary.
    DataMinExceedsSupportLowerBoundError
        If data minimum exceeds support's lower bound.
    DataMaxExceedsSupportUpperBoundError
        If data maximum exceeds support's upper bound.
    Note
    ----
    See `Unimodal density estimation using Bernstein polynomials
    <https://www.sciencedirect.com/science/article/pii/S0167947313003757>`__.
    """
    if support is None:
        xp = array_namespace(x)  # Get the array API namespace
        support = xp.asarray(
            (-xp.inf, xp.inf), device=device(x)
        )  # Default: unbounded support
    else:
        xp = array_namespace(x, support)  # Get the array API namespace

    x_range = xp.asarray((xp.min(x), xp.max(x)), device=device(x))

    condition_lower: bool = x_range[0] < support[0]
    condition_upper: bool = x_range[1] > support[1]

    # Check if data range exceeds support's boundary
    if condition_lower and condition_upper:
        raise DataRangeExceedsSupportBoundError(support, x_range)
    # Check if data minimum exceeds support's lower bound
    elif x_range[0] < support[0]:
        raise DataMinExceedsSupportLowerBoundError(support, x_range)
    # Check if data maximum exceeds support's upper bound
    elif x_range[1] > support[1]:
        raise DataMaxExceedsSupportUpperBoundError(support, x_range)

    n = x.shape[0]

    x_std = std_ns(x)

    adjustment = xp.asarray(x_std / xp.sqrt(n), device=device(x))

    # Defines the minimum value
    a_min = kahan_sum(xp.asarray(x_range[0], device=device(x)), -adjustment)
    a = xp.max(xp.asarray((a_min, support[0]), device=device(x)))

    # Defines the maximum value
    b_max = kahan_sum(xp.asarray(x_range[1], device=device(x)), adjustment)
    b = xp.min(xp.asarray((b_max, support[1]), device=device(x)))

    # b-a
    denominator = kahan_sum(b, -a)

    # -a/(b-a)
    coeff1 = divide_ns(-a, denominator)

    # 1/(b-a)
    coeff2 = divide_ns(
        xp.ones_like(denominator, device=device(denominator)), denominator
    )

    return xp.asarray((coeff1, coeff2), device=device(x))


def minmax_normalization(
    x: array, *, support: array | None = None, coeffs: array | None = None
) -> array:
    r"""Transform `x` to the range :math:`[0, 1]`.

    Linear transform is applied to `x`, given by,

    .. math::
        y = c_1 + c_2 x,

    See :func:`extract_minmax_parameters` for more information
    on how :math:`c_1` and :math:`c_2` can be calculated.

    Parameters
    ----------
    x : array
        Elements to be transformed.
    support : array | None, optional
        Two-elements array containing the lower and upper bounds
        for the elements, by default None. If None, `support`
        is the unbounded interval :math:`(-\infty, \infty)`.
    coeffs : array | None, optional
        Two-elements array containing the intercept and slope for
        a linear transformation, by default None. If None, the
        both parameters will be calculated by
        :func:`extract_minmax_parameters`.

    Returns
    -------
    array
        Elements in the the range :math:`[0, 1]`.
    """
    if coeffs is None:
        coeffs = extract_minmax_parameters(x, support)

    # Transform the data
    return add_intercept_column(x) @ coeffs


###############################################################################
# Copula functions ############################################################
###############################################################################


def multi_normal_cholesky_copula_lpdf(marginal: array, omega_chol: array) -> float:
    r"""Compute multivariate normal copula lpdf (Cholesky parameterisation).

    Considering the copula function :math:`C:[0,1]^d\rightarrow [0,1]`
    and any :math:`(u_1,\dots,u_d)\in[0,1]^d`, such that
    :math:`u_i = F_i(X_i) = P(X_i \leq x)` are cumulative distribution
    functions. The multivariate normal copula is given by
    :math:`C_\Omega(u) = \Phi_\Omega\left(\Phi^{-1}(u_1),\dots, \Phi^{-1}(u_d) \right)`.
    It is parameterized by the correlation matrix :math:`\Omega = LL^T`, from which
    :math:`L` is the Cholesky decomposition. Then, the copula density function is
    given by

    .. math::
        c_\Omega(u) = \frac{\partial^d C_\Omega(u)}{\partial \Phi(u_1)\cdots \partial \Phi(u_d)} \,,

    and this function computes its log density :math:`\log\left(c_\Omega(u)\right)`.


    Parameters
    ----------
    marginal : array
        Matrix of outcomes from marginal calculations.
        In this function, :math:`\text{marginal} = \Phi^{-1}(u)`.
    omega_chol : array
        Cholesky factor of the correlation matrix.

    Returns
    -------
    float
        log density of distribution.
    """  # noqa: B950
    xp = array_namespace(marginal, omega_chol)  # Get the array API namespace
    n, d = marginal.shape
    precision = chol2inv(omega_chol)
    log_density: float = -n * xp.sum(xp.log(xp.diagonal(omega_chol))) - 0.5 * xp.sum(
        xp.multiply(
            precision - xp.eye(d, device=device(precision)), marginal.T @ marginal
        )
    )
    return log_density
