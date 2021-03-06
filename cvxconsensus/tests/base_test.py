"""
Copyright 2018 Anqi Fu

This file is part of CVXConsensus.

CVXConsensus is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

CVXConsensus is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with CVXConsensus. If not, see <http://www.gnu.org/licenses/>.
"""

# Base class for unit tests.
from unittest import TestCase
import numpy as np

class BaseTest(TestCase):
    # AssertAlmostEqual for lists.
    def assertItemsAlmostEqual(self, a, b, places=4):
        if np.isscalar(a):
            a = [a]
        else:
            a = self.mat_to_list(a)
        if np.isscalar(b):
            b = [b]
        else:
            b = self.mat_to_list(b)
        for i in range(len(a)):
            self.assertAlmostEqual(a[i], b[i], places)

    # Overriden method to assume lower accuracy.
    def assertAlmostEqual(self, a, b, places=4):
        super(BaseTest, self).assertAlmostEqual(a, b, places=places)

    def mat_to_list(self, mat):
        """Convert a numpy matrix to a list.
        """
        if isinstance(mat, (np.matrix, np.ndarray)):
            return np.asarray(mat).flatten('F').tolist()
        else:
            return mat

    def compare_results(self, probs, obj_admm, obj_comb, x_admm, x_comb):
        N = len(probs.variables())
        for i in range(N):
            print("\nADMM Solution:\n", x_admm[i])
            print("Base Solution:\n", x_comb[i])
            print("MSE: ", np.mean(np.square(x_admm[i] - x_comb[i])), "\n")
        print("ADMM Objective: %f" % obj_admm)
        print("Base Objective: %f" % obj_comb)
        print("Iterations: %d" % probs.solver_stats["num_iters"])
        print("Elapsed Time: %f" % probs.solver_stats["solve_time"])
