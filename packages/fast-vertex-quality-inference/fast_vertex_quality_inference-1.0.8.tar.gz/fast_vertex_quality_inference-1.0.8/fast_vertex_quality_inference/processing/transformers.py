import numpy as np
from sklearn.preprocessing import QuantileTransformer
from scipy import stats


_residualfrac_limit = 5.0
use_qts_in_reconstruction_loss = True


def symlog(x, linthresh=1.0):
    sign = np.sign(x)
    abs_x = np.abs(x)
    return sign * np.log10(1 + abs_x / linthresh)


def invsymlog(y, linthresh=1.0):
    sign = np.sign(y)
    abs_y = np.abs(y)
    return sign * linthresh * (10**abs_y - 1)


def np_based_qt_transform(X_col, quantiles, inverse):
    """Private function to transform a single feature."""

    quantiles = np.squeeze(quantiles)

    BOUNDS_THRESHOLD = 1e-7
    n_quantiles_ = np.shape(quantiles)[0]
    references_ = np.linspace(0, 1, n_quantiles_, endpoint=True)

    output_distribution = "normal"

    if not inverse:
        lower_bound_x = quantiles[0]
        upper_bound_x = quantiles[-1]
        lower_bound_y = 0
        upper_bound_y = 1
    else:
        lower_bound_x = 0
        upper_bound_x = 1
        lower_bound_y = quantiles[0]
        upper_bound_y = quantiles[-1]
        X_col = stats.norm.cdf(X_col)

    lower_bounds_idx = X_col - BOUNDS_THRESHOLD < lower_bound_x
    upper_bounds_idx = X_col + BOUNDS_THRESHOLD > upper_bound_x

    isfinite_mask = ~np.isnan(X_col)
    X_col_finite = X_col[isfinite_mask]

    if not inverse:
        X_col[isfinite_mask] = 0.5 * (
            np.interp(X_col_finite, quantiles, references_)
            - np.interp(-X_col_finite, -quantiles[::-1], -references_[::-1])
        )
    else:
        X_col[isfinite_mask] = np.interp(X_col_finite, references_, quantiles)

    X_col[upper_bounds_idx] = upper_bound_y
    X_col[lower_bounds_idx] = lower_bound_y
    if not inverse:
        with np.errstate(invalid="ignore"):
            if output_distribution == "normal":
                X_col = stats.norm.ppf(X_col)
                clip_min = stats.norm.ppf(BOUNDS_THRESHOLD - np.spacing(1))
                clip_max = stats.norm.ppf(1 - (BOUNDS_THRESHOLD - np.spacing(1)))
                X_col = np.clip(X_col, clip_min, clip_max)

    return X_col


class UpdatedTransformer:

    def __init__(self):

        self.qt_fit = False
        self.clip_value = 4.0

    # def fit(self, data_raw, column):

    # 	self.column = column

    # 	self.qt = QuantileTransformer(
    # 		n_quantiles=500, output_distribution="normal"
    # 	)

    def fit(self, quantiles, column):

        self.column = column

        self.qt = QuantileTransformer(n_quantiles=500, output_distribution="normal")
        self.qt.quantiles_ = quantiles
        self.qt.references_ = np.linspace(0, 1, 500, endpoint=True)
        # self.quantiles = quantiles
        self.qt_fit = True

    def process(self, data_raw):

        try:
            data = data_raw.copy()
        except:
            # pass # value is likely a single element
            data = np.asarray(data_raw).astype("float64")

        if "residualfrac" in self.column and not use_qts_in_reconstruction_loss:
            limit = _residualfrac_limit
            data[np.where(data < (limit * -1.0))] = -limit
            data[np.where(data > (limit))] = limit
            return symlog(data) / symlog(limit)

        if (
            "TRUEORIGINVERTEX_X" in self.column or "TRUEORIGINVERTEX_Y" in self.column
        ) or ("origX_TRUE" in self.column or "origY_TRUE" in self.column):
            return data

        if "DIRA" in self.column:
            where = np.where(np.isnan(data))
            where_not_nan = np.where(np.logical_not(np.isnan(data)))
            data[where] = np.amin(data[where_not_nan])

        if "VTXISOBDTHARD" in self.column:
            data[np.where(data == -1)] = np.random.uniform(
                low=-1.1, high=-1.0, size=np.shape(data[np.where(data == -1)])
            )
        if "FLIGHT" in self.column or "FD" in self.column or "IP" in self.column:
            data[np.where(data == 0)] = np.random.uniform(
                low=-0.1, high=0.0, size=np.shape(data[np.where(data == 0)])
            )

        if not self.qt_fit:
            self.qt.fit(data.reshape(-1, 1))
            self.qt_fit = True

        data = self.qt.transform(data.reshape(-1, 1))[:, 0]
        # data = np_based_qt_transform(data.reshape(-1, 1), self.quantiles, inverse=False)[:,0]
        data = np.clip(data, -self.clip_value, self.clip_value)
        data = data / self.clip_value

        return data

    def unprocess(self, data_raw):

        data = data_raw.copy()

        if "residualfrac" in self.column and not use_qts_in_reconstruction_loss:
            return invsymlog(data * symlog(_residualfrac_limit))

        if (
            "TRUEORIGINVERTEX_X" in self.column or "TRUEORIGINVERTEX_Y" in self.column
        ) or ("origX_TRUE" in self.column or "origY_TRUE" in self.column):
            return data

        data = data * self.clip_value

        data = self.qt.inverse_transform(data.reshape(-1, 1))[:, 0]
        # data = np_based_qt_transform(data.reshape(-1, 1), self.quantiles, inverse=True)[:,0]

        if "VTXISOBDTHARD" in self.column:
            data[np.where(data < -1)] = -1.0
        if "FLIGHT" in self.column or "FD" in self.column or "IP" in self.column:
            data[np.where(data < 0)] = 0.0

        return data


def transform_df(data, transformers, transform_by_index=False):

    if transform_by_index:
        for (branch, data_i), (transformer_key, transformer) in zip(
            data.items(), transformers.items()
        ):
            convert_units = False
            for P in ["P", "PT", "PX", "PY", "PZ"]:
                if f"_{P}_" in branch or branch[-(len(P) + 1) :] == f"_{P}":
                    convert_units = True
            if "residualfrac" in branch:
                convert_units = False

            if convert_units:
                data[branch] = transformer.process(np.asarray(data[branch]) * 1000.0)
            else:
                data[branch] = transformer.process(np.asarray(data[branch]))
    else:
        branches = list(data.keys())

        for branch in branches:
            convert_units = False
            for P in ["P", "PT", "PX", "PY", "PZ"]:
                if f"_{P}_" in branch or branch[-(len(P) + 1) :] == f"_{P}":
                    convert_units = True
            if "residualfrac" in branch:
                convert_units = False
            if convert_units:
                data[branch] = transformers[branch].process(
                    np.asarray(data[branch]) * 1000.0
                )
            else:
                data[branch] = transformers[branch].process(np.asarray(data[branch]))

    return data


def untransform_df(data, transformers):

    branches = list(data.keys())

    for branch in branches:
        convert_units = False
        for P in ["P", "PT", "PX", "PY", "PZ"]:
            if f"_{P}_" in branch or branch[-(len(P) + 1) :] == f"_{P}":
                convert_units = True
        if "residualfrac" in branch:
            convert_units = False
        if convert_units:
            data[branch] = (
                transformers[branch].unprocess(np.asarray(data[branch])) / 1000.0
            )
        else:
            data[branch] = transformers[branch].unprocess(np.asarray(data[branch]))

    return data
