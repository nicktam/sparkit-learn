import numpy as np
from sklearn.svm import LinearSVC as SklearnLinearSVC
from splearn.svm import LinearSVC
from splearn.utils.testing import SplearnTestCase, assert_array_almost_equal


class TestLinearSVC(SplearnTestCase):

    def test_same_coefs(self):
        X, y, Z = self.make_classification(2, 100000)

        local = SklearnLinearSVC()
        dist = LinearSVC()

        local.fit(X, y)
        dist.fit(Z, classes=np.unique(y))

        assert_array_almost_equal(local.coef_, dist.coef_, decimal=3)
